git remote -v
echo "---------------"
git fetch upstream
echo "---------------"
git merge upstream/main
echo "---------------"
git push origin main
