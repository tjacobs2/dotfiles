#tmux set -g status-fg black
#if [[ `hostname -s` = killdevil* ]]; then
#	tmux set -g status-bg white
#fi
#
if [[ `hostname -s` = koblet* ]]; then
	tmux set -g status-bg cyan
	tmux set -g status-fg black
fi

if [[ `hostname -s` = contador* ]]; then
	tmux set -g status-bg green
	tmux set -g status-fg black
fi

# Path to your oh-my-zsh configuration.
ZSH=$HOME/.oh-my-zsh

# Set name of the theme to load.
# Look in ~/.oh-my-zsh/themes/
# Optionally, if you set this to "random", it'll load a random theme each
# time that oh-my-zsh is loaded.
ZSH_THEME="timjacobs"

# Set to this to use case-sensitive completion
# CASE_SENSITIVE="true"

# Comment this out to disable weekly auto-update checks
DISABLE_AUTO_UPDATE="true"

#Disable auto title renaming (for tmux)
DISABLE_AUTO_TITLE=true

# Uncomment following line if you want to disable colors in ls
# DISABLE_LS_COLORS="true"

# Uncomment following line if you want to disable autosetting terminal title.
# DISABLE_AUTO_TITLE="true"

# Uncomment following line if you want red dots to be displayed while waiting for completion
# COMPLETION_WAITING_DOTS="true"

# Which plugins would you like to load? (plugins can be found in ~/.oh-my-zsh/plugins/*)
# Example format: plugins=(rails git textmate ruby lighthouse)
plugins=(git osx svn)

source $ZSH/oh-my-zsh.sh

bindkey -e
#bindkey "^R" history-incremental-search-backward

# only space for word delimiter
export WORDCHARS="*?_-.[]~=/&;!#$%^(){}<>"

#disable autocorrection
unsetopt correct_all

__git_files () { 
    _wanted files expl 'local files' _files 
}

function git_prompt_info() {
  ref=$(git symbolic-ref HEAD 2> /dev/null) || return
  echo "$ZSH_THEME_GIT_PROMPT_PREFIX${ref#refs/heads/}$ZSH_THEME_GIT_PROMPT_SUFFIX"
}

# Customize to your needs...
export PATH=/usr/local/bin:$PATH:/usr/bin:/bin:/usr/sbin:/sbin:/usr/X11/bin:~/bin:~/Dropbox/TODO

export PYTHONPATH=/Users/tim/bin/pymol_scripts:/Users/tjacobs2/workspace/rosetta_extras/tools/python_pdb_structure:/Applications/MacPyMOL.app/pymol/

export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8

source ~/.nvm/nvm.sh

PATH=$PATH:$HOME/.rvm/bin # Add RVM to PATH for scripting
