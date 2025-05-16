To achieve 0.736 configure:
gap-text2sql/mrat-sql-gap/seq2struct/models/spider/spider_enc.py line 30 

langdata = simplemma.load_data('en')
#langdata = simplemma.load_data('pt','en')
#langdata = simplemma.load_data('en','pt','es','fr')

using 
#langdata = simplemma.load_data('en')
#langdata = simplemma.load_data('pt','en')
langdata = simplemma.load_data('en','pt','es','fr')

the result is 0.735