function [X_Xf,X_Y,X,Xf,Y] = load_dataset(dset)
    %%% [X_Xf,X_Y,X,Xf,Y] = load_dataset(dset)
    global EXP_DIR;
    load(sprintf('%s/Datasets/%s/X_Y.mat',EXP_DIR,dset));
    load(sprintf('%s/Datasets/%s/X_Xf.mat',EXP_DIR,dset));
    
    file = sprintf('%s/Datasets/%s/X.txt',EXP_DIR,dset);
    if nargout>=3 && exist(file, 'file') == 2
        fid = fopen(file,'r');
        X = textscan(fid,'%s','Delimiter','\n');
        X = X{1};
        fclose(fid);
    end
       
    file = sprintf('%s/Datasets/%s/Xf.txt',EXP_DIR,dset);
    if nargout>=4 && exist(file, 'file') == 2
        fid = fopen(file,'r');
        Xf = textscan(fid,'%s','Delimiter','\n');
        Xf = Xf{1};
        fclose(fid);
    end
    
    file = sprintf('%s/Datasets/%s/Y.txt',EXP_DIR,dset);
    if nargout>=5 && exist(file, 'file') == 2
        fid = fopen(file,'r');
        Y = textscan(fid,'%s','Delimiter','\n');
        Y = Y{1};
        fclose(fid);
    end
    
end