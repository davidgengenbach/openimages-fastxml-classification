function fastXML_train(trn_X_Xf, trn_X_Y, param, model_folder)

    addpath('../Tools');
    
    file_trn_X_Xf = tempname;
    write_text_mat(trn_X_Xf,file_trn_X_Xf);
    
    file_trn_X_Y = tempname;
    write_text_mat(trn_X_Y,file_trn_X_Y);

	clear trn_X_Xf trn_X_Y;

    cmd = sprintf('fastXML_train %s %s %s %s', file_trn_X_Xf, file_trn_X_Y, model_folder, get_arguments(param));
    if isunix
       cmd = ['./' cmd]; 
    end
    
	system(cmd);
end

function args = get_arguments(param)
	args = ' ';
	
	if isfield(param,'num_thread')
		args = sprintf(' %s -T %d',args,param.num_thread);
	end

	if isfield(param,'start_tree')
		args = sprintf(' %s -s %d',args,param.start_tree);
	end

	if isfield(param,'num_tree')
		args = sprintf(' %s -t %d',args,param.num_tree);
	end

	if isfield(param,'bias')
		args = sprintf(' %s -b %f',args,param.bias);
	end

	if isfield(param,'log_loss_coeff')
		args = sprintf(' %s -c %f',args,param.log_loss_coeff);
	end

	if isfield(param,'max_leaf')
		args = sprintf(' %s -m %d',args,param.max_leaf);
	end

	if isfield(param,'lbl_per_leaf')
		args = sprintf(' %s -l %d',args,param.lbl_per_leaf);
	end

end
