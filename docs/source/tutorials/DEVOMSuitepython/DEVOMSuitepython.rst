DEVCOMSuitepython Pipeline: Gene Importance, Causal Signal Flow and SURD
=======================================================================

Data
====

- **Data source**: `Google Drive folder <https://drive.google.com/drive/folders/1KjQzdxW56pbZlQtwyb7e-GhN1XbgT1Rd>`_

All paths below are given relative to your project root. Adjust them to match your own directory structure if needed.

-------------------------------------------------------------------------------

1. Gene Importance Core
=======================

.. code-block:: python

   import scanpy as sc
   from DEVCOMSuitepython.CCI_importance_core import compute_gene_importance_all

   cell_types = ["Endothelial", "Erythrocyte"]

   res = compute_gene_importance_all(
       cell_types=cell_types,
       input_dir="./DEVCOM Suite test/tests/testthat/gene importance/",
       output_dir="./DEVCOM Suite test/tests/testthat/gene importance/",
       expr_suffix="_gene_expression.csv",
       threshold_pcc=0.8,
       threshold_p_value=0.05,
       lambda_factor=0.1,
       n_jobs=None,   # None = auto
       verbose=True
   )

**Example console output**

.. code-block:: text

   开始处理所有细胞类型: ['Endothelial', 'Erythrocyte']
   使用进程数: 2
   [Endothelial] 读取表达矩阵: /home/wgh/DEVCOM Suite test/tests/testthat/gene importance/Endothelial_gene_expression.csv
   [Erythrocyte] 读取表达矩阵: /home/wgh/DEVCOM Suite test/tests/testthat/gene importance/Erythrocyte_gene_expression.csv

   [Endothelial] 过滤所有样本表达量均为 0 的基因...
   [Endothelial] 开始计算 PCC 和 p 值...
   [Erythrocyte] 过滤所有样本表达量均为 0 的基因...
   [Erythrocyte] 开始计算 PCC 和 p 值...
   [Erythrocyte] 开始进行多重检验校正 (FDR-BH)...
   [Erythrocyte] 开始构建基因网络...
   [Erythrocyte] 开始计算基因重要性得分...
   [Endothelial] 开始进行多重检验校正 (FDR-BH)...
   [Endothelial] 开始构建基因网络...
   [Erythrocyte] 基因重要性得分已保存为: /home/wgh/DEVCOM Suite test/tests/testthat/gene importance/Erythrocyte_gene_importance_scores.csv
   [Endothelial] 开始计算基因重要性得分...
   [Endothelial] 基因重要性得分已保存为: /home/wgh/DEVCOM Suite test/tests/testthat/gene importance/Endothelial_gene_importance_scores.csv

-------------------------------------------------------------------------------

2. Causal Signal-Flow Inference (FlowSig)
=========================================

.. code-block:: python

   import scanpy as sc
   from DEVCOMSuitepython.flowsig_prior_from import run_flowsig_pipeline

   adata = sc.read("/home/wgh/DEVCOM Suite test/tests/testthat/flow/burkhardt21_merged.h5ad")

   run_flowsig_pipeline(
       adata,
       prior_csv       = "./DEVCOM Suite test/tests/testthat/flow/human_L-R-TF_develop_filtered_LR_TF_top5000.csv",
       condition_key   = "Condition",
       control_name    = "Ctrl",
       construct_gems  = True,
       n_gems          = 10,
       counts_layer    = "counts",
       inflow_construction = "v1",
       edge_threshold  = 0.7,
       save_h5ad       = "./DEVCOM Suite test/tests/testthat/flow/burkhardt21_merged_flow_learned.h5ad"
   )

**Example console output**

.. code-block:: text

   Removing 37 genes not expressing in Ctrl.
   100%|██████████| 30/30 [00:59<00:00,  1.97s/it]
   ... storing 'Type' as categorical
   ... storing 'Downstream_TF' as categorical
   ... storing 'Type' as categorical
   ... storing 'Downstream_TF' as categorical
   Starting 50 bootstraps on 1 cores …
   100%|██████████| 50/50 [23:58<00:00, 28.78s/it]
   Finished in 1,439.0 s
   AnnData object with n_obs × n_vars = 5305 × 18027
       obs: 'sample_labels', 'Donor', 'Condition', 'library_size', 'n_genes_by_counts', 'total_counts', 'total_counts_mt', 'pct_counts_mt', 'doublet_score', 'predicted_doublet', 'n_counts', 'log_counts', 'n_genes', 'leiden', 'Type'
       var: 'gene_symbols', 'mt', 'n_cells_by_counts', 'mean_counts', 'pct_dropout_by_counts', 'total_counts', 'n_cells', 'highly_variable', 'means', 'dispersions', 'dispersions_norm', 'highly_variable_nbatches', 'highly_variable_intersection'
       uns: 'Condition', 'Condition_colors', 'Donor_colors', 'NMF_10', 'NMF_CV', 'Type', 'base_networks', 'base_networks_leiden', 'causal_networks', 'causal_networks_leiden', 'cellchat_output', 'cpdb_Type', 'flowsig_network', 'flowsig_network_cpdb', 'flowsig_network_cpdb_orig', 'flowsig_network_orig', 'hvg', 'learned_networks', 'leiden', 'leiden_colors', 'log1p', 'neighbors', 'pca', 'pyliger', 'pyliger_10', 'pyliger_11', 'pyliger_12', 'pyliger_15', 'pyliger_20', 'pyliger_3', 'pyliger_5', 'pyliger_8', 'pyliger_9', 'pyliger_info', 'pyliger_vars', 'sample_labels_colors', 'scrublet', 'umap'
       obsm: 'X_SC', 'X_celltype_ligand', 'X_celltype_ligand_leiden', 'X_flow', 'X_flow_cpdb', 'X_flow_cpdb_orig', 'X_flow_orig', 'X_gem', 'X_pca', 'X_umap'
       varm: 'PCs'
       layers: 'counts', 'normalized'
       obsp: 'connectivities', 'distances'

