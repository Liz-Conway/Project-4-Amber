name=django.static.bullshit
if [[ -e $name  ]] ; then
    i=1
    while [[ -e $name.$i ]] ; do
        let i++
    done
    name=$name.$i
fi
touch -- "$name"

pushToHeroku() {
    git add .

    git can

    git push heroku main --force

}

pushToHeroku