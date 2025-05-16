# Generated from sql/teradata/TeradataSQLExpressionsParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .TeradataSQLExpressionsParser import TeradataSQLExpressionsParser
else:
    from TeradataSQLExpressionsParser import TeradataSQLExpressionsParser

# This class defines a complete listener for a parse tree produced by TeradataSQLExpressionsParser.
class TeradataSQLExpressionsParserListener(ParseTreeListener):

    # Enter a parse tree produced by TeradataSQLExpressionsParser#query_expr.
    def enterQuery_expr(self, ctx:TeradataSQLExpressionsParser.Query_exprContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#query_expr.
    def exitQuery_expr(self, ctx:TeradataSQLExpressionsParser.Query_exprContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#query_term.
    def enterQuery_term(self, ctx:TeradataSQLExpressionsParser.Query_termContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#query_term.
    def exitQuery_term(self, ctx:TeradataSQLExpressionsParser.Query_termContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#with_deleted_rows.
    def enterWith_deleted_rows(self, ctx:TeradataSQLExpressionsParser.With_deleted_rowsContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#with_deleted_rows.
    def exitWith_deleted_rows(self, ctx:TeradataSQLExpressionsParser.With_deleted_rowsContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#as_json.
    def enterAs_json(self, ctx:TeradataSQLExpressionsParser.As_jsonContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#as_json.
    def exitAs_json(self, ctx:TeradataSQLExpressionsParser.As_jsonContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#select_list.
    def enterSelect_list(self, ctx:TeradataSQLExpressionsParser.Select_listContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#select_list.
    def exitSelect_list(self, ctx:TeradataSQLExpressionsParser.Select_listContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#top_n.
    def enterTop_n(self, ctx:TeradataSQLExpressionsParser.Top_nContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#top_n.
    def exitTop_n(self, ctx:TeradataSQLExpressionsParser.Top_nContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#normalize.
    def enterNormalize(self, ctx:TeradataSQLExpressionsParser.NormalizeContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#normalize.
    def exitNormalize(self, ctx:TeradataSQLExpressionsParser.NormalizeContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#all_operator.
    def enterAll_operator(self, ctx:TeradataSQLExpressionsParser.All_operatorContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#all_operator.
    def exitAll_operator(self, ctx:TeradataSQLExpressionsParser.All_operatorContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#selected_columns.
    def enterSelected_columns(self, ctx:TeradataSQLExpressionsParser.Selected_columnsContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#selected_columns.
    def exitSelected_columns(self, ctx:TeradataSQLExpressionsParser.Selected_columnsContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#selected_column.
    def enterSelected_column(self, ctx:TeradataSQLExpressionsParser.Selected_columnContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#selected_column.
    def exitSelected_column(self, ctx:TeradataSQLExpressionsParser.Selected_columnContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#into_clause.
    def enterInto_clause(self, ctx:TeradataSQLExpressionsParser.Into_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#into_clause.
    def exitInto_clause(self, ctx:TeradataSQLExpressionsParser.Into_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#from_clause.
    def enterFrom_clause(self, ctx:TeradataSQLExpressionsParser.From_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#from_clause.
    def exitFrom_clause(self, ctx:TeradataSQLExpressionsParser.From_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#from_spec.
    def enterFrom_spec(self, ctx:TeradataSQLExpressionsParser.From_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#from_spec.
    def exitFrom_spec(self, ctx:TeradataSQLExpressionsParser.From_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#join_source_spec.
    def enterJoin_source_spec(self, ctx:TeradataSQLExpressionsParser.Join_source_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#join_source_spec.
    def exitJoin_source_spec(self, ctx:TeradataSQLExpressionsParser.Join_source_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#join_joined_spec.
    def enterJoin_joined_spec(self, ctx:TeradataSQLExpressionsParser.Join_joined_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#join_joined_spec.
    def exitJoin_joined_spec(self, ctx:TeradataSQLExpressionsParser.Join_joined_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#from_pivot_spec.
    def enterFrom_pivot_spec(self, ctx:TeradataSQLExpressionsParser.From_pivot_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#from_pivot_spec.
    def exitFrom_pivot_spec(self, ctx:TeradataSQLExpressionsParser.From_pivot_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#from_unpivot_spec.
    def enterFrom_unpivot_spec(self, ctx:TeradataSQLExpressionsParser.From_unpivot_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#from_unpivot_spec.
    def exitFrom_unpivot_spec(self, ctx:TeradataSQLExpressionsParser.From_unpivot_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#table_reference.
    def enterTable_reference(self, ctx:TeradataSQLExpressionsParser.Table_referenceContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#table_reference.
    def exitTable_reference(self, ctx:TeradataSQLExpressionsParser.Table_referenceContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#join_clause.
    def enterJoin_clause(self, ctx:TeradataSQLExpressionsParser.Join_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#join_clause.
    def exitJoin_clause(self, ctx:TeradataSQLExpressionsParser.Join_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#join_on_clause.
    def enterJoin_on_clause(self, ctx:TeradataSQLExpressionsParser.Join_on_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#join_on_clause.
    def exitJoin_on_clause(self, ctx:TeradataSQLExpressionsParser.Join_on_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#foreign_table_reference.
    def enterForeign_table_reference(self, ctx:TeradataSQLExpressionsParser.Foreign_table_referenceContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#foreign_table_reference.
    def exitForeign_table_reference(self, ctx:TeradataSQLExpressionsParser.Foreign_table_referenceContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#foreign_function_reference.
    def enterForeign_function_reference(self, ctx:TeradataSQLExpressionsParser.Foreign_function_referenceContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#foreign_function_reference.
    def exitForeign_function_reference(self, ctx:TeradataSQLExpressionsParser.Foreign_function_referenceContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#foreign_on_clause.
    def enterForeign_on_clause(self, ctx:TeradataSQLExpressionsParser.Foreign_on_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#foreign_on_clause.
    def exitForeign_on_clause(self, ctx:TeradataSQLExpressionsParser.Foreign_on_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#exported_data.
    def enterExported_data(self, ctx:TeradataSQLExpressionsParser.Exported_dataContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#exported_data.
    def exitExported_data(self, ctx:TeradataSQLExpressionsParser.Exported_dataContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#foreign_using_clause.
    def enterForeign_using_clause(self, ctx:TeradataSQLExpressionsParser.Foreign_using_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#foreign_using_clause.
    def exitForeign_using_clause(self, ctx:TeradataSQLExpressionsParser.Foreign_using_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#foreign_parameter.
    def enterForeign_parameter(self, ctx:TeradataSQLExpressionsParser.Foreign_parameterContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#foreign_parameter.
    def exitForeign_parameter(self, ctx:TeradataSQLExpressionsParser.Foreign_parameterContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#foreign_returns_clause.
    def enterForeign_returns_clause(self, ctx:TeradataSQLExpressionsParser.Foreign_returns_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#foreign_returns_clause.
    def exitForeign_returns_clause(self, ctx:TeradataSQLExpressionsParser.Foreign_returns_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#server_name_reference.
    def enterServer_name_reference(self, ctx:TeradataSQLExpressionsParser.Server_name_referenceContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#server_name_reference.
    def exitServer_name_reference(self, ctx:TeradataSQLExpressionsParser.Server_name_referenceContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#table_function_reference.
    def enterTable_function_reference(self, ctx:TeradataSQLExpressionsParser.Table_function_referenceContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#table_function_reference.
    def exitTable_function_reference(self, ctx:TeradataSQLExpressionsParser.Table_function_referenceContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#udt_table_function.
    def enterUdt_table_function(self, ctx:TeradataSQLExpressionsParser.Udt_table_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#udt_table_function.
    def exitUdt_table_function(self, ctx:TeradataSQLExpressionsParser.Udt_table_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#unnest_table_function.
    def enterUnnest_table_function(self, ctx:TeradataSQLExpressionsParser.Unnest_table_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#unnest_table_function.
    def exitUnnest_table_function(self, ctx:TeradataSQLExpressionsParser.Unnest_table_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#table_function_returns_clause.
    def enterTable_function_returns_clause(self, ctx:TeradataSQLExpressionsParser.Table_function_returns_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#table_function_returns_clause.
    def exitTable_function_returns_clause(self, ctx:TeradataSQLExpressionsParser.Table_function_returns_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#table_function_local_order_by_clause.
    def enterTable_function_local_order_by_clause(self, ctx:TeradataSQLExpressionsParser.Table_function_local_order_by_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#table_function_local_order_by_clause.
    def exitTable_function_local_order_by_clause(self, ctx:TeradataSQLExpressionsParser.Table_function_local_order_by_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#table_function_hash_by_clause.
    def enterTable_function_hash_by_clause(self, ctx:TeradataSQLExpressionsParser.Table_function_hash_by_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#table_function_hash_by_clause.
    def exitTable_function_hash_by_clause(self, ctx:TeradataSQLExpressionsParser.Table_function_hash_by_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#table_operator_reference.
    def enterTable_operator_reference(self, ctx:TeradataSQLExpressionsParser.Table_operator_referenceContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#table_operator_reference.
    def exitTable_operator_reference(self, ctx:TeradataSQLExpressionsParser.Table_operator_referenceContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#xmltable_operator.
    def enterXmltable_operator(self, ctx:TeradataSQLExpressionsParser.Xmltable_operatorContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#xmltable_operator.
    def exitXmltable_operator(self, ctx:TeradataSQLExpressionsParser.Xmltable_operatorContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#calcmatrix_table_operator.
    def enterCalcmatrix_table_operator(self, ctx:TeradataSQLExpressionsParser.Calcmatrix_table_operatorContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#calcmatrix_table_operator.
    def exitCalcmatrix_table_operator(self, ctx:TeradataSQLExpressionsParser.Calcmatrix_table_operatorContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#read_nos_table_operator.
    def enterRead_nos_table_operator(self, ctx:TeradataSQLExpressionsParser.Read_nos_table_operatorContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#read_nos_table_operator.
    def exitRead_nos_table_operator(self, ctx:TeradataSQLExpressionsParser.Read_nos_table_operatorContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#script_table_operator.
    def enterScript_table_operator(self, ctx:TeradataSQLExpressionsParser.Script_table_operatorContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#script_table_operator.
    def exitScript_table_operator(self, ctx:TeradataSQLExpressionsParser.Script_table_operatorContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#td_unpivot_table_operator.
    def enterTd_unpivot_table_operator(self, ctx:TeradataSQLExpressionsParser.Td_unpivot_table_operatorContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#td_unpivot_table_operator.
    def exitTd_unpivot_table_operator(self, ctx:TeradataSQLExpressionsParser.Td_unpivot_table_operatorContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#write_nos_table_operator.
    def enterWrite_nos_table_operator(self, ctx:TeradataSQLExpressionsParser.Write_nos_table_operatorContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#write_nos_table_operator.
    def exitWrite_nos_table_operator(self, ctx:TeradataSQLExpressionsParser.Write_nos_table_operatorContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#json_table_table_operator.
    def enterJson_table_table_operator(self, ctx:TeradataSQLExpressionsParser.Json_table_table_operatorContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#json_table_table_operator.
    def exitJson_table_table_operator(self, ctx:TeradataSQLExpressionsParser.Json_table_table_operatorContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#json_keys_table_operator.
    def enterJson_keys_table_operator(self, ctx:TeradataSQLExpressionsParser.Json_keys_table_operatorContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#json_keys_table_operator.
    def exitJson_keys_table_operator(self, ctx:TeradataSQLExpressionsParser.Json_keys_table_operatorContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#json_shred_table_operator.
    def enterJson_shred_table_operator(self, ctx:TeradataSQLExpressionsParser.Json_shred_table_operatorContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#json_shred_table_operator.
    def exitJson_shred_table_operator(self, ctx:TeradataSQLExpressionsParser.Json_shred_table_operatorContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#generic_table_operator.
    def enterGeneric_table_operator(self, ctx:TeradataSQLExpressionsParser.Generic_table_operatorContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#generic_table_operator.
    def exitGeneric_table_operator(self, ctx:TeradataSQLExpressionsParser.Generic_table_operatorContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#table_operator_on_clause.
    def enterTable_operator_on_clause(self, ctx:TeradataSQLExpressionsParser.Table_operator_on_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#table_operator_on_clause.
    def exitTable_operator_on_clause(self, ctx:TeradataSQLExpressionsParser.Table_operator_on_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#table_operator_execute_clause.
    def enterTable_operator_execute_clause(self, ctx:TeradataSQLExpressionsParser.Table_operator_execute_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#table_operator_execute_clause.
    def exitTable_operator_execute_clause(self, ctx:TeradataSQLExpressionsParser.Table_operator_execute_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#table_operator_out_table_clause.
    def enterTable_operator_out_table_clause(self, ctx:TeradataSQLExpressionsParser.Table_operator_out_table_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#table_operator_out_table_clause.
    def exitTable_operator_out_table_clause(self, ctx:TeradataSQLExpressionsParser.Table_operator_out_table_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#table_operator_using_clause.
    def enterTable_operator_using_clause(self, ctx:TeradataSQLExpressionsParser.Table_operator_using_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#table_operator_using_clause.
    def exitTable_operator_using_clause(self, ctx:TeradataSQLExpressionsParser.Table_operator_using_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#table_operator_using_spec.
    def enterTable_operator_using_spec(self, ctx:TeradataSQLExpressionsParser.Table_operator_using_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#table_operator_using_spec.
    def exitTable_operator_using_spec(self, ctx:TeradataSQLExpressionsParser.Table_operator_using_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#json_keys_using_name_value_pair.
    def enterJson_keys_using_name_value_pair(self, ctx:TeradataSQLExpressionsParser.Json_keys_using_name_value_pairContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#json_keys_using_name_value_pair.
    def exitJson_keys_using_name_value_pair(self, ctx:TeradataSQLExpressionsParser.Json_keys_using_name_value_pairContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#hash_or_partition_by.
    def enterHash_or_partition_by(self, ctx:TeradataSQLExpressionsParser.Hash_or_partition_byContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#hash_or_partition_by.
    def exitHash_or_partition_by(self, ctx:TeradataSQLExpressionsParser.Hash_or_partition_byContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#subquery_reference.
    def enterSubquery_reference(self, ctx:TeradataSQLExpressionsParser.Subquery_referenceContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#subquery_reference.
    def exitSubquery_reference(self, ctx:TeradataSQLExpressionsParser.Subquery_referenceContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#location.
    def enterLocation(self, ctx:TeradataSQLExpressionsParser.LocationContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#location.
    def exitLocation(self, ctx:TeradataSQLExpressionsParser.LocationContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#read_nos_option.
    def enterRead_nos_option(self, ctx:TeradataSQLExpressionsParser.Read_nos_optionContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#read_nos_option.
    def exitRead_nos_option(self, ctx:TeradataSQLExpressionsParser.Read_nos_optionContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#write_nos_option.
    def enterWrite_nos_option(self, ctx:TeradataSQLExpressionsParser.Write_nos_optionContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#write_nos_option.
    def exitWrite_nos_option(self, ctx:TeradataSQLExpressionsParser.Write_nos_optionContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#with_clause.
    def enterWith_clause(self, ctx:TeradataSQLExpressionsParser.With_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#with_clause.
    def exitWith_clause(self, ctx:TeradataSQLExpressionsParser.With_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#with_clause_by_phrase.
    def enterWith_clause_by_phrase(self, ctx:TeradataSQLExpressionsParser.With_clause_by_phraseContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#with_clause_by_phrase.
    def exitWith_clause_by_phrase(self, ctx:TeradataSQLExpressionsParser.With_clause_by_phraseContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#with_clause_title_phrase.
    def enterWith_clause_title_phrase(self, ctx:TeradataSQLExpressionsParser.With_clause_title_phraseContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#with_clause_title_phrase.
    def exitWith_clause_title_phrase(self, ctx:TeradataSQLExpressionsParser.With_clause_title_phraseContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#where_clause.
    def enterWhere_clause(self, ctx:TeradataSQLExpressionsParser.Where_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#where_clause.
    def exitWhere_clause(self, ctx:TeradataSQLExpressionsParser.Where_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#group_by_clause.
    def enterGroup_by_clause(self, ctx:TeradataSQLExpressionsParser.Group_by_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#group_by_clause.
    def exitGroup_by_clause(self, ctx:TeradataSQLExpressionsParser.Group_by_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#group_by_spec.
    def enterGroup_by_spec(self, ctx:TeradataSQLExpressionsParser.Group_by_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#group_by_spec.
    def exitGroup_by_spec(self, ctx:TeradataSQLExpressionsParser.Group_by_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#ordinary_grouping_set.
    def enterOrdinary_grouping_set(self, ctx:TeradataSQLExpressionsParser.Ordinary_grouping_setContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#ordinary_grouping_set.
    def exitOrdinary_grouping_set(self, ctx:TeradataSQLExpressionsParser.Ordinary_grouping_setContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#ordinary_grouping_set_parenthesized.
    def enterOrdinary_grouping_set_parenthesized(self, ctx:TeradataSQLExpressionsParser.Ordinary_grouping_set_parenthesizedContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#ordinary_grouping_set_parenthesized.
    def exitOrdinary_grouping_set_parenthesized(self, ctx:TeradataSQLExpressionsParser.Ordinary_grouping_set_parenthesizedContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#empty_grouping_set.
    def enterEmpty_grouping_set(self, ctx:TeradataSQLExpressionsParser.Empty_grouping_setContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#empty_grouping_set.
    def exitEmpty_grouping_set(self, ctx:TeradataSQLExpressionsParser.Empty_grouping_setContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#rollup_option.
    def enterRollup_option(self, ctx:TeradataSQLExpressionsParser.Rollup_optionContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#rollup_option.
    def exitRollup_option(self, ctx:TeradataSQLExpressionsParser.Rollup_optionContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#cube_option.
    def enterCube_option(self, ctx:TeradataSQLExpressionsParser.Cube_optionContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#cube_option.
    def exitCube_option(self, ctx:TeradataSQLExpressionsParser.Cube_optionContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#grouping_sets_option.
    def enterGrouping_sets_option(self, ctx:TeradataSQLExpressionsParser.Grouping_sets_optionContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#grouping_sets_option.
    def exitGrouping_sets_option(self, ctx:TeradataSQLExpressionsParser.Grouping_sets_optionContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#grouping_sets_spec.
    def enterGrouping_sets_spec(self, ctx:TeradataSQLExpressionsParser.Grouping_sets_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#grouping_sets_spec.
    def exitGrouping_sets_spec(self, ctx:TeradataSQLExpressionsParser.Grouping_sets_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#having_clause.
    def enterHaving_clause(self, ctx:TeradataSQLExpressionsParser.Having_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#having_clause.
    def exitHaving_clause(self, ctx:TeradataSQLExpressionsParser.Having_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#qualify_clause.
    def enterQualify_clause(self, ctx:TeradataSQLExpressionsParser.Qualify_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#qualify_clause.
    def exitQualify_clause(self, ctx:TeradataSQLExpressionsParser.Qualify_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#sample_clause.
    def enterSample_clause(self, ctx:TeradataSQLExpressionsParser.Sample_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#sample_clause.
    def exitSample_clause(self, ctx:TeradataSQLExpressionsParser.Sample_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#sample_fraction_description.
    def enterSample_fraction_description(self, ctx:TeradataSQLExpressionsParser.Sample_fraction_descriptionContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#sample_fraction_description.
    def exitSample_fraction_description(self, ctx:TeradataSQLExpressionsParser.Sample_fraction_descriptionContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#sample_count_description.
    def enterSample_count_description(self, ctx:TeradataSQLExpressionsParser.Sample_count_descriptionContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#sample_count_description.
    def exitSample_count_description(self, ctx:TeradataSQLExpressionsParser.Sample_count_descriptionContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#sample_when_clause.
    def enterSample_when_clause(self, ctx:TeradataSQLExpressionsParser.Sample_when_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#sample_when_clause.
    def exitSample_when_clause(self, ctx:TeradataSQLExpressionsParser.Sample_when_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#expand_on_clause.
    def enterExpand_on_clause(self, ctx:TeradataSQLExpressionsParser.Expand_on_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#expand_on_clause.
    def exitExpand_on_clause(self, ctx:TeradataSQLExpressionsParser.Expand_on_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#order_by_clause.
    def enterOrder_by_clause(self, ctx:TeradataSQLExpressionsParser.Order_by_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#order_by_clause.
    def exitOrder_by_clause(self, ctx:TeradataSQLExpressionsParser.Order_by_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#order_by_spec_full.
    def enterOrder_by_spec_full(self, ctx:TeradataSQLExpressionsParser.Order_by_spec_fullContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#order_by_spec_full.
    def exitOrder_by_spec_full(self, ctx:TeradataSQLExpressionsParser.Order_by_spec_fullContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#order_by_spec_asc_desc_only.
    def enterOrder_by_spec_asc_desc_only(self, ctx:TeradataSQLExpressionsParser.Order_by_spec_asc_desc_onlyContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#order_by_spec_asc_desc_only.
    def exitOrder_by_spec_asc_desc_only(self, ctx:TeradataSQLExpressionsParser.Order_by_spec_asc_desc_onlyContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#with_check_option.
    def enterWith_check_option(self, ctx:TeradataSQLExpressionsParser.With_check_optionContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#with_check_option.
    def exitWith_check_option(self, ctx:TeradataSQLExpressionsParser.With_check_optionContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#PeriodMeets.
    def enterPeriodMeets(self, ctx:TeradataSQLExpressionsParser.PeriodMeetsContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#PeriodMeets.
    def exitPeriodMeets(self, ctx:TeradataSQLExpressionsParser.PeriodMeetsContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#PeriodImmediatelySucceeds.
    def enterPeriodImmediatelySucceeds(self, ctx:TeradataSQLExpressionsParser.PeriodImmediatelySucceedsContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#PeriodImmediatelySucceeds.
    def exitPeriodImmediatelySucceeds(self, ctx:TeradataSQLExpressionsParser.PeriodImmediatelySucceedsContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#PeriodEquals.
    def enterPeriodEquals(self, ctx:TeradataSQLExpressionsParser.PeriodEqualsContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#PeriodEquals.
    def exitPeriodEquals(self, ctx:TeradataSQLExpressionsParser.PeriodEqualsContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#ScalarComparelist.
    def enterScalarComparelist(self, ctx:TeradataSQLExpressionsParser.ScalarComparelistContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#ScalarComparelist.
    def exitScalarComparelist(self, ctx:TeradataSQLExpressionsParser.ScalarComparelistContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#TupleInSubquery.
    def enterTupleInSubquery(self, ctx:TeradataSQLExpressionsParser.TupleInSubqueryContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#TupleInSubquery.
    def exitTupleInSubquery(self, ctx:TeradataSQLExpressionsParser.TupleInSubqueryContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#LogicalOr.
    def enterLogicalOr(self, ctx:TeradataSQLExpressionsParser.LogicalOrContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#LogicalOr.
    def exitLogicalOr(self, ctx:TeradataSQLExpressionsParser.LogicalOrContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#ScalarInScalar.
    def enterScalarInScalar(self, ctx:TeradataSQLExpressionsParser.ScalarInScalarContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#ScalarInScalar.
    def exitScalarInScalar(self, ctx:TeradataSQLExpressionsParser.ScalarInScalarContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#ScalarCompareScalar.
    def enterScalarCompareScalar(self, ctx:TeradataSQLExpressionsParser.ScalarCompareScalarContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#ScalarCompareScalar.
    def exitScalarCompareScalar(self, ctx:TeradataSQLExpressionsParser.ScalarCompareScalarContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#LogicalNot.
    def enterLogicalNot(self, ctx:TeradataSQLExpressionsParser.LogicalNotContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#LogicalNot.
    def exitLogicalNot(self, ctx:TeradataSQLExpressionsParser.LogicalNotContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#TupleComparelist.
    def enterTupleComparelist(self, ctx:TeradataSQLExpressionsParser.TupleComparelistContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#TupleComparelist.
    def exitTupleComparelist(self, ctx:TeradataSQLExpressionsParser.TupleComparelistContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#ScalarInList.
    def enterScalarInList(self, ctx:TeradataSQLExpressionsParser.ScalarInListContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#ScalarInList.
    def exitScalarInList(self, ctx:TeradataSQLExpressionsParser.ScalarInListContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#TupleLikeList.
    def enterTupleLikeList(self, ctx:TeradataSQLExpressionsParser.TupleLikeListContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#TupleLikeList.
    def exitTupleLikeList(self, ctx:TeradataSQLExpressionsParser.TupleLikeListContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#LogicalAnd.
    def enterLogicalAnd(self, ctx:TeradataSQLExpressionsParser.LogicalAndContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#LogicalAnd.
    def exitLogicalAnd(self, ctx:TeradataSQLExpressionsParser.LogicalAndContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#ScalarInSubquery.
    def enterScalarInSubquery(self, ctx:TeradataSQLExpressionsParser.ScalarInSubqueryContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#ScalarInSubquery.
    def exitScalarInSubquery(self, ctx:TeradataSQLExpressionsParser.ScalarInSubqueryContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#PeriodContains.
    def enterPeriodContains(self, ctx:TeradataSQLExpressionsParser.PeriodContainsContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#PeriodContains.
    def exitPeriodContains(self, ctx:TeradataSQLExpressionsParser.PeriodContainsContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#PeriodOverlaps.
    def enterPeriodOverlaps(self, ctx:TeradataSQLExpressionsParser.PeriodOverlapsContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#PeriodOverlaps.
    def exitPeriodOverlaps(self, ctx:TeradataSQLExpressionsParser.PeriodOverlapsContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#Between.
    def enterBetween(self, ctx:TeradataSQLExpressionsParser.BetweenContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#Between.
    def exitBetween(self, ctx:TeradataSQLExpressionsParser.BetweenContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#ParenthesizedLogicalExpr.
    def enterParenthesizedLogicalExpr(self, ctx:TeradataSQLExpressionsParser.ParenthesizedLogicalExprContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#ParenthesizedLogicalExpr.
    def exitParenthesizedLogicalExpr(self, ctx:TeradataSQLExpressionsParser.ParenthesizedLogicalExprContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#PeriodImmediatelyPrecedes.
    def enterPeriodImmediatelyPrecedes(self, ctx:TeradataSQLExpressionsParser.PeriodImmediatelyPrecedesContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#PeriodImmediatelyPrecedes.
    def exitPeriodImmediatelyPrecedes(self, ctx:TeradataSQLExpressionsParser.PeriodImmediatelyPrecedesContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#NullCheck.
    def enterNullCheck(self, ctx:TeradataSQLExpressionsParser.NullCheckContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#NullCheck.
    def exitNullCheck(self, ctx:TeradataSQLExpressionsParser.NullCheckContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#PeriodPrecedes.
    def enterPeriodPrecedes(self, ctx:TeradataSQLExpressionsParser.PeriodPrecedesContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#PeriodPrecedes.
    def exitPeriodPrecedes(self, ctx:TeradataSQLExpressionsParser.PeriodPrecedesContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#Exists.
    def enterExists(self, ctx:TeradataSQLExpressionsParser.ExistsContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#Exists.
    def exitExists(self, ctx:TeradataSQLExpressionsParser.ExistsContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#PeriodSucceeds.
    def enterPeriodSucceeds(self, ctx:TeradataSQLExpressionsParser.PeriodSucceedsContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#PeriodSucceeds.
    def exitPeriodSucceeds(self, ctx:TeradataSQLExpressionsParser.PeriodSucceedsContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#ScalarLikeList.
    def enterScalarLikeList(self, ctx:TeradataSQLExpressionsParser.ScalarLikeListContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#ScalarLikeList.
    def exitScalarLikeList(self, ctx:TeradataSQLExpressionsParser.ScalarLikeListContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#ScalarLikeScalar.
    def enterScalarLikeScalar(self, ctx:TeradataSQLExpressionsParser.ScalarLikeScalarContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#ScalarLikeScalar.
    def exitScalarLikeScalar(self, ctx:TeradataSQLExpressionsParser.ScalarLikeScalarContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#JsonMetadata.
    def enterJsonMetadata(self, ctx:TeradataSQLExpressionsParser.JsonMetadataContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#JsonMetadata.
    def exitJsonMetadata(self, ctx:TeradataSQLExpressionsParser.JsonMetadataContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#JsonAsBson.
    def enterJsonAsBson(self, ctx:TeradataSQLExpressionsParser.JsonAsBsonContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#JsonAsBson.
    def exitJsonAsBson(self, ctx:TeradataSQLExpressionsParser.JsonAsBsonContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#VariantTypeConstructor.
    def enterVariantTypeConstructor(self, ctx:TeradataSQLExpressionsParser.VariantTypeConstructorContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#VariantTypeConstructor.
    def exitVariantTypeConstructor(self, ctx:TeradataSQLExpressionsParser.VariantTypeConstructorContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#XMLExtract.
    def enterXMLExtract(self, ctx:TeradataSQLExpressionsParser.XMLExtractContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#XMLExtract.
    def exitXMLExtract(self, ctx:TeradataSQLExpressionsParser.XMLExtractContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#ArrayComparison.
    def enterArrayComparison(self, ctx:TeradataSQLExpressionsParser.ArrayComparisonContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#ArrayComparison.
    def exitArrayComparison(self, ctx:TeradataSQLExpressionsParser.ArrayComparisonContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#ArrayGet.
    def enterArrayGet(self, ctx:TeradataSQLExpressionsParser.ArrayGetContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#ArrayGet.
    def exitArrayGet(self, ctx:TeradataSQLExpressionsParser.ArrayGetContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#XMLConstructor.
    def enterXMLConstructor(self, ctx:TeradataSQLExpressionsParser.XMLConstructorContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#XMLConstructor.
    def exitXMLConstructor(self, ctx:TeradataSQLExpressionsParser.XMLConstructorContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#UDTMethodInvocation.
    def enterUDTMethodInvocation(self, ctx:TeradataSQLExpressionsParser.UDTMethodInvocationContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#UDTMethodInvocation.
    def exitUDTMethodInvocation(self, ctx:TeradataSQLExpressionsParser.UDTMethodInvocationContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#JsonExtractLargeValue.
    def enterJsonExtractLargeValue(self, ctx:TeradataSQLExpressionsParser.JsonExtractLargeValueContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#JsonExtractLargeValue.
    def exitJsonExtractLargeValue(self, ctx:TeradataSQLExpressionsParser.JsonExtractLargeValueContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#JsonRecursiveDescendSlice.
    def enterJsonRecursiveDescendSlice(self, ctx:TeradataSQLExpressionsParser.JsonRecursiveDescendSliceContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#JsonRecursiveDescendSlice.
    def exitJsonRecursiveDescendSlice(self, ctx:TeradataSQLExpressionsParser.JsonRecursiveDescendSliceContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#FunctionInvocation.
    def enterFunctionInvocation(self, ctx:TeradataSQLExpressionsParser.FunctionInvocationContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#FunctionInvocation.
    def exitFunctionInvocation(self, ctx:TeradataSQLExpressionsParser.FunctionInvocationContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#ScalarSubquery.
    def enterScalarSubquery(self, ctx:TeradataSQLExpressionsParser.ScalarSubqueryContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#ScalarSubquery.
    def exitScalarSubquery(self, ctx:TeradataSQLExpressionsParser.ScalarSubqueryContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#JsonExistValue.
    def enterJsonExistValue(self, ctx:TeradataSQLExpressionsParser.JsonExistValueContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#JsonExistValue.
    def exitJsonExistValue(self, ctx:TeradataSQLExpressionsParser.JsonExistValueContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#Modulo.
    def enterModulo(self, ctx:TeradataSQLExpressionsParser.ModuloContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#Modulo.
    def exitModulo(self, ctx:TeradataSQLExpressionsParser.ModuloContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#JsonExtractValue.
    def enterJsonExtractValue(self, ctx:TeradataSQLExpressionsParser.JsonExtractValueContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#JsonExtractValue.
    def exitJsonExtractValue(self, ctx:TeradataSQLExpressionsParser.JsonExtractValueContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#XMLCreateSchemaBasedXML.
    def enterXMLCreateSchemaBasedXML(self, ctx:TeradataSQLExpressionsParser.XMLCreateSchemaBasedXMLContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#XMLCreateSchemaBasedXML.
    def exitXMLCreateSchemaBasedXML(self, ctx:TeradataSQLExpressionsParser.XMLCreateSchemaBasedXMLContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#ArrayUpdate.
    def enterArrayUpdate(self, ctx:TeradataSQLExpressionsParser.ArrayUpdateContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#ArrayUpdate.
    def exitArrayUpdate(self, ctx:TeradataSQLExpressionsParser.ArrayUpdateContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#JsonExtract.
    def enterJsonExtract(self, ctx:TeradataSQLExpressionsParser.JsonExtractContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#JsonExtract.
    def exitJsonExtract(self, ctx:TeradataSQLExpressionsParser.JsonExtractContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#MultDiv.
    def enterMultDiv(self, ctx:TeradataSQLExpressionsParser.MultDivContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#MultDiv.
    def exitMultDiv(self, ctx:TeradataSQLExpressionsParser.MultDivContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#PeriodIntersect.
    def enterPeriodIntersect(self, ctx:TeradataSQLExpressionsParser.PeriodIntersectContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#PeriodIntersect.
    def exitPeriodIntersect(self, ctx:TeradataSQLExpressionsParser.PeriodIntersectContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#IntervalExprParenthesized.
    def enterIntervalExprParenthesized(self, ctx:TeradataSQLExpressionsParser.IntervalExprParenthesizedContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#IntervalExprParenthesized.
    def exitIntervalExprParenthesized(self, ctx:TeradataSQLExpressionsParser.IntervalExprParenthesizedContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#JsonRecursiveDescendAllArrayElements.
    def enterJsonRecursiveDescendAllArrayElements(self, ctx:TeradataSQLExpressionsParser.JsonRecursiveDescendAllArrayElementsContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#JsonRecursiveDescendAllArrayElements.
    def exitJsonRecursiveDescendAllArrayElements(self, ctx:TeradataSQLExpressionsParser.JsonRecursiveDescendAllArrayElementsContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#UnaryPlusMinus.
    def enterUnaryPlusMinus(self, ctx:TeradataSQLExpressionsParser.UnaryPlusMinusContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#UnaryPlusMinus.
    def exitUnaryPlusMinus(self, ctx:TeradataSQLExpressionsParser.UnaryPlusMinusContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#Concatenation.
    def enterConcatenation(self, ctx:TeradataSQLExpressionsParser.ConcatenationContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#Concatenation.
    def exitConcatenation(self, ctx:TeradataSQLExpressionsParser.ConcatenationContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#PeriodDiff.
    def enterPeriodDiff(self, ctx:TeradataSQLExpressionsParser.PeriodDiffContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#PeriodDiff.
    def exitPeriodDiff(self, ctx:TeradataSQLExpressionsParser.PeriodDiffContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#ArrayOmethodWithoudArgs.
    def enterArrayOmethodWithoudArgs(self, ctx:TeradataSQLExpressionsParser.ArrayOmethodWithoudArgsContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#ArrayOmethodWithoudArgs.
    def exitArrayOmethodWithoudArgs(self, ctx:TeradataSQLExpressionsParser.ArrayOmethodWithoudArgsContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#PartitioningExpr.
    def enterPartitioningExpr(self, ctx:TeradataSQLExpressionsParser.PartitioningExprContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#PartitioningExpr.
    def exitPartitioningExpr(self, ctx:TeradataSQLExpressionsParser.PartitioningExprContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#XMLExistNode.
    def enterXMLExistNode(self, ctx:TeradataSQLExpressionsParser.XMLExistNodeContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#XMLExistNode.
    def exitXMLExistNode(self, ctx:TeradataSQLExpressionsParser.XMLExistNodeContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#JsonRecursiveDescendArrayElementReference.
    def enterJsonRecursiveDescendArrayElementReference(self, ctx:TeradataSQLExpressionsParser.JsonRecursiveDescendArrayElementReferenceContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#JsonRecursiveDescendArrayElementReference.
    def exitJsonRecursiveDescendArrayElementReference(self, ctx:TeradataSQLExpressionsParser.JsonRecursiveDescendArrayElementReferenceContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#DataTypeConversion.
    def enterDataTypeConversion(self, ctx:TeradataSQLExpressionsParser.DataTypeConversionContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#DataTypeConversion.
    def exitDataTypeConversion(self, ctx:TeradataSQLExpressionsParser.DataTypeConversionContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#JsonRecursiveDescendObjectMember.
    def enterJsonRecursiveDescendObjectMember(self, ctx:TeradataSQLExpressionsParser.JsonRecursiveDescendObjectMemberContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#JsonRecursiveDescendObjectMember.
    def exitJsonRecursiveDescendObjectMember(self, ctx:TeradataSQLExpressionsParser.JsonRecursiveDescendObjectMemberContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#IntervalExpr.
    def enterIntervalExpr(self, ctx:TeradataSQLExpressionsParser.IntervalExprContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#IntervalExpr.
    def exitIntervalExpr(self, ctx:TeradataSQLExpressionsParser.IntervalExprContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#Exponentiation.
    def enterExponentiation(self, ctx:TeradataSQLExpressionsParser.ExponentiationContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#Exponentiation.
    def exitExponentiation(self, ctx:TeradataSQLExpressionsParser.ExponentiationContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#XMLIsSchemaValidated.
    def enterXMLIsSchemaValidated(self, ctx:TeradataSQLExpressionsParser.XMLIsSchemaValidatedContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#XMLIsSchemaValidated.
    def exitXMLIsSchemaValidated(self, ctx:TeradataSQLExpressionsParser.XMLIsSchemaValidatedContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#JSONConstructor.
    def enterJSONConstructor(self, ctx:TeradataSQLExpressionsParser.JSONConstructorContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#JSONConstructor.
    def exitJSONConstructor(self, ctx:TeradataSQLExpressionsParser.JSONConstructorContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#JsonSlice.
    def enterJsonSlice(self, ctx:TeradataSQLExpressionsParser.JsonSliceContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#JsonSlice.
    def exitJsonSlice(self, ctx:TeradataSQLExpressionsParser.JsonSliceContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#XMLIsSchemaValid.
    def enterXMLIsSchemaValid(self, ctx:TeradataSQLExpressionsParser.XMLIsSchemaValidContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#XMLIsSchemaValid.
    def exitXMLIsSchemaValid(self, ctx:TeradataSQLExpressionsParser.XMLIsSchemaValidContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#ArrayAggregation.
    def enterArrayAggregation(self, ctx:TeradataSQLExpressionsParser.ArrayAggregationContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#ArrayAggregation.
    def exitArrayAggregation(self, ctx:TeradataSQLExpressionsParser.ArrayAggregationContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#ArrayUpdateStride.
    def enterArrayUpdateStride(self, ctx:TeradataSQLExpressionsParser.ArrayUpdateStrideContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#ArrayUpdateStride.
    def exitArrayUpdateStride(self, ctx:TeradataSQLExpressionsParser.ArrayUpdateStrideContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#LiteralExpr.
    def enterLiteralExpr(self, ctx:TeradataSQLExpressionsParser.LiteralExprContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#LiteralExpr.
    def exitLiteralExpr(self, ctx:TeradataSQLExpressionsParser.LiteralExprContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#ArrayOmethodWithArg.
    def enterArrayOmethodWithArg(self, ctx:TeradataSQLExpressionsParser.ArrayOmethodWithArgContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#ArrayOmethodWithArg.
    def exitArrayOmethodWithArg(self, ctx:TeradataSQLExpressionsParser.ArrayOmethodWithArgContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#JsonRecursiveDescendAllObjectMembers.
    def enterJsonRecursiveDescendAllObjectMembers(self, ctx:TeradataSQLExpressionsParser.JsonRecursiveDescendAllObjectMembersContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#JsonRecursiveDescendAllObjectMembers.
    def exitJsonRecursiveDescendAllObjectMembers(self, ctx:TeradataSQLExpressionsParser.JsonRecursiveDescendAllObjectMembersContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#XMLCreateNonSchemaBasedXML.
    def enterXMLCreateNonSchemaBasedXML(self, ctx:TeradataSQLExpressionsParser.XMLCreateNonSchemaBasedXMLContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#XMLCreateNonSchemaBasedXML.
    def exitXMLCreateNonSchemaBasedXML(self, ctx:TeradataSQLExpressionsParser.XMLCreateNonSchemaBasedXMLContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#VariableReference.
    def enterVariableReference(self, ctx:TeradataSQLExpressionsParser.VariableReferenceContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#VariableReference.
    def exitVariableReference(self, ctx:TeradataSQLExpressionsParser.VariableReferenceContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#AddSub.
    def enterAddSub(self, ctx:TeradataSQLExpressionsParser.AddSubContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#AddSub.
    def exitAddSub(self, ctx:TeradataSQLExpressionsParser.AddSubContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#JsonObjectMember.
    def enterJsonObjectMember(self, ctx:TeradataSQLExpressionsParser.JsonObjectMemberContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#JsonObjectMember.
    def exitJsonObjectMember(self, ctx:TeradataSQLExpressionsParser.JsonObjectMemberContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#JsonAllElements.
    def enterJsonAllElements(self, ctx:TeradataSQLExpressionsParser.JsonAllElementsContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#JsonAllElements.
    def exitJsonAllElements(self, ctx:TeradataSQLExpressionsParser.JsonAllElementsContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#ArrayOextend.
    def enterArrayOextend(self, ctx:TeradataSQLExpressionsParser.ArrayOextendContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#ArrayOextend.
    def exitArrayOextend(self, ctx:TeradataSQLExpressionsParser.ArrayOextendContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#ArrayArithmetic.
    def enterArrayArithmetic(self, ctx:TeradataSQLExpressionsParser.ArrayArithmeticContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#ArrayArithmetic.
    def exitArrayArithmetic(self, ctx:TeradataSQLExpressionsParser.ArrayArithmeticContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#UDTConstructor.
    def enterUDTConstructor(self, ctx:TeradataSQLExpressionsParser.UDTConstructorContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#UDTConstructor.
    def exitUDTConstructor(self, ctx:TeradataSQLExpressionsParser.UDTConstructorContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#XMLTransform.
    def enterXMLTransform(self, ctx:TeradataSQLExpressionsParser.XMLTransformContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#XMLTransform.
    def exitXMLTransform(self, ctx:TeradataSQLExpressionsParser.XMLTransformContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#DateTimeExpr.
    def enterDateTimeExpr(self, ctx:TeradataSQLExpressionsParser.DateTimeExprContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#DateTimeExpr.
    def exitDateTimeExpr(self, ctx:TeradataSQLExpressionsParser.DateTimeExprContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#ColumnName.
    def enterColumnName(self, ctx:TeradataSQLExpressionsParser.ColumnNameContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#ColumnName.
    def exitColumnName(self, ctx:TeradataSQLExpressionsParser.ColumnNameContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#ArrayOtrim.
    def enterArrayOtrim(self, ctx:TeradataSQLExpressionsParser.ArrayOtrimContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#ArrayOtrim.
    def exitArrayOtrim(self, ctx:TeradataSQLExpressionsParser.ArrayOtrimContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#CursorVariableReference.
    def enterCursorVariableReference(self, ctx:TeradataSQLExpressionsParser.CursorVariableReferenceContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#CursorVariableReference.
    def exitCursorVariableReference(self, ctx:TeradataSQLExpressionsParser.CursorVariableReferenceContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#Parenthesized.
    def enterParenthesized(self, ctx:TeradataSQLExpressionsParser.ParenthesizedContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#Parenthesized.
    def exitParenthesized(self, ctx:TeradataSQLExpressionsParser.ParenthesizedContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#JsonAsBsonText.
    def enterJsonAsBsonText(self, ctx:TeradataSQLExpressionsParser.JsonAsBsonTextContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#JsonAsBsonText.
    def exitJsonAsBsonText(self, ctx:TeradataSQLExpressionsParser.JsonAsBsonTextContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#AttributeModification.
    def enterAttributeModification(self, ctx:TeradataSQLExpressionsParser.AttributeModificationContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#AttributeModification.
    def exitAttributeModification(self, ctx:TeradataSQLExpressionsParser.AttributeModificationContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#JsonCombine.
    def enterJsonCombine(self, ctx:TeradataSQLExpressionsParser.JsonCombineContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#JsonCombine.
    def exitJsonCombine(self, ctx:TeradataSQLExpressionsParser.JsonCombineContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#XMLIsDocument.
    def enterXMLIsDocument(self, ctx:TeradataSQLExpressionsParser.XMLIsDocumentContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#XMLIsDocument.
    def exitXMLIsDocument(self, ctx:TeradataSQLExpressionsParser.XMLIsDocumentContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#MacroParameterReference.
    def enterMacroParameterReference(self, ctx:TeradataSQLExpressionsParser.MacroParameterReferenceContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#MacroParameterReference.
    def exitMacroParameterReference(self, ctx:TeradataSQLExpressionsParser.MacroParameterReferenceContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#XMLIsContent.
    def enterXMLIsContent(self, ctx:TeradataSQLExpressionsParser.XMLIsContentContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#XMLIsContent.
    def exitXMLIsContent(self, ctx:TeradataSQLExpressionsParser.XMLIsContentContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#ArrayElementReference.
    def enterArrayElementReference(self, ctx:TeradataSQLExpressionsParser.ArrayElementReferenceContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#ArrayElementReference.
    def exitArrayElementReference(self, ctx:TeradataSQLExpressionsParser.ArrayElementReferenceContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#ArrayCardinality.
    def enterArrayCardinality(self, ctx:TeradataSQLExpressionsParser.ArrayCardinalityContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#ArrayCardinality.
    def exitArrayCardinality(self, ctx:TeradataSQLExpressionsParser.ArrayCardinalityContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#CaseExpr.
    def enterCaseExpr(self, ctx:TeradataSQLExpressionsParser.CaseExprContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#CaseExpr.
    def exitCaseExpr(self, ctx:TeradataSQLExpressionsParser.CaseExprContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#JsonKeycount.
    def enterJsonKeycount(self, ctx:TeradataSQLExpressionsParser.JsonKeycountContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#JsonKeycount.
    def exitJsonKeycount(self, ctx:TeradataSQLExpressionsParser.JsonKeycountContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#JsonAllObjectMembers.
    def enterJsonAllObjectMembers(self, ctx:TeradataSQLExpressionsParser.JsonAllObjectMembersContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#JsonAllObjectMembers.
    def exitJsonAllObjectMembers(self, ctx:TeradataSQLExpressionsParser.JsonAllObjectMembersContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#tuple.
    def enterTuple(self, ctx:TeradataSQLExpressionsParser.TupleContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#tuple.
    def exitTuple(self, ctx:TeradataSQLExpressionsParser.TupleContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#tuple_attribute.
    def enterTuple_attribute(self, ctx:TeradataSQLExpressionsParser.Tuple_attributeContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#tuple_attribute.
    def exitTuple_attribute(self, ctx:TeradataSQLExpressionsParser.Tuple_attributeContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#case_expr.
    def enterCase_expr(self, ctx:TeradataSQLExpressionsParser.Case_exprContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#case_expr.
    def exitCase_expr(self, ctx:TeradataSQLExpressionsParser.Case_exprContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#valued_case_expr.
    def enterValued_case_expr(self, ctx:TeradataSQLExpressionsParser.Valued_case_exprContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#valued_case_expr.
    def exitValued_case_expr(self, ctx:TeradataSQLExpressionsParser.Valued_case_exprContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#searched_case_expr.
    def enterSearched_case_expr(self, ctx:TeradataSQLExpressionsParser.Searched_case_exprContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#searched_case_expr.
    def exitSearched_case_expr(self, ctx:TeradataSQLExpressionsParser.Searched_case_exprContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#coalesce_expr.
    def enterCoalesce_expr(self, ctx:TeradataSQLExpressionsParser.Coalesce_exprContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#coalesce_expr.
    def exitCoalesce_expr(self, ctx:TeradataSQLExpressionsParser.Coalesce_exprContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#nullif_expr.
    def enterNullif_expr(self, ctx:TeradataSQLExpressionsParser.Nullif_exprContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#nullif_expr.
    def exitNullif_expr(self, ctx:TeradataSQLExpressionsParser.Nullif_exprContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#interval_expr_base.
    def enterInterval_expr_base(self, ctx:TeradataSQLExpressionsParser.Interval_expr_baseContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#interval_expr_base.
    def exitInterval_expr_base(self, ctx:TeradataSQLExpressionsParser.Interval_expr_baseContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#interval_expr_parenthesized.
    def enterInterval_expr_parenthesized(self, ctx:TeradataSQLExpressionsParser.Interval_expr_parenthesizedContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#interval_expr_parenthesized.
    def exitInterval_expr_parenthesized(self, ctx:TeradataSQLExpressionsParser.Interval_expr_parenthesizedContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#interval_expr_start_end_phrase.
    def enterInterval_expr_start_end_phrase(self, ctx:TeradataSQLExpressionsParser.Interval_expr_start_end_phraseContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#interval_expr_start_end_phrase.
    def exitInterval_expr_start_end_phrase(self, ctx:TeradataSQLExpressionsParser.Interval_expr_start_end_phraseContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#function_invocation.
    def enterFunction_invocation(self, ctx:TeradataSQLExpressionsParser.Function_invocationContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#function_invocation.
    def exitFunction_invocation(self, ctx:TeradataSQLExpressionsParser.Function_invocationContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#AggOneArg.
    def enterAggOneArg(self, ctx:TeradataSQLExpressionsParser.AggOneArgContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#AggOneArg.
    def exitAggOneArg(self, ctx:TeradataSQLExpressionsParser.AggOneArgContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#AggTwoArgs.
    def enterAggTwoArgs(self, ctx:TeradataSQLExpressionsParser.AggTwoArgsContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#AggTwoArgs.
    def exitAggTwoArgs(self, ctx:TeradataSQLExpressionsParser.AggTwoArgsContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#AggCount.
    def enterAggCount(self, ctx:TeradataSQLExpressionsParser.AggCountContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#AggCount.
    def exitAggCount(self, ctx:TeradataSQLExpressionsParser.AggCountContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#Grouping.
    def enterGrouping(self, ctx:TeradataSQLExpressionsParser.GroupingContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#Grouping.
    def exitGrouping(self, ctx:TeradataSQLExpressionsParser.GroupingContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#ListAgg.
    def enterListAgg(self, ctx:TeradataSQLExpressionsParser.ListAggContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#ListAgg.
    def exitListAgg(self, ctx:TeradataSQLExpressionsParser.ListAggContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#analytic_function.
    def enterAnalytic_function(self, ctx:TeradataSQLExpressionsParser.Analytic_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#analytic_function.
    def exitAnalytic_function(self, ctx:TeradataSQLExpressionsParser.Analytic_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#arithmetic_function.
    def enterArithmetic_function(self, ctx:TeradataSQLExpressionsParser.Arithmetic_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#arithmetic_function.
    def exitArithmetic_function(self, ctx:TeradataSQLExpressionsParser.Arithmetic_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#array_function.
    def enterArray_function(self, ctx:TeradataSQLExpressionsParser.Array_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#array_function.
    def exitArray_function(self, ctx:TeradataSQLExpressionsParser.Array_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#attribute_function.
    def enterAttribute_function(self, ctx:TeradataSQLExpressionsParser.Attribute_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#attribute_function.
    def exitAttribute_function(self, ctx:TeradataSQLExpressionsParser.Attribute_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#byte_function.
    def enterByte_function(self, ctx:TeradataSQLExpressionsParser.Byte_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#byte_function.
    def exitByte_function(self, ctx:TeradataSQLExpressionsParser.Byte_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#builtin_function.
    def enterBuiltin_function(self, ctx:TeradataSQLExpressionsParser.Builtin_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#builtin_function.
    def exitBuiltin_function(self, ctx:TeradataSQLExpressionsParser.Builtin_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#calendar_function.
    def enterCalendar_function(self, ctx:TeradataSQLExpressionsParser.Calendar_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#calendar_function.
    def exitCalendar_function(self, ctx:TeradataSQLExpressionsParser.Calendar_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#comparison_function.
    def enterComparison_function(self, ctx:TeradataSQLExpressionsParser.Comparison_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#comparison_function.
    def exitComparison_function(self, ctx:TeradataSQLExpressionsParser.Comparison_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#compression_function.
    def enterCompression_function(self, ctx:TeradataSQLExpressionsParser.Compression_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#compression_function.
    def exitCompression_function(self, ctx:TeradataSQLExpressionsParser.Compression_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#conversion_function.
    def enterConversion_function(self, ctx:TeradataSQLExpressionsParser.Conversion_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#conversion_function.
    def exitConversion_function(self, ctx:TeradataSQLExpressionsParser.Conversion_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#date_function.
    def enterDate_function(self, ctx:TeradataSQLExpressionsParser.Date_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#date_function.
    def exitDate_function(self, ctx:TeradataSQLExpressionsParser.Date_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#hash_function.
    def enterHash_function(self, ctx:TeradataSQLExpressionsParser.Hash_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#hash_function.
    def exitHash_function(self, ctx:TeradataSQLExpressionsParser.Hash_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#lob_function.
    def enterLob_function(self, ctx:TeradataSQLExpressionsParser.Lob_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#lob_function.
    def exitLob_function(self, ctx:TeradataSQLExpressionsParser.Lob_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#map_function.
    def enterMap_function(self, ctx:TeradataSQLExpressionsParser.Map_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#map_function.
    def exitMap_function(self, ctx:TeradataSQLExpressionsParser.Map_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#nvl_funtion.
    def enterNvl_funtion(self, ctx:TeradataSQLExpressionsParser.Nvl_funtionContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#nvl_funtion.
    def exitNvl_funtion(self, ctx:TeradataSQLExpressionsParser.Nvl_funtionContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#period_function.
    def enterPeriod_function(self, ctx:TeradataSQLExpressionsParser.Period_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#period_function.
    def exitPeriod_function(self, ctx:TeradataSQLExpressionsParser.Period_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#regexp_function.
    def enterRegexp_function(self, ctx:TeradataSQLExpressionsParser.Regexp_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#regexp_function.
    def exitRegexp_function(self, ctx:TeradataSQLExpressionsParser.Regexp_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#string_function.
    def enterString_function(self, ctx:TeradataSQLExpressionsParser.String_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#string_function.
    def exitString_function(self, ctx:TeradataSQLExpressionsParser.String_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#json_function.
    def enterJson_function(self, ctx:TeradataSQLExpressionsParser.Json_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#json_function.
    def exitJson_function(self, ctx:TeradataSQLExpressionsParser.Json_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#xml_function.
    def enterXml_function(self, ctx:TeradataSQLExpressionsParser.Xml_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#xml_function.
    def exitXml_function(self, ctx:TeradataSQLExpressionsParser.Xml_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#other_function.
    def enterOther_function(self, ctx:TeradataSQLExpressionsParser.Other_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#other_function.
    def exitOther_function(self, ctx:TeradataSQLExpressionsParser.Other_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#partitioning_expr.
    def enterPartitioning_expr(self, ctx:TeradataSQLExpressionsParser.Partitioning_exprContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#partitioning_expr.
    def exitPartitioning_expr(self, ctx:TeradataSQLExpressionsParser.Partitioning_exprContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#td_sysfnlib.
    def enterTd_sysfnlib(self, ctx:TeradataSQLExpressionsParser.Td_sysfnlibContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#td_sysfnlib.
    def exitTd_sysfnlib(self, ctx:TeradataSQLExpressionsParser.Td_sysfnlibContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#td_sysxml.
    def enterTd_sysxml(self, ctx:TeradataSQLExpressionsParser.Td_sysxmlContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#td_sysxml.
    def exitTd_sysxml(self, ctx:TeradataSQLExpressionsParser.Td_sysxmlContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#syslib.
    def enterSyslib(self, ctx:TeradataSQLExpressionsParser.SyslibContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#syslib.
    def exitSyslib(self, ctx:TeradataSQLExpressionsParser.SyslibContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#td_server_db.
    def enterTd_server_db(self, ctx:TeradataSQLExpressionsParser.Td_server_dbContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#td_server_db.
    def exitTd_server_db(self, ctx:TeradataSQLExpressionsParser.Td_server_dbContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#translation_mapping.
    def enterTranslation_mapping(self, ctx:TeradataSQLExpressionsParser.Translation_mappingContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#translation_mapping.
    def exitTranslation_mapping(self, ctx:TeradataSQLExpressionsParser.Translation_mappingContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#attribute_modification.
    def enterAttribute_modification(self, ctx:TeradataSQLExpressionsParser.Attribute_modificationContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#attribute_modification.
    def exitAttribute_modification(self, ctx:TeradataSQLExpressionsParser.Attribute_modificationContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#returns_clause.
    def enterReturns_clause(self, ctx:TeradataSQLExpressionsParser.Returns_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#returns_clause.
    def exitReturns_clause(self, ctx:TeradataSQLExpressionsParser.Returns_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#attribute_modification_option.
    def enterAttribute_modification_option(self, ctx:TeradataSQLExpressionsParser.Attribute_modification_optionContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#attribute_modification_option.
    def exitAttribute_modification_option(self, ctx:TeradataSQLExpressionsParser.Attribute_modification_optionContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#teradata_type_conversion.
    def enterTeradata_type_conversion(self, ctx:TeradataSQLExpressionsParser.Teradata_type_conversionContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#teradata_type_conversion.
    def exitTeradata_type_conversion(self, ctx:TeradataSQLExpressionsParser.Teradata_type_conversionContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#teradata_type_conversion_data_attribute.
    def enterTeradata_type_conversion_data_attribute(self, ctx:TeradataSQLExpressionsParser.Teradata_type_conversion_data_attributeContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#teradata_type_conversion_data_attribute.
    def exitTeradata_type_conversion_data_attribute(self, ctx:TeradataSQLExpressionsParser.Teradata_type_conversion_data_attributeContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#case_spec.
    def enterCase_spec(self, ctx:TeradataSQLExpressionsParser.Case_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#case_spec.
    def exitCase_spec(self, ctx:TeradataSQLExpressionsParser.Case_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#range_expr.
    def enterRange_expr(self, ctx:TeradataSQLExpressionsParser.Range_exprContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#range_expr.
    def exitRange_expr(self, ctx:TeradataSQLExpressionsParser.Range_exprContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#range_list.
    def enterRange_list(self, ctx:TeradataSQLExpressionsParser.Range_listContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#range_list.
    def exitRange_list(self, ctx:TeradataSQLExpressionsParser.Range_listContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#range_expr_1.
    def enterRange_expr_1(self, ctx:TeradataSQLExpressionsParser.Range_expr_1Context):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#range_expr_1.
    def exitRange_expr_1(self, ctx:TeradataSQLExpressionsParser.Range_expr_1Context):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#range_expr_2.
    def enterRange_expr_2(self, ctx:TeradataSQLExpressionsParser.Range_expr_2Context):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#range_expr_2.
    def exitRange_expr_2(self, ctx:TeradataSQLExpressionsParser.Range_expr_2Context):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#range_expr_3.
    def enterRange_expr_3(self, ctx:TeradataSQLExpressionsParser.Range_expr_3Context):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#range_expr_3.
    def exitRange_expr_3(self, ctx:TeradataSQLExpressionsParser.Range_expr_3Context):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#range_spec.
    def enterRange_spec(self, ctx:TeradataSQLExpressionsParser.Range_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#range_spec.
    def exitRange_spec(self, ctx:TeradataSQLExpressionsParser.Range_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#hash_bucket_number_expr.
    def enterHash_bucket_number_expr(self, ctx:TeradataSQLExpressionsParser.Hash_bucket_number_exprContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#hash_bucket_number_expr.
    def exitHash_bucket_number_expr(self, ctx:TeradataSQLExpressionsParser.Hash_bucket_number_exprContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#window_spec.
    def enterWindow_spec(self, ctx:TeradataSQLExpressionsParser.Window_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#window_spec.
    def exitWindow_spec(self, ctx:TeradataSQLExpressionsParser.Window_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#window_spec_without_rows.
    def enterWindow_spec_without_rows(self, ctx:TeradataSQLExpressionsParser.Window_spec_without_rowsContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#window_spec_without_rows.
    def exitWindow_spec_without_rows(self, ctx:TeradataSQLExpressionsParser.Window_spec_without_rowsContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#window_spec_with_ties.
    def enterWindow_spec_with_ties(self, ctx:TeradataSQLExpressionsParser.Window_spec_with_tiesContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#window_spec_with_ties.
    def exitWindow_spec_with_ties(self, ctx:TeradataSQLExpressionsParser.Window_spec_with_tiesContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#window_partition_by.
    def enterWindow_partition_by(self, ctx:TeradataSQLExpressionsParser.Window_partition_byContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#window_partition_by.
    def exitWindow_partition_by(self, ctx:TeradataSQLExpressionsParser.Window_partition_byContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#window_order_by.
    def enterWindow_order_by(self, ctx:TeradataSQLExpressionsParser.Window_order_byContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#window_order_by.
    def exitWindow_order_by(self, ctx:TeradataSQLExpressionsParser.Window_order_byContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#window_rows.
    def enterWindow_rows(self, ctx:TeradataSQLExpressionsParser.Window_rowsContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#window_rows.
    def exitWindow_rows(self, ctx:TeradataSQLExpressionsParser.Window_rowsContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#json_param_spec.
    def enterJson_param_spec(self, ctx:TeradataSQLExpressionsParser.Json_param_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#json_param_spec.
    def exitJson_param_spec(self, ctx:TeradataSQLExpressionsParser.Json_param_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#xml_query_argument.
    def enterXml_query_argument(self, ctx:TeradataSQLExpressionsParser.Xml_query_argumentContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#xml_query_argument.
    def exitXml_query_argument(self, ctx:TeradataSQLExpressionsParser.Xml_query_argumentContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#xml_query_variable_spec.
    def enterXml_query_variable_spec(self, ctx:TeradataSQLExpressionsParser.Xml_query_variable_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#xml_query_variable_spec.
    def exitXml_query_variable_spec(self, ctx:TeradataSQLExpressionsParser.Xml_query_variable_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#xml_attribute_declaration.
    def enterXml_attribute_declaration(self, ctx:TeradataSQLExpressionsParser.Xml_attribute_declarationContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#xml_attribute_declaration.
    def exitXml_attribute_declaration(self, ctx:TeradataSQLExpressionsParser.Xml_attribute_declarationContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#xml_attribute_spec.
    def enterXml_attribute_spec(self, ctx:TeradataSQLExpressionsParser.Xml_attribute_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#xml_attribute_spec.
    def exitXml_attribute_spec(self, ctx:TeradataSQLExpressionsParser.Xml_attribute_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#xml_forest_element_spec.
    def enterXml_forest_element_spec(self, ctx:TeradataSQLExpressionsParser.Xml_forest_element_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#xml_forest_element_spec.
    def exitXml_forest_element_spec(self, ctx:TeradataSQLExpressionsParser.Xml_forest_element_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#xml_value_declaration.
    def enterXml_value_declaration(self, ctx:TeradataSQLExpressionsParser.Xml_value_declarationContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#xml_value_declaration.
    def exitXml_value_declaration(self, ctx:TeradataSQLExpressionsParser.Xml_value_declarationContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#xml_namespace_declaration.
    def enterXml_namespace_declaration(self, ctx:TeradataSQLExpressionsParser.Xml_namespace_declarationContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#xml_namespace_declaration.
    def exitXml_namespace_declaration(self, ctx:TeradataSQLExpressionsParser.Xml_namespace_declarationContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#xml_namespace_spec.
    def enterXml_namespace_spec(self, ctx:TeradataSQLExpressionsParser.Xml_namespace_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#xml_namespace_spec.
    def exitXml_namespace_spec(self, ctx:TeradataSQLExpressionsParser.Xml_namespace_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#xml_columns_spec.
    def enterXml_columns_spec(self, ctx:TeradataSQLExpressionsParser.Xml_columns_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#xml_columns_spec.
    def exitXml_columns_spec(self, ctx:TeradataSQLExpressionsParser.Xml_columns_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#xml_regular_column_definition.
    def enterXml_regular_column_definition(self, ctx:TeradataSQLExpressionsParser.Xml_regular_column_definitionContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#xml_regular_column_definition.
    def exitXml_regular_column_definition(self, ctx:TeradataSQLExpressionsParser.Xml_regular_column_definitionContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#xml_encoding.
    def enterXml_encoding(self, ctx:TeradataSQLExpressionsParser.Xml_encodingContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#xml_encoding.
    def exitXml_encoding(self, ctx:TeradataSQLExpressionsParser.Xml_encodingContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#xml_query_on_empty.
    def enterXml_query_on_empty(self, ctx:TeradataSQLExpressionsParser.Xml_query_on_emptyContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#xml_query_on_empty.
    def exitXml_query_on_empty(self, ctx:TeradataSQLExpressionsParser.Xml_query_on_emptyContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#xml_returning_spec.
    def enterXml_returning_spec(self, ctx:TeradataSQLExpressionsParser.Xml_returning_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#xml_returning_spec.
    def exitXml_returning_spec(self, ctx:TeradataSQLExpressionsParser.Xml_returning_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#xml_content_option_spec.
    def enterXml_content_option_spec(self, ctx:TeradataSQLExpressionsParser.Xml_content_option_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#xml_content_option_spec.
    def exitXml_content_option_spec(self, ctx:TeradataSQLExpressionsParser.Xml_content_option_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#ignore_respect_nulls.
    def enterIgnore_respect_nulls(self, ctx:TeradataSQLExpressionsParser.Ignore_respect_nullsContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#ignore_respect_nulls.
    def exitIgnore_respect_nulls(self, ctx:TeradataSQLExpressionsParser.Ignore_respect_nullsContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#number_of_rows.
    def enterNumber_of_rows(self, ctx:TeradataSQLExpressionsParser.Number_of_rowsContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#number_of_rows.
    def exitNumber_of_rows(self, ctx:TeradataSQLExpressionsParser.Number_of_rowsContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#with_ties.
    def enterWith_ties(self, ctx:TeradataSQLExpressionsParser.With_tiesContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#with_ties.
    def exitWith_ties(self, ctx:TeradataSQLExpressionsParser.With_tiesContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#pivot.
    def enterPivot(self, ctx:TeradataSQLExpressionsParser.PivotContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#pivot.
    def exitPivot(self, ctx:TeradataSQLExpressionsParser.PivotContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#pivot_spec.
    def enterPivot_spec(self, ctx:TeradataSQLExpressionsParser.Pivot_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#pivot_spec.
    def exitPivot_spec(self, ctx:TeradataSQLExpressionsParser.Pivot_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#pivot_with_phrase.
    def enterPivot_with_phrase(self, ctx:TeradataSQLExpressionsParser.Pivot_with_phraseContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#pivot_with_phrase.
    def exitPivot_with_phrase(self, ctx:TeradataSQLExpressionsParser.Pivot_with_phraseContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#pivot_agg_func_spec.
    def enterPivot_agg_func_spec(self, ctx:TeradataSQLExpressionsParser.Pivot_agg_func_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#pivot_agg_func_spec.
    def exitPivot_agg_func_spec(self, ctx:TeradataSQLExpressionsParser.Pivot_agg_func_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#pivot_for_phrase.
    def enterPivot_for_phrase(self, ctx:TeradataSQLExpressionsParser.Pivot_for_phraseContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#pivot_for_phrase.
    def exitPivot_for_phrase(self, ctx:TeradataSQLExpressionsParser.Pivot_for_phraseContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#pivot_with_spec.
    def enterPivot_with_spec(self, ctx:TeradataSQLExpressionsParser.Pivot_with_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#pivot_with_spec.
    def exitPivot_with_spec(self, ctx:TeradataSQLExpressionsParser.Pivot_with_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#pivot_expr_spec_scalar.
    def enterPivot_expr_spec_scalar(self, ctx:TeradataSQLExpressionsParser.Pivot_expr_spec_scalarContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#pivot_expr_spec_scalar.
    def exitPivot_expr_spec_scalar(self, ctx:TeradataSQLExpressionsParser.Pivot_expr_spec_scalarContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#pivot_expr_spec_list.
    def enterPivot_expr_spec_list(self, ctx:TeradataSQLExpressionsParser.Pivot_expr_spec_listContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#pivot_expr_spec_list.
    def exitPivot_expr_spec_list(self, ctx:TeradataSQLExpressionsParser.Pivot_expr_spec_listContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#unpivot.
    def enterUnpivot(self, ctx:TeradataSQLExpressionsParser.UnpivotContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#unpivot.
    def exitUnpivot(self, ctx:TeradataSQLExpressionsParser.UnpivotContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#unpivot_spec.
    def enterUnpivot_spec(self, ctx:TeradataSQLExpressionsParser.Unpivot_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#unpivot_spec.
    def exitUnpivot_spec(self, ctx:TeradataSQLExpressionsParser.Unpivot_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#unpivot_column_name_spec_single.
    def enterUnpivot_column_name_spec_single(self, ctx:TeradataSQLExpressionsParser.Unpivot_column_name_spec_singleContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#unpivot_column_name_spec_single.
    def exitUnpivot_column_name_spec_single(self, ctx:TeradataSQLExpressionsParser.Unpivot_column_name_spec_singleContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#unpivot_column_name_spec_list.
    def enterUnpivot_column_name_spec_list(self, ctx:TeradataSQLExpressionsParser.Unpivot_column_name_spec_listContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#unpivot_column_name_spec_list.
    def exitUnpivot_column_name_spec_list(self, ctx:TeradataSQLExpressionsParser.Unpivot_column_name_spec_listContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#at_timezone.
    def enterAt_timezone(self, ctx:TeradataSQLExpressionsParser.At_timezoneContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#at_timezone.
    def exitAt_timezone(self, ctx:TeradataSQLExpressionsParser.At_timezoneContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#elements_list.
    def enterElements_list(self, ctx:TeradataSQLExpressionsParser.Elements_listContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#elements_list.
    def exitElements_list(self, ctx:TeradataSQLExpressionsParser.Elements_listContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#scalar_expr_list.
    def enterScalar_expr_list(self, ctx:TeradataSQLExpressionsParser.Scalar_expr_listContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#scalar_expr_list.
    def exitScalar_expr_list(self, ctx:TeradataSQLExpressionsParser.Scalar_expr_listContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#scalar_expr_list_comma_separated.
    def enterScalar_expr_list_comma_separated(self, ctx:TeradataSQLExpressionsParser.Scalar_expr_list_comma_separatedContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#scalar_expr_list_comma_separated.
    def exitScalar_expr_list_comma_separated(self, ctx:TeradataSQLExpressionsParser.Scalar_expr_list_comma_separatedContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#column_list.
    def enterColumn_list(self, ctx:TeradataSQLExpressionsParser.Column_listContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#column_list.
    def exitColumn_list(self, ctx:TeradataSQLExpressionsParser.Column_listContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#subquery.
    def enterSubquery(self, ctx:TeradataSQLExpressionsParser.SubqueryContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#subquery.
    def exitSubquery(self, ctx:TeradataSQLExpressionsParser.SubqueryContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#column_spec.
    def enterColumn_spec(self, ctx:TeradataSQLExpressionsParser.Column_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#column_spec.
    def exitColumn_spec(self, ctx:TeradataSQLExpressionsParser.Column_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#variable_reference.
    def enterVariable_reference(self, ctx:TeradataSQLExpressionsParser.Variable_referenceContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#variable_reference.
    def exitVariable_reference(self, ctx:TeradataSQLExpressionsParser.Variable_referenceContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#cursor_variable_reference.
    def enterCursor_variable_reference(self, ctx:TeradataSQLExpressionsParser.Cursor_variable_referenceContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#cursor_variable_reference.
    def exitCursor_variable_reference(self, ctx:TeradataSQLExpressionsParser.Cursor_variable_referenceContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#macro_parameter_reference.
    def enterMacro_parameter_reference(self, ctx:TeradataSQLExpressionsParser.Macro_parameter_referenceContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#macro_parameter_reference.
    def exitMacro_parameter_reference(self, ctx:TeradataSQLExpressionsParser.Macro_parameter_referenceContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#array_scope_reference.
    def enterArray_scope_reference(self, ctx:TeradataSQLExpressionsParser.Array_scope_referenceContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#array_scope_reference.
    def exitArray_scope_reference(self, ctx:TeradataSQLExpressionsParser.Array_scope_referenceContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#comparison_operator.
    def enterComparison_operator(self, ctx:TeradataSQLExpressionsParser.Comparison_operatorContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#comparison_operator.
    def exitComparison_operator(self, ctx:TeradataSQLExpressionsParser.Comparison_operatorContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#quantifier.
    def enterQuantifier(self, ctx:TeradataSQLExpressionsParser.QuantifierContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#quantifier.
    def exitQuantifier(self, ctx:TeradataSQLExpressionsParser.QuantifierContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#literal.
    def enterLiteral(self, ctx:TeradataSQLExpressionsParser.LiteralContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#literal.
    def exitLiteral(self, ctx:TeradataSQLExpressionsParser.LiteralContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#hex_byte_literal.
    def enterHex_byte_literal(self, ctx:TeradataSQLExpressionsParser.Hex_byte_literalContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#hex_byte_literal.
    def exitHex_byte_literal(self, ctx:TeradataSQLExpressionsParser.Hex_byte_literalContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#char_string_literal.
    def enterChar_string_literal(self, ctx:TeradataSQLExpressionsParser.Char_string_literalContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#char_string_literal.
    def exitChar_string_literal(self, ctx:TeradataSQLExpressionsParser.Char_string_literalContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#unicode_char_string_literal.
    def enterUnicode_char_string_literal(self, ctx:TeradataSQLExpressionsParser.Unicode_char_string_literalContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#unicode_char_string_literal.
    def exitUnicode_char_string_literal(self, ctx:TeradataSQLExpressionsParser.Unicode_char_string_literalContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#hex_char_string_literal.
    def enterHex_char_string_literal(self, ctx:TeradataSQLExpressionsParser.Hex_char_string_literalContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#hex_char_string_literal.
    def exitHex_char_string_literal(self, ctx:TeradataSQLExpressionsParser.Hex_char_string_literalContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#integer_literal.
    def enterInteger_literal(self, ctx:TeradataSQLExpressionsParser.Integer_literalContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#integer_literal.
    def exitInteger_literal(self, ctx:TeradataSQLExpressionsParser.Integer_literalContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#hex_integer_literal.
    def enterHex_integer_literal(self, ctx:TeradataSQLExpressionsParser.Hex_integer_literalContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#hex_integer_literal.
    def exitHex_integer_literal(self, ctx:TeradataSQLExpressionsParser.Hex_integer_literalContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#float_literal.
    def enterFloat_literal(self, ctx:TeradataSQLExpressionsParser.Float_literalContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#float_literal.
    def exitFloat_literal(self, ctx:TeradataSQLExpressionsParser.Float_literalContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#character_set_prefix.
    def enterCharacter_set_prefix(self, ctx:TeradataSQLExpressionsParser.Character_set_prefixContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#character_set_prefix.
    def exitCharacter_set_prefix(self, ctx:TeradataSQLExpressionsParser.Character_set_prefixContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#date_literal.
    def enterDate_literal(self, ctx:TeradataSQLExpressionsParser.Date_literalContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#date_literal.
    def exitDate_literal(self, ctx:TeradataSQLExpressionsParser.Date_literalContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#time_literal.
    def enterTime_literal(self, ctx:TeradataSQLExpressionsParser.Time_literalContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#time_literal.
    def exitTime_literal(self, ctx:TeradataSQLExpressionsParser.Time_literalContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#timestamp_literal.
    def enterTimestamp_literal(self, ctx:TeradataSQLExpressionsParser.Timestamp_literalContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#timestamp_literal.
    def exitTimestamp_literal(self, ctx:TeradataSQLExpressionsParser.Timestamp_literalContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#interval_literal.
    def enterInterval_literal(self, ctx:TeradataSQLExpressionsParser.Interval_literalContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#interval_literal.
    def exitInterval_literal(self, ctx:TeradataSQLExpressionsParser.Interval_literalContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#interval_qualifier.
    def enterInterval_qualifier(self, ctx:TeradataSQLExpressionsParser.Interval_qualifierContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#interval_qualifier.
    def exitInterval_qualifier(self, ctx:TeradataSQLExpressionsParser.Interval_qualifierContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#period_literal.
    def enterPeriod_literal(self, ctx:TeradataSQLExpressionsParser.Period_literalContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#period_literal.
    def exitPeriod_literal(self, ctx:TeradataSQLExpressionsParser.Period_literalContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#column_name.
    def enterColumn_name(self, ctx:TeradataSQLExpressionsParser.Column_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#column_name.
    def exitColumn_name(self, ctx:TeradataSQLExpressionsParser.Column_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#unqualified_column_name.
    def enterUnqualified_column_name(self, ctx:TeradataSQLExpressionsParser.Unqualified_column_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#unqualified_column_name.
    def exitUnqualified_column_name(self, ctx:TeradataSQLExpressionsParser.Unqualified_column_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#unqualified_name.
    def enterUnqualified_name(self, ctx:TeradataSQLExpressionsParser.Unqualified_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#unqualified_name.
    def exitUnqualified_name(self, ctx:TeradataSQLExpressionsParser.Unqualified_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#object_name.
    def enterObject_name(self, ctx:TeradataSQLExpressionsParser.Object_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#object_name.
    def exitObject_name(self, ctx:TeradataSQLExpressionsParser.Object_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#table_name.
    def enterTable_name(self, ctx:TeradataSQLExpressionsParser.Table_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#table_name.
    def exitTable_name(self, ctx:TeradataSQLExpressionsParser.Table_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#procedure_name.
    def enterProcedure_name(self, ctx:TeradataSQLExpressionsParser.Procedure_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#procedure_name.
    def exitProcedure_name(self, ctx:TeradataSQLExpressionsParser.Procedure_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#function_name.
    def enterFunction_name(self, ctx:TeradataSQLExpressionsParser.Function_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#function_name.
    def exitFunction_name(self, ctx:TeradataSQLExpressionsParser.Function_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#macro_name.
    def enterMacro_name(self, ctx:TeradataSQLExpressionsParser.Macro_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#macro_name.
    def exitMacro_name(self, ctx:TeradataSQLExpressionsParser.Macro_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#database_name.
    def enterDatabase_name(self, ctx:TeradataSQLExpressionsParser.Database_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#database_name.
    def exitDatabase_name(self, ctx:TeradataSQLExpressionsParser.Database_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#user_name.
    def enterUser_name(self, ctx:TeradataSQLExpressionsParser.User_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#user_name.
    def exitUser_name(self, ctx:TeradataSQLExpressionsParser.User_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#role_name.
    def enterRole_name(self, ctx:TeradataSQLExpressionsParser.Role_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#role_name.
    def exitRole_name(self, ctx:TeradataSQLExpressionsParser.Role_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#profile_name.
    def enterProfile_name(self, ctx:TeradataSQLExpressionsParser.Profile_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#profile_name.
    def exitProfile_name(self, ctx:TeradataSQLExpressionsParser.Profile_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#alias_name.
    def enterAlias_name(self, ctx:TeradataSQLExpressionsParser.Alias_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#alias_name.
    def exitAlias_name(self, ctx:TeradataSQLExpressionsParser.Alias_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#variable_name.
    def enterVariable_name(self, ctx:TeradataSQLExpressionsParser.Variable_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#variable_name.
    def exitVariable_name(self, ctx:TeradataSQLExpressionsParser.Variable_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#parameter_name.
    def enterParameter_name(self, ctx:TeradataSQLExpressionsParser.Parameter_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#parameter_name.
    def exitParameter_name(self, ctx:TeradataSQLExpressionsParser.Parameter_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#label_name.
    def enterLabel_name(self, ctx:TeradataSQLExpressionsParser.Label_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#label_name.
    def exitLabel_name(self, ctx:TeradataSQLExpressionsParser.Label_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#condition_name.
    def enterCondition_name(self, ctx:TeradataSQLExpressionsParser.Condition_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#condition_name.
    def exitCondition_name(self, ctx:TeradataSQLExpressionsParser.Condition_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#cursor_name.
    def enterCursor_name(self, ctx:TeradataSQLExpressionsParser.Cursor_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#cursor_name.
    def exitCursor_name(self, ctx:TeradataSQLExpressionsParser.Cursor_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#statement_name.
    def enterStatement_name(self, ctx:TeradataSQLExpressionsParser.Statement_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#statement_name.
    def exitStatement_name(self, ctx:TeradataSQLExpressionsParser.Statement_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#statistics_name.
    def enterStatistics_name(self, ctx:TeradataSQLExpressionsParser.Statistics_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#statistics_name.
    def exitStatistics_name(self, ctx:TeradataSQLExpressionsParser.Statistics_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#udt_name.
    def enterUdt_name(self, ctx:TeradataSQLExpressionsParser.Udt_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#udt_name.
    def exitUdt_name(self, ctx:TeradataSQLExpressionsParser.Udt_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#attribute_name.
    def enterAttribute_name(self, ctx:TeradataSQLExpressionsParser.Attribute_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#attribute_name.
    def exitAttribute_name(self, ctx:TeradataSQLExpressionsParser.Attribute_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#method_name.
    def enterMethod_name(self, ctx:TeradataSQLExpressionsParser.Method_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#method_name.
    def exitMethod_name(self, ctx:TeradataSQLExpressionsParser.Method_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#anchor_name.
    def enterAnchor_name(self, ctx:TeradataSQLExpressionsParser.Anchor_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#anchor_name.
    def exitAnchor_name(self, ctx:TeradataSQLExpressionsParser.Anchor_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#nonreserved_word.
    def enterNonreserved_word(self, ctx:TeradataSQLExpressionsParser.Nonreserved_wordContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#nonreserved_word.
    def exitNonreserved_word(self, ctx:TeradataSQLExpressionsParser.Nonreserved_wordContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#data_type.
    def enterData_type(self, ctx:TeradataSQLExpressionsParser.Data_typeContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#data_type.
    def exitData_type(self, ctx:TeradataSQLExpressionsParser.Data_typeContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#variable_data_type.
    def enterVariable_data_type(self, ctx:TeradataSQLExpressionsParser.Variable_data_typeContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#variable_data_type.
    def exitVariable_data_type(self, ctx:TeradataSQLExpressionsParser.Variable_data_typeContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#external_function_data_type.
    def enterExternal_function_data_type(self, ctx:TeradataSQLExpressionsParser.External_function_data_typeContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#external_function_data_type.
    def exitExternal_function_data_type(self, ctx:TeradataSQLExpressionsParser.External_function_data_typeContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#numeric_data_type.
    def enterNumeric_data_type(self, ctx:TeradataSQLExpressionsParser.Numeric_data_typeContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#numeric_data_type.
    def exitNumeric_data_type(self, ctx:TeradataSQLExpressionsParser.Numeric_data_typeContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#char_data_type.
    def enterChar_data_type(self, ctx:TeradataSQLExpressionsParser.Char_data_typeContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#char_data_type.
    def exitChar_data_type(self, ctx:TeradataSQLExpressionsParser.Char_data_typeContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#precisionless_char_data_type.
    def enterPrecisionless_char_data_type(self, ctx:TeradataSQLExpressionsParser.Precisionless_char_data_typeContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#precisionless_char_data_type.
    def exitPrecisionless_char_data_type(self, ctx:TeradataSQLExpressionsParser.Precisionless_char_data_typeContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#lob_as_locator_data_type.
    def enterLob_as_locator_data_type(self, ctx:TeradataSQLExpressionsParser.Lob_as_locator_data_typeContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#lob_as_locator_data_type.
    def exitLob_as_locator_data_type(self, ctx:TeradataSQLExpressionsParser.Lob_as_locator_data_typeContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#binary_data_type.
    def enterBinary_data_type(self, ctx:TeradataSQLExpressionsParser.Binary_data_typeContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#binary_data_type.
    def exitBinary_data_type(self, ctx:TeradataSQLExpressionsParser.Binary_data_typeContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#datetime_type.
    def enterDatetime_type(self, ctx:TeradataSQLExpressionsParser.Datetime_typeContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#datetime_type.
    def exitDatetime_type(self, ctx:TeradataSQLExpressionsParser.Datetime_typeContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#period_type.
    def enterPeriod_type(self, ctx:TeradataSQLExpressionsParser.Period_typeContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#period_type.
    def exitPeriod_type(self, ctx:TeradataSQLExpressionsParser.Period_typeContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#udt_type.
    def enterUdt_type(self, ctx:TeradataSQLExpressionsParser.Udt_typeContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#udt_type.
    def exitUdt_type(self, ctx:TeradataSQLExpressionsParser.Udt_typeContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#data_type_attribute.
    def enterData_type_attribute(self, ctx:TeradataSQLExpressionsParser.Data_type_attributeContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#data_type_attribute.
    def exitData_type_attribute(self, ctx:TeradataSQLExpressionsParser.Data_type_attributeContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#default_value_control_phrase.
    def enterDefault_value_control_phrase(self, ctx:TeradataSQLExpressionsParser.Default_value_control_phraseContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#default_value_control_phrase.
    def exitDefault_value_control_phrase(self, ctx:TeradataSQLExpressionsParser.Default_value_control_phraseContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#default_value.
    def enterDefault_value(self, ctx:TeradataSQLExpressionsParser.Default_valueContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#default_value.
    def exitDefault_value(self, ctx:TeradataSQLExpressionsParser.Default_valueContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#column_naming_phrase.
    def enterColumn_naming_phrase(self, ctx:TeradataSQLExpressionsParser.Column_naming_phraseContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#column_naming_phrase.
    def exitColumn_naming_phrase(self, ctx:TeradataSQLExpressionsParser.Column_naming_phraseContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#sysudtlib.
    def enterSysudtlib(self, ctx:TeradataSQLExpressionsParser.SysudtlibContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#sysudtlib.
    def exitSysudtlib(self, ctx:TeradataSQLExpressionsParser.SysudtlibContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#interval_period_spec.
    def enterInterval_period_spec(self, ctx:TeradataSQLExpressionsParser.Interval_period_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#interval_period_spec.
    def exitInterval_period_spec(self, ctx:TeradataSQLExpressionsParser.Interval_period_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#type_precision.
    def enterType_precision(self, ctx:TeradataSQLExpressionsParser.Type_precisionContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#type_precision.
    def exitType_precision(self, ctx:TeradataSQLExpressionsParser.Type_precisionContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#max_length_k_m_g.
    def enterMax_length_k_m_g(self, ctx:TeradataSQLExpressionsParser.Max_length_k_m_gContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#max_length_k_m_g.
    def exitMax_length_k_m_g(self, ctx:TeradataSQLExpressionsParser.Max_length_k_m_gContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#max_length_k_m.
    def enterMax_length_k_m(self, ctx:TeradataSQLExpressionsParser.Max_length_k_mContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#max_length_k_m.
    def exitMax_length_k_m(self, ctx:TeradataSQLExpressionsParser.Max_length_k_mContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#character_set_phrase.
    def enterCharacter_set_phrase(self, ctx:TeradataSQLExpressionsParser.Character_set_phraseContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#character_set_phrase.
    def exitCharacter_set_phrase(self, ctx:TeradataSQLExpressionsParser.Character_set_phraseContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#uppercase_phrase.
    def enterUppercase_phrase(self, ctx:TeradataSQLExpressionsParser.Uppercase_phraseContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#uppercase_phrase.
    def exitUppercase_phrase(self, ctx:TeradataSQLExpressionsParser.Uppercase_phraseContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#casespecific_phrase.
    def enterCasespecific_phrase(self, ctx:TeradataSQLExpressionsParser.Casespecific_phraseContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#casespecific_phrase.
    def exitCasespecific_phrase(self, ctx:TeradataSQLExpressionsParser.Casespecific_phraseContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#format_phrase.
    def enterFormat_phrase(self, ctx:TeradataSQLExpressionsParser.Format_phraseContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#format_phrase.
    def exitFormat_phrase(self, ctx:TeradataSQLExpressionsParser.Format_phraseContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#title_phrase.
    def enterTitle_phrase(self, ctx:TeradataSQLExpressionsParser.Title_phraseContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#title_phrase.
    def exitTitle_phrase(self, ctx:TeradataSQLExpressionsParser.Title_phraseContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#named_phrase.
    def enterNamed_phrase(self, ctx:TeradataSQLExpressionsParser.Named_phraseContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#named_phrase.
    def exitNamed_phrase(self, ctx:TeradataSQLExpressionsParser.Named_phraseContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#latin_unicode_character_set_phrase.
    def enterLatin_unicode_character_set_phrase(self, ctx:TeradataSQLExpressionsParser.Latin_unicode_character_set_phraseContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#latin_unicode_character_set_phrase.
    def exitLatin_unicode_character_set_phrase(self, ctx:TeradataSQLExpressionsParser.Latin_unicode_character_set_phraseContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#inline_length.
    def enterInline_length(self, ctx:TeradataSQLExpressionsParser.Inline_lengthContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#inline_length.
    def exitInline_length(self, ctx:TeradataSQLExpressionsParser.Inline_lengthContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#json_storage_format.
    def enterJson_storage_format(self, ctx:TeradataSQLExpressionsParser.Json_storage_formatContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#json_storage_format.
    def exitJson_storage_format(self, ctx:TeradataSQLExpressionsParser.Json_storage_formatContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#dataset_storage_format_clause.
    def enterDataset_storage_format_clause(self, ctx:TeradataSQLExpressionsParser.Dataset_storage_format_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#dataset_storage_format_clause.
    def exitDataset_storage_format_clause(self, ctx:TeradataSQLExpressionsParser.Dataset_storage_format_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#dataset_storage_format.
    def enterDataset_storage_format(self, ctx:TeradataSQLExpressionsParser.Dataset_storage_formatContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#dataset_storage_format.
    def exitDataset_storage_format(self, ctx:TeradataSQLExpressionsParser.Dataset_storage_formatContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#with_schema.
    def enterWith_schema(self, ctx:TeradataSQLExpressionsParser.With_schemaContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#with_schema.
    def exitWith_schema(self, ctx:TeradataSQLExpressionsParser.With_schemaContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#with_time_zone.
    def enterWith_time_zone(self, ctx:TeradataSQLExpressionsParser.With_time_zoneContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#with_time_zone.
    def exitWith_time_zone(self, ctx:TeradataSQLExpressionsParser.With_time_zoneContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#request_modifier.
    def enterRequest_modifier(self, ctx:TeradataSQLExpressionsParser.Request_modifierContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#request_modifier.
    def exitRequest_modifier(self, ctx:TeradataSQLExpressionsParser.Request_modifierContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#locking_request_modifier.
    def enterLocking_request_modifier(self, ctx:TeradataSQLExpressionsParser.Locking_request_modifierContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#locking_request_modifier.
    def exitLocking_request_modifier(self, ctx:TeradataSQLExpressionsParser.Locking_request_modifierContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#locking_spec.
    def enterLocking_spec(self, ctx:TeradataSQLExpressionsParser.Locking_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#locking_spec.
    def exitLocking_spec(self, ctx:TeradataSQLExpressionsParser.Locking_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#lock_type.
    def enterLock_type(self, ctx:TeradataSQLExpressionsParser.Lock_typeContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#lock_type.
    def exitLock_type(self, ctx:TeradataSQLExpressionsParser.Lock_typeContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#with_request_modifier.
    def enterWith_request_modifier(self, ctx:TeradataSQLExpressionsParser.With_request_modifierContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#with_request_modifier.
    def exitWith_request_modifier(self, ctx:TeradataSQLExpressionsParser.With_request_modifierContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#cte_spec.
    def enterCte_spec(self, ctx:TeradataSQLExpressionsParser.Cte_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#cte_spec.
    def exitCte_spec(self, ctx:TeradataSQLExpressionsParser.Cte_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#regular_cte_spec.
    def enterRegular_cte_spec(self, ctx:TeradataSQLExpressionsParser.Regular_cte_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#regular_cte_spec.
    def exitRegular_cte_spec(self, ctx:TeradataSQLExpressionsParser.Regular_cte_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#recursive_cte_spec.
    def enterRecursive_cte_spec(self, ctx:TeradataSQLExpressionsParser.Recursive_cte_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#recursive_cte_spec.
    def exitRecursive_cte_spec(self, ctx:TeradataSQLExpressionsParser.Recursive_cte_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#using_request_modifier.
    def enterUsing_request_modifier(self, ctx:TeradataSQLExpressionsParser.Using_request_modifierContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#using_request_modifier.
    def exitUsing_request_modifier(self, ctx:TeradataSQLExpressionsParser.Using_request_modifierContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#using_spec.
    def enterUsing_spec(self, ctx:TeradataSQLExpressionsParser.Using_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#using_spec.
    def exitUsing_spec(self, ctx:TeradataSQLExpressionsParser.Using_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLExpressionsParser#explain_request_modifier.
    def enterExplain_request_modifier(self, ctx:TeradataSQLExpressionsParser.Explain_request_modifierContext):
        pass

    # Exit a parse tree produced by TeradataSQLExpressionsParser#explain_request_modifier.
    def exitExplain_request_modifier(self, ctx:TeradataSQLExpressionsParser.Explain_request_modifierContext):
        pass



del TeradataSQLExpressionsParser