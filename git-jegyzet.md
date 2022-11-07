# Git
## Mi a Git?
A Git egy verzió követő rendszer ami a fájlokban történő módosításokat tárolja, így ezek a változtatások visszakövethetőek és visszaállíthatóak.\

## Hogyan működik a Git?
Egy projekt lokálisan és központi szerveren (Distributed Version Control) is tárolja az adatokat. Ennek köszönhetően nincs szükség állandó kapcsolatra a szerverrel.

## Branch

A branch-ekkel el lehtet különíteni és egyszerre több verziót is lehet tárolni.

Jelenlegi branch: `git branch`\
Új branch: `git branch pelda-pranch` / `git checkout -b pelda-pranch`\
Branch törlése: `git branch -d pelda-pranch`\
Váltás branch-ek között: `git checkout pelda2-branch`

## Parancsok

|Parancs|Mit csinál|Példák|
|:---|:---|:---|
|git init|Könyvtár létrehozása|`git init pelda`|
|git add|Fájlok színpadra helyezése (stage)|`git add pelda.txt` && `git add .`|
|git reset|Fájlok eltávolítása a színpadról|`git reset pelda.txt`|
|git rm|Fájlok törlése|`git rm pelda.txt`|
|git restore|Fájl állapotának visszaállítása|`git restore `|
|git commit|Commit létrhozása|`git commit -m "Ez egy megjegyzés"`|
|git checkout|Branch kezelés|`git chekout pelda2-branch`|
|git branch|Branch kezelés|`git branch `|
|git remote|Távoli könyvtár kezelése|`git remote add origin https://github.com/peldanev/pelda` && `git remote rm https://github.com/peldanev/pelda`|
|git config|Git beállítások|`git --global user.email pelda@gmail.com` && `git --global user.name peldanev`|
|git push|Távoli könytárba való feltöltés|`git push -u origin pelda-branch`|
|git pull|Távoli könytárból való változások leöltés|`git pull origin master --allow-unrelated-hitories`|
|git status|Információ a lokális könyvtárról|
|git diff|Külömbségek távoli és lokális könyvtár között|`git diff HEAD` && `git diff pelda.txt`|
|git clone|Távoli könytár letöltése|`git clone https://github.com/peldanev/pelda`|