-------------------------------------------------------------------------------

3. Interpretable Causal Signal Flow with SURD
=============================================

3.1 Running SURD Segments
-------------------------

.. code-block:: python

   import scanpy as sc

   # from surd_segments_api import load_surd_from_dir
   # utils file
   # load_surd_from_dir("/home/wgh/SOUD/SURD-main/utils")

   from DEVCOMSuitepython.utils.surd import surd
   from DEVCOMSuitepython.surd_segments import run_surd_segments
   import DEVCOMSuitepython.surd_segments as ss

   ss.surd = surd

   adata = sc.read("/home/wgh/DEVCOM Suite test/tests/testthat/SURD/burkhardt21_merged_flow_learned.h5ad")

   res = run_surd_segments(
       adata,
       ctrl_name  = "Ctrl",   # condition control
       treat_name = "IFNg",   # condition treat
       out_dir    = "./",
       fast_mode  = True
   )

**Example console output**

.. code-block:: text

   [SURD] condition_key = Condition
   [SURD] condition value_counts = {'IFNg': 3129, 'Ctrl': 2176}
   [SURD] celltype_key = Type, n_types = 3
   [SURD] picked adjacency from uns path: flowsig_network.network.adjacency_validated, shape=(236, 236)
   [SURD] matched_groups = 3, total_treat_cells = 3129
   [SURD] inflows=180, gems=10, outflows=46
   [SURD] graph_edges=734, inflow->GEM edges=247, GEM->outflow edges=161

-------------------------------------------------------------------------------

4. KNN Sweep for SURD (K Selection)
===================================

.. code-block:: python

   import os
   import scanpy as sc

   from DEVCOMSuitepython.utils.surd import surd
   from DEVCOMSuitepython.surd_segments import run_surd_k_sweep
   import DEVCOMSuitepython.surd_segments as ss

   ss.surd = surd

   adata = sc.read("./DEVCOM Suite test/tests/testthat/SURD/burkhardt21_merged_flow_learned.h5ad")

   # 2) Path settings
   DATA_DIR = "./DEVCOM Suite test/tests/testthat/SURD/"

   H5AD_OUT = os.path.join(
       DATA_DIR,
       "burkhardt21_merged_SURD.h5ad"
   )

   # Output directory of the main SURD pipeline
   # (should already contain gem2out_unique_synergy_redundancy.csv)
   SEGMENTS_DIR = os.path.join(
       DATA_DIR,
       "surd_segments_results"
   )

   # IMPORTANT: only join the file name here, do NOT prepend an absolute path again
   parent_csv_path = os.path.join(
       SEGMENTS_DIR,
       "gem2out_unique_synergy_redundancy.csv"
   )

   # 3) Load h5ad
   adata = sc.read(H5AD_OUT)

   # 4) Run K sweep (post-hoc)
   k_df, best_row = run_surd_k_sweep(
       adata,
       ctrl_name="Ctrl",
       treat_name="IFNg",
       parent_csv_path=parent_csv_path,
       out_dir=SEGMENTS_DIR,          # K sweep results will also be written here
       k_range=range(1, 21),
       top_parents_per_target=8,
       n_perm_small=50,
       nbins_target=16,
       min_bins_per_dim=6,
       max_total_bins=20_000_000,
       discretize="quantile",
       min_samples_block=100,
       make_plots=True,
   )

   print("K sweep finished. Results written to:",
         os.path.join(SEGMENTS_DIR, "k_sweep_summary.csv"))

   if best_row is not None:
       print("Best K:", int(best_row["K"]), "score =", float(best_row["score"]))
   else:
       print("No valid blocks found, k_df is empty. "
             "Please check the parent CSV or condition column.")

**Example console output**

.. code-block:: text

   [load_surd_from_dir] 已从 /home/wgh/SOUD/SURD-main/utils 导入 surd()
   K 扫描完成：结果写入： /home/wgh/DEVCOM Suite test/tests/testthat/SURD/surd_segments_results/k_sweep_summary.csv
   最佳 K: 9 score = 0.9969896487413793
