(general-setup)=

# General Setup

## Installing Python

<center><img src="https://www.python.org/static/community_logos/python-logo-master-v3-TM-flattened.png" width="200px"></img></center>

Please follow the [Real Python](https://realpython.com/) website's [excellent tutorial](https://realpython.com/installing-python/) to setup Python on your operating system.

## Installing an IDE

<center><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Visual_Studio_Code_1.35_icon.svg/1200px-Visual_Studio_Code_1.35_icon.svg.png" width="100px"></img></center><br />

Now that you have Python installed, you're going to want to write some code to run with it. Python code can be written in any editor, as long as the file is saved with a `.py` suffix. However, not all editors were made equal. In this course, I _highly recommend_ using [Visual Studio Code (VSCode)](https://code.visualstudio.com) as your main editor, especially if you have no prior Python experience.

- Download and install VSCode from its [download page](https://code.visualstudio.com/Download).
- Install the Python Extension:
  - Inside VSCode press the <img src="vsc_extensions.png" alt="VSC Extensions Marketplace" width="30" style="display:inline"></img> (or Ctrl+Shift+X), search for Python and install it.
    _or_
  - From the VSC Marketplace website ([here](https://marketplace.visualstudio.com/items?itemName=ms-python.python)).
- Help VSCode find your Python installation. After opening a `.py` file (you can create one just for this purpose), click on the yellow "Select Python Environment" button on the bottom left side of your screen and select the latest installed Python version.

:::{note}
If you're on a Windows machine, it's better to change the default VSCode terminal to the command prompt. Do so by opening the bottom terminal ("View" -> "Terminal", or Ctrl+\`), click the downfacing arrow to the left of the "+" sign, click "Select default shell" in the menu and choose the command prompt (`cmd`). You'll need to re-open VSCode for this change to take effect.
:::

## Installing Git

<center><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Git-logo.svg/1024px-Git-logo.svg.png" width="120px"></img></center><br />

Code is archived and catalogued using [version control](https://en.wikipedia.org/wiki/Version_control). The application we'll use in this course (and by far the most popular choice) is [`git`](https://git-scm.com/), complemented with [GitHub](https://www.github.com), which we will use to store our archive online and share it.

- Install `git` from the [download page](https://git-scm.com/downloads).
- Before using it you'll have to tell `git` who you are. Open a new command-line or terminal instance and write the following two commands (with the values between `< >` replaced):

  ```bash
  git config --global user.name "<MY_NAME>"
  git config --global user.email "<MY_EMAIL_ADDRESS>"
  ```

  This user profile will identify you whenever you make any commits in the future.
