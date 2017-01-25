function split = load_split(dset,varargin)
    global EXP_DIR;
    sno = 0;
    if nargin>1
        sno = varargin{1};
    end
    split = csvread(sprintf('%s/Datasets/%s/split.%d.txt',EXP_DIR,dset,sno));
end