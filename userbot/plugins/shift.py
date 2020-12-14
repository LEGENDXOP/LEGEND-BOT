"""
Shifter plugin From Dark Cobra Userbot 
Added And Edited by @rohithaditya for @godhackerzuserbot

orginally created by Team Dark Cobra 
don't try to kang Without asking 
Â© @Godhackerzuserbot
"""

import asyncio

import sys

from os import environ, execle, path, remove

from typing import Tuple

from git import Repo

from git.exc import GitCommandError, InvalidGitRepositoryError, NoSuchPathError



from userbot.utils import admin_cmd

from userbot import CMD_HELP 



HEROKU_APP_NAME = Config.HEROKU_APP_NAME or None

HEROKU_API_KEY = Config.HEROKU_API_KEY or None





requirements_path = path.join(

    path.dirname(path.dirname(path.dirname(__file__))), "requirements.txt"

)



async def runcmd(cmd: str) -> Tuple[str, str, int, int]:

    """ run command in terminal """

    args = shlex.split(cmd)

    process = await asyncio.create_subprocess_exec(*args,

                                                   stdout=asyncio.subprocess.PIPE,

                                                   stderr=asyncio.subprocess.PIPE)

    stdout, stderr = await process.communicate()

    return (stdout.decode('utf-8', 'replace').strip(),

            stderr.decode('utf-8', 'replace').strip(),

            process.returncode,

            process.pid)



async def gen_chlog(repo, diff):

    ch_log = ""

    d_form = "%d/%m/%y"

    for c in repo.iter_commits(diff):

        ch_log += (

            f"  Ã¢Â€Â¢ {c.summary} ({c.committed_datetime.strftime(d_form)}) <{c.author}>\n"

        )

    return ch_log





async def print_changelogs(event, ac_br, changelog):

    changelog_str = (

        f"**New UPDATE available for [{ac_br}]:\n\nCHANGELOG:**\n`{changelog}`"

    )

    if len(changelog_str) > 4096:

        await event.edit("`Changelog is too big, view the file to see it.`")

        with open("output.txt", "w+") as file:

            file.write(changelog_str)

        await event.client.send_file(

            event.chat_id,

            "output.txt",

            reply_to=event.id,

        )

        remove("output.txt")

    else:

        await event.client.send_message(

            event.chat_id,

            changelog_str,

            reply_to=event.id,

        )

    return True





async def update_requirements():

    reqs = str(requirements_path)

    try:

        process = await asyncio.create_subprocess_shell(

            " ".join([sys.executable, "-m", "pip", "install", "-r", reqs]),

            stdout=asyncio.subprocess.PIPE,

            stderr=asyncio.subprocess.PIPE,

        )

        await process.communicate()

        return process.returncode

    except Exception as e:

        return repr(e)





async def deploy(event, repo, ups_rem, ac_br, txt):

    if HEROKU_API_KEY is not None:

        import heroku3



        heroku = heroku3.from_key(HEROKU_API_KEY)

        heroku_app = None

        heroku_applications = heroku.apps()

        if HEROKU_APP_NAME is None:

            await event.edit(

                "`Please set up the` **HEROKU_APP_NAME** `Var`"

                " to be able to deploy your userbot...`"

            )

            repo.__del__()

            return

        for app in heroku_applications:

            if app.name == HEROKU_APP_NAME:

                heroku_app = app

                break

        if heroku_app is None:

            await event.edit(

                f"{txt}\n" "`Invalid Heroku credentials for deploying userbot dyno.`"

            )

            return repo.__del__()

        await event.edit(

            "`Userbot dyno build in progress, please wait until the process finishes it usually takes 4 to 5 minutes .`"

        )

        ups_rem.fetch(ac_br)

        repo.git.reset("--hard", "FETCH_HEAD")

        heroku_git_url = heroku_app.git_url.replace(

            "https://", "https://api:" + HEROKU_API_KEY + "@"

        )

        if "heroku" in repo.remotes:

            remote = repo.remote("heroku")

            remote.set_url(heroku_git_url)

        else:

            remote = repo.create_remote("heroku", heroku_git_url)

        try:

            remote.push(refspec="HEAD:refs/heads/master", force=True)

        except Exception as error:

            await event.edit(f"{txt}\n`Here is the error log:\n{error}`")

            return repo.__del__()

        build = app.builds(order_by="created_at", sort="desc")[0]

        if build.status == "failed":

            await event.edit(

                "`Build failed!\n" "Cancelled or there were some errors...`"

            )

            await asyncio.sleep(5)

            return await event.delete()

        await event.edit("`Successfully deployed!\n" "Restarting, please wait...`")

    else:

        await event.edit("`Please set up`  **HEROKU_API_KEY**  ` Var...`")

    return





@bot.on(admin_cmd(outgoing=True, pattern=r"shift$"))



async def upstream(event):

    event = await event.edit("`Pulling the Godhackerzuserbot repo wait a sec ....`")

    off_repo = "https://github.com/rohithaditya/Godhackerz-userbot"

    cmd = f"rm -rf .git"

    try:

        await runcmd(cmd)

    except BaseException:

        pass

    try:

        txt = "`Oops.. Updater cannot continue due to "

        txt += "some problems occured`\n\n**LOGTRACE:**\n"

        repo = Repo()

    except NoSuchPathError as error:

        await event.edit(f"{txt}\n`directory {error} is not found`")

        return repo.__del__()

    except GitCommandError as error:

        await event.edit(f"{txt}\n`Early failure! {error}`")

        return repo.__del__()

    except InvalidGitRepositoryError:

        repo = Repo.init()

        origin = repo.create_remote("upstream", off_repo)

        origin.fetch()

        repo.create_head("master", origin.refs.master)

        repo.heads.master.set_tracking_branch(origin.refs.master)

        repo.heads.master.checkout(True)

    try:

        repo.create_remote("upstream", off_repo)

    except BaseException:

        pass

    ac_br = repo.active_branch.name

    ups_rem = repo.remote("upstream")

    ups_rem.fetch(ac_br)

    await event.edit("`Deploying userbot, please wait....`")

    await deploy(event, repo, ups_rem, ac_br, txt)
