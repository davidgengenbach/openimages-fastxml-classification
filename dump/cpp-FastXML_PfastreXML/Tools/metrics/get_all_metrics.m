function metrics = get_all_metrics(score_mat, tst_lbl_mat, inv_prop)

	%% Inputs:
	%%	score_file: test label scores matrix file in sparse format
	%%	tst_lbl_file: test label ground truth matrix file in sparse format
	%%		sizes of matrices in score_file and tst_lbl_file must match, otherwise code will break
	%%  inv_prop: inverse propensity label weights, calculated using "inv_propensity" function

	%% Prints and returns:
	%% - precision at 1--5
	%% - nDCG at 1--5
	%% - propensity weighted precision at 1--5
	%% - propensity weighted nDCG at 1--5

	
	fprintf('precision at 1--5\n');
	prec = precision_k(score_mat,tst_lbl_mat,5);
	disp(prec);
	metrics.prec_k = prec;

	fprintf('nDCG at 1--5\n');
	nDCG = nDCG_k(score_mat,tst_lbl_mat,5);
	disp(nDCG);
	metrics.nDCG_k = nDCG;

	fprintf('propensity weighted precision at 1--5\n');
	prec_wt = precision_wt_k(score_mat,tst_lbl_mat,inv_prop,5);
	disp(prec_wt);
	metrics.prec_wt_k = prec_wt;

	fprintf('propensity weighted nDCG at 1--5\n');
	nDCG_wt = nDCG_wt_k(score_mat,tst_lbl_mat,inv_prop,5);
	disp(nDCG_wt);
	metrics.nDCG_wt_k = nDCG_wt;

end
