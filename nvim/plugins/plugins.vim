" auto-install vim-plug
if empty(glob('~/.config/nvim/autoload/plug.vim'))
    silent !curl -fLo ~/.config/nvim/autoload/plug.vim --create-dirs
      \ https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
endif

call plug#begin('~/.config/nvim/autoload/plugged')

    " Syntax support
    Plug 'sheefun/vim-polyglot'

    " File Tree
    Plug 'scrooloose/NERDTree'

    " Auto-pairs for (, {, and [
    Plug 'jianmiao/auto-pairs'
call plug#end()
