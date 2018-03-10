# MachineLearningReference
 @AUTHOR TREVOR KNOTT
 @EMAIL tk@trevorknott.io
 @LanguagesHere Python, Shell, Markdown

TODO: Write a project description

## Installation

TODO: Describe the installation process

## Usage

TODO: Write usage instructions

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## History

Used a book which taught me alot: 
    \\*Hands-On Machine Learning with Scikit-Learn and TensorFlo*\\

## Other Reference - Books Used With, Etc

1. http://shop.oreilly.com/product/0636920052289.do
2. ...



## Shell Commiting
```
Place in ~/.bash_profile (bashrc is for every instantiation of terminal)
```

```
# @SHELL_SCRIPT
# VARS BY TREV
    function gam() {
        date_custom=$(date '+%d/%m/%Y %H:%M:%S');
        commit_ending=" || @TK - $date_custom"

        echo "Commit Ending:  $commit_ending"

        echo '1) Adding . in Repo: '
        git add .
    
        echo '2) Enter Your Git Commit Message: '
        read $1

        echo `git commit -m $1$commit_ending && git push`
    }

# END BY TREV
```


## License

Trevcense @2017
Mojo @Copyright Trevor 'Tex' Knott