# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'DEVOM'
copyright = '2025, wuguanhao'
author = 'wuguanhao'
release = '0.1.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# extensions = []

templates_path = ['_templates']
exclude_patterns = []
templates_path = ['_templates']
exclude_patterns = []

# Sphinx 扩展
extensions = [
    'nbsphinx',   # 允许解析 Jupyter Notebook
    'sphinx.ext.mathjax',  # 支持数学公式
    'sphinx.ext.githubpages'  # 可选，用于 GitHub Pages 部署
]

# 确保 Sphinx 忽略 .ipynb 生成的输出缓存
nbsphinx_allow_errors = True  # 允许 Notebook 代码执行时出错（可选）
exclude_patterns = ['build', '**.ipynb_checkpoints']  # 忽略 Jupyter Notebook 的缓存文件
nbsphinx_execute = 'never'


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']



