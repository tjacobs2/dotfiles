" set tabstops and auto-indent to be 2 spaces
set tabstop=4
set sw=4

" allow mouse scrolling
set mouse=a

" prevent dark blue on black background
set bg=dark

" look back in the directory tree until we find a tags file
set tags=./tags;/

" allow definition searching with cscope
set cscopetag
set csto=1

" allow bash-like completion of characters
set wildmode=longest,list,full
set wildmenu

" change current dir to be dir of buffer
set autochdir

" enable syntax highlighting
syntax on

" allow w!! to write files that I forgot to open as 'sudo'
cmap w!! %!sudo tee > /dev/null %
set backspace=2
set nu
set nowrap
set ai
set hlsearch
set viminfo='1000,f1,:1000,/1000

" map <C-\> to open function definition in a new tab
map <C-\> :tab split<CR>:exec("tag ".expand("<cword>"))<CR>

"set F7 and F8 to change tabs
map <F7> :tabp<CR>
map <F8> :tabn<CR>
map :sh :ConqueTermSplit bash
nmap <C-N><C-N> :set invnumber<CR>
set history=500
nnoremap <F2> :set invpaste paste?<CR>
set pastetoggle=<F2>
set showmode
filetype plugin on
set ofu=syntaxcomplete#Complete
" when we reload, tell vim to restore the cursor to the saved position
augroup JumpCursorOnEdit
 au!
 autocmd BufReadPost *
 \ if expand("<afile>:p:h") !=? $TEMP |
 \ if line("'\"") > 1 && line("'\"") <= line("$") |
 \ let JumpCursorOnEdit_foo = line("'\"") |
 \ let b:doopenfold = 1 |
 \ if (foldlevel(JumpCursorOnEdit_foo) > foldlevel(JumpCursorOnEdit_foo - 1)) |
 \ let JumpCursorOnEdit_foo = JumpCursorOnEdit_foo - 1 |
 \ let b:doopenfold = 2 |
 \ endif |
 \ exe JumpCursorOnEdit_foo |
 \ endif |
 \ endif
 " Need to postpone using "zv" until after reading the modelines.
 autocmd BufWinEnter *
 \ if exists("b:doopenfold") |
 \ exe "normal zv" |
 \ if(b:doopenfold > 1) |
 \ exe "+".1 |
 \ endif |
 \ unlet b:doopenfold |
 \ endif
augroup END

