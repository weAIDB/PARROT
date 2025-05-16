# Generated from sql/teradata/TeradataSQLRequestModifiersParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .TeradataSQLRequestModifiersParser import TeradataSQLRequestModifiersParser
else:
    from TeradataSQLRequestModifiersParser import TeradataSQLRequestModifiersParser

# This class defines a complete listener for a parse tree produced by TeradataSQLRequestModifiersParser.
class TeradataSQLRequestModifiersParserListener(ParseTreeListener):

    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#request_modifier.
    def enterRequest_modifier(self, ctx:TeradataSQLRequestModifiersParser.Request_modifierContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#request_modifier.
    def exitRequest_modifier(self, ctx:TeradataSQLRequestModifiersParser.Request_modifierContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#locking_request_modifier.
    def enterLocking_request_modifier(self, ctx:TeradataSQLRequestModifiersParser.Locking_request_modifierContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#locking_request_modifier.
    def exitLocking_request_modifier(self, ctx:TeradataSQLRequestModifiersParser.Locking_request_modifierContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#locking_spec.
    def enterLocking_spec(self, ctx:TeradataSQLRequestModifiersParser.Locking_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#locking_spec.
    def exitLocking_spec(self, ctx:TeradataSQLRequestModifiersParser.Locking_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#lock_type.
    def enterLock_type(self, ctx:TeradataSQLRequestModifiersParser.Lock_typeContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#lock_type.
    def exitLock_type(self, ctx:TeradataSQLRequestModifiersParser.Lock_typeContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#with_request_modifier.
    def enterWith_request_modifier(self, ctx:TeradataSQLRequestModifiersParser.With_request_modifierContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#with_request_modifier.
    def exitWith_request_modifier(self, ctx:TeradataSQLRequestModifiersParser.With_request_modifierContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#cte_spec.
    def enterCte_spec(self, ctx:TeradataSQLRequestModifiersParser.Cte_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#cte_spec.
    def exitCte_spec(self, ctx:TeradataSQLRequestModifiersParser.Cte_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#regular_cte_spec.
    def enterRegular_cte_spec(self, ctx:TeradataSQLRequestModifiersParser.Regular_cte_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#regular_cte_spec.
    def exitRegular_cte_spec(self, ctx:TeradataSQLRequestModifiersParser.Regular_cte_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#recursive_cte_spec.
    def enterRecursive_cte_spec(self, ctx:TeradataSQLRequestModifiersParser.Recursive_cte_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#recursive_cte_spec.
    def exitRecursive_cte_spec(self, ctx:TeradataSQLRequestModifiersParser.Recursive_cte_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#using_request_modifier.
    def enterUsing_request_modifier(self, ctx:TeradataSQLRequestModifiersParser.Using_request_modifierContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#using_request_modifier.
    def exitUsing_request_modifier(self, ctx:TeradataSQLRequestModifiersParser.Using_request_modifierContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#using_spec.
    def enterUsing_spec(self, ctx:TeradataSQLRequestModifiersParser.Using_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#using_spec.
    def exitUsing_spec(self, ctx:TeradataSQLRequestModifiersParser.Using_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#explain_request_modifier.
    def enterExplain_request_modifier(self, ctx:TeradataSQLRequestModifiersParser.Explain_request_modifierContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#explain_request_modifier.
    def exitExplain_request_modifier(self, ctx:TeradataSQLRequestModifiersParser.Explain_request_modifierContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#query_expr.
    def enterQuery_expr(self, ctx:TeradataSQLRequestModifiersParser.Query_exprContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#query_expr.
    def exitQuery_expr(self, ctx:TeradataSQLRequestModifiersParser.Query_exprContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#query_term.
    def enterQuery_term(self, ctx:TeradataSQLRequestModifiersParser.Query_termContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#query_term.
    def exitQuery_term(self, ctx:TeradataSQLRequestModifiersParser.Query_termContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#with_deleted_rows.
    def enterWith_deleted_rows(self, ctx:TeradataSQLRequestModifiersParser.With_deleted_rowsContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#with_deleted_rows.
    def exitWith_deleted_rows(self, ctx:TeradataSQLRequestModifiersParser.With_deleted_rowsContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#as_json.
    def enterAs_json(self, ctx:TeradataSQLRequestModifiersParser.As_jsonContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#as_json.
    def exitAs_json(self, ctx:TeradataSQLRequestModifiersParser.As_jsonContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#select_list.
    def enterSelect_list(self, ctx:TeradataSQLRequestModifiersParser.Select_listContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#select_list.
    def exitSelect_list(self, ctx:TeradataSQLRequestModifiersParser.Select_listContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#top_n.
    def enterTop_n(self, ctx:TeradataSQLRequestModifiersParser.Top_nContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#top_n.
    def exitTop_n(self, ctx:TeradataSQLRequestModifiersParser.Top_nContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#normalize.
    def enterNormalize(self, ctx:TeradataSQLRequestModifiersParser.NormalizeContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#normalize.
    def exitNormalize(self, ctx:TeradataSQLRequestModifiersParser.NormalizeContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#all_operator.
    def enterAll_operator(self, ctx:TeradataSQLRequestModifiersParser.All_operatorContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#all_operator.
    def exitAll_operator(self, ctx:TeradataSQLRequestModifiersParser.All_operatorContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#selected_columns.
    def enterSelected_columns(self, ctx:TeradataSQLRequestModifiersParser.Selected_columnsContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#selected_columns.
    def exitSelected_columns(self, ctx:TeradataSQLRequestModifiersParser.Selected_columnsContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#selected_column.
    def enterSelected_column(self, ctx:TeradataSQLRequestModifiersParser.Selected_columnContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#selected_column.
    def exitSelected_column(self, ctx:TeradataSQLRequestModifiersParser.Selected_columnContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#into_clause.
    def enterInto_clause(self, ctx:TeradataSQLRequestModifiersParser.Into_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#into_clause.
    def exitInto_clause(self, ctx:TeradataSQLRequestModifiersParser.Into_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#from_clause.
    def enterFrom_clause(self, ctx:TeradataSQLRequestModifiersParser.From_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#from_clause.
    def exitFrom_clause(self, ctx:TeradataSQLRequestModifiersParser.From_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#from_spec.
    def enterFrom_spec(self, ctx:TeradataSQLRequestModifiersParser.From_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#from_spec.
    def exitFrom_spec(self, ctx:TeradataSQLRequestModifiersParser.From_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#join_source_spec.
    def enterJoin_source_spec(self, ctx:TeradataSQLRequestModifiersParser.Join_source_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#join_source_spec.
    def exitJoin_source_spec(self, ctx:TeradataSQLRequestModifiersParser.Join_source_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#join_joined_spec.
    def enterJoin_joined_spec(self, ctx:TeradataSQLRequestModifiersParser.Join_joined_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#join_joined_spec.
    def exitJoin_joined_spec(self, ctx:TeradataSQLRequestModifiersParser.Join_joined_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#from_pivot_spec.
    def enterFrom_pivot_spec(self, ctx:TeradataSQLRequestModifiersParser.From_pivot_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#from_pivot_spec.
    def exitFrom_pivot_spec(self, ctx:TeradataSQLRequestModifiersParser.From_pivot_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#from_unpivot_spec.
    def enterFrom_unpivot_spec(self, ctx:TeradataSQLRequestModifiersParser.From_unpivot_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#from_unpivot_spec.
    def exitFrom_unpivot_spec(self, ctx:TeradataSQLRequestModifiersParser.From_unpivot_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#table_reference.
    def enterTable_reference(self, ctx:TeradataSQLRequestModifiersParser.Table_referenceContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#table_reference.
    def exitTable_reference(self, ctx:TeradataSQLRequestModifiersParser.Table_referenceContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#join_clause.
    def enterJoin_clause(self, ctx:TeradataSQLRequestModifiersParser.Join_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#join_clause.
    def exitJoin_clause(self, ctx:TeradataSQLRequestModifiersParser.Join_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#join_on_clause.
    def enterJoin_on_clause(self, ctx:TeradataSQLRequestModifiersParser.Join_on_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#join_on_clause.
    def exitJoin_on_clause(self, ctx:TeradataSQLRequestModifiersParser.Join_on_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#foreign_table_reference.
    def enterForeign_table_reference(self, ctx:TeradataSQLRequestModifiersParser.Foreign_table_referenceContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#foreign_table_reference.
    def exitForeign_table_reference(self, ctx:TeradataSQLRequestModifiersParser.Foreign_table_referenceContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#foreign_function_reference.
    def enterForeign_function_reference(self, ctx:TeradataSQLRequestModifiersParser.Foreign_function_referenceContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#foreign_function_reference.
    def exitForeign_function_reference(self, ctx:TeradataSQLRequestModifiersParser.Foreign_function_referenceContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#foreign_on_clause.
    def enterForeign_on_clause(self, ctx:TeradataSQLRequestModifiersParser.Foreign_on_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#foreign_on_clause.
    def exitForeign_on_clause(self, ctx:TeradataSQLRequestModifiersParser.Foreign_on_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#exported_data.
    def enterExported_data(self, ctx:TeradataSQLRequestModifiersParser.Exported_dataContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#exported_data.
    def exitExported_data(self, ctx:TeradataSQLRequestModifiersParser.Exported_dataContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#foreign_using_clause.
    def enterForeign_using_clause(self, ctx:TeradataSQLRequestModifiersParser.Foreign_using_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#foreign_using_clause.
    def exitForeign_using_clause(self, ctx:TeradataSQLRequestModifiersParser.Foreign_using_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#foreign_parameter.
    def enterForeign_parameter(self, ctx:TeradataSQLRequestModifiersParser.Foreign_parameterContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#foreign_parameter.
    def exitForeign_parameter(self, ctx:TeradataSQLRequestModifiersParser.Foreign_parameterContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#foreign_returns_clause.
    def enterForeign_returns_clause(self, ctx:TeradataSQLRequestModifiersParser.Foreign_returns_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#foreign_returns_clause.
    def exitForeign_returns_clause(self, ctx:TeradataSQLRequestModifiersParser.Foreign_returns_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#server_name_reference.
    def enterServer_name_reference(self, ctx:TeradataSQLRequestModifiersParser.Server_name_referenceContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#server_name_reference.
    def exitServer_name_reference(self, ctx:TeradataSQLRequestModifiersParser.Server_name_referenceContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#table_function_reference.
    def enterTable_function_reference(self, ctx:TeradataSQLRequestModifiersParser.Table_function_referenceContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#table_function_reference.
    def exitTable_function_reference(self, ctx:TeradataSQLRequestModifiersParser.Table_function_referenceContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#udt_table_function.
    def enterUdt_table_function(self, ctx:TeradataSQLRequestModifiersParser.Udt_table_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#udt_table_function.
    def exitUdt_table_function(self, ctx:TeradataSQLRequestModifiersParser.Udt_table_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#unnest_table_function.
    def enterUnnest_table_function(self, ctx:TeradataSQLRequestModifiersParser.Unnest_table_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#unnest_table_function.
    def exitUnnest_table_function(self, ctx:TeradataSQLRequestModifiersParser.Unnest_table_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#table_function_returns_clause.
    def enterTable_function_returns_clause(self, ctx:TeradataSQLRequestModifiersParser.Table_function_returns_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#table_function_returns_clause.
    def exitTable_function_returns_clause(self, ctx:TeradataSQLRequestModifiersParser.Table_function_returns_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#table_function_local_order_by_clause.
    def enterTable_function_local_order_by_clause(self, ctx:TeradataSQLRequestModifiersParser.Table_function_local_order_by_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#table_function_local_order_by_clause.
    def exitTable_function_local_order_by_clause(self, ctx:TeradataSQLRequestModifiersParser.Table_function_local_order_by_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#table_function_hash_by_clause.
    def enterTable_function_hash_by_clause(self, ctx:TeradataSQLRequestModifiersParser.Table_function_hash_by_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#table_function_hash_by_clause.
    def exitTable_function_hash_by_clause(self, ctx:TeradataSQLRequestModifiersParser.Table_function_hash_by_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#table_operator_reference.
    def enterTable_operator_reference(self, ctx:TeradataSQLRequestModifiersParser.Table_operator_referenceContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#table_operator_reference.
    def exitTable_operator_reference(self, ctx:TeradataSQLRequestModifiersParser.Table_operator_referenceContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#xmltable_operator.
    def enterXmltable_operator(self, ctx:TeradataSQLRequestModifiersParser.Xmltable_operatorContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#xmltable_operator.
    def exitXmltable_operator(self, ctx:TeradataSQLRequestModifiersParser.Xmltable_operatorContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#calcmatrix_table_operator.
    def enterCalcmatrix_table_operator(self, ctx:TeradataSQLRequestModifiersParser.Calcmatrix_table_operatorContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#calcmatrix_table_operator.
    def exitCalcmatrix_table_operator(self, ctx:TeradataSQLRequestModifiersParser.Calcmatrix_table_operatorContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#read_nos_table_operator.
    def enterRead_nos_table_operator(self, ctx:TeradataSQLRequestModifiersParser.Read_nos_table_operatorContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#read_nos_table_operator.
    def exitRead_nos_table_operator(self, ctx:TeradataSQLRequestModifiersParser.Read_nos_table_operatorContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#script_table_operator.
    def enterScript_table_operator(self, ctx:TeradataSQLRequestModifiersParser.Script_table_operatorContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#script_table_operator.
    def exitScript_table_operator(self, ctx:TeradataSQLRequestModifiersParser.Script_table_operatorContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#td_unpivot_table_operator.
    def enterTd_unpivot_table_operator(self, ctx:TeradataSQLRequestModifiersParser.Td_unpivot_table_operatorContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#td_unpivot_table_operator.
    def exitTd_unpivot_table_operator(self, ctx:TeradataSQLRequestModifiersParser.Td_unpivot_table_operatorContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#write_nos_table_operator.
    def enterWrite_nos_table_operator(self, ctx:TeradataSQLRequestModifiersParser.Write_nos_table_operatorContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#write_nos_table_operator.
    def exitWrite_nos_table_operator(self, ctx:TeradataSQLRequestModifiersParser.Write_nos_table_operatorContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#json_table_table_operator.
    def enterJson_table_table_operator(self, ctx:TeradataSQLRequestModifiersParser.Json_table_table_operatorContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#json_table_table_operator.
    def exitJson_table_table_operator(self, ctx:TeradataSQLRequestModifiersParser.Json_table_table_operatorContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#json_keys_table_operator.
    def enterJson_keys_table_operator(self, ctx:TeradataSQLRequestModifiersParser.Json_keys_table_operatorContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#json_keys_table_operator.
    def exitJson_keys_table_operator(self, ctx:TeradataSQLRequestModifiersParser.Json_keys_table_operatorContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#json_shred_table_operator.
    def enterJson_shred_table_operator(self, ctx:TeradataSQLRequestModifiersParser.Json_shred_table_operatorContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#json_shred_table_operator.
    def exitJson_shred_table_operator(self, ctx:TeradataSQLRequestModifiersParser.Json_shred_table_operatorContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#generic_table_operator.
    def enterGeneric_table_operator(self, ctx:TeradataSQLRequestModifiersParser.Generic_table_operatorContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#generic_table_operator.
    def exitGeneric_table_operator(self, ctx:TeradataSQLRequestModifiersParser.Generic_table_operatorContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#table_operator_on_clause.
    def enterTable_operator_on_clause(self, ctx:TeradataSQLRequestModifiersParser.Table_operator_on_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#table_operator_on_clause.
    def exitTable_operator_on_clause(self, ctx:TeradataSQLRequestModifiersParser.Table_operator_on_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#table_operator_execute_clause.
    def enterTable_operator_execute_clause(self, ctx:TeradataSQLRequestModifiersParser.Table_operator_execute_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#table_operator_execute_clause.
    def exitTable_operator_execute_clause(self, ctx:TeradataSQLRequestModifiersParser.Table_operator_execute_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#table_operator_out_table_clause.
    def enterTable_operator_out_table_clause(self, ctx:TeradataSQLRequestModifiersParser.Table_operator_out_table_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#table_operator_out_table_clause.
    def exitTable_operator_out_table_clause(self, ctx:TeradataSQLRequestModifiersParser.Table_operator_out_table_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#table_operator_using_clause.
    def enterTable_operator_using_clause(self, ctx:TeradataSQLRequestModifiersParser.Table_operator_using_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#table_operator_using_clause.
    def exitTable_operator_using_clause(self, ctx:TeradataSQLRequestModifiersParser.Table_operator_using_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#table_operator_using_spec.
    def enterTable_operator_using_spec(self, ctx:TeradataSQLRequestModifiersParser.Table_operator_using_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#table_operator_using_spec.
    def exitTable_operator_using_spec(self, ctx:TeradataSQLRequestModifiersParser.Table_operator_using_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#json_keys_using_name_value_pair.
    def enterJson_keys_using_name_value_pair(self, ctx:TeradataSQLRequestModifiersParser.Json_keys_using_name_value_pairContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#json_keys_using_name_value_pair.
    def exitJson_keys_using_name_value_pair(self, ctx:TeradataSQLRequestModifiersParser.Json_keys_using_name_value_pairContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#hash_or_partition_by.
    def enterHash_or_partition_by(self, ctx:TeradataSQLRequestModifiersParser.Hash_or_partition_byContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#hash_or_partition_by.
    def exitHash_or_partition_by(self, ctx:TeradataSQLRequestModifiersParser.Hash_or_partition_byContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#subquery_reference.
    def enterSubquery_reference(self, ctx:TeradataSQLRequestModifiersParser.Subquery_referenceContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#subquery_reference.
    def exitSubquery_reference(self, ctx:TeradataSQLRequestModifiersParser.Subquery_referenceContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#location.
    def enterLocation(self, ctx:TeradataSQLRequestModifiersParser.LocationContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#location.
    def exitLocation(self, ctx:TeradataSQLRequestModifiersParser.LocationContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#read_nos_option.
    def enterRead_nos_option(self, ctx:TeradataSQLRequestModifiersParser.Read_nos_optionContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#read_nos_option.
    def exitRead_nos_option(self, ctx:TeradataSQLRequestModifiersParser.Read_nos_optionContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#write_nos_option.
    def enterWrite_nos_option(self, ctx:TeradataSQLRequestModifiersParser.Write_nos_optionContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#write_nos_option.
    def exitWrite_nos_option(self, ctx:TeradataSQLRequestModifiersParser.Write_nos_optionContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#with_clause.
    def enterWith_clause(self, ctx:TeradataSQLRequestModifiersParser.With_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#with_clause.
    def exitWith_clause(self, ctx:TeradataSQLRequestModifiersParser.With_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#with_clause_by_phrase.
    def enterWith_clause_by_phrase(self, ctx:TeradataSQLRequestModifiersParser.With_clause_by_phraseContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#with_clause_by_phrase.
    def exitWith_clause_by_phrase(self, ctx:TeradataSQLRequestModifiersParser.With_clause_by_phraseContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#with_clause_title_phrase.
    def enterWith_clause_title_phrase(self, ctx:TeradataSQLRequestModifiersParser.With_clause_title_phraseContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#with_clause_title_phrase.
    def exitWith_clause_title_phrase(self, ctx:TeradataSQLRequestModifiersParser.With_clause_title_phraseContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#where_clause.
    def enterWhere_clause(self, ctx:TeradataSQLRequestModifiersParser.Where_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#where_clause.
    def exitWhere_clause(self, ctx:TeradataSQLRequestModifiersParser.Where_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#group_by_clause.
    def enterGroup_by_clause(self, ctx:TeradataSQLRequestModifiersParser.Group_by_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#group_by_clause.
    def exitGroup_by_clause(self, ctx:TeradataSQLRequestModifiersParser.Group_by_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#group_by_spec.
    def enterGroup_by_spec(self, ctx:TeradataSQLRequestModifiersParser.Group_by_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#group_by_spec.
    def exitGroup_by_spec(self, ctx:TeradataSQLRequestModifiersParser.Group_by_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#ordinary_grouping_set.
    def enterOrdinary_grouping_set(self, ctx:TeradataSQLRequestModifiersParser.Ordinary_grouping_setContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#ordinary_grouping_set.
    def exitOrdinary_grouping_set(self, ctx:TeradataSQLRequestModifiersParser.Ordinary_grouping_setContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#ordinary_grouping_set_parenthesized.
    def enterOrdinary_grouping_set_parenthesized(self, ctx:TeradataSQLRequestModifiersParser.Ordinary_grouping_set_parenthesizedContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#ordinary_grouping_set_parenthesized.
    def exitOrdinary_grouping_set_parenthesized(self, ctx:TeradataSQLRequestModifiersParser.Ordinary_grouping_set_parenthesizedContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#empty_grouping_set.
    def enterEmpty_grouping_set(self, ctx:TeradataSQLRequestModifiersParser.Empty_grouping_setContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#empty_grouping_set.
    def exitEmpty_grouping_set(self, ctx:TeradataSQLRequestModifiersParser.Empty_grouping_setContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#rollup_option.
    def enterRollup_option(self, ctx:TeradataSQLRequestModifiersParser.Rollup_optionContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#rollup_option.
    def exitRollup_option(self, ctx:TeradataSQLRequestModifiersParser.Rollup_optionContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#cube_option.
    def enterCube_option(self, ctx:TeradataSQLRequestModifiersParser.Cube_optionContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#cube_option.
    def exitCube_option(self, ctx:TeradataSQLRequestModifiersParser.Cube_optionContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#grouping_sets_option.
    def enterGrouping_sets_option(self, ctx:TeradataSQLRequestModifiersParser.Grouping_sets_optionContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#grouping_sets_option.
    def exitGrouping_sets_option(self, ctx:TeradataSQLRequestModifiersParser.Grouping_sets_optionContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#grouping_sets_spec.
    def enterGrouping_sets_spec(self, ctx:TeradataSQLRequestModifiersParser.Grouping_sets_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#grouping_sets_spec.
    def exitGrouping_sets_spec(self, ctx:TeradataSQLRequestModifiersParser.Grouping_sets_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#having_clause.
    def enterHaving_clause(self, ctx:TeradataSQLRequestModifiersParser.Having_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#having_clause.
    def exitHaving_clause(self, ctx:TeradataSQLRequestModifiersParser.Having_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#qualify_clause.
    def enterQualify_clause(self, ctx:TeradataSQLRequestModifiersParser.Qualify_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#qualify_clause.
    def exitQualify_clause(self, ctx:TeradataSQLRequestModifiersParser.Qualify_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#sample_clause.
    def enterSample_clause(self, ctx:TeradataSQLRequestModifiersParser.Sample_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#sample_clause.
    def exitSample_clause(self, ctx:TeradataSQLRequestModifiersParser.Sample_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#sample_fraction_description.
    def enterSample_fraction_description(self, ctx:TeradataSQLRequestModifiersParser.Sample_fraction_descriptionContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#sample_fraction_description.
    def exitSample_fraction_description(self, ctx:TeradataSQLRequestModifiersParser.Sample_fraction_descriptionContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#sample_count_description.
    def enterSample_count_description(self, ctx:TeradataSQLRequestModifiersParser.Sample_count_descriptionContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#sample_count_description.
    def exitSample_count_description(self, ctx:TeradataSQLRequestModifiersParser.Sample_count_descriptionContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#sample_when_clause.
    def enterSample_when_clause(self, ctx:TeradataSQLRequestModifiersParser.Sample_when_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#sample_when_clause.
    def exitSample_when_clause(self, ctx:TeradataSQLRequestModifiersParser.Sample_when_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#expand_on_clause.
    def enterExpand_on_clause(self, ctx:TeradataSQLRequestModifiersParser.Expand_on_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#expand_on_clause.
    def exitExpand_on_clause(self, ctx:TeradataSQLRequestModifiersParser.Expand_on_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#order_by_clause.
    def enterOrder_by_clause(self, ctx:TeradataSQLRequestModifiersParser.Order_by_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#order_by_clause.
    def exitOrder_by_clause(self, ctx:TeradataSQLRequestModifiersParser.Order_by_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#order_by_spec_full.
    def enterOrder_by_spec_full(self, ctx:TeradataSQLRequestModifiersParser.Order_by_spec_fullContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#order_by_spec_full.
    def exitOrder_by_spec_full(self, ctx:TeradataSQLRequestModifiersParser.Order_by_spec_fullContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#order_by_spec_asc_desc_only.
    def enterOrder_by_spec_asc_desc_only(self, ctx:TeradataSQLRequestModifiersParser.Order_by_spec_asc_desc_onlyContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#order_by_spec_asc_desc_only.
    def exitOrder_by_spec_asc_desc_only(self, ctx:TeradataSQLRequestModifiersParser.Order_by_spec_asc_desc_onlyContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#with_check_option.
    def enterWith_check_option(self, ctx:TeradataSQLRequestModifiersParser.With_check_optionContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#with_check_option.
    def exitWith_check_option(self, ctx:TeradataSQLRequestModifiersParser.With_check_optionContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#PeriodMeets.
    def enterPeriodMeets(self, ctx:TeradataSQLRequestModifiersParser.PeriodMeetsContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#PeriodMeets.
    def exitPeriodMeets(self, ctx:TeradataSQLRequestModifiersParser.PeriodMeetsContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#PeriodImmediatelySucceeds.
    def enterPeriodImmediatelySucceeds(self, ctx:TeradataSQLRequestModifiersParser.PeriodImmediatelySucceedsContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#PeriodImmediatelySucceeds.
    def exitPeriodImmediatelySucceeds(self, ctx:TeradataSQLRequestModifiersParser.PeriodImmediatelySucceedsContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#PeriodEquals.
    def enterPeriodEquals(self, ctx:TeradataSQLRequestModifiersParser.PeriodEqualsContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#PeriodEquals.
    def exitPeriodEquals(self, ctx:TeradataSQLRequestModifiersParser.PeriodEqualsContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#ScalarComparelist.
    def enterScalarComparelist(self, ctx:TeradataSQLRequestModifiersParser.ScalarComparelistContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#ScalarComparelist.
    def exitScalarComparelist(self, ctx:TeradataSQLRequestModifiersParser.ScalarComparelistContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#TupleInSubquery.
    def enterTupleInSubquery(self, ctx:TeradataSQLRequestModifiersParser.TupleInSubqueryContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#TupleInSubquery.
    def exitTupleInSubquery(self, ctx:TeradataSQLRequestModifiersParser.TupleInSubqueryContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#LogicalOr.
    def enterLogicalOr(self, ctx:TeradataSQLRequestModifiersParser.LogicalOrContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#LogicalOr.
    def exitLogicalOr(self, ctx:TeradataSQLRequestModifiersParser.LogicalOrContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#ScalarInScalar.
    def enterScalarInScalar(self, ctx:TeradataSQLRequestModifiersParser.ScalarInScalarContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#ScalarInScalar.
    def exitScalarInScalar(self, ctx:TeradataSQLRequestModifiersParser.ScalarInScalarContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#ScalarCompareScalar.
    def enterScalarCompareScalar(self, ctx:TeradataSQLRequestModifiersParser.ScalarCompareScalarContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#ScalarCompareScalar.
    def exitScalarCompareScalar(self, ctx:TeradataSQLRequestModifiersParser.ScalarCompareScalarContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#LogicalNot.
    def enterLogicalNot(self, ctx:TeradataSQLRequestModifiersParser.LogicalNotContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#LogicalNot.
    def exitLogicalNot(self, ctx:TeradataSQLRequestModifiersParser.LogicalNotContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#TupleComparelist.
    def enterTupleComparelist(self, ctx:TeradataSQLRequestModifiersParser.TupleComparelistContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#TupleComparelist.
    def exitTupleComparelist(self, ctx:TeradataSQLRequestModifiersParser.TupleComparelistContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#ScalarInList.
    def enterScalarInList(self, ctx:TeradataSQLRequestModifiersParser.ScalarInListContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#ScalarInList.
    def exitScalarInList(self, ctx:TeradataSQLRequestModifiersParser.ScalarInListContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#TupleLikeList.
    def enterTupleLikeList(self, ctx:TeradataSQLRequestModifiersParser.TupleLikeListContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#TupleLikeList.
    def exitTupleLikeList(self, ctx:TeradataSQLRequestModifiersParser.TupleLikeListContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#LogicalAnd.
    def enterLogicalAnd(self, ctx:TeradataSQLRequestModifiersParser.LogicalAndContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#LogicalAnd.
    def exitLogicalAnd(self, ctx:TeradataSQLRequestModifiersParser.LogicalAndContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#ScalarInSubquery.
    def enterScalarInSubquery(self, ctx:TeradataSQLRequestModifiersParser.ScalarInSubqueryContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#ScalarInSubquery.
    def exitScalarInSubquery(self, ctx:TeradataSQLRequestModifiersParser.ScalarInSubqueryContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#PeriodContains.
    def enterPeriodContains(self, ctx:TeradataSQLRequestModifiersParser.PeriodContainsContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#PeriodContains.
    def exitPeriodContains(self, ctx:TeradataSQLRequestModifiersParser.PeriodContainsContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#PeriodOverlaps.
    def enterPeriodOverlaps(self, ctx:TeradataSQLRequestModifiersParser.PeriodOverlapsContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#PeriodOverlaps.
    def exitPeriodOverlaps(self, ctx:TeradataSQLRequestModifiersParser.PeriodOverlapsContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#Between.
    def enterBetween(self, ctx:TeradataSQLRequestModifiersParser.BetweenContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#Between.
    def exitBetween(self, ctx:TeradataSQLRequestModifiersParser.BetweenContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#ParenthesizedLogicalExpr.
    def enterParenthesizedLogicalExpr(self, ctx:TeradataSQLRequestModifiersParser.ParenthesizedLogicalExprContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#ParenthesizedLogicalExpr.
    def exitParenthesizedLogicalExpr(self, ctx:TeradataSQLRequestModifiersParser.ParenthesizedLogicalExprContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#PeriodImmediatelyPrecedes.
    def enterPeriodImmediatelyPrecedes(self, ctx:TeradataSQLRequestModifiersParser.PeriodImmediatelyPrecedesContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#PeriodImmediatelyPrecedes.
    def exitPeriodImmediatelyPrecedes(self, ctx:TeradataSQLRequestModifiersParser.PeriodImmediatelyPrecedesContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#NullCheck.
    def enterNullCheck(self, ctx:TeradataSQLRequestModifiersParser.NullCheckContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#NullCheck.
    def exitNullCheck(self, ctx:TeradataSQLRequestModifiersParser.NullCheckContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#PeriodPrecedes.
    def enterPeriodPrecedes(self, ctx:TeradataSQLRequestModifiersParser.PeriodPrecedesContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#PeriodPrecedes.
    def exitPeriodPrecedes(self, ctx:TeradataSQLRequestModifiersParser.PeriodPrecedesContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#Exists.
    def enterExists(self, ctx:TeradataSQLRequestModifiersParser.ExistsContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#Exists.
    def exitExists(self, ctx:TeradataSQLRequestModifiersParser.ExistsContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#PeriodSucceeds.
    def enterPeriodSucceeds(self, ctx:TeradataSQLRequestModifiersParser.PeriodSucceedsContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#PeriodSucceeds.
    def exitPeriodSucceeds(self, ctx:TeradataSQLRequestModifiersParser.PeriodSucceedsContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#ScalarLikeList.
    def enterScalarLikeList(self, ctx:TeradataSQLRequestModifiersParser.ScalarLikeListContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#ScalarLikeList.
    def exitScalarLikeList(self, ctx:TeradataSQLRequestModifiersParser.ScalarLikeListContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#ScalarLikeScalar.
    def enterScalarLikeScalar(self, ctx:TeradataSQLRequestModifiersParser.ScalarLikeScalarContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#ScalarLikeScalar.
    def exitScalarLikeScalar(self, ctx:TeradataSQLRequestModifiersParser.ScalarLikeScalarContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#JsonMetadata.
    def enterJsonMetadata(self, ctx:TeradataSQLRequestModifiersParser.JsonMetadataContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#JsonMetadata.
    def exitJsonMetadata(self, ctx:TeradataSQLRequestModifiersParser.JsonMetadataContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#JsonAsBson.
    def enterJsonAsBson(self, ctx:TeradataSQLRequestModifiersParser.JsonAsBsonContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#JsonAsBson.
    def exitJsonAsBson(self, ctx:TeradataSQLRequestModifiersParser.JsonAsBsonContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#VariantTypeConstructor.
    def enterVariantTypeConstructor(self, ctx:TeradataSQLRequestModifiersParser.VariantTypeConstructorContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#VariantTypeConstructor.
    def exitVariantTypeConstructor(self, ctx:TeradataSQLRequestModifiersParser.VariantTypeConstructorContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#XMLExtract.
    def enterXMLExtract(self, ctx:TeradataSQLRequestModifiersParser.XMLExtractContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#XMLExtract.
    def exitXMLExtract(self, ctx:TeradataSQLRequestModifiersParser.XMLExtractContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#ArrayComparison.
    def enterArrayComparison(self, ctx:TeradataSQLRequestModifiersParser.ArrayComparisonContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#ArrayComparison.
    def exitArrayComparison(self, ctx:TeradataSQLRequestModifiersParser.ArrayComparisonContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#ArrayGet.
    def enterArrayGet(self, ctx:TeradataSQLRequestModifiersParser.ArrayGetContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#ArrayGet.
    def exitArrayGet(self, ctx:TeradataSQLRequestModifiersParser.ArrayGetContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#XMLConstructor.
    def enterXMLConstructor(self, ctx:TeradataSQLRequestModifiersParser.XMLConstructorContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#XMLConstructor.
    def exitXMLConstructor(self, ctx:TeradataSQLRequestModifiersParser.XMLConstructorContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#UDTMethodInvocation.
    def enterUDTMethodInvocation(self, ctx:TeradataSQLRequestModifiersParser.UDTMethodInvocationContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#UDTMethodInvocation.
    def exitUDTMethodInvocation(self, ctx:TeradataSQLRequestModifiersParser.UDTMethodInvocationContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#JsonExtractLargeValue.
    def enterJsonExtractLargeValue(self, ctx:TeradataSQLRequestModifiersParser.JsonExtractLargeValueContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#JsonExtractLargeValue.
    def exitJsonExtractLargeValue(self, ctx:TeradataSQLRequestModifiersParser.JsonExtractLargeValueContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#JsonRecursiveDescendSlice.
    def enterJsonRecursiveDescendSlice(self, ctx:TeradataSQLRequestModifiersParser.JsonRecursiveDescendSliceContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#JsonRecursiveDescendSlice.
    def exitJsonRecursiveDescendSlice(self, ctx:TeradataSQLRequestModifiersParser.JsonRecursiveDescendSliceContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#FunctionInvocation.
    def enterFunctionInvocation(self, ctx:TeradataSQLRequestModifiersParser.FunctionInvocationContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#FunctionInvocation.
    def exitFunctionInvocation(self, ctx:TeradataSQLRequestModifiersParser.FunctionInvocationContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#ScalarSubquery.
    def enterScalarSubquery(self, ctx:TeradataSQLRequestModifiersParser.ScalarSubqueryContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#ScalarSubquery.
    def exitScalarSubquery(self, ctx:TeradataSQLRequestModifiersParser.ScalarSubqueryContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#JsonExistValue.
    def enterJsonExistValue(self, ctx:TeradataSQLRequestModifiersParser.JsonExistValueContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#JsonExistValue.
    def exitJsonExistValue(self, ctx:TeradataSQLRequestModifiersParser.JsonExistValueContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#Modulo.
    def enterModulo(self, ctx:TeradataSQLRequestModifiersParser.ModuloContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#Modulo.
    def exitModulo(self, ctx:TeradataSQLRequestModifiersParser.ModuloContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#JsonExtractValue.
    def enterJsonExtractValue(self, ctx:TeradataSQLRequestModifiersParser.JsonExtractValueContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#JsonExtractValue.
    def exitJsonExtractValue(self, ctx:TeradataSQLRequestModifiersParser.JsonExtractValueContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#XMLCreateSchemaBasedXML.
    def enterXMLCreateSchemaBasedXML(self, ctx:TeradataSQLRequestModifiersParser.XMLCreateSchemaBasedXMLContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#XMLCreateSchemaBasedXML.
    def exitXMLCreateSchemaBasedXML(self, ctx:TeradataSQLRequestModifiersParser.XMLCreateSchemaBasedXMLContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#ArrayUpdate.
    def enterArrayUpdate(self, ctx:TeradataSQLRequestModifiersParser.ArrayUpdateContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#ArrayUpdate.
    def exitArrayUpdate(self, ctx:TeradataSQLRequestModifiersParser.ArrayUpdateContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#JsonExtract.
    def enterJsonExtract(self, ctx:TeradataSQLRequestModifiersParser.JsonExtractContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#JsonExtract.
    def exitJsonExtract(self, ctx:TeradataSQLRequestModifiersParser.JsonExtractContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#MultDiv.
    def enterMultDiv(self, ctx:TeradataSQLRequestModifiersParser.MultDivContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#MultDiv.
    def exitMultDiv(self, ctx:TeradataSQLRequestModifiersParser.MultDivContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#PeriodIntersect.
    def enterPeriodIntersect(self, ctx:TeradataSQLRequestModifiersParser.PeriodIntersectContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#PeriodIntersect.
    def exitPeriodIntersect(self, ctx:TeradataSQLRequestModifiersParser.PeriodIntersectContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#IntervalExprParenthesized.
    def enterIntervalExprParenthesized(self, ctx:TeradataSQLRequestModifiersParser.IntervalExprParenthesizedContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#IntervalExprParenthesized.
    def exitIntervalExprParenthesized(self, ctx:TeradataSQLRequestModifiersParser.IntervalExprParenthesizedContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#JsonRecursiveDescendAllArrayElements.
    def enterJsonRecursiveDescendAllArrayElements(self, ctx:TeradataSQLRequestModifiersParser.JsonRecursiveDescendAllArrayElementsContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#JsonRecursiveDescendAllArrayElements.
    def exitJsonRecursiveDescendAllArrayElements(self, ctx:TeradataSQLRequestModifiersParser.JsonRecursiveDescendAllArrayElementsContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#UnaryPlusMinus.
    def enterUnaryPlusMinus(self, ctx:TeradataSQLRequestModifiersParser.UnaryPlusMinusContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#UnaryPlusMinus.
    def exitUnaryPlusMinus(self, ctx:TeradataSQLRequestModifiersParser.UnaryPlusMinusContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#Concatenation.
    def enterConcatenation(self, ctx:TeradataSQLRequestModifiersParser.ConcatenationContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#Concatenation.
    def exitConcatenation(self, ctx:TeradataSQLRequestModifiersParser.ConcatenationContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#PeriodDiff.
    def enterPeriodDiff(self, ctx:TeradataSQLRequestModifiersParser.PeriodDiffContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#PeriodDiff.
    def exitPeriodDiff(self, ctx:TeradataSQLRequestModifiersParser.PeriodDiffContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#ArrayOmethodWithoudArgs.
    def enterArrayOmethodWithoudArgs(self, ctx:TeradataSQLRequestModifiersParser.ArrayOmethodWithoudArgsContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#ArrayOmethodWithoudArgs.
    def exitArrayOmethodWithoudArgs(self, ctx:TeradataSQLRequestModifiersParser.ArrayOmethodWithoudArgsContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#PartitioningExpr.
    def enterPartitioningExpr(self, ctx:TeradataSQLRequestModifiersParser.PartitioningExprContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#PartitioningExpr.
    def exitPartitioningExpr(self, ctx:TeradataSQLRequestModifiersParser.PartitioningExprContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#XMLExistNode.
    def enterXMLExistNode(self, ctx:TeradataSQLRequestModifiersParser.XMLExistNodeContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#XMLExistNode.
    def exitXMLExistNode(self, ctx:TeradataSQLRequestModifiersParser.XMLExistNodeContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#JsonRecursiveDescendArrayElementReference.
    def enterJsonRecursiveDescendArrayElementReference(self, ctx:TeradataSQLRequestModifiersParser.JsonRecursiveDescendArrayElementReferenceContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#JsonRecursiveDescendArrayElementReference.
    def exitJsonRecursiveDescendArrayElementReference(self, ctx:TeradataSQLRequestModifiersParser.JsonRecursiveDescendArrayElementReferenceContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#DataTypeConversion.
    def enterDataTypeConversion(self, ctx:TeradataSQLRequestModifiersParser.DataTypeConversionContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#DataTypeConversion.
    def exitDataTypeConversion(self, ctx:TeradataSQLRequestModifiersParser.DataTypeConversionContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#JsonRecursiveDescendObjectMember.
    def enterJsonRecursiveDescendObjectMember(self, ctx:TeradataSQLRequestModifiersParser.JsonRecursiveDescendObjectMemberContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#JsonRecursiveDescendObjectMember.
    def exitJsonRecursiveDescendObjectMember(self, ctx:TeradataSQLRequestModifiersParser.JsonRecursiveDescendObjectMemberContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#IntervalExpr.
    def enterIntervalExpr(self, ctx:TeradataSQLRequestModifiersParser.IntervalExprContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#IntervalExpr.
    def exitIntervalExpr(self, ctx:TeradataSQLRequestModifiersParser.IntervalExprContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#Exponentiation.
    def enterExponentiation(self, ctx:TeradataSQLRequestModifiersParser.ExponentiationContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#Exponentiation.
    def exitExponentiation(self, ctx:TeradataSQLRequestModifiersParser.ExponentiationContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#XMLIsSchemaValidated.
    def enterXMLIsSchemaValidated(self, ctx:TeradataSQLRequestModifiersParser.XMLIsSchemaValidatedContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#XMLIsSchemaValidated.
    def exitXMLIsSchemaValidated(self, ctx:TeradataSQLRequestModifiersParser.XMLIsSchemaValidatedContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#JSONConstructor.
    def enterJSONConstructor(self, ctx:TeradataSQLRequestModifiersParser.JSONConstructorContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#JSONConstructor.
    def exitJSONConstructor(self, ctx:TeradataSQLRequestModifiersParser.JSONConstructorContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#JsonSlice.
    def enterJsonSlice(self, ctx:TeradataSQLRequestModifiersParser.JsonSliceContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#JsonSlice.
    def exitJsonSlice(self, ctx:TeradataSQLRequestModifiersParser.JsonSliceContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#XMLIsSchemaValid.
    def enterXMLIsSchemaValid(self, ctx:TeradataSQLRequestModifiersParser.XMLIsSchemaValidContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#XMLIsSchemaValid.
    def exitXMLIsSchemaValid(self, ctx:TeradataSQLRequestModifiersParser.XMLIsSchemaValidContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#ArrayAggregation.
    def enterArrayAggregation(self, ctx:TeradataSQLRequestModifiersParser.ArrayAggregationContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#ArrayAggregation.
    def exitArrayAggregation(self, ctx:TeradataSQLRequestModifiersParser.ArrayAggregationContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#ArrayUpdateStride.
    def enterArrayUpdateStride(self, ctx:TeradataSQLRequestModifiersParser.ArrayUpdateStrideContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#ArrayUpdateStride.
    def exitArrayUpdateStride(self, ctx:TeradataSQLRequestModifiersParser.ArrayUpdateStrideContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#LiteralExpr.
    def enterLiteralExpr(self, ctx:TeradataSQLRequestModifiersParser.LiteralExprContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#LiteralExpr.
    def exitLiteralExpr(self, ctx:TeradataSQLRequestModifiersParser.LiteralExprContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#ArrayOmethodWithArg.
    def enterArrayOmethodWithArg(self, ctx:TeradataSQLRequestModifiersParser.ArrayOmethodWithArgContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#ArrayOmethodWithArg.
    def exitArrayOmethodWithArg(self, ctx:TeradataSQLRequestModifiersParser.ArrayOmethodWithArgContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#JsonRecursiveDescendAllObjectMembers.
    def enterJsonRecursiveDescendAllObjectMembers(self, ctx:TeradataSQLRequestModifiersParser.JsonRecursiveDescendAllObjectMembersContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#JsonRecursiveDescendAllObjectMembers.
    def exitJsonRecursiveDescendAllObjectMembers(self, ctx:TeradataSQLRequestModifiersParser.JsonRecursiveDescendAllObjectMembersContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#XMLCreateNonSchemaBasedXML.
    def enterXMLCreateNonSchemaBasedXML(self, ctx:TeradataSQLRequestModifiersParser.XMLCreateNonSchemaBasedXMLContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#XMLCreateNonSchemaBasedXML.
    def exitXMLCreateNonSchemaBasedXML(self, ctx:TeradataSQLRequestModifiersParser.XMLCreateNonSchemaBasedXMLContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#VariableReference.
    def enterVariableReference(self, ctx:TeradataSQLRequestModifiersParser.VariableReferenceContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#VariableReference.
    def exitVariableReference(self, ctx:TeradataSQLRequestModifiersParser.VariableReferenceContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#AddSub.
    def enterAddSub(self, ctx:TeradataSQLRequestModifiersParser.AddSubContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#AddSub.
    def exitAddSub(self, ctx:TeradataSQLRequestModifiersParser.AddSubContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#JsonObjectMember.
    def enterJsonObjectMember(self, ctx:TeradataSQLRequestModifiersParser.JsonObjectMemberContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#JsonObjectMember.
    def exitJsonObjectMember(self, ctx:TeradataSQLRequestModifiersParser.JsonObjectMemberContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#JsonAllElements.
    def enterJsonAllElements(self, ctx:TeradataSQLRequestModifiersParser.JsonAllElementsContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#JsonAllElements.
    def exitJsonAllElements(self, ctx:TeradataSQLRequestModifiersParser.JsonAllElementsContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#ArrayOextend.
    def enterArrayOextend(self, ctx:TeradataSQLRequestModifiersParser.ArrayOextendContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#ArrayOextend.
    def exitArrayOextend(self, ctx:TeradataSQLRequestModifiersParser.ArrayOextendContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#ArrayArithmetic.
    def enterArrayArithmetic(self, ctx:TeradataSQLRequestModifiersParser.ArrayArithmeticContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#ArrayArithmetic.
    def exitArrayArithmetic(self, ctx:TeradataSQLRequestModifiersParser.ArrayArithmeticContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#UDTConstructor.
    def enterUDTConstructor(self, ctx:TeradataSQLRequestModifiersParser.UDTConstructorContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#UDTConstructor.
    def exitUDTConstructor(self, ctx:TeradataSQLRequestModifiersParser.UDTConstructorContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#XMLTransform.
    def enterXMLTransform(self, ctx:TeradataSQLRequestModifiersParser.XMLTransformContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#XMLTransform.
    def exitXMLTransform(self, ctx:TeradataSQLRequestModifiersParser.XMLTransformContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#DateTimeExpr.
    def enterDateTimeExpr(self, ctx:TeradataSQLRequestModifiersParser.DateTimeExprContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#DateTimeExpr.
    def exitDateTimeExpr(self, ctx:TeradataSQLRequestModifiersParser.DateTimeExprContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#ColumnName.
    def enterColumnName(self, ctx:TeradataSQLRequestModifiersParser.ColumnNameContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#ColumnName.
    def exitColumnName(self, ctx:TeradataSQLRequestModifiersParser.ColumnNameContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#ArrayOtrim.
    def enterArrayOtrim(self, ctx:TeradataSQLRequestModifiersParser.ArrayOtrimContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#ArrayOtrim.
    def exitArrayOtrim(self, ctx:TeradataSQLRequestModifiersParser.ArrayOtrimContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#CursorVariableReference.
    def enterCursorVariableReference(self, ctx:TeradataSQLRequestModifiersParser.CursorVariableReferenceContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#CursorVariableReference.
    def exitCursorVariableReference(self, ctx:TeradataSQLRequestModifiersParser.CursorVariableReferenceContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#Parenthesized.
    def enterParenthesized(self, ctx:TeradataSQLRequestModifiersParser.ParenthesizedContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#Parenthesized.
    def exitParenthesized(self, ctx:TeradataSQLRequestModifiersParser.ParenthesizedContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#JsonAsBsonText.
    def enterJsonAsBsonText(self, ctx:TeradataSQLRequestModifiersParser.JsonAsBsonTextContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#JsonAsBsonText.
    def exitJsonAsBsonText(self, ctx:TeradataSQLRequestModifiersParser.JsonAsBsonTextContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#AttributeModification.
    def enterAttributeModification(self, ctx:TeradataSQLRequestModifiersParser.AttributeModificationContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#AttributeModification.
    def exitAttributeModification(self, ctx:TeradataSQLRequestModifiersParser.AttributeModificationContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#JsonCombine.
    def enterJsonCombine(self, ctx:TeradataSQLRequestModifiersParser.JsonCombineContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#JsonCombine.
    def exitJsonCombine(self, ctx:TeradataSQLRequestModifiersParser.JsonCombineContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#XMLIsDocument.
    def enterXMLIsDocument(self, ctx:TeradataSQLRequestModifiersParser.XMLIsDocumentContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#XMLIsDocument.
    def exitXMLIsDocument(self, ctx:TeradataSQLRequestModifiersParser.XMLIsDocumentContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#MacroParameterReference.
    def enterMacroParameterReference(self, ctx:TeradataSQLRequestModifiersParser.MacroParameterReferenceContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#MacroParameterReference.
    def exitMacroParameterReference(self, ctx:TeradataSQLRequestModifiersParser.MacroParameterReferenceContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#XMLIsContent.
    def enterXMLIsContent(self, ctx:TeradataSQLRequestModifiersParser.XMLIsContentContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#XMLIsContent.
    def exitXMLIsContent(self, ctx:TeradataSQLRequestModifiersParser.XMLIsContentContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#ArrayElementReference.
    def enterArrayElementReference(self, ctx:TeradataSQLRequestModifiersParser.ArrayElementReferenceContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#ArrayElementReference.
    def exitArrayElementReference(self, ctx:TeradataSQLRequestModifiersParser.ArrayElementReferenceContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#ArrayCardinality.
    def enterArrayCardinality(self, ctx:TeradataSQLRequestModifiersParser.ArrayCardinalityContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#ArrayCardinality.
    def exitArrayCardinality(self, ctx:TeradataSQLRequestModifiersParser.ArrayCardinalityContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#CaseExpr.
    def enterCaseExpr(self, ctx:TeradataSQLRequestModifiersParser.CaseExprContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#CaseExpr.
    def exitCaseExpr(self, ctx:TeradataSQLRequestModifiersParser.CaseExprContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#JsonKeycount.
    def enterJsonKeycount(self, ctx:TeradataSQLRequestModifiersParser.JsonKeycountContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#JsonKeycount.
    def exitJsonKeycount(self, ctx:TeradataSQLRequestModifiersParser.JsonKeycountContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#JsonAllObjectMembers.
    def enterJsonAllObjectMembers(self, ctx:TeradataSQLRequestModifiersParser.JsonAllObjectMembersContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#JsonAllObjectMembers.
    def exitJsonAllObjectMembers(self, ctx:TeradataSQLRequestModifiersParser.JsonAllObjectMembersContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#tuple.
    def enterTuple(self, ctx:TeradataSQLRequestModifiersParser.TupleContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#tuple.
    def exitTuple(self, ctx:TeradataSQLRequestModifiersParser.TupleContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#tuple_attribute.
    def enterTuple_attribute(self, ctx:TeradataSQLRequestModifiersParser.Tuple_attributeContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#tuple_attribute.
    def exitTuple_attribute(self, ctx:TeradataSQLRequestModifiersParser.Tuple_attributeContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#case_expr.
    def enterCase_expr(self, ctx:TeradataSQLRequestModifiersParser.Case_exprContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#case_expr.
    def exitCase_expr(self, ctx:TeradataSQLRequestModifiersParser.Case_exprContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#valued_case_expr.
    def enterValued_case_expr(self, ctx:TeradataSQLRequestModifiersParser.Valued_case_exprContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#valued_case_expr.
    def exitValued_case_expr(self, ctx:TeradataSQLRequestModifiersParser.Valued_case_exprContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#searched_case_expr.
    def enterSearched_case_expr(self, ctx:TeradataSQLRequestModifiersParser.Searched_case_exprContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#searched_case_expr.
    def exitSearched_case_expr(self, ctx:TeradataSQLRequestModifiersParser.Searched_case_exprContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#coalesce_expr.
    def enterCoalesce_expr(self, ctx:TeradataSQLRequestModifiersParser.Coalesce_exprContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#coalesce_expr.
    def exitCoalesce_expr(self, ctx:TeradataSQLRequestModifiersParser.Coalesce_exprContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#nullif_expr.
    def enterNullif_expr(self, ctx:TeradataSQLRequestModifiersParser.Nullif_exprContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#nullif_expr.
    def exitNullif_expr(self, ctx:TeradataSQLRequestModifiersParser.Nullif_exprContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#interval_expr_base.
    def enterInterval_expr_base(self, ctx:TeradataSQLRequestModifiersParser.Interval_expr_baseContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#interval_expr_base.
    def exitInterval_expr_base(self, ctx:TeradataSQLRequestModifiersParser.Interval_expr_baseContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#interval_expr_parenthesized.
    def enterInterval_expr_parenthesized(self, ctx:TeradataSQLRequestModifiersParser.Interval_expr_parenthesizedContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#interval_expr_parenthesized.
    def exitInterval_expr_parenthesized(self, ctx:TeradataSQLRequestModifiersParser.Interval_expr_parenthesizedContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#interval_expr_start_end_phrase.
    def enterInterval_expr_start_end_phrase(self, ctx:TeradataSQLRequestModifiersParser.Interval_expr_start_end_phraseContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#interval_expr_start_end_phrase.
    def exitInterval_expr_start_end_phrase(self, ctx:TeradataSQLRequestModifiersParser.Interval_expr_start_end_phraseContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#function_invocation.
    def enterFunction_invocation(self, ctx:TeradataSQLRequestModifiersParser.Function_invocationContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#function_invocation.
    def exitFunction_invocation(self, ctx:TeradataSQLRequestModifiersParser.Function_invocationContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#AggOneArg.
    def enterAggOneArg(self, ctx:TeradataSQLRequestModifiersParser.AggOneArgContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#AggOneArg.
    def exitAggOneArg(self, ctx:TeradataSQLRequestModifiersParser.AggOneArgContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#AggTwoArgs.
    def enterAggTwoArgs(self, ctx:TeradataSQLRequestModifiersParser.AggTwoArgsContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#AggTwoArgs.
    def exitAggTwoArgs(self, ctx:TeradataSQLRequestModifiersParser.AggTwoArgsContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#AggCount.
    def enterAggCount(self, ctx:TeradataSQLRequestModifiersParser.AggCountContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#AggCount.
    def exitAggCount(self, ctx:TeradataSQLRequestModifiersParser.AggCountContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#Grouping.
    def enterGrouping(self, ctx:TeradataSQLRequestModifiersParser.GroupingContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#Grouping.
    def exitGrouping(self, ctx:TeradataSQLRequestModifiersParser.GroupingContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#ListAgg.
    def enterListAgg(self, ctx:TeradataSQLRequestModifiersParser.ListAggContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#ListAgg.
    def exitListAgg(self, ctx:TeradataSQLRequestModifiersParser.ListAggContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#analytic_function.
    def enterAnalytic_function(self, ctx:TeradataSQLRequestModifiersParser.Analytic_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#analytic_function.
    def exitAnalytic_function(self, ctx:TeradataSQLRequestModifiersParser.Analytic_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#arithmetic_function.
    def enterArithmetic_function(self, ctx:TeradataSQLRequestModifiersParser.Arithmetic_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#arithmetic_function.
    def exitArithmetic_function(self, ctx:TeradataSQLRequestModifiersParser.Arithmetic_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#array_function.
    def enterArray_function(self, ctx:TeradataSQLRequestModifiersParser.Array_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#array_function.
    def exitArray_function(self, ctx:TeradataSQLRequestModifiersParser.Array_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#attribute_function.
    def enterAttribute_function(self, ctx:TeradataSQLRequestModifiersParser.Attribute_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#attribute_function.
    def exitAttribute_function(self, ctx:TeradataSQLRequestModifiersParser.Attribute_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#byte_function.
    def enterByte_function(self, ctx:TeradataSQLRequestModifiersParser.Byte_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#byte_function.
    def exitByte_function(self, ctx:TeradataSQLRequestModifiersParser.Byte_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#builtin_function.
    def enterBuiltin_function(self, ctx:TeradataSQLRequestModifiersParser.Builtin_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#builtin_function.
    def exitBuiltin_function(self, ctx:TeradataSQLRequestModifiersParser.Builtin_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#calendar_function.
    def enterCalendar_function(self, ctx:TeradataSQLRequestModifiersParser.Calendar_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#calendar_function.
    def exitCalendar_function(self, ctx:TeradataSQLRequestModifiersParser.Calendar_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#comparison_function.
    def enterComparison_function(self, ctx:TeradataSQLRequestModifiersParser.Comparison_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#comparison_function.
    def exitComparison_function(self, ctx:TeradataSQLRequestModifiersParser.Comparison_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#compression_function.
    def enterCompression_function(self, ctx:TeradataSQLRequestModifiersParser.Compression_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#compression_function.
    def exitCompression_function(self, ctx:TeradataSQLRequestModifiersParser.Compression_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#conversion_function.
    def enterConversion_function(self, ctx:TeradataSQLRequestModifiersParser.Conversion_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#conversion_function.
    def exitConversion_function(self, ctx:TeradataSQLRequestModifiersParser.Conversion_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#date_function.
    def enterDate_function(self, ctx:TeradataSQLRequestModifiersParser.Date_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#date_function.
    def exitDate_function(self, ctx:TeradataSQLRequestModifiersParser.Date_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#hash_function.
    def enterHash_function(self, ctx:TeradataSQLRequestModifiersParser.Hash_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#hash_function.
    def exitHash_function(self, ctx:TeradataSQLRequestModifiersParser.Hash_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#lob_function.
    def enterLob_function(self, ctx:TeradataSQLRequestModifiersParser.Lob_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#lob_function.
    def exitLob_function(self, ctx:TeradataSQLRequestModifiersParser.Lob_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#map_function.
    def enterMap_function(self, ctx:TeradataSQLRequestModifiersParser.Map_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#map_function.
    def exitMap_function(self, ctx:TeradataSQLRequestModifiersParser.Map_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#nvl_funtion.
    def enterNvl_funtion(self, ctx:TeradataSQLRequestModifiersParser.Nvl_funtionContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#nvl_funtion.
    def exitNvl_funtion(self, ctx:TeradataSQLRequestModifiersParser.Nvl_funtionContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#period_function.
    def enterPeriod_function(self, ctx:TeradataSQLRequestModifiersParser.Period_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#period_function.
    def exitPeriod_function(self, ctx:TeradataSQLRequestModifiersParser.Period_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#regexp_function.
    def enterRegexp_function(self, ctx:TeradataSQLRequestModifiersParser.Regexp_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#regexp_function.
    def exitRegexp_function(self, ctx:TeradataSQLRequestModifiersParser.Regexp_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#string_function.
    def enterString_function(self, ctx:TeradataSQLRequestModifiersParser.String_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#string_function.
    def exitString_function(self, ctx:TeradataSQLRequestModifiersParser.String_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#json_function.
    def enterJson_function(self, ctx:TeradataSQLRequestModifiersParser.Json_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#json_function.
    def exitJson_function(self, ctx:TeradataSQLRequestModifiersParser.Json_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#xml_function.
    def enterXml_function(self, ctx:TeradataSQLRequestModifiersParser.Xml_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#xml_function.
    def exitXml_function(self, ctx:TeradataSQLRequestModifiersParser.Xml_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#other_function.
    def enterOther_function(self, ctx:TeradataSQLRequestModifiersParser.Other_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#other_function.
    def exitOther_function(self, ctx:TeradataSQLRequestModifiersParser.Other_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#partitioning_expr.
    def enterPartitioning_expr(self, ctx:TeradataSQLRequestModifiersParser.Partitioning_exprContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#partitioning_expr.
    def exitPartitioning_expr(self, ctx:TeradataSQLRequestModifiersParser.Partitioning_exprContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#td_sysfnlib.
    def enterTd_sysfnlib(self, ctx:TeradataSQLRequestModifiersParser.Td_sysfnlibContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#td_sysfnlib.
    def exitTd_sysfnlib(self, ctx:TeradataSQLRequestModifiersParser.Td_sysfnlibContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#td_sysxml.
    def enterTd_sysxml(self, ctx:TeradataSQLRequestModifiersParser.Td_sysxmlContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#td_sysxml.
    def exitTd_sysxml(self, ctx:TeradataSQLRequestModifiersParser.Td_sysxmlContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#syslib.
    def enterSyslib(self, ctx:TeradataSQLRequestModifiersParser.SyslibContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#syslib.
    def exitSyslib(self, ctx:TeradataSQLRequestModifiersParser.SyslibContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#td_server_db.
    def enterTd_server_db(self, ctx:TeradataSQLRequestModifiersParser.Td_server_dbContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#td_server_db.
    def exitTd_server_db(self, ctx:TeradataSQLRequestModifiersParser.Td_server_dbContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#translation_mapping.
    def enterTranslation_mapping(self, ctx:TeradataSQLRequestModifiersParser.Translation_mappingContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#translation_mapping.
    def exitTranslation_mapping(self, ctx:TeradataSQLRequestModifiersParser.Translation_mappingContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#attribute_modification.
    def enterAttribute_modification(self, ctx:TeradataSQLRequestModifiersParser.Attribute_modificationContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#attribute_modification.
    def exitAttribute_modification(self, ctx:TeradataSQLRequestModifiersParser.Attribute_modificationContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#returns_clause.
    def enterReturns_clause(self, ctx:TeradataSQLRequestModifiersParser.Returns_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#returns_clause.
    def exitReturns_clause(self, ctx:TeradataSQLRequestModifiersParser.Returns_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#attribute_modification_option.
    def enterAttribute_modification_option(self, ctx:TeradataSQLRequestModifiersParser.Attribute_modification_optionContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#attribute_modification_option.
    def exitAttribute_modification_option(self, ctx:TeradataSQLRequestModifiersParser.Attribute_modification_optionContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#teradata_type_conversion.
    def enterTeradata_type_conversion(self, ctx:TeradataSQLRequestModifiersParser.Teradata_type_conversionContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#teradata_type_conversion.
    def exitTeradata_type_conversion(self, ctx:TeradataSQLRequestModifiersParser.Teradata_type_conversionContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#teradata_type_conversion_data_attribute.
    def enterTeradata_type_conversion_data_attribute(self, ctx:TeradataSQLRequestModifiersParser.Teradata_type_conversion_data_attributeContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#teradata_type_conversion_data_attribute.
    def exitTeradata_type_conversion_data_attribute(self, ctx:TeradataSQLRequestModifiersParser.Teradata_type_conversion_data_attributeContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#case_spec.
    def enterCase_spec(self, ctx:TeradataSQLRequestModifiersParser.Case_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#case_spec.
    def exitCase_spec(self, ctx:TeradataSQLRequestModifiersParser.Case_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#range_expr.
    def enterRange_expr(self, ctx:TeradataSQLRequestModifiersParser.Range_exprContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#range_expr.
    def exitRange_expr(self, ctx:TeradataSQLRequestModifiersParser.Range_exprContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#range_list.
    def enterRange_list(self, ctx:TeradataSQLRequestModifiersParser.Range_listContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#range_list.
    def exitRange_list(self, ctx:TeradataSQLRequestModifiersParser.Range_listContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#range_expr_1.
    def enterRange_expr_1(self, ctx:TeradataSQLRequestModifiersParser.Range_expr_1Context):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#range_expr_1.
    def exitRange_expr_1(self, ctx:TeradataSQLRequestModifiersParser.Range_expr_1Context):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#range_expr_2.
    def enterRange_expr_2(self, ctx:TeradataSQLRequestModifiersParser.Range_expr_2Context):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#range_expr_2.
    def exitRange_expr_2(self, ctx:TeradataSQLRequestModifiersParser.Range_expr_2Context):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#range_expr_3.
    def enterRange_expr_3(self, ctx:TeradataSQLRequestModifiersParser.Range_expr_3Context):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#range_expr_3.
    def exitRange_expr_3(self, ctx:TeradataSQLRequestModifiersParser.Range_expr_3Context):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#range_spec.
    def enterRange_spec(self, ctx:TeradataSQLRequestModifiersParser.Range_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#range_spec.
    def exitRange_spec(self, ctx:TeradataSQLRequestModifiersParser.Range_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#hash_bucket_number_expr.
    def enterHash_bucket_number_expr(self, ctx:TeradataSQLRequestModifiersParser.Hash_bucket_number_exprContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#hash_bucket_number_expr.
    def exitHash_bucket_number_expr(self, ctx:TeradataSQLRequestModifiersParser.Hash_bucket_number_exprContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#window_spec.
    def enterWindow_spec(self, ctx:TeradataSQLRequestModifiersParser.Window_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#window_spec.
    def exitWindow_spec(self, ctx:TeradataSQLRequestModifiersParser.Window_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#window_spec_without_rows.
    def enterWindow_spec_without_rows(self, ctx:TeradataSQLRequestModifiersParser.Window_spec_without_rowsContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#window_spec_without_rows.
    def exitWindow_spec_without_rows(self, ctx:TeradataSQLRequestModifiersParser.Window_spec_without_rowsContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#window_spec_with_ties.
    def enterWindow_spec_with_ties(self, ctx:TeradataSQLRequestModifiersParser.Window_spec_with_tiesContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#window_spec_with_ties.
    def exitWindow_spec_with_ties(self, ctx:TeradataSQLRequestModifiersParser.Window_spec_with_tiesContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#window_partition_by.
    def enterWindow_partition_by(self, ctx:TeradataSQLRequestModifiersParser.Window_partition_byContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#window_partition_by.
    def exitWindow_partition_by(self, ctx:TeradataSQLRequestModifiersParser.Window_partition_byContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#window_order_by.
    def enterWindow_order_by(self, ctx:TeradataSQLRequestModifiersParser.Window_order_byContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#window_order_by.
    def exitWindow_order_by(self, ctx:TeradataSQLRequestModifiersParser.Window_order_byContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#window_rows.
    def enterWindow_rows(self, ctx:TeradataSQLRequestModifiersParser.Window_rowsContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#window_rows.
    def exitWindow_rows(self, ctx:TeradataSQLRequestModifiersParser.Window_rowsContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#json_param_spec.
    def enterJson_param_spec(self, ctx:TeradataSQLRequestModifiersParser.Json_param_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#json_param_spec.
    def exitJson_param_spec(self, ctx:TeradataSQLRequestModifiersParser.Json_param_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#xml_query_argument.
    def enterXml_query_argument(self, ctx:TeradataSQLRequestModifiersParser.Xml_query_argumentContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#xml_query_argument.
    def exitXml_query_argument(self, ctx:TeradataSQLRequestModifiersParser.Xml_query_argumentContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#xml_query_variable_spec.
    def enterXml_query_variable_spec(self, ctx:TeradataSQLRequestModifiersParser.Xml_query_variable_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#xml_query_variable_spec.
    def exitXml_query_variable_spec(self, ctx:TeradataSQLRequestModifiersParser.Xml_query_variable_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#xml_attribute_declaration.
    def enterXml_attribute_declaration(self, ctx:TeradataSQLRequestModifiersParser.Xml_attribute_declarationContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#xml_attribute_declaration.
    def exitXml_attribute_declaration(self, ctx:TeradataSQLRequestModifiersParser.Xml_attribute_declarationContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#xml_attribute_spec.
    def enterXml_attribute_spec(self, ctx:TeradataSQLRequestModifiersParser.Xml_attribute_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#xml_attribute_spec.
    def exitXml_attribute_spec(self, ctx:TeradataSQLRequestModifiersParser.Xml_attribute_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#xml_forest_element_spec.
    def enterXml_forest_element_spec(self, ctx:TeradataSQLRequestModifiersParser.Xml_forest_element_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#xml_forest_element_spec.
    def exitXml_forest_element_spec(self, ctx:TeradataSQLRequestModifiersParser.Xml_forest_element_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#xml_value_declaration.
    def enterXml_value_declaration(self, ctx:TeradataSQLRequestModifiersParser.Xml_value_declarationContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#xml_value_declaration.
    def exitXml_value_declaration(self, ctx:TeradataSQLRequestModifiersParser.Xml_value_declarationContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#xml_namespace_declaration.
    def enterXml_namespace_declaration(self, ctx:TeradataSQLRequestModifiersParser.Xml_namespace_declarationContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#xml_namespace_declaration.
    def exitXml_namespace_declaration(self, ctx:TeradataSQLRequestModifiersParser.Xml_namespace_declarationContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#xml_namespace_spec.
    def enterXml_namespace_spec(self, ctx:TeradataSQLRequestModifiersParser.Xml_namespace_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#xml_namespace_spec.
    def exitXml_namespace_spec(self, ctx:TeradataSQLRequestModifiersParser.Xml_namespace_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#xml_columns_spec.
    def enterXml_columns_spec(self, ctx:TeradataSQLRequestModifiersParser.Xml_columns_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#xml_columns_spec.
    def exitXml_columns_spec(self, ctx:TeradataSQLRequestModifiersParser.Xml_columns_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#xml_regular_column_definition.
    def enterXml_regular_column_definition(self, ctx:TeradataSQLRequestModifiersParser.Xml_regular_column_definitionContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#xml_regular_column_definition.
    def exitXml_regular_column_definition(self, ctx:TeradataSQLRequestModifiersParser.Xml_regular_column_definitionContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#xml_encoding.
    def enterXml_encoding(self, ctx:TeradataSQLRequestModifiersParser.Xml_encodingContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#xml_encoding.
    def exitXml_encoding(self, ctx:TeradataSQLRequestModifiersParser.Xml_encodingContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#xml_query_on_empty.
    def enterXml_query_on_empty(self, ctx:TeradataSQLRequestModifiersParser.Xml_query_on_emptyContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#xml_query_on_empty.
    def exitXml_query_on_empty(self, ctx:TeradataSQLRequestModifiersParser.Xml_query_on_emptyContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#xml_returning_spec.
    def enterXml_returning_spec(self, ctx:TeradataSQLRequestModifiersParser.Xml_returning_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#xml_returning_spec.
    def exitXml_returning_spec(self, ctx:TeradataSQLRequestModifiersParser.Xml_returning_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#xml_content_option_spec.
    def enterXml_content_option_spec(self, ctx:TeradataSQLRequestModifiersParser.Xml_content_option_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#xml_content_option_spec.
    def exitXml_content_option_spec(self, ctx:TeradataSQLRequestModifiersParser.Xml_content_option_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#ignore_respect_nulls.
    def enterIgnore_respect_nulls(self, ctx:TeradataSQLRequestModifiersParser.Ignore_respect_nullsContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#ignore_respect_nulls.
    def exitIgnore_respect_nulls(self, ctx:TeradataSQLRequestModifiersParser.Ignore_respect_nullsContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#number_of_rows.
    def enterNumber_of_rows(self, ctx:TeradataSQLRequestModifiersParser.Number_of_rowsContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#number_of_rows.
    def exitNumber_of_rows(self, ctx:TeradataSQLRequestModifiersParser.Number_of_rowsContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#with_ties.
    def enterWith_ties(self, ctx:TeradataSQLRequestModifiersParser.With_tiesContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#with_ties.
    def exitWith_ties(self, ctx:TeradataSQLRequestModifiersParser.With_tiesContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#pivot.
    def enterPivot(self, ctx:TeradataSQLRequestModifiersParser.PivotContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#pivot.
    def exitPivot(self, ctx:TeradataSQLRequestModifiersParser.PivotContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#pivot_spec.
    def enterPivot_spec(self, ctx:TeradataSQLRequestModifiersParser.Pivot_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#pivot_spec.
    def exitPivot_spec(self, ctx:TeradataSQLRequestModifiersParser.Pivot_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#pivot_with_phrase.
    def enterPivot_with_phrase(self, ctx:TeradataSQLRequestModifiersParser.Pivot_with_phraseContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#pivot_with_phrase.
    def exitPivot_with_phrase(self, ctx:TeradataSQLRequestModifiersParser.Pivot_with_phraseContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#pivot_agg_func_spec.
    def enterPivot_agg_func_spec(self, ctx:TeradataSQLRequestModifiersParser.Pivot_agg_func_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#pivot_agg_func_spec.
    def exitPivot_agg_func_spec(self, ctx:TeradataSQLRequestModifiersParser.Pivot_agg_func_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#pivot_for_phrase.
    def enterPivot_for_phrase(self, ctx:TeradataSQLRequestModifiersParser.Pivot_for_phraseContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#pivot_for_phrase.
    def exitPivot_for_phrase(self, ctx:TeradataSQLRequestModifiersParser.Pivot_for_phraseContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#pivot_with_spec.
    def enterPivot_with_spec(self, ctx:TeradataSQLRequestModifiersParser.Pivot_with_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#pivot_with_spec.
    def exitPivot_with_spec(self, ctx:TeradataSQLRequestModifiersParser.Pivot_with_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#pivot_expr_spec_scalar.
    def enterPivot_expr_spec_scalar(self, ctx:TeradataSQLRequestModifiersParser.Pivot_expr_spec_scalarContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#pivot_expr_spec_scalar.
    def exitPivot_expr_spec_scalar(self, ctx:TeradataSQLRequestModifiersParser.Pivot_expr_spec_scalarContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#pivot_expr_spec_list.
    def enterPivot_expr_spec_list(self, ctx:TeradataSQLRequestModifiersParser.Pivot_expr_spec_listContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#pivot_expr_spec_list.
    def exitPivot_expr_spec_list(self, ctx:TeradataSQLRequestModifiersParser.Pivot_expr_spec_listContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#unpivot.
    def enterUnpivot(self, ctx:TeradataSQLRequestModifiersParser.UnpivotContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#unpivot.
    def exitUnpivot(self, ctx:TeradataSQLRequestModifiersParser.UnpivotContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#unpivot_spec.
    def enterUnpivot_spec(self, ctx:TeradataSQLRequestModifiersParser.Unpivot_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#unpivot_spec.
    def exitUnpivot_spec(self, ctx:TeradataSQLRequestModifiersParser.Unpivot_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#unpivot_column_name_spec_single.
    def enterUnpivot_column_name_spec_single(self, ctx:TeradataSQLRequestModifiersParser.Unpivot_column_name_spec_singleContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#unpivot_column_name_spec_single.
    def exitUnpivot_column_name_spec_single(self, ctx:TeradataSQLRequestModifiersParser.Unpivot_column_name_spec_singleContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#unpivot_column_name_spec_list.
    def enterUnpivot_column_name_spec_list(self, ctx:TeradataSQLRequestModifiersParser.Unpivot_column_name_spec_listContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#unpivot_column_name_spec_list.
    def exitUnpivot_column_name_spec_list(self, ctx:TeradataSQLRequestModifiersParser.Unpivot_column_name_spec_listContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#at_timezone.
    def enterAt_timezone(self, ctx:TeradataSQLRequestModifiersParser.At_timezoneContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#at_timezone.
    def exitAt_timezone(self, ctx:TeradataSQLRequestModifiersParser.At_timezoneContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#elements_list.
    def enterElements_list(self, ctx:TeradataSQLRequestModifiersParser.Elements_listContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#elements_list.
    def exitElements_list(self, ctx:TeradataSQLRequestModifiersParser.Elements_listContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#scalar_expr_list.
    def enterScalar_expr_list(self, ctx:TeradataSQLRequestModifiersParser.Scalar_expr_listContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#scalar_expr_list.
    def exitScalar_expr_list(self, ctx:TeradataSQLRequestModifiersParser.Scalar_expr_listContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#scalar_expr_list_comma_separated.
    def enterScalar_expr_list_comma_separated(self, ctx:TeradataSQLRequestModifiersParser.Scalar_expr_list_comma_separatedContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#scalar_expr_list_comma_separated.
    def exitScalar_expr_list_comma_separated(self, ctx:TeradataSQLRequestModifiersParser.Scalar_expr_list_comma_separatedContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#column_list.
    def enterColumn_list(self, ctx:TeradataSQLRequestModifiersParser.Column_listContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#column_list.
    def exitColumn_list(self, ctx:TeradataSQLRequestModifiersParser.Column_listContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#subquery.
    def enterSubquery(self, ctx:TeradataSQLRequestModifiersParser.SubqueryContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#subquery.
    def exitSubquery(self, ctx:TeradataSQLRequestModifiersParser.SubqueryContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#column_spec.
    def enterColumn_spec(self, ctx:TeradataSQLRequestModifiersParser.Column_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#column_spec.
    def exitColumn_spec(self, ctx:TeradataSQLRequestModifiersParser.Column_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#variable_reference.
    def enterVariable_reference(self, ctx:TeradataSQLRequestModifiersParser.Variable_referenceContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#variable_reference.
    def exitVariable_reference(self, ctx:TeradataSQLRequestModifiersParser.Variable_referenceContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#cursor_variable_reference.
    def enterCursor_variable_reference(self, ctx:TeradataSQLRequestModifiersParser.Cursor_variable_referenceContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#cursor_variable_reference.
    def exitCursor_variable_reference(self, ctx:TeradataSQLRequestModifiersParser.Cursor_variable_referenceContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#macro_parameter_reference.
    def enterMacro_parameter_reference(self, ctx:TeradataSQLRequestModifiersParser.Macro_parameter_referenceContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#macro_parameter_reference.
    def exitMacro_parameter_reference(self, ctx:TeradataSQLRequestModifiersParser.Macro_parameter_referenceContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#array_scope_reference.
    def enterArray_scope_reference(self, ctx:TeradataSQLRequestModifiersParser.Array_scope_referenceContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#array_scope_reference.
    def exitArray_scope_reference(self, ctx:TeradataSQLRequestModifiersParser.Array_scope_referenceContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#comparison_operator.
    def enterComparison_operator(self, ctx:TeradataSQLRequestModifiersParser.Comparison_operatorContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#comparison_operator.
    def exitComparison_operator(self, ctx:TeradataSQLRequestModifiersParser.Comparison_operatorContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#quantifier.
    def enterQuantifier(self, ctx:TeradataSQLRequestModifiersParser.QuantifierContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#quantifier.
    def exitQuantifier(self, ctx:TeradataSQLRequestModifiersParser.QuantifierContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#literal.
    def enterLiteral(self, ctx:TeradataSQLRequestModifiersParser.LiteralContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#literal.
    def exitLiteral(self, ctx:TeradataSQLRequestModifiersParser.LiteralContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#hex_byte_literal.
    def enterHex_byte_literal(self, ctx:TeradataSQLRequestModifiersParser.Hex_byte_literalContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#hex_byte_literal.
    def exitHex_byte_literal(self, ctx:TeradataSQLRequestModifiersParser.Hex_byte_literalContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#char_string_literal.
    def enterChar_string_literal(self, ctx:TeradataSQLRequestModifiersParser.Char_string_literalContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#char_string_literal.
    def exitChar_string_literal(self, ctx:TeradataSQLRequestModifiersParser.Char_string_literalContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#unicode_char_string_literal.
    def enterUnicode_char_string_literal(self, ctx:TeradataSQLRequestModifiersParser.Unicode_char_string_literalContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#unicode_char_string_literal.
    def exitUnicode_char_string_literal(self, ctx:TeradataSQLRequestModifiersParser.Unicode_char_string_literalContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#hex_char_string_literal.
    def enterHex_char_string_literal(self, ctx:TeradataSQLRequestModifiersParser.Hex_char_string_literalContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#hex_char_string_literal.
    def exitHex_char_string_literal(self, ctx:TeradataSQLRequestModifiersParser.Hex_char_string_literalContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#integer_literal.
    def enterInteger_literal(self, ctx:TeradataSQLRequestModifiersParser.Integer_literalContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#integer_literal.
    def exitInteger_literal(self, ctx:TeradataSQLRequestModifiersParser.Integer_literalContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#hex_integer_literal.
    def enterHex_integer_literal(self, ctx:TeradataSQLRequestModifiersParser.Hex_integer_literalContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#hex_integer_literal.
    def exitHex_integer_literal(self, ctx:TeradataSQLRequestModifiersParser.Hex_integer_literalContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#float_literal.
    def enterFloat_literal(self, ctx:TeradataSQLRequestModifiersParser.Float_literalContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#float_literal.
    def exitFloat_literal(self, ctx:TeradataSQLRequestModifiersParser.Float_literalContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#character_set_prefix.
    def enterCharacter_set_prefix(self, ctx:TeradataSQLRequestModifiersParser.Character_set_prefixContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#character_set_prefix.
    def exitCharacter_set_prefix(self, ctx:TeradataSQLRequestModifiersParser.Character_set_prefixContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#date_literal.
    def enterDate_literal(self, ctx:TeradataSQLRequestModifiersParser.Date_literalContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#date_literal.
    def exitDate_literal(self, ctx:TeradataSQLRequestModifiersParser.Date_literalContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#time_literal.
    def enterTime_literal(self, ctx:TeradataSQLRequestModifiersParser.Time_literalContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#time_literal.
    def exitTime_literal(self, ctx:TeradataSQLRequestModifiersParser.Time_literalContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#timestamp_literal.
    def enterTimestamp_literal(self, ctx:TeradataSQLRequestModifiersParser.Timestamp_literalContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#timestamp_literal.
    def exitTimestamp_literal(self, ctx:TeradataSQLRequestModifiersParser.Timestamp_literalContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#interval_literal.
    def enterInterval_literal(self, ctx:TeradataSQLRequestModifiersParser.Interval_literalContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#interval_literal.
    def exitInterval_literal(self, ctx:TeradataSQLRequestModifiersParser.Interval_literalContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#interval_qualifier.
    def enterInterval_qualifier(self, ctx:TeradataSQLRequestModifiersParser.Interval_qualifierContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#interval_qualifier.
    def exitInterval_qualifier(self, ctx:TeradataSQLRequestModifiersParser.Interval_qualifierContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#period_literal.
    def enterPeriod_literal(self, ctx:TeradataSQLRequestModifiersParser.Period_literalContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#period_literal.
    def exitPeriod_literal(self, ctx:TeradataSQLRequestModifiersParser.Period_literalContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#column_name.
    def enterColumn_name(self, ctx:TeradataSQLRequestModifiersParser.Column_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#column_name.
    def exitColumn_name(self, ctx:TeradataSQLRequestModifiersParser.Column_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#unqualified_column_name.
    def enterUnqualified_column_name(self, ctx:TeradataSQLRequestModifiersParser.Unqualified_column_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#unqualified_column_name.
    def exitUnqualified_column_name(self, ctx:TeradataSQLRequestModifiersParser.Unqualified_column_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#unqualified_name.
    def enterUnqualified_name(self, ctx:TeradataSQLRequestModifiersParser.Unqualified_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#unqualified_name.
    def exitUnqualified_name(self, ctx:TeradataSQLRequestModifiersParser.Unqualified_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#object_name.
    def enterObject_name(self, ctx:TeradataSQLRequestModifiersParser.Object_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#object_name.
    def exitObject_name(self, ctx:TeradataSQLRequestModifiersParser.Object_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#table_name.
    def enterTable_name(self, ctx:TeradataSQLRequestModifiersParser.Table_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#table_name.
    def exitTable_name(self, ctx:TeradataSQLRequestModifiersParser.Table_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#procedure_name.
    def enterProcedure_name(self, ctx:TeradataSQLRequestModifiersParser.Procedure_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#procedure_name.
    def exitProcedure_name(self, ctx:TeradataSQLRequestModifiersParser.Procedure_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#function_name.
    def enterFunction_name(self, ctx:TeradataSQLRequestModifiersParser.Function_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#function_name.
    def exitFunction_name(self, ctx:TeradataSQLRequestModifiersParser.Function_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#macro_name.
    def enterMacro_name(self, ctx:TeradataSQLRequestModifiersParser.Macro_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#macro_name.
    def exitMacro_name(self, ctx:TeradataSQLRequestModifiersParser.Macro_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#database_name.
    def enterDatabase_name(self, ctx:TeradataSQLRequestModifiersParser.Database_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#database_name.
    def exitDatabase_name(self, ctx:TeradataSQLRequestModifiersParser.Database_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#user_name.
    def enterUser_name(self, ctx:TeradataSQLRequestModifiersParser.User_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#user_name.
    def exitUser_name(self, ctx:TeradataSQLRequestModifiersParser.User_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#role_name.
    def enterRole_name(self, ctx:TeradataSQLRequestModifiersParser.Role_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#role_name.
    def exitRole_name(self, ctx:TeradataSQLRequestModifiersParser.Role_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#profile_name.
    def enterProfile_name(self, ctx:TeradataSQLRequestModifiersParser.Profile_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#profile_name.
    def exitProfile_name(self, ctx:TeradataSQLRequestModifiersParser.Profile_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#alias_name.
    def enterAlias_name(self, ctx:TeradataSQLRequestModifiersParser.Alias_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#alias_name.
    def exitAlias_name(self, ctx:TeradataSQLRequestModifiersParser.Alias_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#variable_name.
    def enterVariable_name(self, ctx:TeradataSQLRequestModifiersParser.Variable_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#variable_name.
    def exitVariable_name(self, ctx:TeradataSQLRequestModifiersParser.Variable_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#parameter_name.
    def enterParameter_name(self, ctx:TeradataSQLRequestModifiersParser.Parameter_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#parameter_name.
    def exitParameter_name(self, ctx:TeradataSQLRequestModifiersParser.Parameter_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#label_name.
    def enterLabel_name(self, ctx:TeradataSQLRequestModifiersParser.Label_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#label_name.
    def exitLabel_name(self, ctx:TeradataSQLRequestModifiersParser.Label_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#condition_name.
    def enterCondition_name(self, ctx:TeradataSQLRequestModifiersParser.Condition_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#condition_name.
    def exitCondition_name(self, ctx:TeradataSQLRequestModifiersParser.Condition_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#cursor_name.
    def enterCursor_name(self, ctx:TeradataSQLRequestModifiersParser.Cursor_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#cursor_name.
    def exitCursor_name(self, ctx:TeradataSQLRequestModifiersParser.Cursor_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#statement_name.
    def enterStatement_name(self, ctx:TeradataSQLRequestModifiersParser.Statement_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#statement_name.
    def exitStatement_name(self, ctx:TeradataSQLRequestModifiersParser.Statement_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#statistics_name.
    def enterStatistics_name(self, ctx:TeradataSQLRequestModifiersParser.Statistics_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#statistics_name.
    def exitStatistics_name(self, ctx:TeradataSQLRequestModifiersParser.Statistics_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#udt_name.
    def enterUdt_name(self, ctx:TeradataSQLRequestModifiersParser.Udt_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#udt_name.
    def exitUdt_name(self, ctx:TeradataSQLRequestModifiersParser.Udt_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#attribute_name.
    def enterAttribute_name(self, ctx:TeradataSQLRequestModifiersParser.Attribute_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#attribute_name.
    def exitAttribute_name(self, ctx:TeradataSQLRequestModifiersParser.Attribute_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#method_name.
    def enterMethod_name(self, ctx:TeradataSQLRequestModifiersParser.Method_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#method_name.
    def exitMethod_name(self, ctx:TeradataSQLRequestModifiersParser.Method_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#anchor_name.
    def enterAnchor_name(self, ctx:TeradataSQLRequestModifiersParser.Anchor_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#anchor_name.
    def exitAnchor_name(self, ctx:TeradataSQLRequestModifiersParser.Anchor_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#nonreserved_word.
    def enterNonreserved_word(self, ctx:TeradataSQLRequestModifiersParser.Nonreserved_wordContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#nonreserved_word.
    def exitNonreserved_word(self, ctx:TeradataSQLRequestModifiersParser.Nonreserved_wordContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#data_type.
    def enterData_type(self, ctx:TeradataSQLRequestModifiersParser.Data_typeContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#data_type.
    def exitData_type(self, ctx:TeradataSQLRequestModifiersParser.Data_typeContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#variable_data_type.
    def enterVariable_data_type(self, ctx:TeradataSQLRequestModifiersParser.Variable_data_typeContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#variable_data_type.
    def exitVariable_data_type(self, ctx:TeradataSQLRequestModifiersParser.Variable_data_typeContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#external_function_data_type.
    def enterExternal_function_data_type(self, ctx:TeradataSQLRequestModifiersParser.External_function_data_typeContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#external_function_data_type.
    def exitExternal_function_data_type(self, ctx:TeradataSQLRequestModifiersParser.External_function_data_typeContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#numeric_data_type.
    def enterNumeric_data_type(self, ctx:TeradataSQLRequestModifiersParser.Numeric_data_typeContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#numeric_data_type.
    def exitNumeric_data_type(self, ctx:TeradataSQLRequestModifiersParser.Numeric_data_typeContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#char_data_type.
    def enterChar_data_type(self, ctx:TeradataSQLRequestModifiersParser.Char_data_typeContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#char_data_type.
    def exitChar_data_type(self, ctx:TeradataSQLRequestModifiersParser.Char_data_typeContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#precisionless_char_data_type.
    def enterPrecisionless_char_data_type(self, ctx:TeradataSQLRequestModifiersParser.Precisionless_char_data_typeContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#precisionless_char_data_type.
    def exitPrecisionless_char_data_type(self, ctx:TeradataSQLRequestModifiersParser.Precisionless_char_data_typeContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#lob_as_locator_data_type.
    def enterLob_as_locator_data_type(self, ctx:TeradataSQLRequestModifiersParser.Lob_as_locator_data_typeContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#lob_as_locator_data_type.
    def exitLob_as_locator_data_type(self, ctx:TeradataSQLRequestModifiersParser.Lob_as_locator_data_typeContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#binary_data_type.
    def enterBinary_data_type(self, ctx:TeradataSQLRequestModifiersParser.Binary_data_typeContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#binary_data_type.
    def exitBinary_data_type(self, ctx:TeradataSQLRequestModifiersParser.Binary_data_typeContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#datetime_type.
    def enterDatetime_type(self, ctx:TeradataSQLRequestModifiersParser.Datetime_typeContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#datetime_type.
    def exitDatetime_type(self, ctx:TeradataSQLRequestModifiersParser.Datetime_typeContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#period_type.
    def enterPeriod_type(self, ctx:TeradataSQLRequestModifiersParser.Period_typeContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#period_type.
    def exitPeriod_type(self, ctx:TeradataSQLRequestModifiersParser.Period_typeContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#udt_type.
    def enterUdt_type(self, ctx:TeradataSQLRequestModifiersParser.Udt_typeContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#udt_type.
    def exitUdt_type(self, ctx:TeradataSQLRequestModifiersParser.Udt_typeContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#data_type_attribute.
    def enterData_type_attribute(self, ctx:TeradataSQLRequestModifiersParser.Data_type_attributeContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#data_type_attribute.
    def exitData_type_attribute(self, ctx:TeradataSQLRequestModifiersParser.Data_type_attributeContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#default_value_control_phrase.
    def enterDefault_value_control_phrase(self, ctx:TeradataSQLRequestModifiersParser.Default_value_control_phraseContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#default_value_control_phrase.
    def exitDefault_value_control_phrase(self, ctx:TeradataSQLRequestModifiersParser.Default_value_control_phraseContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#default_value.
    def enterDefault_value(self, ctx:TeradataSQLRequestModifiersParser.Default_valueContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#default_value.
    def exitDefault_value(self, ctx:TeradataSQLRequestModifiersParser.Default_valueContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#column_naming_phrase.
    def enterColumn_naming_phrase(self, ctx:TeradataSQLRequestModifiersParser.Column_naming_phraseContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#column_naming_phrase.
    def exitColumn_naming_phrase(self, ctx:TeradataSQLRequestModifiersParser.Column_naming_phraseContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#sysudtlib.
    def enterSysudtlib(self, ctx:TeradataSQLRequestModifiersParser.SysudtlibContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#sysudtlib.
    def exitSysudtlib(self, ctx:TeradataSQLRequestModifiersParser.SysudtlibContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#interval_period_spec.
    def enterInterval_period_spec(self, ctx:TeradataSQLRequestModifiersParser.Interval_period_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#interval_period_spec.
    def exitInterval_period_spec(self, ctx:TeradataSQLRequestModifiersParser.Interval_period_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#type_precision.
    def enterType_precision(self, ctx:TeradataSQLRequestModifiersParser.Type_precisionContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#type_precision.
    def exitType_precision(self, ctx:TeradataSQLRequestModifiersParser.Type_precisionContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#max_length_k_m_g.
    def enterMax_length_k_m_g(self, ctx:TeradataSQLRequestModifiersParser.Max_length_k_m_gContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#max_length_k_m_g.
    def exitMax_length_k_m_g(self, ctx:TeradataSQLRequestModifiersParser.Max_length_k_m_gContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#max_length_k_m.
    def enterMax_length_k_m(self, ctx:TeradataSQLRequestModifiersParser.Max_length_k_mContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#max_length_k_m.
    def exitMax_length_k_m(self, ctx:TeradataSQLRequestModifiersParser.Max_length_k_mContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#character_set_phrase.
    def enterCharacter_set_phrase(self, ctx:TeradataSQLRequestModifiersParser.Character_set_phraseContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#character_set_phrase.
    def exitCharacter_set_phrase(self, ctx:TeradataSQLRequestModifiersParser.Character_set_phraseContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#uppercase_phrase.
    def enterUppercase_phrase(self, ctx:TeradataSQLRequestModifiersParser.Uppercase_phraseContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#uppercase_phrase.
    def exitUppercase_phrase(self, ctx:TeradataSQLRequestModifiersParser.Uppercase_phraseContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#casespecific_phrase.
    def enterCasespecific_phrase(self, ctx:TeradataSQLRequestModifiersParser.Casespecific_phraseContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#casespecific_phrase.
    def exitCasespecific_phrase(self, ctx:TeradataSQLRequestModifiersParser.Casespecific_phraseContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#format_phrase.
    def enterFormat_phrase(self, ctx:TeradataSQLRequestModifiersParser.Format_phraseContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#format_phrase.
    def exitFormat_phrase(self, ctx:TeradataSQLRequestModifiersParser.Format_phraseContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#title_phrase.
    def enterTitle_phrase(self, ctx:TeradataSQLRequestModifiersParser.Title_phraseContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#title_phrase.
    def exitTitle_phrase(self, ctx:TeradataSQLRequestModifiersParser.Title_phraseContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#named_phrase.
    def enterNamed_phrase(self, ctx:TeradataSQLRequestModifiersParser.Named_phraseContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#named_phrase.
    def exitNamed_phrase(self, ctx:TeradataSQLRequestModifiersParser.Named_phraseContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#latin_unicode_character_set_phrase.
    def enterLatin_unicode_character_set_phrase(self, ctx:TeradataSQLRequestModifiersParser.Latin_unicode_character_set_phraseContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#latin_unicode_character_set_phrase.
    def exitLatin_unicode_character_set_phrase(self, ctx:TeradataSQLRequestModifiersParser.Latin_unicode_character_set_phraseContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#inline_length.
    def enterInline_length(self, ctx:TeradataSQLRequestModifiersParser.Inline_lengthContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#inline_length.
    def exitInline_length(self, ctx:TeradataSQLRequestModifiersParser.Inline_lengthContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#json_storage_format.
    def enterJson_storage_format(self, ctx:TeradataSQLRequestModifiersParser.Json_storage_formatContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#json_storage_format.
    def exitJson_storage_format(self, ctx:TeradataSQLRequestModifiersParser.Json_storage_formatContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#dataset_storage_format_clause.
    def enterDataset_storage_format_clause(self, ctx:TeradataSQLRequestModifiersParser.Dataset_storage_format_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#dataset_storage_format_clause.
    def exitDataset_storage_format_clause(self, ctx:TeradataSQLRequestModifiersParser.Dataset_storage_format_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#dataset_storage_format.
    def enterDataset_storage_format(self, ctx:TeradataSQLRequestModifiersParser.Dataset_storage_formatContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#dataset_storage_format.
    def exitDataset_storage_format(self, ctx:TeradataSQLRequestModifiersParser.Dataset_storage_formatContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#with_schema.
    def enterWith_schema(self, ctx:TeradataSQLRequestModifiersParser.With_schemaContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#with_schema.
    def exitWith_schema(self, ctx:TeradataSQLRequestModifiersParser.With_schemaContext):
        pass


    # Enter a parse tree produced by TeradataSQLRequestModifiersParser#with_time_zone.
    def enterWith_time_zone(self, ctx:TeradataSQLRequestModifiersParser.With_time_zoneContext):
        pass

    # Exit a parse tree produced by TeradataSQLRequestModifiersParser#with_time_zone.
    def exitWith_time_zone(self, ctx:TeradataSQLRequestModifiersParser.With_time_zoneContext):
        pass



del TeradataSQLRequestModifiersParser