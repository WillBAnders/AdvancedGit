# Advanced Git Workshop

 - Slides: https://docs.google.com/presentation/d/1nbdKmQWBS2oqB7_AzSWjcOZ_lFYT3UOJvy3T18zJCo4/edit?usp=sharing

# Workshop 2A

One of your team members has started work on Issue #1, implementing the
custom_sqrt function. They have opened Pull Request #2 for these changes,
however in code review you notice their work doesn't meet the Git Workflow
standards for your company. Using history rewrites, help them update their PR.

You will need to decide what to do to improve the PR using what we've discussed
in Part 1 (slides above). Likewise, you will need to determine what commands
are needed to rewrite history (multiple approaches work).

<details> 
  <summary>Hint 1</summary>
  
> You can choose between combining both commits into a single one (easier) or
> rewriting both commits individually (harder, but more accurate).
</details>

<details> 
  <summary>Hint 2</summary>

> For combining both commits, the easiest way is through `git revert` and then
> creating an entirely new commit. To keep them separate, try `git rebase -i`
> (interactive mode).
</details>

# Workshop 2B

During your code review, another team member created and merged a PR that
conflicts with your code. Resolve the merge conflict.

<details> 
  <summary>Hint</summary>

> You can either use a rebase (preferred) or merge commit for this.
</details>


https://user-images.githubusercontent.com/32403644/215910777-12693f0c-ce2c-4976-86ea-90e109ebbccb.MOV

