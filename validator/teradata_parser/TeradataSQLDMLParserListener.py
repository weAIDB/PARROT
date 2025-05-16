# Generated from sql/teradata/TeradataSQLDMLParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .TeradataSQLDMLParser import TeradataSQLDMLParser
else:
    from TeradataSQLDMLParser import TeradataSQLDMLParser

# This class defines a complete listener for a parse tree produced by TeradataSQLDMLParser.
class TeradataSQLDMLParserListener(ParseTreeListener):

    # Enter a parse tree produced by TeradataSQLDMLParser#dml_stat.
    def enterDml_stat(self, ctx:TeradataSQLDMLParser.Dml_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#dml_stat.
    def exitDml_stat(self, ctx:TeradataSQLDMLParser.Dml_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#select_stat.
    def enterSelect_stat(self, ctx:TeradataSQLDMLParser.Select_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#select_stat.
    def exitSelect_stat(self, ctx:TeradataSQLDMLParser.Select_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#select_and_consume_stat.
    def enterSelect_and_consume_stat(self, ctx:TeradataSQLDMLParser.Select_and_consume_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#select_and_consume_stat.
    def exitSelect_and_consume_stat(self, ctx:TeradataSQLDMLParser.Select_and_consume_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#delete_stat.
    def enterDelete_stat(self, ctx:TeradataSQLDMLParser.Delete_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#delete_stat.
    def exitDelete_stat(self, ctx:TeradataSQLDMLParser.Delete_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#delete_table_spec.
    def enterDelete_table_spec(self, ctx:TeradataSQLDMLParser.Delete_table_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#delete_table_spec.
    def exitDelete_table_spec(self, ctx:TeradataSQLDMLParser.Delete_table_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#insert_stat.
    def enterInsert_stat(self, ctx:TeradataSQLDMLParser.Insert_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#insert_stat.
    def exitInsert_stat(self, ctx:TeradataSQLDMLParser.Insert_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#hash_by.
    def enterHash_by(self, ctx:TeradataSQLDMLParser.Hash_byContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#hash_by.
    def exitHash_by(self, ctx:TeradataSQLDMLParser.Hash_byContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#local_order_by.
    def enterLocal_order_by(self, ctx:TeradataSQLDMLParser.Local_order_byContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#local_order_by.
    def exitLocal_order_by(self, ctx:TeradataSQLDMLParser.Local_order_byContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#update_stat.
    def enterUpdate_stat(self, ctx:TeradataSQLDMLParser.Update_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#update_stat.
    def exitUpdate_stat(self, ctx:TeradataSQLDMLParser.Update_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#update_basic_form_stat.
    def enterUpdate_basic_form_stat(self, ctx:TeradataSQLDMLParser.Update_basic_form_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#update_basic_form_stat.
    def exitUpdate_basic_form_stat(self, ctx:TeradataSQLDMLParser.Update_basic_form_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#update_with_from_stat.
    def enterUpdate_with_from_stat(self, ctx:TeradataSQLDMLParser.Update_with_from_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#update_with_from_stat.
    def exitUpdate_with_from_stat(self, ctx:TeradataSQLDMLParser.Update_with_from_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#update_upsert_form_stat.
    def enterUpdate_upsert_form_stat(self, ctx:TeradataSQLDMLParser.Update_upsert_form_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#update_upsert_form_stat.
    def exitUpdate_upsert_form_stat(self, ctx:TeradataSQLDMLParser.Update_upsert_form_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#update_table_spec.
    def enterUpdate_table_spec(self, ctx:TeradataSQLDMLParser.Update_table_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#update_table_spec.
    def exitUpdate_table_spec(self, ctx:TeradataSQLDMLParser.Update_table_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#merge_stat.
    def enterMerge_stat(self, ctx:TeradataSQLDMLParser.Merge_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#merge_stat.
    def exitMerge_stat(self, ctx:TeradataSQLDMLParser.Merge_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#when_matched.
    def enterWhen_matched(self, ctx:TeradataSQLDMLParser.When_matchedContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#when_matched.
    def exitWhen_matched(self, ctx:TeradataSQLDMLParser.When_matchedContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#when_not_matched.
    def enterWhen_not_matched(self, ctx:TeradataSQLDMLParser.When_not_matchedContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#when_not_matched.
    def exitWhen_not_matched(self, ctx:TeradataSQLDMLParser.When_not_matchedContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#collect_demographics_stat.
    def enterCollect_demographics_stat(self, ctx:TeradataSQLDMLParser.Collect_demographics_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#collect_demographics_stat.
    def exitCollect_demographics_stat(self, ctx:TeradataSQLDMLParser.Collect_demographics_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#collect_statistics_qcd_form_stat.
    def enterCollect_statistics_qcd_form_stat(self, ctx:TeradataSQLDMLParser.Collect_statistics_qcd_form_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#collect_statistics_qcd_form_stat.
    def exitCollect_statistics_qcd_form_stat(self, ctx:TeradataSQLDMLParser.Collect_statistics_qcd_form_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#qcd_stats_target_spec.
    def enterQcd_stats_target_spec(self, ctx:TeradataSQLDMLParser.Qcd_stats_target_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#qcd_stats_target_spec.
    def exitQcd_stats_target_spec(self, ctx:TeradataSQLDMLParser.Qcd_stats_target_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#drop_statistics_qcd_form_stat.
    def enterDrop_statistics_qcd_form_stat(self, ctx:TeradataSQLDMLParser.Drop_statistics_qcd_form_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#drop_statistics_qcd_form_stat.
    def exitDrop_statistics_qcd_form_stat(self, ctx:TeradataSQLDMLParser.Drop_statistics_qcd_form_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#dump_explain_stat.
    def enterDump_explain_stat(self, ctx:TeradataSQLDMLParser.Dump_explain_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#dump_explain_stat.
    def exitDump_explain_stat(self, ctx:TeradataSQLDMLParser.Dump_explain_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#initiate_index_analysis_stat.
    def enterInitiate_index_analysis_stat(self, ctx:TeradataSQLDMLParser.Initiate_index_analysis_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#initiate_index_analysis_stat.
    def exitInitiate_index_analysis_stat(self, ctx:TeradataSQLDMLParser.Initiate_index_analysis_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#index_analysis_set_spec.
    def enterIndex_analysis_set_spec(self, ctx:TeradataSQLDMLParser.Index_analysis_set_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#index_analysis_set_spec.
    def exitIndex_analysis_set_spec(self, ctx:TeradataSQLDMLParser.Index_analysis_set_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#index_analysis_boundary_option.
    def enterIndex_analysis_boundary_option(self, ctx:TeradataSQLDMLParser.Index_analysis_boundary_optionContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#index_analysis_boundary_option.
    def exitIndex_analysis_boundary_option(self, ctx:TeradataSQLDMLParser.Index_analysis_boundary_optionContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#initiate_partition_analysis_stat.
    def enterInitiate_partition_analysis_stat(self, ctx:TeradataSQLDMLParser.Initiate_partition_analysis_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#initiate_partition_analysis_stat.
    def exitInitiate_partition_analysis_stat(self, ctx:TeradataSQLDMLParser.Initiate_partition_analysis_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#insert_explain_stat.
    def enterInsert_explain_stat(self, ctx:TeradataSQLDMLParser.Insert_explain_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#insert_explain_stat.
    def exitInsert_explain_stat(self, ctx:TeradataSQLDMLParser.Insert_explain_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#restart_index_analysis_stat.
    def enterRestart_index_analysis_stat(self, ctx:TeradataSQLDMLParser.Restart_index_analysis_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#restart_index_analysis_stat.
    def exitRestart_index_analysis_stat(self, ctx:TeradataSQLDMLParser.Restart_index_analysis_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#call_stat.
    def enterCall_stat(self, ctx:TeradataSQLDMLParser.Call_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#call_stat.
    def exitCall_stat(self, ctx:TeradataSQLDMLParser.Call_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#argument.
    def enterArgument(self, ctx:TeradataSQLDMLParser.ArgumentContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#argument.
    def exitArgument(self, ctx:TeradataSQLDMLParser.ArgumentContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#execute_stat.
    def enterExecute_stat(self, ctx:TeradataSQLDMLParser.Execute_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#execute_stat.
    def exitExecute_stat(self, ctx:TeradataSQLDMLParser.Execute_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#commit_stat.
    def enterCommit_stat(self, ctx:TeradataSQLDMLParser.Commit_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#commit_stat.
    def exitCommit_stat(self, ctx:TeradataSQLDMLParser.Commit_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#rollback_stat.
    def enterRollback_stat(self, ctx:TeradataSQLDMLParser.Rollback_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#rollback_stat.
    def exitRollback_stat(self, ctx:TeradataSQLDMLParser.Rollback_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#abort_stat.
    def enterAbort_stat(self, ctx:TeradataSQLDMLParser.Abort_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#abort_stat.
    def exitAbort_stat(self, ctx:TeradataSQLDMLParser.Abort_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#begin_transaction_stat.
    def enterBegin_transaction_stat(self, ctx:TeradataSQLDMLParser.Begin_transaction_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#begin_transaction_stat.
    def exitBegin_transaction_stat(self, ctx:TeradataSQLDMLParser.Begin_transaction_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#end_transaction_stat.
    def enterEnd_transaction_stat(self, ctx:TeradataSQLDMLParser.End_transaction_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#end_transaction_stat.
    def exitEnd_transaction_stat(self, ctx:TeradataSQLDMLParser.End_transaction_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#locking_stat.
    def enterLocking_stat(self, ctx:TeradataSQLDMLParser.Locking_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#locking_stat.
    def exitLocking_stat(self, ctx:TeradataSQLDMLParser.Locking_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#comment_retrieving_stat.
    def enterComment_retrieving_stat(self, ctx:TeradataSQLDMLParser.Comment_retrieving_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#comment_retrieving_stat.
    def exitComment_retrieving_stat(self, ctx:TeradataSQLDMLParser.Comment_retrieving_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#checkpoint_stat.
    def enterCheckpoint_stat(self, ctx:TeradataSQLDMLParser.Checkpoint_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#checkpoint_stat.
    def exitCheckpoint_stat(self, ctx:TeradataSQLDMLParser.Checkpoint_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#echo_stat.
    def enterEcho_stat(self, ctx:TeradataSQLDMLParser.Echo_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#echo_stat.
    def exitEcho_stat(self, ctx:TeradataSQLDMLParser.Echo_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#null_stat.
    def enterNull_stat(self, ctx:TeradataSQLDMLParser.Null_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#null_stat.
    def exitNull_stat(self, ctx:TeradataSQLDMLParser.Null_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#set_spec.
    def enterSet_spec(self, ctx:TeradataSQLDMLParser.Set_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#set_spec.
    def exitSet_spec(self, ctx:TeradataSQLDMLParser.Set_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#with_isolated_loading.
    def enterWith_isolated_loading(self, ctx:TeradataSQLDMLParser.With_isolated_loadingContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#with_isolated_loading.
    def exitWith_isolated_loading(self, ctx:TeradataSQLDMLParser.With_isolated_loadingContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#logging_errors.
    def enterLogging_errors(self, ctx:TeradataSQLDMLParser.Logging_errorsContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#logging_errors.
    def exitLogging_errors(self, ctx:TeradataSQLDMLParser.Logging_errorsContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#object_kind.
    def enterObject_kind(self, ctx:TeradataSQLDMLParser.Object_kindContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#object_kind.
    def exitObject_kind(self, ctx:TeradataSQLDMLParser.Object_kindContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#explained_sql_request.
    def enterExplained_sql_request(self, ctx:TeradataSQLDMLParser.Explained_sql_requestContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#explained_sql_request.
    def exitExplained_sql_request(self, ctx:TeradataSQLDMLParser.Explained_sql_requestContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#limit_sql_clause.
    def enterLimit_sql_clause(self, ctx:TeradataSQLDMLParser.Limit_sql_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#limit_sql_clause.
    def exitLimit_sql_clause(self, ctx:TeradataSQLDMLParser.Limit_sql_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#analysis_time_limit_clause.
    def enterAnalysis_time_limit_clause(self, ctx:TeradataSQLDMLParser.Analysis_time_limit_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#analysis_time_limit_clause.
    def exitAnalysis_time_limit_clause(self, ctx:TeradataSQLDMLParser.Analysis_time_limit_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#data_type.
    def enterData_type(self, ctx:TeradataSQLDMLParser.Data_typeContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#data_type.
    def exitData_type(self, ctx:TeradataSQLDMLParser.Data_typeContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#variable_data_type.
    def enterVariable_data_type(self, ctx:TeradataSQLDMLParser.Variable_data_typeContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#variable_data_type.
    def exitVariable_data_type(self, ctx:TeradataSQLDMLParser.Variable_data_typeContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#external_function_data_type.
    def enterExternal_function_data_type(self, ctx:TeradataSQLDMLParser.External_function_data_typeContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#external_function_data_type.
    def exitExternal_function_data_type(self, ctx:TeradataSQLDMLParser.External_function_data_typeContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#numeric_data_type.
    def enterNumeric_data_type(self, ctx:TeradataSQLDMLParser.Numeric_data_typeContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#numeric_data_type.
    def exitNumeric_data_type(self, ctx:TeradataSQLDMLParser.Numeric_data_typeContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#char_data_type.
    def enterChar_data_type(self, ctx:TeradataSQLDMLParser.Char_data_typeContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#char_data_type.
    def exitChar_data_type(self, ctx:TeradataSQLDMLParser.Char_data_typeContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#precisionless_char_data_type.
    def enterPrecisionless_char_data_type(self, ctx:TeradataSQLDMLParser.Precisionless_char_data_typeContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#precisionless_char_data_type.
    def exitPrecisionless_char_data_type(self, ctx:TeradataSQLDMLParser.Precisionless_char_data_typeContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#lob_as_locator_data_type.
    def enterLob_as_locator_data_type(self, ctx:TeradataSQLDMLParser.Lob_as_locator_data_typeContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#lob_as_locator_data_type.
    def exitLob_as_locator_data_type(self, ctx:TeradataSQLDMLParser.Lob_as_locator_data_typeContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#binary_data_type.
    def enterBinary_data_type(self, ctx:TeradataSQLDMLParser.Binary_data_typeContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#binary_data_type.
    def exitBinary_data_type(self, ctx:TeradataSQLDMLParser.Binary_data_typeContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#datetime_type.
    def enterDatetime_type(self, ctx:TeradataSQLDMLParser.Datetime_typeContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#datetime_type.
    def exitDatetime_type(self, ctx:TeradataSQLDMLParser.Datetime_typeContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#period_type.
    def enterPeriod_type(self, ctx:TeradataSQLDMLParser.Period_typeContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#period_type.
    def exitPeriod_type(self, ctx:TeradataSQLDMLParser.Period_typeContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#udt_type.
    def enterUdt_type(self, ctx:TeradataSQLDMLParser.Udt_typeContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#udt_type.
    def exitUdt_type(self, ctx:TeradataSQLDMLParser.Udt_typeContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#data_type_attribute.
    def enterData_type_attribute(self, ctx:TeradataSQLDMLParser.Data_type_attributeContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#data_type_attribute.
    def exitData_type_attribute(self, ctx:TeradataSQLDMLParser.Data_type_attributeContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#default_value_control_phrase.
    def enterDefault_value_control_phrase(self, ctx:TeradataSQLDMLParser.Default_value_control_phraseContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#default_value_control_phrase.
    def exitDefault_value_control_phrase(self, ctx:TeradataSQLDMLParser.Default_value_control_phraseContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#default_value.
    def enterDefault_value(self, ctx:TeradataSQLDMLParser.Default_valueContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#default_value.
    def exitDefault_value(self, ctx:TeradataSQLDMLParser.Default_valueContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#column_naming_phrase.
    def enterColumn_naming_phrase(self, ctx:TeradataSQLDMLParser.Column_naming_phraseContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#column_naming_phrase.
    def exitColumn_naming_phrase(self, ctx:TeradataSQLDMLParser.Column_naming_phraseContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#sysudtlib.
    def enterSysudtlib(self, ctx:TeradataSQLDMLParser.SysudtlibContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#sysudtlib.
    def exitSysudtlib(self, ctx:TeradataSQLDMLParser.SysudtlibContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#interval_period_spec.
    def enterInterval_period_spec(self, ctx:TeradataSQLDMLParser.Interval_period_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#interval_period_spec.
    def exitInterval_period_spec(self, ctx:TeradataSQLDMLParser.Interval_period_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#type_precision.
    def enterType_precision(self, ctx:TeradataSQLDMLParser.Type_precisionContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#type_precision.
    def exitType_precision(self, ctx:TeradataSQLDMLParser.Type_precisionContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#max_length_k_m_g.
    def enterMax_length_k_m_g(self, ctx:TeradataSQLDMLParser.Max_length_k_m_gContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#max_length_k_m_g.
    def exitMax_length_k_m_g(self, ctx:TeradataSQLDMLParser.Max_length_k_m_gContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#max_length_k_m.
    def enterMax_length_k_m(self, ctx:TeradataSQLDMLParser.Max_length_k_mContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#max_length_k_m.
    def exitMax_length_k_m(self, ctx:TeradataSQLDMLParser.Max_length_k_mContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#character_set_phrase.
    def enterCharacter_set_phrase(self, ctx:TeradataSQLDMLParser.Character_set_phraseContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#character_set_phrase.
    def exitCharacter_set_phrase(self, ctx:TeradataSQLDMLParser.Character_set_phraseContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#uppercase_phrase.
    def enterUppercase_phrase(self, ctx:TeradataSQLDMLParser.Uppercase_phraseContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#uppercase_phrase.
    def exitUppercase_phrase(self, ctx:TeradataSQLDMLParser.Uppercase_phraseContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#casespecific_phrase.
    def enterCasespecific_phrase(self, ctx:TeradataSQLDMLParser.Casespecific_phraseContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#casespecific_phrase.
    def exitCasespecific_phrase(self, ctx:TeradataSQLDMLParser.Casespecific_phraseContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#format_phrase.
    def enterFormat_phrase(self, ctx:TeradataSQLDMLParser.Format_phraseContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#format_phrase.
    def exitFormat_phrase(self, ctx:TeradataSQLDMLParser.Format_phraseContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#title_phrase.
    def enterTitle_phrase(self, ctx:TeradataSQLDMLParser.Title_phraseContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#title_phrase.
    def exitTitle_phrase(self, ctx:TeradataSQLDMLParser.Title_phraseContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#named_phrase.
    def enterNamed_phrase(self, ctx:TeradataSQLDMLParser.Named_phraseContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#named_phrase.
    def exitNamed_phrase(self, ctx:TeradataSQLDMLParser.Named_phraseContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#latin_unicode_character_set_phrase.
    def enterLatin_unicode_character_set_phrase(self, ctx:TeradataSQLDMLParser.Latin_unicode_character_set_phraseContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#latin_unicode_character_set_phrase.
    def exitLatin_unicode_character_set_phrase(self, ctx:TeradataSQLDMLParser.Latin_unicode_character_set_phraseContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#inline_length.
    def enterInline_length(self, ctx:TeradataSQLDMLParser.Inline_lengthContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#inline_length.
    def exitInline_length(self, ctx:TeradataSQLDMLParser.Inline_lengthContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#json_storage_format.
    def enterJson_storage_format(self, ctx:TeradataSQLDMLParser.Json_storage_formatContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#json_storage_format.
    def exitJson_storage_format(self, ctx:TeradataSQLDMLParser.Json_storage_formatContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#dataset_storage_format_clause.
    def enterDataset_storage_format_clause(self, ctx:TeradataSQLDMLParser.Dataset_storage_format_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#dataset_storage_format_clause.
    def exitDataset_storage_format_clause(self, ctx:TeradataSQLDMLParser.Dataset_storage_format_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#dataset_storage_format.
    def enterDataset_storage_format(self, ctx:TeradataSQLDMLParser.Dataset_storage_formatContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#dataset_storage_format.
    def exitDataset_storage_format(self, ctx:TeradataSQLDMLParser.Dataset_storage_formatContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#with_schema.
    def enterWith_schema(self, ctx:TeradataSQLDMLParser.With_schemaContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#with_schema.
    def exitWith_schema(self, ctx:TeradataSQLDMLParser.With_schemaContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#with_time_zone.
    def enterWith_time_zone(self, ctx:TeradataSQLDMLParser.With_time_zoneContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#with_time_zone.
    def exitWith_time_zone(self, ctx:TeradataSQLDMLParser.With_time_zoneContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#literal.
    def enterLiteral(self, ctx:TeradataSQLDMLParser.LiteralContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#literal.
    def exitLiteral(self, ctx:TeradataSQLDMLParser.LiteralContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#hex_byte_literal.
    def enterHex_byte_literal(self, ctx:TeradataSQLDMLParser.Hex_byte_literalContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#hex_byte_literal.
    def exitHex_byte_literal(self, ctx:TeradataSQLDMLParser.Hex_byte_literalContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#char_string_literal.
    def enterChar_string_literal(self, ctx:TeradataSQLDMLParser.Char_string_literalContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#char_string_literal.
    def exitChar_string_literal(self, ctx:TeradataSQLDMLParser.Char_string_literalContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#unicode_char_string_literal.
    def enterUnicode_char_string_literal(self, ctx:TeradataSQLDMLParser.Unicode_char_string_literalContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#unicode_char_string_literal.
    def exitUnicode_char_string_literal(self, ctx:TeradataSQLDMLParser.Unicode_char_string_literalContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#hex_char_string_literal.
    def enterHex_char_string_literal(self, ctx:TeradataSQLDMLParser.Hex_char_string_literalContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#hex_char_string_literal.
    def exitHex_char_string_literal(self, ctx:TeradataSQLDMLParser.Hex_char_string_literalContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#integer_literal.
    def enterInteger_literal(self, ctx:TeradataSQLDMLParser.Integer_literalContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#integer_literal.
    def exitInteger_literal(self, ctx:TeradataSQLDMLParser.Integer_literalContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#hex_integer_literal.
    def enterHex_integer_literal(self, ctx:TeradataSQLDMLParser.Hex_integer_literalContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#hex_integer_literal.
    def exitHex_integer_literal(self, ctx:TeradataSQLDMLParser.Hex_integer_literalContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#float_literal.
    def enterFloat_literal(self, ctx:TeradataSQLDMLParser.Float_literalContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#float_literal.
    def exitFloat_literal(self, ctx:TeradataSQLDMLParser.Float_literalContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#character_set_prefix.
    def enterCharacter_set_prefix(self, ctx:TeradataSQLDMLParser.Character_set_prefixContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#character_set_prefix.
    def exitCharacter_set_prefix(self, ctx:TeradataSQLDMLParser.Character_set_prefixContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#date_literal.
    def enterDate_literal(self, ctx:TeradataSQLDMLParser.Date_literalContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#date_literal.
    def exitDate_literal(self, ctx:TeradataSQLDMLParser.Date_literalContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#time_literal.
    def enterTime_literal(self, ctx:TeradataSQLDMLParser.Time_literalContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#time_literal.
    def exitTime_literal(self, ctx:TeradataSQLDMLParser.Time_literalContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#timestamp_literal.
    def enterTimestamp_literal(self, ctx:TeradataSQLDMLParser.Timestamp_literalContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#timestamp_literal.
    def exitTimestamp_literal(self, ctx:TeradataSQLDMLParser.Timestamp_literalContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#interval_literal.
    def enterInterval_literal(self, ctx:TeradataSQLDMLParser.Interval_literalContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#interval_literal.
    def exitInterval_literal(self, ctx:TeradataSQLDMLParser.Interval_literalContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#interval_qualifier.
    def enterInterval_qualifier(self, ctx:TeradataSQLDMLParser.Interval_qualifierContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#interval_qualifier.
    def exitInterval_qualifier(self, ctx:TeradataSQLDMLParser.Interval_qualifierContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#period_literal.
    def enterPeriod_literal(self, ctx:TeradataSQLDMLParser.Period_literalContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#period_literal.
    def exitPeriod_literal(self, ctx:TeradataSQLDMLParser.Period_literalContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#column_name.
    def enterColumn_name(self, ctx:TeradataSQLDMLParser.Column_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#column_name.
    def exitColumn_name(self, ctx:TeradataSQLDMLParser.Column_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#unqualified_column_name.
    def enterUnqualified_column_name(self, ctx:TeradataSQLDMLParser.Unqualified_column_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#unqualified_column_name.
    def exitUnqualified_column_name(self, ctx:TeradataSQLDMLParser.Unqualified_column_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#unqualified_name.
    def enterUnqualified_name(self, ctx:TeradataSQLDMLParser.Unqualified_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#unqualified_name.
    def exitUnqualified_name(self, ctx:TeradataSQLDMLParser.Unqualified_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#object_name.
    def enterObject_name(self, ctx:TeradataSQLDMLParser.Object_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#object_name.
    def exitObject_name(self, ctx:TeradataSQLDMLParser.Object_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#table_name.
    def enterTable_name(self, ctx:TeradataSQLDMLParser.Table_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#table_name.
    def exitTable_name(self, ctx:TeradataSQLDMLParser.Table_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#procedure_name.
    def enterProcedure_name(self, ctx:TeradataSQLDMLParser.Procedure_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#procedure_name.
    def exitProcedure_name(self, ctx:TeradataSQLDMLParser.Procedure_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#function_name.
    def enterFunction_name(self, ctx:TeradataSQLDMLParser.Function_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#function_name.
    def exitFunction_name(self, ctx:TeradataSQLDMLParser.Function_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#macro_name.
    def enterMacro_name(self, ctx:TeradataSQLDMLParser.Macro_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#macro_name.
    def exitMacro_name(self, ctx:TeradataSQLDMLParser.Macro_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#database_name.
    def enterDatabase_name(self, ctx:TeradataSQLDMLParser.Database_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#database_name.
    def exitDatabase_name(self, ctx:TeradataSQLDMLParser.Database_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#user_name.
    def enterUser_name(self, ctx:TeradataSQLDMLParser.User_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#user_name.
    def exitUser_name(self, ctx:TeradataSQLDMLParser.User_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#role_name.
    def enterRole_name(self, ctx:TeradataSQLDMLParser.Role_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#role_name.
    def exitRole_name(self, ctx:TeradataSQLDMLParser.Role_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#profile_name.
    def enterProfile_name(self, ctx:TeradataSQLDMLParser.Profile_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#profile_name.
    def exitProfile_name(self, ctx:TeradataSQLDMLParser.Profile_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#alias_name.
    def enterAlias_name(self, ctx:TeradataSQLDMLParser.Alias_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#alias_name.
    def exitAlias_name(self, ctx:TeradataSQLDMLParser.Alias_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#variable_name.
    def enterVariable_name(self, ctx:TeradataSQLDMLParser.Variable_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#variable_name.
    def exitVariable_name(self, ctx:TeradataSQLDMLParser.Variable_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#parameter_name.
    def enterParameter_name(self, ctx:TeradataSQLDMLParser.Parameter_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#parameter_name.
    def exitParameter_name(self, ctx:TeradataSQLDMLParser.Parameter_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#label_name.
    def enterLabel_name(self, ctx:TeradataSQLDMLParser.Label_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#label_name.
    def exitLabel_name(self, ctx:TeradataSQLDMLParser.Label_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#condition_name.
    def enterCondition_name(self, ctx:TeradataSQLDMLParser.Condition_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#condition_name.
    def exitCondition_name(self, ctx:TeradataSQLDMLParser.Condition_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#cursor_name.
    def enterCursor_name(self, ctx:TeradataSQLDMLParser.Cursor_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#cursor_name.
    def exitCursor_name(self, ctx:TeradataSQLDMLParser.Cursor_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#statement_name.
    def enterStatement_name(self, ctx:TeradataSQLDMLParser.Statement_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#statement_name.
    def exitStatement_name(self, ctx:TeradataSQLDMLParser.Statement_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#statistics_name.
    def enterStatistics_name(self, ctx:TeradataSQLDMLParser.Statistics_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#statistics_name.
    def exitStatistics_name(self, ctx:TeradataSQLDMLParser.Statistics_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#udt_name.
    def enterUdt_name(self, ctx:TeradataSQLDMLParser.Udt_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#udt_name.
    def exitUdt_name(self, ctx:TeradataSQLDMLParser.Udt_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#attribute_name.
    def enterAttribute_name(self, ctx:TeradataSQLDMLParser.Attribute_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#attribute_name.
    def exitAttribute_name(self, ctx:TeradataSQLDMLParser.Attribute_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#method_name.
    def enterMethod_name(self, ctx:TeradataSQLDMLParser.Method_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#method_name.
    def exitMethod_name(self, ctx:TeradataSQLDMLParser.Method_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#anchor_name.
    def enterAnchor_name(self, ctx:TeradataSQLDMLParser.Anchor_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#anchor_name.
    def exitAnchor_name(self, ctx:TeradataSQLDMLParser.Anchor_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#nonreserved_word.
    def enterNonreserved_word(self, ctx:TeradataSQLDMLParser.Nonreserved_wordContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#nonreserved_word.
    def exitNonreserved_word(self, ctx:TeradataSQLDMLParser.Nonreserved_wordContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#query_expr.
    def enterQuery_expr(self, ctx:TeradataSQLDMLParser.Query_exprContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#query_expr.
    def exitQuery_expr(self, ctx:TeradataSQLDMLParser.Query_exprContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#query_term.
    def enterQuery_term(self, ctx:TeradataSQLDMLParser.Query_termContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#query_term.
    def exitQuery_term(self, ctx:TeradataSQLDMLParser.Query_termContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#with_deleted_rows.
    def enterWith_deleted_rows(self, ctx:TeradataSQLDMLParser.With_deleted_rowsContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#with_deleted_rows.
    def exitWith_deleted_rows(self, ctx:TeradataSQLDMLParser.With_deleted_rowsContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#as_json.
    def enterAs_json(self, ctx:TeradataSQLDMLParser.As_jsonContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#as_json.
    def exitAs_json(self, ctx:TeradataSQLDMLParser.As_jsonContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#select_list.
    def enterSelect_list(self, ctx:TeradataSQLDMLParser.Select_listContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#select_list.
    def exitSelect_list(self, ctx:TeradataSQLDMLParser.Select_listContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#top_n.
    def enterTop_n(self, ctx:TeradataSQLDMLParser.Top_nContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#top_n.
    def exitTop_n(self, ctx:TeradataSQLDMLParser.Top_nContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#normalize.
    def enterNormalize(self, ctx:TeradataSQLDMLParser.NormalizeContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#normalize.
    def exitNormalize(self, ctx:TeradataSQLDMLParser.NormalizeContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#all_operator.
    def enterAll_operator(self, ctx:TeradataSQLDMLParser.All_operatorContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#all_operator.
    def exitAll_operator(self, ctx:TeradataSQLDMLParser.All_operatorContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#selected_columns.
    def enterSelected_columns(self, ctx:TeradataSQLDMLParser.Selected_columnsContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#selected_columns.
    def exitSelected_columns(self, ctx:TeradataSQLDMLParser.Selected_columnsContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#selected_column.
    def enterSelected_column(self, ctx:TeradataSQLDMLParser.Selected_columnContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#selected_column.
    def exitSelected_column(self, ctx:TeradataSQLDMLParser.Selected_columnContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#into_clause.
    def enterInto_clause(self, ctx:TeradataSQLDMLParser.Into_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#into_clause.
    def exitInto_clause(self, ctx:TeradataSQLDMLParser.Into_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#from_clause.
    def enterFrom_clause(self, ctx:TeradataSQLDMLParser.From_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#from_clause.
    def exitFrom_clause(self, ctx:TeradataSQLDMLParser.From_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#from_spec.
    def enterFrom_spec(self, ctx:TeradataSQLDMLParser.From_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#from_spec.
    def exitFrom_spec(self, ctx:TeradataSQLDMLParser.From_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#join_source_spec.
    def enterJoin_source_spec(self, ctx:TeradataSQLDMLParser.Join_source_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#join_source_spec.
    def exitJoin_source_spec(self, ctx:TeradataSQLDMLParser.Join_source_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#join_joined_spec.
    def enterJoin_joined_spec(self, ctx:TeradataSQLDMLParser.Join_joined_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#join_joined_spec.
    def exitJoin_joined_spec(self, ctx:TeradataSQLDMLParser.Join_joined_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#from_pivot_spec.
    def enterFrom_pivot_spec(self, ctx:TeradataSQLDMLParser.From_pivot_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#from_pivot_spec.
    def exitFrom_pivot_spec(self, ctx:TeradataSQLDMLParser.From_pivot_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#from_unpivot_spec.
    def enterFrom_unpivot_spec(self, ctx:TeradataSQLDMLParser.From_unpivot_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#from_unpivot_spec.
    def exitFrom_unpivot_spec(self, ctx:TeradataSQLDMLParser.From_unpivot_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#table_reference.
    def enterTable_reference(self, ctx:TeradataSQLDMLParser.Table_referenceContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#table_reference.
    def exitTable_reference(self, ctx:TeradataSQLDMLParser.Table_referenceContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#join_clause.
    def enterJoin_clause(self, ctx:TeradataSQLDMLParser.Join_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#join_clause.
    def exitJoin_clause(self, ctx:TeradataSQLDMLParser.Join_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#join_on_clause.
    def enterJoin_on_clause(self, ctx:TeradataSQLDMLParser.Join_on_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#join_on_clause.
    def exitJoin_on_clause(self, ctx:TeradataSQLDMLParser.Join_on_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#foreign_table_reference.
    def enterForeign_table_reference(self, ctx:TeradataSQLDMLParser.Foreign_table_referenceContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#foreign_table_reference.
    def exitForeign_table_reference(self, ctx:TeradataSQLDMLParser.Foreign_table_referenceContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#foreign_function_reference.
    def enterForeign_function_reference(self, ctx:TeradataSQLDMLParser.Foreign_function_referenceContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#foreign_function_reference.
    def exitForeign_function_reference(self, ctx:TeradataSQLDMLParser.Foreign_function_referenceContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#foreign_on_clause.
    def enterForeign_on_clause(self, ctx:TeradataSQLDMLParser.Foreign_on_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#foreign_on_clause.
    def exitForeign_on_clause(self, ctx:TeradataSQLDMLParser.Foreign_on_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#exported_data.
    def enterExported_data(self, ctx:TeradataSQLDMLParser.Exported_dataContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#exported_data.
    def exitExported_data(self, ctx:TeradataSQLDMLParser.Exported_dataContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#foreign_using_clause.
    def enterForeign_using_clause(self, ctx:TeradataSQLDMLParser.Foreign_using_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#foreign_using_clause.
    def exitForeign_using_clause(self, ctx:TeradataSQLDMLParser.Foreign_using_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#foreign_parameter.
    def enterForeign_parameter(self, ctx:TeradataSQLDMLParser.Foreign_parameterContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#foreign_parameter.
    def exitForeign_parameter(self, ctx:TeradataSQLDMLParser.Foreign_parameterContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#foreign_returns_clause.
    def enterForeign_returns_clause(self, ctx:TeradataSQLDMLParser.Foreign_returns_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#foreign_returns_clause.
    def exitForeign_returns_clause(self, ctx:TeradataSQLDMLParser.Foreign_returns_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#server_name_reference.
    def enterServer_name_reference(self, ctx:TeradataSQLDMLParser.Server_name_referenceContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#server_name_reference.
    def exitServer_name_reference(self, ctx:TeradataSQLDMLParser.Server_name_referenceContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#table_function_reference.
    def enterTable_function_reference(self, ctx:TeradataSQLDMLParser.Table_function_referenceContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#table_function_reference.
    def exitTable_function_reference(self, ctx:TeradataSQLDMLParser.Table_function_referenceContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#udt_table_function.
    def enterUdt_table_function(self, ctx:TeradataSQLDMLParser.Udt_table_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#udt_table_function.
    def exitUdt_table_function(self, ctx:TeradataSQLDMLParser.Udt_table_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#unnest_table_function.
    def enterUnnest_table_function(self, ctx:TeradataSQLDMLParser.Unnest_table_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#unnest_table_function.
    def exitUnnest_table_function(self, ctx:TeradataSQLDMLParser.Unnest_table_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#table_function_returns_clause.
    def enterTable_function_returns_clause(self, ctx:TeradataSQLDMLParser.Table_function_returns_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#table_function_returns_clause.
    def exitTable_function_returns_clause(self, ctx:TeradataSQLDMLParser.Table_function_returns_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#table_function_local_order_by_clause.
    def enterTable_function_local_order_by_clause(self, ctx:TeradataSQLDMLParser.Table_function_local_order_by_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#table_function_local_order_by_clause.
    def exitTable_function_local_order_by_clause(self, ctx:TeradataSQLDMLParser.Table_function_local_order_by_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#table_function_hash_by_clause.
    def enterTable_function_hash_by_clause(self, ctx:TeradataSQLDMLParser.Table_function_hash_by_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#table_function_hash_by_clause.
    def exitTable_function_hash_by_clause(self, ctx:TeradataSQLDMLParser.Table_function_hash_by_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#table_operator_reference.
    def enterTable_operator_reference(self, ctx:TeradataSQLDMLParser.Table_operator_referenceContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#table_operator_reference.
    def exitTable_operator_reference(self, ctx:TeradataSQLDMLParser.Table_operator_referenceContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#xmltable_operator.
    def enterXmltable_operator(self, ctx:TeradataSQLDMLParser.Xmltable_operatorContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#xmltable_operator.
    def exitXmltable_operator(self, ctx:TeradataSQLDMLParser.Xmltable_operatorContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#calcmatrix_table_operator.
    def enterCalcmatrix_table_operator(self, ctx:TeradataSQLDMLParser.Calcmatrix_table_operatorContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#calcmatrix_table_operator.
    def exitCalcmatrix_table_operator(self, ctx:TeradataSQLDMLParser.Calcmatrix_table_operatorContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#read_nos_table_operator.
    def enterRead_nos_table_operator(self, ctx:TeradataSQLDMLParser.Read_nos_table_operatorContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#read_nos_table_operator.
    def exitRead_nos_table_operator(self, ctx:TeradataSQLDMLParser.Read_nos_table_operatorContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#script_table_operator.
    def enterScript_table_operator(self, ctx:TeradataSQLDMLParser.Script_table_operatorContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#script_table_operator.
    def exitScript_table_operator(self, ctx:TeradataSQLDMLParser.Script_table_operatorContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#td_unpivot_table_operator.
    def enterTd_unpivot_table_operator(self, ctx:TeradataSQLDMLParser.Td_unpivot_table_operatorContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#td_unpivot_table_operator.
    def exitTd_unpivot_table_operator(self, ctx:TeradataSQLDMLParser.Td_unpivot_table_operatorContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#write_nos_table_operator.
    def enterWrite_nos_table_operator(self, ctx:TeradataSQLDMLParser.Write_nos_table_operatorContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#write_nos_table_operator.
    def exitWrite_nos_table_operator(self, ctx:TeradataSQLDMLParser.Write_nos_table_operatorContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#json_table_table_operator.
    def enterJson_table_table_operator(self, ctx:TeradataSQLDMLParser.Json_table_table_operatorContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#json_table_table_operator.
    def exitJson_table_table_operator(self, ctx:TeradataSQLDMLParser.Json_table_table_operatorContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#json_keys_table_operator.
    def enterJson_keys_table_operator(self, ctx:TeradataSQLDMLParser.Json_keys_table_operatorContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#json_keys_table_operator.
    def exitJson_keys_table_operator(self, ctx:TeradataSQLDMLParser.Json_keys_table_operatorContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#json_shred_table_operator.
    def enterJson_shred_table_operator(self, ctx:TeradataSQLDMLParser.Json_shred_table_operatorContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#json_shred_table_operator.
    def exitJson_shred_table_operator(self, ctx:TeradataSQLDMLParser.Json_shred_table_operatorContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#generic_table_operator.
    def enterGeneric_table_operator(self, ctx:TeradataSQLDMLParser.Generic_table_operatorContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#generic_table_operator.
    def exitGeneric_table_operator(self, ctx:TeradataSQLDMLParser.Generic_table_operatorContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#table_operator_on_clause.
    def enterTable_operator_on_clause(self, ctx:TeradataSQLDMLParser.Table_operator_on_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#table_operator_on_clause.
    def exitTable_operator_on_clause(self, ctx:TeradataSQLDMLParser.Table_operator_on_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#table_operator_execute_clause.
    def enterTable_operator_execute_clause(self, ctx:TeradataSQLDMLParser.Table_operator_execute_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#table_operator_execute_clause.
    def exitTable_operator_execute_clause(self, ctx:TeradataSQLDMLParser.Table_operator_execute_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#table_operator_out_table_clause.
    def enterTable_operator_out_table_clause(self, ctx:TeradataSQLDMLParser.Table_operator_out_table_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#table_operator_out_table_clause.
    def exitTable_operator_out_table_clause(self, ctx:TeradataSQLDMLParser.Table_operator_out_table_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#table_operator_using_clause.
    def enterTable_operator_using_clause(self, ctx:TeradataSQLDMLParser.Table_operator_using_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#table_operator_using_clause.
    def exitTable_operator_using_clause(self, ctx:TeradataSQLDMLParser.Table_operator_using_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#table_operator_using_spec.
    def enterTable_operator_using_spec(self, ctx:TeradataSQLDMLParser.Table_operator_using_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#table_operator_using_spec.
    def exitTable_operator_using_spec(self, ctx:TeradataSQLDMLParser.Table_operator_using_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#json_keys_using_name_value_pair.
    def enterJson_keys_using_name_value_pair(self, ctx:TeradataSQLDMLParser.Json_keys_using_name_value_pairContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#json_keys_using_name_value_pair.
    def exitJson_keys_using_name_value_pair(self, ctx:TeradataSQLDMLParser.Json_keys_using_name_value_pairContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#hash_or_partition_by.
    def enterHash_or_partition_by(self, ctx:TeradataSQLDMLParser.Hash_or_partition_byContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#hash_or_partition_by.
    def exitHash_or_partition_by(self, ctx:TeradataSQLDMLParser.Hash_or_partition_byContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#subquery_reference.
    def enterSubquery_reference(self, ctx:TeradataSQLDMLParser.Subquery_referenceContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#subquery_reference.
    def exitSubquery_reference(self, ctx:TeradataSQLDMLParser.Subquery_referenceContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#location.
    def enterLocation(self, ctx:TeradataSQLDMLParser.LocationContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#location.
    def exitLocation(self, ctx:TeradataSQLDMLParser.LocationContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#read_nos_option.
    def enterRead_nos_option(self, ctx:TeradataSQLDMLParser.Read_nos_optionContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#read_nos_option.
    def exitRead_nos_option(self, ctx:TeradataSQLDMLParser.Read_nos_optionContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#write_nos_option.
    def enterWrite_nos_option(self, ctx:TeradataSQLDMLParser.Write_nos_optionContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#write_nos_option.
    def exitWrite_nos_option(self, ctx:TeradataSQLDMLParser.Write_nos_optionContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#with_clause.
    def enterWith_clause(self, ctx:TeradataSQLDMLParser.With_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#with_clause.
    def exitWith_clause(self, ctx:TeradataSQLDMLParser.With_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#with_clause_by_phrase.
    def enterWith_clause_by_phrase(self, ctx:TeradataSQLDMLParser.With_clause_by_phraseContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#with_clause_by_phrase.
    def exitWith_clause_by_phrase(self, ctx:TeradataSQLDMLParser.With_clause_by_phraseContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#with_clause_title_phrase.
    def enterWith_clause_title_phrase(self, ctx:TeradataSQLDMLParser.With_clause_title_phraseContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#with_clause_title_phrase.
    def exitWith_clause_title_phrase(self, ctx:TeradataSQLDMLParser.With_clause_title_phraseContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#where_clause.
    def enterWhere_clause(self, ctx:TeradataSQLDMLParser.Where_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#where_clause.
    def exitWhere_clause(self, ctx:TeradataSQLDMLParser.Where_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#group_by_clause.
    def enterGroup_by_clause(self, ctx:TeradataSQLDMLParser.Group_by_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#group_by_clause.
    def exitGroup_by_clause(self, ctx:TeradataSQLDMLParser.Group_by_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#group_by_spec.
    def enterGroup_by_spec(self, ctx:TeradataSQLDMLParser.Group_by_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#group_by_spec.
    def exitGroup_by_spec(self, ctx:TeradataSQLDMLParser.Group_by_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#ordinary_grouping_set.
    def enterOrdinary_grouping_set(self, ctx:TeradataSQLDMLParser.Ordinary_grouping_setContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#ordinary_grouping_set.
    def exitOrdinary_grouping_set(self, ctx:TeradataSQLDMLParser.Ordinary_grouping_setContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#ordinary_grouping_set_parenthesized.
    def enterOrdinary_grouping_set_parenthesized(self, ctx:TeradataSQLDMLParser.Ordinary_grouping_set_parenthesizedContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#ordinary_grouping_set_parenthesized.
    def exitOrdinary_grouping_set_parenthesized(self, ctx:TeradataSQLDMLParser.Ordinary_grouping_set_parenthesizedContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#empty_grouping_set.
    def enterEmpty_grouping_set(self, ctx:TeradataSQLDMLParser.Empty_grouping_setContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#empty_grouping_set.
    def exitEmpty_grouping_set(self, ctx:TeradataSQLDMLParser.Empty_grouping_setContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#rollup_option.
    def enterRollup_option(self, ctx:TeradataSQLDMLParser.Rollup_optionContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#rollup_option.
    def exitRollup_option(self, ctx:TeradataSQLDMLParser.Rollup_optionContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#cube_option.
    def enterCube_option(self, ctx:TeradataSQLDMLParser.Cube_optionContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#cube_option.
    def exitCube_option(self, ctx:TeradataSQLDMLParser.Cube_optionContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#grouping_sets_option.
    def enterGrouping_sets_option(self, ctx:TeradataSQLDMLParser.Grouping_sets_optionContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#grouping_sets_option.
    def exitGrouping_sets_option(self, ctx:TeradataSQLDMLParser.Grouping_sets_optionContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#grouping_sets_spec.
    def enterGrouping_sets_spec(self, ctx:TeradataSQLDMLParser.Grouping_sets_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#grouping_sets_spec.
    def exitGrouping_sets_spec(self, ctx:TeradataSQLDMLParser.Grouping_sets_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#having_clause.
    def enterHaving_clause(self, ctx:TeradataSQLDMLParser.Having_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#having_clause.
    def exitHaving_clause(self, ctx:TeradataSQLDMLParser.Having_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#qualify_clause.
    def enterQualify_clause(self, ctx:TeradataSQLDMLParser.Qualify_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#qualify_clause.
    def exitQualify_clause(self, ctx:TeradataSQLDMLParser.Qualify_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#sample_clause.
    def enterSample_clause(self, ctx:TeradataSQLDMLParser.Sample_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#sample_clause.
    def exitSample_clause(self, ctx:TeradataSQLDMLParser.Sample_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#sample_fraction_description.
    def enterSample_fraction_description(self, ctx:TeradataSQLDMLParser.Sample_fraction_descriptionContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#sample_fraction_description.
    def exitSample_fraction_description(self, ctx:TeradataSQLDMLParser.Sample_fraction_descriptionContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#sample_count_description.
    def enterSample_count_description(self, ctx:TeradataSQLDMLParser.Sample_count_descriptionContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#sample_count_description.
    def exitSample_count_description(self, ctx:TeradataSQLDMLParser.Sample_count_descriptionContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#sample_when_clause.
    def enterSample_when_clause(self, ctx:TeradataSQLDMLParser.Sample_when_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#sample_when_clause.
    def exitSample_when_clause(self, ctx:TeradataSQLDMLParser.Sample_when_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#expand_on_clause.
    def enterExpand_on_clause(self, ctx:TeradataSQLDMLParser.Expand_on_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#expand_on_clause.
    def exitExpand_on_clause(self, ctx:TeradataSQLDMLParser.Expand_on_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#order_by_clause.
    def enterOrder_by_clause(self, ctx:TeradataSQLDMLParser.Order_by_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#order_by_clause.
    def exitOrder_by_clause(self, ctx:TeradataSQLDMLParser.Order_by_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#order_by_spec_full.
    def enterOrder_by_spec_full(self, ctx:TeradataSQLDMLParser.Order_by_spec_fullContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#order_by_spec_full.
    def exitOrder_by_spec_full(self, ctx:TeradataSQLDMLParser.Order_by_spec_fullContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#order_by_spec_asc_desc_only.
    def enterOrder_by_spec_asc_desc_only(self, ctx:TeradataSQLDMLParser.Order_by_spec_asc_desc_onlyContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#order_by_spec_asc_desc_only.
    def exitOrder_by_spec_asc_desc_only(self, ctx:TeradataSQLDMLParser.Order_by_spec_asc_desc_onlyContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#with_check_option.
    def enterWith_check_option(self, ctx:TeradataSQLDMLParser.With_check_optionContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#with_check_option.
    def exitWith_check_option(self, ctx:TeradataSQLDMLParser.With_check_optionContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#PeriodMeets.
    def enterPeriodMeets(self, ctx:TeradataSQLDMLParser.PeriodMeetsContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#PeriodMeets.
    def exitPeriodMeets(self, ctx:TeradataSQLDMLParser.PeriodMeetsContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#PeriodImmediatelySucceeds.
    def enterPeriodImmediatelySucceeds(self, ctx:TeradataSQLDMLParser.PeriodImmediatelySucceedsContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#PeriodImmediatelySucceeds.
    def exitPeriodImmediatelySucceeds(self, ctx:TeradataSQLDMLParser.PeriodImmediatelySucceedsContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#PeriodEquals.
    def enterPeriodEquals(self, ctx:TeradataSQLDMLParser.PeriodEqualsContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#PeriodEquals.
    def exitPeriodEquals(self, ctx:TeradataSQLDMLParser.PeriodEqualsContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#ScalarComparelist.
    def enterScalarComparelist(self, ctx:TeradataSQLDMLParser.ScalarComparelistContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#ScalarComparelist.
    def exitScalarComparelist(self, ctx:TeradataSQLDMLParser.ScalarComparelistContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#TupleInSubquery.
    def enterTupleInSubquery(self, ctx:TeradataSQLDMLParser.TupleInSubqueryContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#TupleInSubquery.
    def exitTupleInSubquery(self, ctx:TeradataSQLDMLParser.TupleInSubqueryContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#LogicalOr.
    def enterLogicalOr(self, ctx:TeradataSQLDMLParser.LogicalOrContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#LogicalOr.
    def exitLogicalOr(self, ctx:TeradataSQLDMLParser.LogicalOrContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#ScalarInScalar.
    def enterScalarInScalar(self, ctx:TeradataSQLDMLParser.ScalarInScalarContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#ScalarInScalar.
    def exitScalarInScalar(self, ctx:TeradataSQLDMLParser.ScalarInScalarContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#ScalarCompareScalar.
    def enterScalarCompareScalar(self, ctx:TeradataSQLDMLParser.ScalarCompareScalarContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#ScalarCompareScalar.
    def exitScalarCompareScalar(self, ctx:TeradataSQLDMLParser.ScalarCompareScalarContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#LogicalNot.
    def enterLogicalNot(self, ctx:TeradataSQLDMLParser.LogicalNotContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#LogicalNot.
    def exitLogicalNot(self, ctx:TeradataSQLDMLParser.LogicalNotContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#TupleComparelist.
    def enterTupleComparelist(self, ctx:TeradataSQLDMLParser.TupleComparelistContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#TupleComparelist.
    def exitTupleComparelist(self, ctx:TeradataSQLDMLParser.TupleComparelistContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#ScalarInList.
    def enterScalarInList(self, ctx:TeradataSQLDMLParser.ScalarInListContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#ScalarInList.
    def exitScalarInList(self, ctx:TeradataSQLDMLParser.ScalarInListContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#TupleLikeList.
    def enterTupleLikeList(self, ctx:TeradataSQLDMLParser.TupleLikeListContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#TupleLikeList.
    def exitTupleLikeList(self, ctx:TeradataSQLDMLParser.TupleLikeListContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#LogicalAnd.
    def enterLogicalAnd(self, ctx:TeradataSQLDMLParser.LogicalAndContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#LogicalAnd.
    def exitLogicalAnd(self, ctx:TeradataSQLDMLParser.LogicalAndContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#ScalarInSubquery.
    def enterScalarInSubquery(self, ctx:TeradataSQLDMLParser.ScalarInSubqueryContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#ScalarInSubquery.
    def exitScalarInSubquery(self, ctx:TeradataSQLDMLParser.ScalarInSubqueryContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#PeriodContains.
    def enterPeriodContains(self, ctx:TeradataSQLDMLParser.PeriodContainsContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#PeriodContains.
    def exitPeriodContains(self, ctx:TeradataSQLDMLParser.PeriodContainsContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#PeriodOverlaps.
    def enterPeriodOverlaps(self, ctx:TeradataSQLDMLParser.PeriodOverlapsContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#PeriodOverlaps.
    def exitPeriodOverlaps(self, ctx:TeradataSQLDMLParser.PeriodOverlapsContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#Between.
    def enterBetween(self, ctx:TeradataSQLDMLParser.BetweenContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#Between.
    def exitBetween(self, ctx:TeradataSQLDMLParser.BetweenContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#ParenthesizedLogicalExpr.
    def enterParenthesizedLogicalExpr(self, ctx:TeradataSQLDMLParser.ParenthesizedLogicalExprContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#ParenthesizedLogicalExpr.
    def exitParenthesizedLogicalExpr(self, ctx:TeradataSQLDMLParser.ParenthesizedLogicalExprContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#PeriodImmediatelyPrecedes.
    def enterPeriodImmediatelyPrecedes(self, ctx:TeradataSQLDMLParser.PeriodImmediatelyPrecedesContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#PeriodImmediatelyPrecedes.
    def exitPeriodImmediatelyPrecedes(self, ctx:TeradataSQLDMLParser.PeriodImmediatelyPrecedesContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#NullCheck.
    def enterNullCheck(self, ctx:TeradataSQLDMLParser.NullCheckContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#NullCheck.
    def exitNullCheck(self, ctx:TeradataSQLDMLParser.NullCheckContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#PeriodPrecedes.
    def enterPeriodPrecedes(self, ctx:TeradataSQLDMLParser.PeriodPrecedesContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#PeriodPrecedes.
    def exitPeriodPrecedes(self, ctx:TeradataSQLDMLParser.PeriodPrecedesContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#Exists.
    def enterExists(self, ctx:TeradataSQLDMLParser.ExistsContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#Exists.
    def exitExists(self, ctx:TeradataSQLDMLParser.ExistsContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#PeriodSucceeds.
    def enterPeriodSucceeds(self, ctx:TeradataSQLDMLParser.PeriodSucceedsContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#PeriodSucceeds.
    def exitPeriodSucceeds(self, ctx:TeradataSQLDMLParser.PeriodSucceedsContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#ScalarLikeList.
    def enterScalarLikeList(self, ctx:TeradataSQLDMLParser.ScalarLikeListContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#ScalarLikeList.
    def exitScalarLikeList(self, ctx:TeradataSQLDMLParser.ScalarLikeListContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#ScalarLikeScalar.
    def enterScalarLikeScalar(self, ctx:TeradataSQLDMLParser.ScalarLikeScalarContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#ScalarLikeScalar.
    def exitScalarLikeScalar(self, ctx:TeradataSQLDMLParser.ScalarLikeScalarContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#JsonMetadata.
    def enterJsonMetadata(self, ctx:TeradataSQLDMLParser.JsonMetadataContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#JsonMetadata.
    def exitJsonMetadata(self, ctx:TeradataSQLDMLParser.JsonMetadataContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#JsonAsBson.
    def enterJsonAsBson(self, ctx:TeradataSQLDMLParser.JsonAsBsonContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#JsonAsBson.
    def exitJsonAsBson(self, ctx:TeradataSQLDMLParser.JsonAsBsonContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#VariantTypeConstructor.
    def enterVariantTypeConstructor(self, ctx:TeradataSQLDMLParser.VariantTypeConstructorContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#VariantTypeConstructor.
    def exitVariantTypeConstructor(self, ctx:TeradataSQLDMLParser.VariantTypeConstructorContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#XMLExtract.
    def enterXMLExtract(self, ctx:TeradataSQLDMLParser.XMLExtractContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#XMLExtract.
    def exitXMLExtract(self, ctx:TeradataSQLDMLParser.XMLExtractContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#ArrayComparison.
    def enterArrayComparison(self, ctx:TeradataSQLDMLParser.ArrayComparisonContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#ArrayComparison.
    def exitArrayComparison(self, ctx:TeradataSQLDMLParser.ArrayComparisonContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#ArrayGet.
    def enterArrayGet(self, ctx:TeradataSQLDMLParser.ArrayGetContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#ArrayGet.
    def exitArrayGet(self, ctx:TeradataSQLDMLParser.ArrayGetContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#XMLConstructor.
    def enterXMLConstructor(self, ctx:TeradataSQLDMLParser.XMLConstructorContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#XMLConstructor.
    def exitXMLConstructor(self, ctx:TeradataSQLDMLParser.XMLConstructorContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#UDTMethodInvocation.
    def enterUDTMethodInvocation(self, ctx:TeradataSQLDMLParser.UDTMethodInvocationContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#UDTMethodInvocation.
    def exitUDTMethodInvocation(self, ctx:TeradataSQLDMLParser.UDTMethodInvocationContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#JsonExtractLargeValue.
    def enterJsonExtractLargeValue(self, ctx:TeradataSQLDMLParser.JsonExtractLargeValueContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#JsonExtractLargeValue.
    def exitJsonExtractLargeValue(self, ctx:TeradataSQLDMLParser.JsonExtractLargeValueContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#JsonRecursiveDescendSlice.
    def enterJsonRecursiveDescendSlice(self, ctx:TeradataSQLDMLParser.JsonRecursiveDescendSliceContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#JsonRecursiveDescendSlice.
    def exitJsonRecursiveDescendSlice(self, ctx:TeradataSQLDMLParser.JsonRecursiveDescendSliceContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#FunctionInvocation.
    def enterFunctionInvocation(self, ctx:TeradataSQLDMLParser.FunctionInvocationContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#FunctionInvocation.
    def exitFunctionInvocation(self, ctx:TeradataSQLDMLParser.FunctionInvocationContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#ScalarSubquery.
    def enterScalarSubquery(self, ctx:TeradataSQLDMLParser.ScalarSubqueryContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#ScalarSubquery.
    def exitScalarSubquery(self, ctx:TeradataSQLDMLParser.ScalarSubqueryContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#JsonExistValue.
    def enterJsonExistValue(self, ctx:TeradataSQLDMLParser.JsonExistValueContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#JsonExistValue.
    def exitJsonExistValue(self, ctx:TeradataSQLDMLParser.JsonExistValueContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#Modulo.
    def enterModulo(self, ctx:TeradataSQLDMLParser.ModuloContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#Modulo.
    def exitModulo(self, ctx:TeradataSQLDMLParser.ModuloContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#JsonExtractValue.
    def enterJsonExtractValue(self, ctx:TeradataSQLDMLParser.JsonExtractValueContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#JsonExtractValue.
    def exitJsonExtractValue(self, ctx:TeradataSQLDMLParser.JsonExtractValueContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#XMLCreateSchemaBasedXML.
    def enterXMLCreateSchemaBasedXML(self, ctx:TeradataSQLDMLParser.XMLCreateSchemaBasedXMLContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#XMLCreateSchemaBasedXML.
    def exitXMLCreateSchemaBasedXML(self, ctx:TeradataSQLDMLParser.XMLCreateSchemaBasedXMLContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#ArrayUpdate.
    def enterArrayUpdate(self, ctx:TeradataSQLDMLParser.ArrayUpdateContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#ArrayUpdate.
    def exitArrayUpdate(self, ctx:TeradataSQLDMLParser.ArrayUpdateContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#JsonExtract.
    def enterJsonExtract(self, ctx:TeradataSQLDMLParser.JsonExtractContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#JsonExtract.
    def exitJsonExtract(self, ctx:TeradataSQLDMLParser.JsonExtractContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#MultDiv.
    def enterMultDiv(self, ctx:TeradataSQLDMLParser.MultDivContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#MultDiv.
    def exitMultDiv(self, ctx:TeradataSQLDMLParser.MultDivContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#PeriodIntersect.
    def enterPeriodIntersect(self, ctx:TeradataSQLDMLParser.PeriodIntersectContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#PeriodIntersect.
    def exitPeriodIntersect(self, ctx:TeradataSQLDMLParser.PeriodIntersectContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#IntervalExprParenthesized.
    def enterIntervalExprParenthesized(self, ctx:TeradataSQLDMLParser.IntervalExprParenthesizedContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#IntervalExprParenthesized.
    def exitIntervalExprParenthesized(self, ctx:TeradataSQLDMLParser.IntervalExprParenthesizedContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#JsonRecursiveDescendAllArrayElements.
    def enterJsonRecursiveDescendAllArrayElements(self, ctx:TeradataSQLDMLParser.JsonRecursiveDescendAllArrayElementsContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#JsonRecursiveDescendAllArrayElements.
    def exitJsonRecursiveDescendAllArrayElements(self, ctx:TeradataSQLDMLParser.JsonRecursiveDescendAllArrayElementsContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#UnaryPlusMinus.
    def enterUnaryPlusMinus(self, ctx:TeradataSQLDMLParser.UnaryPlusMinusContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#UnaryPlusMinus.
    def exitUnaryPlusMinus(self, ctx:TeradataSQLDMLParser.UnaryPlusMinusContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#Concatenation.
    def enterConcatenation(self, ctx:TeradataSQLDMLParser.ConcatenationContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#Concatenation.
    def exitConcatenation(self, ctx:TeradataSQLDMLParser.ConcatenationContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#PeriodDiff.
    def enterPeriodDiff(self, ctx:TeradataSQLDMLParser.PeriodDiffContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#PeriodDiff.
    def exitPeriodDiff(self, ctx:TeradataSQLDMLParser.PeriodDiffContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#ArrayOmethodWithoudArgs.
    def enterArrayOmethodWithoudArgs(self, ctx:TeradataSQLDMLParser.ArrayOmethodWithoudArgsContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#ArrayOmethodWithoudArgs.
    def exitArrayOmethodWithoudArgs(self, ctx:TeradataSQLDMLParser.ArrayOmethodWithoudArgsContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#PartitioningExpr.
    def enterPartitioningExpr(self, ctx:TeradataSQLDMLParser.PartitioningExprContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#PartitioningExpr.
    def exitPartitioningExpr(self, ctx:TeradataSQLDMLParser.PartitioningExprContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#XMLExistNode.
    def enterXMLExistNode(self, ctx:TeradataSQLDMLParser.XMLExistNodeContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#XMLExistNode.
    def exitXMLExistNode(self, ctx:TeradataSQLDMLParser.XMLExistNodeContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#JsonRecursiveDescendArrayElementReference.
    def enterJsonRecursiveDescendArrayElementReference(self, ctx:TeradataSQLDMLParser.JsonRecursiveDescendArrayElementReferenceContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#JsonRecursiveDescendArrayElementReference.
    def exitJsonRecursiveDescendArrayElementReference(self, ctx:TeradataSQLDMLParser.JsonRecursiveDescendArrayElementReferenceContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#DataTypeConversion.
    def enterDataTypeConversion(self, ctx:TeradataSQLDMLParser.DataTypeConversionContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#DataTypeConversion.
    def exitDataTypeConversion(self, ctx:TeradataSQLDMLParser.DataTypeConversionContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#JsonRecursiveDescendObjectMember.
    def enterJsonRecursiveDescendObjectMember(self, ctx:TeradataSQLDMLParser.JsonRecursiveDescendObjectMemberContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#JsonRecursiveDescendObjectMember.
    def exitJsonRecursiveDescendObjectMember(self, ctx:TeradataSQLDMLParser.JsonRecursiveDescendObjectMemberContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#IntervalExpr.
    def enterIntervalExpr(self, ctx:TeradataSQLDMLParser.IntervalExprContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#IntervalExpr.
    def exitIntervalExpr(self, ctx:TeradataSQLDMLParser.IntervalExprContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#Exponentiation.
    def enterExponentiation(self, ctx:TeradataSQLDMLParser.ExponentiationContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#Exponentiation.
    def exitExponentiation(self, ctx:TeradataSQLDMLParser.ExponentiationContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#XMLIsSchemaValidated.
    def enterXMLIsSchemaValidated(self, ctx:TeradataSQLDMLParser.XMLIsSchemaValidatedContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#XMLIsSchemaValidated.
    def exitXMLIsSchemaValidated(self, ctx:TeradataSQLDMLParser.XMLIsSchemaValidatedContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#JSONConstructor.
    def enterJSONConstructor(self, ctx:TeradataSQLDMLParser.JSONConstructorContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#JSONConstructor.
    def exitJSONConstructor(self, ctx:TeradataSQLDMLParser.JSONConstructorContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#JsonSlice.
    def enterJsonSlice(self, ctx:TeradataSQLDMLParser.JsonSliceContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#JsonSlice.
    def exitJsonSlice(self, ctx:TeradataSQLDMLParser.JsonSliceContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#XMLIsSchemaValid.
    def enterXMLIsSchemaValid(self, ctx:TeradataSQLDMLParser.XMLIsSchemaValidContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#XMLIsSchemaValid.
    def exitXMLIsSchemaValid(self, ctx:TeradataSQLDMLParser.XMLIsSchemaValidContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#ArrayAggregation.
    def enterArrayAggregation(self, ctx:TeradataSQLDMLParser.ArrayAggregationContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#ArrayAggregation.
    def exitArrayAggregation(self, ctx:TeradataSQLDMLParser.ArrayAggregationContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#ArrayUpdateStride.
    def enterArrayUpdateStride(self, ctx:TeradataSQLDMLParser.ArrayUpdateStrideContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#ArrayUpdateStride.
    def exitArrayUpdateStride(self, ctx:TeradataSQLDMLParser.ArrayUpdateStrideContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#LiteralExpr.
    def enterLiteralExpr(self, ctx:TeradataSQLDMLParser.LiteralExprContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#LiteralExpr.
    def exitLiteralExpr(self, ctx:TeradataSQLDMLParser.LiteralExprContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#ArrayOmethodWithArg.
    def enterArrayOmethodWithArg(self, ctx:TeradataSQLDMLParser.ArrayOmethodWithArgContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#ArrayOmethodWithArg.
    def exitArrayOmethodWithArg(self, ctx:TeradataSQLDMLParser.ArrayOmethodWithArgContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#JsonRecursiveDescendAllObjectMembers.
    def enterJsonRecursiveDescendAllObjectMembers(self, ctx:TeradataSQLDMLParser.JsonRecursiveDescendAllObjectMembersContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#JsonRecursiveDescendAllObjectMembers.
    def exitJsonRecursiveDescendAllObjectMembers(self, ctx:TeradataSQLDMLParser.JsonRecursiveDescendAllObjectMembersContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#XMLCreateNonSchemaBasedXML.
    def enterXMLCreateNonSchemaBasedXML(self, ctx:TeradataSQLDMLParser.XMLCreateNonSchemaBasedXMLContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#XMLCreateNonSchemaBasedXML.
    def exitXMLCreateNonSchemaBasedXML(self, ctx:TeradataSQLDMLParser.XMLCreateNonSchemaBasedXMLContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#VariableReference.
    def enterVariableReference(self, ctx:TeradataSQLDMLParser.VariableReferenceContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#VariableReference.
    def exitVariableReference(self, ctx:TeradataSQLDMLParser.VariableReferenceContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#AddSub.
    def enterAddSub(self, ctx:TeradataSQLDMLParser.AddSubContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#AddSub.
    def exitAddSub(self, ctx:TeradataSQLDMLParser.AddSubContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#JsonObjectMember.
    def enterJsonObjectMember(self, ctx:TeradataSQLDMLParser.JsonObjectMemberContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#JsonObjectMember.
    def exitJsonObjectMember(self, ctx:TeradataSQLDMLParser.JsonObjectMemberContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#JsonAllElements.
    def enterJsonAllElements(self, ctx:TeradataSQLDMLParser.JsonAllElementsContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#JsonAllElements.
    def exitJsonAllElements(self, ctx:TeradataSQLDMLParser.JsonAllElementsContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#ArrayOextend.
    def enterArrayOextend(self, ctx:TeradataSQLDMLParser.ArrayOextendContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#ArrayOextend.
    def exitArrayOextend(self, ctx:TeradataSQLDMLParser.ArrayOextendContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#ArrayArithmetic.
    def enterArrayArithmetic(self, ctx:TeradataSQLDMLParser.ArrayArithmeticContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#ArrayArithmetic.
    def exitArrayArithmetic(self, ctx:TeradataSQLDMLParser.ArrayArithmeticContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#UDTConstructor.
    def enterUDTConstructor(self, ctx:TeradataSQLDMLParser.UDTConstructorContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#UDTConstructor.
    def exitUDTConstructor(self, ctx:TeradataSQLDMLParser.UDTConstructorContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#XMLTransform.
    def enterXMLTransform(self, ctx:TeradataSQLDMLParser.XMLTransformContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#XMLTransform.
    def exitXMLTransform(self, ctx:TeradataSQLDMLParser.XMLTransformContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#DateTimeExpr.
    def enterDateTimeExpr(self, ctx:TeradataSQLDMLParser.DateTimeExprContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#DateTimeExpr.
    def exitDateTimeExpr(self, ctx:TeradataSQLDMLParser.DateTimeExprContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#ColumnName.
    def enterColumnName(self, ctx:TeradataSQLDMLParser.ColumnNameContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#ColumnName.
    def exitColumnName(self, ctx:TeradataSQLDMLParser.ColumnNameContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#ArrayOtrim.
    def enterArrayOtrim(self, ctx:TeradataSQLDMLParser.ArrayOtrimContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#ArrayOtrim.
    def exitArrayOtrim(self, ctx:TeradataSQLDMLParser.ArrayOtrimContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#CursorVariableReference.
    def enterCursorVariableReference(self, ctx:TeradataSQLDMLParser.CursorVariableReferenceContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#CursorVariableReference.
    def exitCursorVariableReference(self, ctx:TeradataSQLDMLParser.CursorVariableReferenceContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#Parenthesized.
    def enterParenthesized(self, ctx:TeradataSQLDMLParser.ParenthesizedContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#Parenthesized.
    def exitParenthesized(self, ctx:TeradataSQLDMLParser.ParenthesizedContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#JsonAsBsonText.
    def enterJsonAsBsonText(self, ctx:TeradataSQLDMLParser.JsonAsBsonTextContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#JsonAsBsonText.
    def exitJsonAsBsonText(self, ctx:TeradataSQLDMLParser.JsonAsBsonTextContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#AttributeModification.
    def enterAttributeModification(self, ctx:TeradataSQLDMLParser.AttributeModificationContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#AttributeModification.
    def exitAttributeModification(self, ctx:TeradataSQLDMLParser.AttributeModificationContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#JsonCombine.
    def enterJsonCombine(self, ctx:TeradataSQLDMLParser.JsonCombineContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#JsonCombine.
    def exitJsonCombine(self, ctx:TeradataSQLDMLParser.JsonCombineContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#XMLIsDocument.
    def enterXMLIsDocument(self, ctx:TeradataSQLDMLParser.XMLIsDocumentContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#XMLIsDocument.
    def exitXMLIsDocument(self, ctx:TeradataSQLDMLParser.XMLIsDocumentContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#MacroParameterReference.
    def enterMacroParameterReference(self, ctx:TeradataSQLDMLParser.MacroParameterReferenceContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#MacroParameterReference.
    def exitMacroParameterReference(self, ctx:TeradataSQLDMLParser.MacroParameterReferenceContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#XMLIsContent.
    def enterXMLIsContent(self, ctx:TeradataSQLDMLParser.XMLIsContentContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#XMLIsContent.
    def exitXMLIsContent(self, ctx:TeradataSQLDMLParser.XMLIsContentContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#ArrayElementReference.
    def enterArrayElementReference(self, ctx:TeradataSQLDMLParser.ArrayElementReferenceContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#ArrayElementReference.
    def exitArrayElementReference(self, ctx:TeradataSQLDMLParser.ArrayElementReferenceContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#ArrayCardinality.
    def enterArrayCardinality(self, ctx:TeradataSQLDMLParser.ArrayCardinalityContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#ArrayCardinality.
    def exitArrayCardinality(self, ctx:TeradataSQLDMLParser.ArrayCardinalityContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#CaseExpr.
    def enterCaseExpr(self, ctx:TeradataSQLDMLParser.CaseExprContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#CaseExpr.
    def exitCaseExpr(self, ctx:TeradataSQLDMLParser.CaseExprContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#JsonKeycount.
    def enterJsonKeycount(self, ctx:TeradataSQLDMLParser.JsonKeycountContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#JsonKeycount.
    def exitJsonKeycount(self, ctx:TeradataSQLDMLParser.JsonKeycountContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#JsonAllObjectMembers.
    def enterJsonAllObjectMembers(self, ctx:TeradataSQLDMLParser.JsonAllObjectMembersContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#JsonAllObjectMembers.
    def exitJsonAllObjectMembers(self, ctx:TeradataSQLDMLParser.JsonAllObjectMembersContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#tuple.
    def enterTuple(self, ctx:TeradataSQLDMLParser.TupleContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#tuple.
    def exitTuple(self, ctx:TeradataSQLDMLParser.TupleContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#tuple_attribute.
    def enterTuple_attribute(self, ctx:TeradataSQLDMLParser.Tuple_attributeContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#tuple_attribute.
    def exitTuple_attribute(self, ctx:TeradataSQLDMLParser.Tuple_attributeContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#case_expr.
    def enterCase_expr(self, ctx:TeradataSQLDMLParser.Case_exprContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#case_expr.
    def exitCase_expr(self, ctx:TeradataSQLDMLParser.Case_exprContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#valued_case_expr.
    def enterValued_case_expr(self, ctx:TeradataSQLDMLParser.Valued_case_exprContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#valued_case_expr.
    def exitValued_case_expr(self, ctx:TeradataSQLDMLParser.Valued_case_exprContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#searched_case_expr.
    def enterSearched_case_expr(self, ctx:TeradataSQLDMLParser.Searched_case_exprContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#searched_case_expr.
    def exitSearched_case_expr(self, ctx:TeradataSQLDMLParser.Searched_case_exprContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#coalesce_expr.
    def enterCoalesce_expr(self, ctx:TeradataSQLDMLParser.Coalesce_exprContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#coalesce_expr.
    def exitCoalesce_expr(self, ctx:TeradataSQLDMLParser.Coalesce_exprContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#nullif_expr.
    def enterNullif_expr(self, ctx:TeradataSQLDMLParser.Nullif_exprContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#nullif_expr.
    def exitNullif_expr(self, ctx:TeradataSQLDMLParser.Nullif_exprContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#interval_expr_base.
    def enterInterval_expr_base(self, ctx:TeradataSQLDMLParser.Interval_expr_baseContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#interval_expr_base.
    def exitInterval_expr_base(self, ctx:TeradataSQLDMLParser.Interval_expr_baseContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#interval_expr_parenthesized.
    def enterInterval_expr_parenthesized(self, ctx:TeradataSQLDMLParser.Interval_expr_parenthesizedContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#interval_expr_parenthesized.
    def exitInterval_expr_parenthesized(self, ctx:TeradataSQLDMLParser.Interval_expr_parenthesizedContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#interval_expr_start_end_phrase.
    def enterInterval_expr_start_end_phrase(self, ctx:TeradataSQLDMLParser.Interval_expr_start_end_phraseContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#interval_expr_start_end_phrase.
    def exitInterval_expr_start_end_phrase(self, ctx:TeradataSQLDMLParser.Interval_expr_start_end_phraseContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#function_invocation.
    def enterFunction_invocation(self, ctx:TeradataSQLDMLParser.Function_invocationContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#function_invocation.
    def exitFunction_invocation(self, ctx:TeradataSQLDMLParser.Function_invocationContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#AggOneArg.
    def enterAggOneArg(self, ctx:TeradataSQLDMLParser.AggOneArgContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#AggOneArg.
    def exitAggOneArg(self, ctx:TeradataSQLDMLParser.AggOneArgContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#AggTwoArgs.
    def enterAggTwoArgs(self, ctx:TeradataSQLDMLParser.AggTwoArgsContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#AggTwoArgs.
    def exitAggTwoArgs(self, ctx:TeradataSQLDMLParser.AggTwoArgsContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#AggCount.
    def enterAggCount(self, ctx:TeradataSQLDMLParser.AggCountContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#AggCount.
    def exitAggCount(self, ctx:TeradataSQLDMLParser.AggCountContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#Grouping.
    def enterGrouping(self, ctx:TeradataSQLDMLParser.GroupingContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#Grouping.
    def exitGrouping(self, ctx:TeradataSQLDMLParser.GroupingContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#ListAgg.
    def enterListAgg(self, ctx:TeradataSQLDMLParser.ListAggContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#ListAgg.
    def exitListAgg(self, ctx:TeradataSQLDMLParser.ListAggContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#analytic_function.
    def enterAnalytic_function(self, ctx:TeradataSQLDMLParser.Analytic_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#analytic_function.
    def exitAnalytic_function(self, ctx:TeradataSQLDMLParser.Analytic_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#arithmetic_function.
    def enterArithmetic_function(self, ctx:TeradataSQLDMLParser.Arithmetic_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#arithmetic_function.
    def exitArithmetic_function(self, ctx:TeradataSQLDMLParser.Arithmetic_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#array_function.
    def enterArray_function(self, ctx:TeradataSQLDMLParser.Array_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#array_function.
    def exitArray_function(self, ctx:TeradataSQLDMLParser.Array_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#attribute_function.
    def enterAttribute_function(self, ctx:TeradataSQLDMLParser.Attribute_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#attribute_function.
    def exitAttribute_function(self, ctx:TeradataSQLDMLParser.Attribute_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#byte_function.
    def enterByte_function(self, ctx:TeradataSQLDMLParser.Byte_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#byte_function.
    def exitByte_function(self, ctx:TeradataSQLDMLParser.Byte_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#builtin_function.
    def enterBuiltin_function(self, ctx:TeradataSQLDMLParser.Builtin_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#builtin_function.
    def exitBuiltin_function(self, ctx:TeradataSQLDMLParser.Builtin_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#calendar_function.
    def enterCalendar_function(self, ctx:TeradataSQLDMLParser.Calendar_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#calendar_function.
    def exitCalendar_function(self, ctx:TeradataSQLDMLParser.Calendar_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#comparison_function.
    def enterComparison_function(self, ctx:TeradataSQLDMLParser.Comparison_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#comparison_function.
    def exitComparison_function(self, ctx:TeradataSQLDMLParser.Comparison_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#compression_function.
    def enterCompression_function(self, ctx:TeradataSQLDMLParser.Compression_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#compression_function.
    def exitCompression_function(self, ctx:TeradataSQLDMLParser.Compression_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#conversion_function.
    def enterConversion_function(self, ctx:TeradataSQLDMLParser.Conversion_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#conversion_function.
    def exitConversion_function(self, ctx:TeradataSQLDMLParser.Conversion_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#date_function.
    def enterDate_function(self, ctx:TeradataSQLDMLParser.Date_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#date_function.
    def exitDate_function(self, ctx:TeradataSQLDMLParser.Date_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#hash_function.
    def enterHash_function(self, ctx:TeradataSQLDMLParser.Hash_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#hash_function.
    def exitHash_function(self, ctx:TeradataSQLDMLParser.Hash_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#lob_function.
    def enterLob_function(self, ctx:TeradataSQLDMLParser.Lob_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#lob_function.
    def exitLob_function(self, ctx:TeradataSQLDMLParser.Lob_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#map_function.
    def enterMap_function(self, ctx:TeradataSQLDMLParser.Map_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#map_function.
    def exitMap_function(self, ctx:TeradataSQLDMLParser.Map_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#nvl_funtion.
    def enterNvl_funtion(self, ctx:TeradataSQLDMLParser.Nvl_funtionContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#nvl_funtion.
    def exitNvl_funtion(self, ctx:TeradataSQLDMLParser.Nvl_funtionContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#period_function.
    def enterPeriod_function(self, ctx:TeradataSQLDMLParser.Period_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#period_function.
    def exitPeriod_function(self, ctx:TeradataSQLDMLParser.Period_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#regexp_function.
    def enterRegexp_function(self, ctx:TeradataSQLDMLParser.Regexp_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#regexp_function.
    def exitRegexp_function(self, ctx:TeradataSQLDMLParser.Regexp_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#string_function.
    def enterString_function(self, ctx:TeradataSQLDMLParser.String_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#string_function.
    def exitString_function(self, ctx:TeradataSQLDMLParser.String_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#json_function.
    def enterJson_function(self, ctx:TeradataSQLDMLParser.Json_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#json_function.
    def exitJson_function(self, ctx:TeradataSQLDMLParser.Json_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#xml_function.
    def enterXml_function(self, ctx:TeradataSQLDMLParser.Xml_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#xml_function.
    def exitXml_function(self, ctx:TeradataSQLDMLParser.Xml_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#other_function.
    def enterOther_function(self, ctx:TeradataSQLDMLParser.Other_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#other_function.
    def exitOther_function(self, ctx:TeradataSQLDMLParser.Other_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#partitioning_expr.
    def enterPartitioning_expr(self, ctx:TeradataSQLDMLParser.Partitioning_exprContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#partitioning_expr.
    def exitPartitioning_expr(self, ctx:TeradataSQLDMLParser.Partitioning_exprContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#td_sysfnlib.
    def enterTd_sysfnlib(self, ctx:TeradataSQLDMLParser.Td_sysfnlibContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#td_sysfnlib.
    def exitTd_sysfnlib(self, ctx:TeradataSQLDMLParser.Td_sysfnlibContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#td_sysxml.
    def enterTd_sysxml(self, ctx:TeradataSQLDMLParser.Td_sysxmlContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#td_sysxml.
    def exitTd_sysxml(self, ctx:TeradataSQLDMLParser.Td_sysxmlContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#syslib.
    def enterSyslib(self, ctx:TeradataSQLDMLParser.SyslibContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#syslib.
    def exitSyslib(self, ctx:TeradataSQLDMLParser.SyslibContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#td_server_db.
    def enterTd_server_db(self, ctx:TeradataSQLDMLParser.Td_server_dbContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#td_server_db.
    def exitTd_server_db(self, ctx:TeradataSQLDMLParser.Td_server_dbContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#translation_mapping.
    def enterTranslation_mapping(self, ctx:TeradataSQLDMLParser.Translation_mappingContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#translation_mapping.
    def exitTranslation_mapping(self, ctx:TeradataSQLDMLParser.Translation_mappingContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#attribute_modification.
    def enterAttribute_modification(self, ctx:TeradataSQLDMLParser.Attribute_modificationContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#attribute_modification.
    def exitAttribute_modification(self, ctx:TeradataSQLDMLParser.Attribute_modificationContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#returns_clause.
    def enterReturns_clause(self, ctx:TeradataSQLDMLParser.Returns_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#returns_clause.
    def exitReturns_clause(self, ctx:TeradataSQLDMLParser.Returns_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#attribute_modification_option.
    def enterAttribute_modification_option(self, ctx:TeradataSQLDMLParser.Attribute_modification_optionContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#attribute_modification_option.
    def exitAttribute_modification_option(self, ctx:TeradataSQLDMLParser.Attribute_modification_optionContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#teradata_type_conversion.
    def enterTeradata_type_conversion(self, ctx:TeradataSQLDMLParser.Teradata_type_conversionContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#teradata_type_conversion.
    def exitTeradata_type_conversion(self, ctx:TeradataSQLDMLParser.Teradata_type_conversionContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#teradata_type_conversion_data_attribute.
    def enterTeradata_type_conversion_data_attribute(self, ctx:TeradataSQLDMLParser.Teradata_type_conversion_data_attributeContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#teradata_type_conversion_data_attribute.
    def exitTeradata_type_conversion_data_attribute(self, ctx:TeradataSQLDMLParser.Teradata_type_conversion_data_attributeContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#case_spec.
    def enterCase_spec(self, ctx:TeradataSQLDMLParser.Case_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#case_spec.
    def exitCase_spec(self, ctx:TeradataSQLDMLParser.Case_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#range_expr.
    def enterRange_expr(self, ctx:TeradataSQLDMLParser.Range_exprContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#range_expr.
    def exitRange_expr(self, ctx:TeradataSQLDMLParser.Range_exprContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#range_list.
    def enterRange_list(self, ctx:TeradataSQLDMLParser.Range_listContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#range_list.
    def exitRange_list(self, ctx:TeradataSQLDMLParser.Range_listContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#range_expr_1.
    def enterRange_expr_1(self, ctx:TeradataSQLDMLParser.Range_expr_1Context):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#range_expr_1.
    def exitRange_expr_1(self, ctx:TeradataSQLDMLParser.Range_expr_1Context):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#range_expr_2.
    def enterRange_expr_2(self, ctx:TeradataSQLDMLParser.Range_expr_2Context):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#range_expr_2.
    def exitRange_expr_2(self, ctx:TeradataSQLDMLParser.Range_expr_2Context):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#range_expr_3.
    def enterRange_expr_3(self, ctx:TeradataSQLDMLParser.Range_expr_3Context):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#range_expr_3.
    def exitRange_expr_3(self, ctx:TeradataSQLDMLParser.Range_expr_3Context):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#range_spec.
    def enterRange_spec(self, ctx:TeradataSQLDMLParser.Range_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#range_spec.
    def exitRange_spec(self, ctx:TeradataSQLDMLParser.Range_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#hash_bucket_number_expr.
    def enterHash_bucket_number_expr(self, ctx:TeradataSQLDMLParser.Hash_bucket_number_exprContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#hash_bucket_number_expr.
    def exitHash_bucket_number_expr(self, ctx:TeradataSQLDMLParser.Hash_bucket_number_exprContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#window_spec.
    def enterWindow_spec(self, ctx:TeradataSQLDMLParser.Window_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#window_spec.
    def exitWindow_spec(self, ctx:TeradataSQLDMLParser.Window_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#window_spec_without_rows.
    def enterWindow_spec_without_rows(self, ctx:TeradataSQLDMLParser.Window_spec_without_rowsContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#window_spec_without_rows.
    def exitWindow_spec_without_rows(self, ctx:TeradataSQLDMLParser.Window_spec_without_rowsContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#window_spec_with_ties.
    def enterWindow_spec_with_ties(self, ctx:TeradataSQLDMLParser.Window_spec_with_tiesContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#window_spec_with_ties.
    def exitWindow_spec_with_ties(self, ctx:TeradataSQLDMLParser.Window_spec_with_tiesContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#window_partition_by.
    def enterWindow_partition_by(self, ctx:TeradataSQLDMLParser.Window_partition_byContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#window_partition_by.
    def exitWindow_partition_by(self, ctx:TeradataSQLDMLParser.Window_partition_byContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#window_order_by.
    def enterWindow_order_by(self, ctx:TeradataSQLDMLParser.Window_order_byContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#window_order_by.
    def exitWindow_order_by(self, ctx:TeradataSQLDMLParser.Window_order_byContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#window_rows.
    def enterWindow_rows(self, ctx:TeradataSQLDMLParser.Window_rowsContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#window_rows.
    def exitWindow_rows(self, ctx:TeradataSQLDMLParser.Window_rowsContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#json_param_spec.
    def enterJson_param_spec(self, ctx:TeradataSQLDMLParser.Json_param_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#json_param_spec.
    def exitJson_param_spec(self, ctx:TeradataSQLDMLParser.Json_param_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#xml_query_argument.
    def enterXml_query_argument(self, ctx:TeradataSQLDMLParser.Xml_query_argumentContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#xml_query_argument.
    def exitXml_query_argument(self, ctx:TeradataSQLDMLParser.Xml_query_argumentContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#xml_query_variable_spec.
    def enterXml_query_variable_spec(self, ctx:TeradataSQLDMLParser.Xml_query_variable_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#xml_query_variable_spec.
    def exitXml_query_variable_spec(self, ctx:TeradataSQLDMLParser.Xml_query_variable_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#xml_attribute_declaration.
    def enterXml_attribute_declaration(self, ctx:TeradataSQLDMLParser.Xml_attribute_declarationContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#xml_attribute_declaration.
    def exitXml_attribute_declaration(self, ctx:TeradataSQLDMLParser.Xml_attribute_declarationContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#xml_attribute_spec.
    def enterXml_attribute_spec(self, ctx:TeradataSQLDMLParser.Xml_attribute_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#xml_attribute_spec.
    def exitXml_attribute_spec(self, ctx:TeradataSQLDMLParser.Xml_attribute_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#xml_forest_element_spec.
    def enterXml_forest_element_spec(self, ctx:TeradataSQLDMLParser.Xml_forest_element_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#xml_forest_element_spec.
    def exitXml_forest_element_spec(self, ctx:TeradataSQLDMLParser.Xml_forest_element_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#xml_value_declaration.
    def enterXml_value_declaration(self, ctx:TeradataSQLDMLParser.Xml_value_declarationContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#xml_value_declaration.
    def exitXml_value_declaration(self, ctx:TeradataSQLDMLParser.Xml_value_declarationContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#xml_namespace_declaration.
    def enterXml_namespace_declaration(self, ctx:TeradataSQLDMLParser.Xml_namespace_declarationContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#xml_namespace_declaration.
    def exitXml_namespace_declaration(self, ctx:TeradataSQLDMLParser.Xml_namespace_declarationContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#xml_namespace_spec.
    def enterXml_namespace_spec(self, ctx:TeradataSQLDMLParser.Xml_namespace_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#xml_namespace_spec.
    def exitXml_namespace_spec(self, ctx:TeradataSQLDMLParser.Xml_namespace_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#xml_columns_spec.
    def enterXml_columns_spec(self, ctx:TeradataSQLDMLParser.Xml_columns_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#xml_columns_spec.
    def exitXml_columns_spec(self, ctx:TeradataSQLDMLParser.Xml_columns_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#xml_regular_column_definition.
    def enterXml_regular_column_definition(self, ctx:TeradataSQLDMLParser.Xml_regular_column_definitionContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#xml_regular_column_definition.
    def exitXml_regular_column_definition(self, ctx:TeradataSQLDMLParser.Xml_regular_column_definitionContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#xml_encoding.
    def enterXml_encoding(self, ctx:TeradataSQLDMLParser.Xml_encodingContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#xml_encoding.
    def exitXml_encoding(self, ctx:TeradataSQLDMLParser.Xml_encodingContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#xml_query_on_empty.
    def enterXml_query_on_empty(self, ctx:TeradataSQLDMLParser.Xml_query_on_emptyContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#xml_query_on_empty.
    def exitXml_query_on_empty(self, ctx:TeradataSQLDMLParser.Xml_query_on_emptyContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#xml_returning_spec.
    def enterXml_returning_spec(self, ctx:TeradataSQLDMLParser.Xml_returning_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#xml_returning_spec.
    def exitXml_returning_spec(self, ctx:TeradataSQLDMLParser.Xml_returning_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#xml_content_option_spec.
    def enterXml_content_option_spec(self, ctx:TeradataSQLDMLParser.Xml_content_option_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#xml_content_option_spec.
    def exitXml_content_option_spec(self, ctx:TeradataSQLDMLParser.Xml_content_option_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#ignore_respect_nulls.
    def enterIgnore_respect_nulls(self, ctx:TeradataSQLDMLParser.Ignore_respect_nullsContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#ignore_respect_nulls.
    def exitIgnore_respect_nulls(self, ctx:TeradataSQLDMLParser.Ignore_respect_nullsContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#number_of_rows.
    def enterNumber_of_rows(self, ctx:TeradataSQLDMLParser.Number_of_rowsContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#number_of_rows.
    def exitNumber_of_rows(self, ctx:TeradataSQLDMLParser.Number_of_rowsContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#with_ties.
    def enterWith_ties(self, ctx:TeradataSQLDMLParser.With_tiesContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#with_ties.
    def exitWith_ties(self, ctx:TeradataSQLDMLParser.With_tiesContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#pivot.
    def enterPivot(self, ctx:TeradataSQLDMLParser.PivotContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#pivot.
    def exitPivot(self, ctx:TeradataSQLDMLParser.PivotContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#pivot_spec.
    def enterPivot_spec(self, ctx:TeradataSQLDMLParser.Pivot_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#pivot_spec.
    def exitPivot_spec(self, ctx:TeradataSQLDMLParser.Pivot_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#pivot_with_phrase.
    def enterPivot_with_phrase(self, ctx:TeradataSQLDMLParser.Pivot_with_phraseContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#pivot_with_phrase.
    def exitPivot_with_phrase(self, ctx:TeradataSQLDMLParser.Pivot_with_phraseContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#pivot_agg_func_spec.
    def enterPivot_agg_func_spec(self, ctx:TeradataSQLDMLParser.Pivot_agg_func_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#pivot_agg_func_spec.
    def exitPivot_agg_func_spec(self, ctx:TeradataSQLDMLParser.Pivot_agg_func_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#pivot_for_phrase.
    def enterPivot_for_phrase(self, ctx:TeradataSQLDMLParser.Pivot_for_phraseContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#pivot_for_phrase.
    def exitPivot_for_phrase(self, ctx:TeradataSQLDMLParser.Pivot_for_phraseContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#pivot_with_spec.
    def enterPivot_with_spec(self, ctx:TeradataSQLDMLParser.Pivot_with_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#pivot_with_spec.
    def exitPivot_with_spec(self, ctx:TeradataSQLDMLParser.Pivot_with_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#pivot_expr_spec_scalar.
    def enterPivot_expr_spec_scalar(self, ctx:TeradataSQLDMLParser.Pivot_expr_spec_scalarContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#pivot_expr_spec_scalar.
    def exitPivot_expr_spec_scalar(self, ctx:TeradataSQLDMLParser.Pivot_expr_spec_scalarContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#pivot_expr_spec_list.
    def enterPivot_expr_spec_list(self, ctx:TeradataSQLDMLParser.Pivot_expr_spec_listContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#pivot_expr_spec_list.
    def exitPivot_expr_spec_list(self, ctx:TeradataSQLDMLParser.Pivot_expr_spec_listContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#unpivot.
    def enterUnpivot(self, ctx:TeradataSQLDMLParser.UnpivotContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#unpivot.
    def exitUnpivot(self, ctx:TeradataSQLDMLParser.UnpivotContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#unpivot_spec.
    def enterUnpivot_spec(self, ctx:TeradataSQLDMLParser.Unpivot_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#unpivot_spec.
    def exitUnpivot_spec(self, ctx:TeradataSQLDMLParser.Unpivot_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#unpivot_column_name_spec_single.
    def enterUnpivot_column_name_spec_single(self, ctx:TeradataSQLDMLParser.Unpivot_column_name_spec_singleContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#unpivot_column_name_spec_single.
    def exitUnpivot_column_name_spec_single(self, ctx:TeradataSQLDMLParser.Unpivot_column_name_spec_singleContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#unpivot_column_name_spec_list.
    def enterUnpivot_column_name_spec_list(self, ctx:TeradataSQLDMLParser.Unpivot_column_name_spec_listContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#unpivot_column_name_spec_list.
    def exitUnpivot_column_name_spec_list(self, ctx:TeradataSQLDMLParser.Unpivot_column_name_spec_listContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#at_timezone.
    def enterAt_timezone(self, ctx:TeradataSQLDMLParser.At_timezoneContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#at_timezone.
    def exitAt_timezone(self, ctx:TeradataSQLDMLParser.At_timezoneContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#elements_list.
    def enterElements_list(self, ctx:TeradataSQLDMLParser.Elements_listContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#elements_list.
    def exitElements_list(self, ctx:TeradataSQLDMLParser.Elements_listContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#scalar_expr_list.
    def enterScalar_expr_list(self, ctx:TeradataSQLDMLParser.Scalar_expr_listContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#scalar_expr_list.
    def exitScalar_expr_list(self, ctx:TeradataSQLDMLParser.Scalar_expr_listContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#scalar_expr_list_comma_separated.
    def enterScalar_expr_list_comma_separated(self, ctx:TeradataSQLDMLParser.Scalar_expr_list_comma_separatedContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#scalar_expr_list_comma_separated.
    def exitScalar_expr_list_comma_separated(self, ctx:TeradataSQLDMLParser.Scalar_expr_list_comma_separatedContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#column_list.
    def enterColumn_list(self, ctx:TeradataSQLDMLParser.Column_listContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#column_list.
    def exitColumn_list(self, ctx:TeradataSQLDMLParser.Column_listContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#subquery.
    def enterSubquery(self, ctx:TeradataSQLDMLParser.SubqueryContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#subquery.
    def exitSubquery(self, ctx:TeradataSQLDMLParser.SubqueryContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#column_spec.
    def enterColumn_spec(self, ctx:TeradataSQLDMLParser.Column_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#column_spec.
    def exitColumn_spec(self, ctx:TeradataSQLDMLParser.Column_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#variable_reference.
    def enterVariable_reference(self, ctx:TeradataSQLDMLParser.Variable_referenceContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#variable_reference.
    def exitVariable_reference(self, ctx:TeradataSQLDMLParser.Variable_referenceContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#cursor_variable_reference.
    def enterCursor_variable_reference(self, ctx:TeradataSQLDMLParser.Cursor_variable_referenceContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#cursor_variable_reference.
    def exitCursor_variable_reference(self, ctx:TeradataSQLDMLParser.Cursor_variable_referenceContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#macro_parameter_reference.
    def enterMacro_parameter_reference(self, ctx:TeradataSQLDMLParser.Macro_parameter_referenceContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#macro_parameter_reference.
    def exitMacro_parameter_reference(self, ctx:TeradataSQLDMLParser.Macro_parameter_referenceContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#array_scope_reference.
    def enterArray_scope_reference(self, ctx:TeradataSQLDMLParser.Array_scope_referenceContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#array_scope_reference.
    def exitArray_scope_reference(self, ctx:TeradataSQLDMLParser.Array_scope_referenceContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#comparison_operator.
    def enterComparison_operator(self, ctx:TeradataSQLDMLParser.Comparison_operatorContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#comparison_operator.
    def exitComparison_operator(self, ctx:TeradataSQLDMLParser.Comparison_operatorContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#quantifier.
    def enterQuantifier(self, ctx:TeradataSQLDMLParser.QuantifierContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#quantifier.
    def exitQuantifier(self, ctx:TeradataSQLDMLParser.QuantifierContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#request_modifier.
    def enterRequest_modifier(self, ctx:TeradataSQLDMLParser.Request_modifierContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#request_modifier.
    def exitRequest_modifier(self, ctx:TeradataSQLDMLParser.Request_modifierContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#locking_request_modifier.
    def enterLocking_request_modifier(self, ctx:TeradataSQLDMLParser.Locking_request_modifierContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#locking_request_modifier.
    def exitLocking_request_modifier(self, ctx:TeradataSQLDMLParser.Locking_request_modifierContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#locking_spec.
    def enterLocking_spec(self, ctx:TeradataSQLDMLParser.Locking_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#locking_spec.
    def exitLocking_spec(self, ctx:TeradataSQLDMLParser.Locking_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#lock_type.
    def enterLock_type(self, ctx:TeradataSQLDMLParser.Lock_typeContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#lock_type.
    def exitLock_type(self, ctx:TeradataSQLDMLParser.Lock_typeContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#with_request_modifier.
    def enterWith_request_modifier(self, ctx:TeradataSQLDMLParser.With_request_modifierContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#with_request_modifier.
    def exitWith_request_modifier(self, ctx:TeradataSQLDMLParser.With_request_modifierContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#cte_spec.
    def enterCte_spec(self, ctx:TeradataSQLDMLParser.Cte_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#cte_spec.
    def exitCte_spec(self, ctx:TeradataSQLDMLParser.Cte_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#regular_cte_spec.
    def enterRegular_cte_spec(self, ctx:TeradataSQLDMLParser.Regular_cte_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#regular_cte_spec.
    def exitRegular_cte_spec(self, ctx:TeradataSQLDMLParser.Regular_cte_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#recursive_cte_spec.
    def enterRecursive_cte_spec(self, ctx:TeradataSQLDMLParser.Recursive_cte_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#recursive_cte_spec.
    def exitRecursive_cte_spec(self, ctx:TeradataSQLDMLParser.Recursive_cte_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#using_request_modifier.
    def enterUsing_request_modifier(self, ctx:TeradataSQLDMLParser.Using_request_modifierContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#using_request_modifier.
    def exitUsing_request_modifier(self, ctx:TeradataSQLDMLParser.Using_request_modifierContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#using_spec.
    def enterUsing_spec(self, ctx:TeradataSQLDMLParser.Using_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#using_spec.
    def exitUsing_spec(self, ctx:TeradataSQLDMLParser.Using_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLDMLParser#explain_request_modifier.
    def enterExplain_request_modifier(self, ctx:TeradataSQLDMLParser.Explain_request_modifierContext):
        pass

    # Exit a parse tree produced by TeradataSQLDMLParser#explain_request_modifier.
    def exitExplain_request_modifier(self, ctx:TeradataSQLDMLParser.Explain_request_modifierContext):
        pass



del TeradataSQLDMLParser