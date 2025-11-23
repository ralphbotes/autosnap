1. Get the folder path.
    Example: C:\Users\YOU\Downloads\autosnap\

2. Open PowerShell and run:
    cd [paste_path_here]

    Example: cd C:\Users\YOU\Downloads\autosnap\

3. Run following command to start:
    .\run.ps1


# Note:
    If PowerShell complains about permission issues, fix your user policy:
        Set-ExecutionPolicy -Scope CurrentUser RemoteSigned

4. To stop:
   Ctrl + C