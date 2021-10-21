source $HOME/.config/nvim/plugins/plugins.vim "This needs to be line one.

" Gruvbox theme
autocmd vimenter * ++nested colorscheme gruvbox

" NERDTree Map
map <C-f> :NERDTreeToggle<CR>

" Terminal Map
map <C-x> :FloatermToggle<CR>



"Binds
set number 
set encoding=utf8
set nowrap
set ignorecase
set mouse=a "Enable mouse usage
set autoread "Update file if edited elsewhere
set hlsearch "Search highlight
set noerrorbells
set noswapfile
set expandtab "Spaces, no tabs
set tabstop=2
set ai "Auto indent
