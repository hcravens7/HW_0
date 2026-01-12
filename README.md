# Assignment 0 — Tools Bootcamp 

**Points:** 0 (optional, but strongly recommended)

## Why we’re doing this

This assignment is **not required for course credit** and is worth **0 points**.

However:

> If you do **not** complete this practice assignment, you are **not eligible for leniency or extensions** on future assignments due to **technical issues** (e.g., GitHub problems, Gradescope submission issues, environment setup issues, etc.).

The goal is to make sure everyone has practiced the full workflow *before* it counts.

## Learning goals

By the end of this assignment you will be able to:
- Create a GitHub account (if needed) and connect it to our course roster
- Accept a GitHub Classroom assignment and get your own repository
- Clone a repository and work locally
- Create a branch, commit changes, and push them to GitHub
- Open and merge a Pull Request (PR)
- Merge an **instructor update** via GitHub Classroom
- Pull updates to your local machine
- Run tests and a style checker locally
- Submit a GitHub repository to Gradescope
- Read autograder output, fix issues, and resubmit

## Part 0 — GitHub + GitHub Classroom setup

### Step 0A: Create a GitHub account (if you don’t already have one)
1. Go to https://github.com and create an account.
2. Choose a username you are comfortable using professionally.
3. Verify your email address.

If you already have a GitHub account, you can skip this step.

### Step 0B: Accept the GitHub Classroom assignment and link your name
1. Click the GitHub Classroom invite link posted on Canvas.
2. Log in to GitHub if prompted.
3. When asked, **select your name from the course roster**.
   - This step is required so we can associate your repository with you.
4. Accept the assignment and wait for your repository to be created.

If you do **not** see your name in the roster list, stop and contact us before continuing.

## Part 1 — Install Git (if needed)

### Check whether Git is already installed
In Terminal (macOS/Linux) or Git Bash / PowerShell (Windows), run:
```bash
git --version
```

If you see a version number, Git is installed and you can continue.

### Install Git if needed

#### macOS
```bash
xcode-select --install
```
or download Git from https://git-scm.com/download/mac

#### Windows
Download and install **Git for Windows**:
https://git-scm.com/download/win  
Accept the default options.

#### Linux
```bash
sudo apt install git
```

### Configure your Git name and email (required once)
These identify you as the author of your commits.

```bash
git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"
```

## Part 2 — Find and clone your repository

### Step 2A: Find your repository on GitHub
1. Go to https://github.com
2. Click your profile picture (top right)
3. Select **Your repositories**
4. Click the repository created by GitHub Classroom for this assignment

You should see files like `practice.py` and `README.md`.

### Step 2B: Copy your repository URL
1. Click the green **Code** button
2. Make sure **HTTPS** is selected
3. Click the copy icon next to the URL

Example:
```
https://github.com/<course-org>/<your-repo-name>.git
```

### Step 2C: Clone the repository to your computer

**Cloning** means making a local copy of the repository on your computer.

```bash
git clone <PASTE_THE_URL_YOU_COPIED>
cd <your-repo-name>
```

You are now working **locally**.

## Part 3 — Install required Python tools

This assignment uses:
- `pytest` — runs automated tests
- `pylint` — a **linter**, which checks code style and common mistakes

```bash
python -m pip install -r requirements.txt
```

If this fails, ask for help before continuing.

## Part 4 — Work on a branch and open a Pull Request

### What is a branch (and why use one)?

A **branch** is a separate line of development.
- `main` is the official version of your code.
- You do your work on a branch so mistakes don’t affect `main`.

### Step 4A: Create a branch named `part-4`
```bash
git checkout -b part-4
```

### Step 4B: Edit `practice.py`
Open `practice.py` and complete the TODOs.

All code for this assignment goes in this file.

**Important: Do not edit config files**

For this assignment, **do not change** any of the following files:

- `.pylintrc`
- `.gitignore`
- `requirements.txt`

These files control the tools used by the autograder (and by our course workflow).  
If you change them, your code may work on your computer but fail on Gradescope.

**Only edit:** `practice.py`

If you already changed one of these files by accident, undo it with:
```bash
git checkout -- .pylintrc .gitignore requirements.txt
```

### Step 4C — Run tests and record proof that you ran them

You will run some tests on your code locally via `pytest` to confirm your setup works.

```bash
pytest
```

When pytest finishes, it prints a line like:
```
===================== 6 passed in 0.03s =====================
```

Copy that line and paste it as a **comment at the very top of `practice.py`**.

Example:
```python
# pytest output: ===================== 6 passed in 0.03s =====================
```

This is required.

The local tests we provide are a small “smoke test.” Gradescope runs additional tests via the Autograder that may be different. If Gradescope fails but your local tests pass, read the Gradescope output and update your code accordingly.

### Step 4D — Run the linter

Run the `pylint` via:

```bash
pylint practice.py
```

A **linter** checks formatting and common mistakes.
You do not need to understand every message — just fix a few until it passes.

You should see a Pylint 'score', copy your score and paste it as a **comment below your pytest output comment**.

Example:
```python
# pytest output: ===================== 6 passed in 0.03s =====================
# pylint score: 4
```

This is required.

For now, do not worry about what is considered a 'good' pylint score.

### Step 4E — Commit and push your changes

**Committing** saves a snapshot of your work locally.  
**Pushing** uploads those commits to GitHub.

Commit and push your changes via:

```bash
git add practice.py
git commit -m "Complete Assignment 0"
git push -u origin part-4
```

### Step 4F — Open and merge a Pull Request

A **Pull Request (PR)** is how changes become part of `main`.

1. Go to your repository on GitHub
2. Click **Compare & pull request**
3. Make sure it shows `part-4 → main`
4. Open the PR
5. Review the changes
6. Click **Merge pull request**

Then update your local copy:
```bash
git checkout main
git pull
```

## Part 5 — Merge the instructor update

After we create the repositories in class, we will push an update to the starter code.

### What to do
1. Go to your GitHub repository
2. Open the PR titled something link **“Update from starter code”**
3. Read the changes
4. Merge the PR into `main`

Then pull the update locally:
```bash
git checkout main
git pull
```

Update your code if needed.

After updating, **run pytest again** and **update the pytest output comment**.

## Part 6 — Submit to Gradescope

### Submit your repository
On Gradescope:
1. Select this assignment
2. Choose **GitHub** as the submission method
3. Select your repository and submit

**Do not upload a zip file.**

If the autograder reports failures:
- fix them locally,
- commit and push,
- resubmit.

## Completion verification (what counts as “done”)

This assignment is considered **complete** if all of the following are true:

- [ ] Repository created via GitHub Classroom
- [ ] Branch created and merged via PR
- [ ] Instructor update PR merged
- [ ] `pytest` run and output recorded in `practice.py`
- [ ] `pylint practice.py` run
- [ ] Repository submitted to Gradescope
- [ ] Final Gradescope submission passes

## Why this matters for the rest of the course

Future assignments will assume you can:
- use GitHub Classroom,
- run tests and linters locally,
- submit repositories to Gradescope,
- and interpret autograder feedback.

If you encounter technical issues later **and you did not complete this assignment**, those issues will **not** be grounds for deadline extensions or leniency.

## Getting help early

If something goes wrong:
- stop early,
- copy the **exact error message**,
- and ask for help during office hours or on Ed Discussion.

This assignment is designed so that getting help now prevents bigger problems later.

