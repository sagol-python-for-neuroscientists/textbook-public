# Lessons and thoughts for next year

* Should JupyterLab receive a recommendation when reviewing IDEs? As of early 2020 it isn't a polished product yet, but they did just added a debugger, and it might be a whole lot better in early 2021.
* Every class that occurs after HW submission should start with a review of the submitted HW, even if a few students were allowed delayed submission. Reviewing the "correct" code is important, and seeing how good Python code looks like is eye-opening.
* Currenlty I ask Windows-students to change their default terminal to the command prompt. The new Windows Terminal is almost released. Will it be a better fit for the course?
* Environments - the current situation in the Python ecosystem is crap. `conda` sucks, but it's currently the best option. As of early 2020, poetry seems promising but it still has issues. If these are resolved by next year then it perhaps should be the default for our students, it might be simpler to explain as well. If not, then perhaps `virtualenv` + `pyenv` (currently doesn't really work on windows, but it does on WSL. So if WSL becomes available in all windows machines it could work) is the best solution to teach the students. Not sure...
* Class 3 has a pretty thorough demo on environments, git and VSCode. Basically setting it all up from scratch. This is extremely important for the students. However - these aren't recorded\documented anywhere, since it's done "live" from VSCode. I need to record a screencast.
* In the beginning of class 4, before or after HW review, I do another git + conda overview.
* OOP (Class 3): Many improvements were made in 2020, but these are perhaps not enough. For example, the start of class 4 is about inheritance, including an exercise. Perhaps mentioning inheritance is important, but I don't think that this exercise is necessary. Perhaps we should start the numpy part earlier.
* HW3 - FolderIterator question is a difficult nut to crack. It's "technical" in a way, but it also has some very important aspects to it. It forces people to debug their code, it makes them use Pathlib (somewhat) effectively, it teaches about properties of different collections (inserting new keys in dicts overrides existing ones, list(set(list())) destroys ordering) but it also keeps giving students the sense that everything they're doing is right, but the tests are wrong.
* Move the "assignment 2 comments" from the start of class 4 to the start of class 3, or perhaps class 2?
* Seaborn should receive a larger emphasis when plotting. Bascially 99% of plots can be accomplished using seaborn with ease. If we start numpy earlier then seaborn can take more space, instead of the unneeded parts on OOP.
* Computational pipelines library? Dask? Luigi? Something simpler?
*
