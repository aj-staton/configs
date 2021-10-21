" auto-install vim-plug
if empty(glob('~/.config/nvim/autoload/plug.vim'))
    silent !curl -fLo ~/.config/nvim/autoload/plug.vim --create-dirs
      \ https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
endif

call plug#begin('~/.config/nvim/autoload/plugged')

    " Syntax support
    Plug 'sheerun/vim-polyglot'

    " File Tree
    Plug 'scrooloose/NERDTree'

    " Terminal
    Plug 'voldikss/vim-floaterm'

    " Auto-pairs for (, {, and [
    Plug 'jiangmiao/auto-pairs'

    " Color Scheme
    Plug 'rafi/awesome-vim-colorschemes'

call plug#end()
