# Generated from sql/teradata/TeradataSQLParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .TeradataSQLParser import TeradataSQLParser
else:
    from TeradataSQLParser import TeradataSQLParser

# This class defines a complete listener for a parse tree produced by TeradataSQLParser.
class TeradataSQLParserListener(ParseTreeListener):

    # Enter a parse tree produced by TeradataSQLParser#sql_script.
    def enterSql_script(self, ctx:TeradataSQLParser.Sql_scriptContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#sql_script.
    def exitSql_script(self, ctx:TeradataSQLParser.Sql_scriptContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#unit_stat.
    def enterUnit_stat(self, ctx:TeradataSQLParser.Unit_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#unit_stat.
    def exitUnit_stat(self, ctx:TeradataSQLParser.Unit_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#ddl_stat.
    def enterDdl_stat(self, ctx:TeradataSQLParser.Ddl_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#ddl_stat.
    def exitDdl_stat(self, ctx:TeradataSQLParser.Ddl_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#alter_foreign_server_stat.
    def enterAlter_foreign_server_stat(self, ctx:TeradataSQLParser.Alter_foreign_server_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#alter_foreign_server_stat.
    def exitAlter_foreign_server_stat(self, ctx:TeradataSQLParser.Alter_foreign_server_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#foreign_server_add_clause.
    def enterForeign_server_add_clause(self, ctx:TeradataSQLParser.Foreign_server_add_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#foreign_server_add_clause.
    def exitForeign_server_add_clause(self, ctx:TeradataSQLParser.Foreign_server_add_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#foreign_server_drop_clause.
    def enterForeign_server_drop_clause(self, ctx:TeradataSQLParser.Foreign_server_drop_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#foreign_server_drop_clause.
    def exitForeign_server_drop_clause(self, ctx:TeradataSQLParser.Foreign_server_drop_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#alter_function_stat.
    def enterAlter_function_stat(self, ctx:TeradataSQLParser.Alter_function_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#alter_function_stat.
    def exitAlter_function_stat(self, ctx:TeradataSQLParser.Alter_function_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#alter_join_index_stat.
    def enterAlter_join_index_stat(self, ctx:TeradataSQLParser.Alter_join_index_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#alter_join_index_stat.
    def exitAlter_join_index_stat(self, ctx:TeradataSQLParser.Alter_join_index_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#alter_hash_index_stat.
    def enterAlter_hash_index_stat(self, ctx:TeradataSQLParser.Alter_hash_index_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#alter_hash_index_stat.
    def exitAlter_hash_index_stat(self, ctx:TeradataSQLParser.Alter_hash_index_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#alter_table_stat.
    def enterAlter_table_stat(self, ctx:TeradataSQLParser.Alter_table_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#alter_table_stat.
    def exitAlter_table_stat(self, ctx:TeradataSQLParser.Alter_table_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#alter_table_basic_stat.
    def enterAlter_table_basic_stat(self, ctx:TeradataSQLParser.Alter_table_basic_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#alter_table_basic_stat.
    def exitAlter_table_basic_stat(self, ctx:TeradataSQLParser.Alter_table_basic_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#alter_table_join_index_stat.
    def enterAlter_table_join_index_stat(self, ctx:TeradataSQLParser.Alter_table_join_index_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#alter_table_join_index_stat.
    def exitAlter_table_join_index_stat(self, ctx:TeradataSQLParser.Alter_table_join_index_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#alter_table_revalidation_stat.
    def enterAlter_table_revalidation_stat(self, ctx:TeradataSQLParser.Alter_table_revalidation_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#alter_table_revalidation_stat.
    def exitAlter_table_revalidation_stat(self, ctx:TeradataSQLParser.Alter_table_revalidation_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#alter_table_release_rows_stat.
    def enterAlter_table_release_rows_stat(self, ctx:TeradataSQLParser.Alter_table_release_rows_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#alter_table_release_rows_stat.
    def exitAlter_table_release_rows_stat(self, ctx:TeradataSQLParser.Alter_table_release_rows_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#alter_table_map_and_collocation_form_stat.
    def enterAlter_table_map_and_collocation_form_stat(self, ctx:TeradataSQLParser.Alter_table_map_and_collocation_form_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#alter_table_map_and_collocation_form_stat.
    def exitAlter_table_map_and_collocation_form_stat(self, ctx:TeradataSQLParser.Alter_table_map_and_collocation_form_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#alter_foreign_table_stat.
    def enterAlter_foreign_table_stat(self, ctx:TeradataSQLParser.Alter_foreign_table_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#alter_foreign_table_stat.
    def exitAlter_foreign_table_stat(self, ctx:TeradataSQLParser.Alter_foreign_table_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#alter_foreign_column_option.
    def enterAlter_foreign_column_option(self, ctx:TeradataSQLParser.Alter_foreign_column_optionContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#alter_foreign_column_option.
    def exitAlter_foreign_column_option(self, ctx:TeradataSQLParser.Alter_foreign_column_optionContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#alter_table_to_current_stat.
    def enterAlter_table_to_current_stat(self, ctx:TeradataSQLParser.Alter_table_to_current_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#alter_table_to_current_stat.
    def exitAlter_table_to_current_stat(self, ctx:TeradataSQLParser.Alter_table_to_current_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#alter_option.
    def enterAlter_option(self, ctx:TeradataSQLParser.Alter_optionContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#alter_option.
    def exitAlter_option(self, ctx:TeradataSQLParser.Alter_optionContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#table_option_alter_form.
    def enterTable_option_alter_form(self, ctx:TeradataSQLParser.Table_option_alter_formContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#table_option_alter_form.
    def exitTable_option_alter_form(self, ctx:TeradataSQLParser.Table_option_alter_formContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#add_option.
    def enterAdd_option(self, ctx:TeradataSQLParser.Add_optionContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#add_option.
    def exitAdd_option(self, ctx:TeradataSQLParser.Add_optionContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#drop_option.
    def enterDrop_option(self, ctx:TeradataSQLParser.Drop_optionContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#drop_option.
    def exitDrop_option(self, ctx:TeradataSQLParser.Drop_optionContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#modify_primary.
    def enterModify_primary(self, ctx:TeradataSQLParser.Modify_primaryContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#modify_primary.
    def exitModify_primary(self, ctx:TeradataSQLParser.Modify_primaryContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#alter_partitioning.
    def enterAlter_partitioning(self, ctx:TeradataSQLParser.Alter_partitioningContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#alter_partitioning.
    def exitAlter_partitioning(self, ctx:TeradataSQLParser.Alter_partitioningContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#add_drop_range_option.
    def enterAdd_drop_range_option(self, ctx:TeradataSQLParser.Add_drop_range_optionContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#add_drop_range_option.
    def exitAdd_drop_range_option(self, ctx:TeradataSQLParser.Add_drop_range_optionContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#alter_column_spec.
    def enterAlter_column_spec(self, ctx:TeradataSQLParser.Alter_column_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#alter_column_spec.
    def exitAlter_column_spec(self, ctx:TeradataSQLParser.Alter_column_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#alter_range_expr.
    def enterAlter_range_expr(self, ctx:TeradataSQLParser.Alter_range_exprContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#alter_range_expr.
    def exitAlter_range_expr(self, ctx:TeradataSQLParser.Alter_range_exprContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#with_isolated_loading_alter_form.
    def enterWith_isolated_loading_alter_form(self, ctx:TeradataSQLParser.With_isolated_loading_alter_formContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#with_isolated_loading_alter_form.
    def exitWith_isolated_loading_alter_form(self, ctx:TeradataSQLParser.With_isolated_loading_alter_formContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#join_index_add_option.
    def enterJoin_index_add_option(self, ctx:TeradataSQLParser.Join_index_add_optionContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#join_index_add_option.
    def exitJoin_index_add_option(self, ctx:TeradataSQLParser.Join_index_add_optionContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#alter_type_stat.
    def enterAlter_type_stat(self, ctx:TeradataSQLParser.Alter_type_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#alter_type_stat.
    def exitAlter_type_stat(self, ctx:TeradataSQLParser.Alter_type_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#add_attribute_clause.
    def enterAdd_attribute_clause(self, ctx:TeradataSQLParser.Add_attribute_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#add_attribute_clause.
    def exitAdd_attribute_clause(self, ctx:TeradataSQLParser.Add_attribute_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#add_method_clause.
    def enterAdd_method_clause(self, ctx:TeradataSQLParser.Add_method_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#add_method_clause.
    def exitAdd_method_clause(self, ctx:TeradataSQLParser.Add_method_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#add_specific_method_clause.
    def enterAdd_specific_method_clause(self, ctx:TeradataSQLParser.Add_specific_method_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#add_specific_method_clause.
    def exitAdd_specific_method_clause(self, ctx:TeradataSQLParser.Add_specific_method_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#drop_attribute_clause.
    def enterDrop_attribute_clause(self, ctx:TeradataSQLParser.Drop_attribute_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#drop_attribute_clause.
    def exitDrop_attribute_clause(self, ctx:TeradataSQLParser.Drop_attribute_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#drop_method_clause.
    def enterDrop_method_clause(self, ctx:TeradataSQLParser.Drop_method_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#drop_method_clause.
    def exitDrop_method_clause(self, ctx:TeradataSQLParser.Drop_method_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#drop_specific_method_clause.
    def enterDrop_specific_method_clause(self, ctx:TeradataSQLParser.Drop_specific_method_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#drop_specific_method_clause.
    def exitDrop_specific_method_clause(self, ctx:TeradataSQLParser.Drop_specific_method_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#add_method_spec.
    def enterAdd_method_spec(self, ctx:TeradataSQLParser.Add_method_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#add_method_spec.
    def exitAdd_method_spec(self, ctx:TeradataSQLParser.Add_method_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#add_specific_method_spec.
    def enterAdd_specific_method_spec(self, ctx:TeradataSQLParser.Add_specific_method_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#add_specific_method_spec.
    def exitAdd_specific_method_spec(self, ctx:TeradataSQLParser.Add_specific_method_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#begin_isolated_loading_stat.
    def enterBegin_isolated_loading_stat(self, ctx:TeradataSQLParser.Begin_isolated_loading_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#begin_isolated_loading_stat.
    def exitBegin_isolated_loading_stat(self, ctx:TeradataSQLParser.Begin_isolated_loading_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#begin_logging_stat.
    def enterBegin_logging_stat(self, ctx:TeradataSQLParser.Begin_logging_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#begin_logging_stat.
    def exitBegin_logging_stat(self, ctx:TeradataSQLParser.Begin_logging_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#operation.
    def enterOperation(self, ctx:TeradataSQLParser.OperationContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#operation.
    def exitOperation(self, ctx:TeradataSQLParser.OperationContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#logging_frequency.
    def enterLogging_frequency(self, ctx:TeradataSQLParser.Logging_frequencyContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#logging_frequency.
    def exitLogging_frequency(self, ctx:TeradataSQLParser.Logging_frequencyContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#logging_item.
    def enterLogging_item(self, ctx:TeradataSQLParser.Logging_itemContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#logging_item.
    def exitLogging_item(self, ctx:TeradataSQLParser.Logging_itemContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#begin_query_capture_stat.
    def enterBegin_query_capture_stat(self, ctx:TeradataSQLParser.Begin_query_capture_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#begin_query_capture_stat.
    def exitBegin_query_capture_stat(self, ctx:TeradataSQLParser.Begin_query_capture_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#begin_query_logging_stat.
    def enterBegin_query_logging_stat(self, ctx:TeradataSQLParser.Begin_query_logging_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#begin_query_logging_stat.
    def exitBegin_query_logging_stat(self, ctx:TeradataSQLParser.Begin_query_logging_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#query_logging_with_item.
    def enterQuery_logging_with_item(self, ctx:TeradataSQLParser.Query_logging_with_itemContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#query_logging_with_item.
    def exitQuery_logging_with_item(self, ctx:TeradataSQLParser.Query_logging_with_itemContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#query_logging_limit_item.
    def enterQuery_logging_limit_item(self, ctx:TeradataSQLParser.Query_logging_limit_itemContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#query_logging_limit_item.
    def exitQuery_logging_limit_item(self, ctx:TeradataSQLParser.Query_logging_limit_itemContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#query_logging_on_items.
    def enterQuery_logging_on_items(self, ctx:TeradataSQLParser.Query_logging_on_itemsContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#query_logging_on_items.
    def exitQuery_logging_on_items(self, ctx:TeradataSQLParser.Query_logging_on_itemsContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#query_logging_on_all.
    def enterQuery_logging_on_all(self, ctx:TeradataSQLParser.Query_logging_on_allContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#query_logging_on_all.
    def exitQuery_logging_on_all(self, ctx:TeradataSQLParser.Query_logging_on_allContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#query_logging_on_users.
    def enterQuery_logging_on_users(self, ctx:TeradataSQLParser.Query_logging_on_usersContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#query_logging_on_users.
    def exitQuery_logging_on_users(self, ctx:TeradataSQLParser.Query_logging_on_usersContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#query_logging_on_application.
    def enterQuery_logging_on_application(self, ctx:TeradataSQLParser.Query_logging_on_applicationContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#query_logging_on_application.
    def exitQuery_logging_on_application(self, ctx:TeradataSQLParser.Query_logging_on_applicationContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#account_spec.
    def enterAccount_spec(self, ctx:TeradataSQLParser.Account_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#account_spec.
    def exitAccount_spec(self, ctx:TeradataSQLParser.Account_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#checkpoint_isolated_loading_stat.
    def enterCheckpoint_isolated_loading_stat(self, ctx:TeradataSQLParser.Checkpoint_isolated_loading_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#checkpoint_isolated_loading_stat.
    def exitCheckpoint_isolated_loading_stat(self, ctx:TeradataSQLParser.Checkpoint_isolated_loading_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#collect_statistics_optimizer_form_stat.
    def enterCollect_statistics_optimizer_form_stat(self, ctx:TeradataSQLParser.Collect_statistics_optimizer_form_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#collect_statistics_optimizer_form_stat.
    def exitCollect_statistics_optimizer_form_stat(self, ctx:TeradataSQLParser.Collect_statistics_optimizer_form_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#using_option.
    def enterUsing_option(self, ctx:TeradataSQLParser.Using_optionContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#using_option.
    def exitUsing_option(self, ctx:TeradataSQLParser.Using_optionContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#stats_target_spec.
    def enterStats_target_spec(self, ctx:TeradataSQLParser.Stats_target_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#stats_target_spec.
    def exitStats_target_spec(self, ctx:TeradataSQLParser.Stats_target_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#stats_index_spec.
    def enterStats_index_spec(self, ctx:TeradataSQLParser.Stats_index_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#stats_index_spec.
    def exitStats_index_spec(self, ctx:TeradataSQLParser.Stats_index_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#stats_column_spec.
    def enterStats_column_spec(self, ctx:TeradataSQLParser.Stats_column_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#stats_column_spec.
    def exitStats_column_spec(self, ctx:TeradataSQLParser.Stats_column_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#collection_source.
    def enterCollection_source(self, ctx:TeradataSQLParser.Collection_sourceContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#collection_source.
    def exitCollection_source(self, ctx:TeradataSQLParser.Collection_sourceContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#from_stats_option.
    def enterFrom_stats_option(self, ctx:TeradataSQLParser.From_stats_optionContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#from_stats_option.
    def exitFrom_stats_option(self, ctx:TeradataSQLParser.From_stats_optionContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#comment_placing_stat.
    def enterComment_placing_stat(self, ctx:TeradataSQLParser.Comment_placing_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#comment_placing_stat.
    def exitComment_placing_stat(self, ctx:TeradataSQLParser.Comment_placing_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#create_replace_authorization_stat.
    def enterCreate_replace_authorization_stat(self, ctx:TeradataSQLParser.Create_replace_authorization_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#create_replace_authorization_stat.
    def exitCreate_replace_authorization_stat(self, ctx:TeradataSQLParser.Create_replace_authorization_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#create_replace_function_stat.
    def enterCreate_replace_function_stat(self, ctx:TeradataSQLParser.Create_replace_function_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#create_replace_function_stat.
    def exitCreate_replace_function_stat(self, ctx:TeradataSQLParser.Create_replace_function_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#create_replace_sql_function_stat.
    def enterCreate_replace_sql_function_stat(self, ctx:TeradataSQLParser.Create_replace_sql_function_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#create_replace_sql_function_stat.
    def exitCreate_replace_sql_function_stat(self, ctx:TeradataSQLParser.Create_replace_sql_function_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#create_replace_table_function_stat.
    def enterCreate_replace_table_function_stat(self, ctx:TeradataSQLParser.Create_replace_table_function_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#create_replace_table_function_stat.
    def exitCreate_replace_table_function_stat(self, ctx:TeradataSQLParser.Create_replace_table_function_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#create_replace_external_function_stat.
    def enterCreate_replace_external_function_stat(self, ctx:TeradataSQLParser.Create_replace_external_function_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#create_replace_external_function_stat.
    def exitCreate_replace_external_function_stat(self, ctx:TeradataSQLParser.Create_replace_external_function_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#sql_function_parameter_spec.
    def enterSql_function_parameter_spec(self, ctx:TeradataSQLParser.Sql_function_parameter_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#sql_function_parameter_spec.
    def exitSql_function_parameter_spec(self, ctx:TeradataSQLParser.Sql_function_parameter_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#sql_function_language_spec.
    def enterSql_function_language_spec(self, ctx:TeradataSQLParser.Sql_function_language_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#sql_function_language_spec.
    def exitSql_function_language_spec(self, ctx:TeradataSQLParser.Sql_function_language_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#sql_function_access_spec.
    def enterSql_function_access_spec(self, ctx:TeradataSQLParser.Sql_function_access_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#sql_function_access_spec.
    def exitSql_function_access_spec(self, ctx:TeradataSQLParser.Sql_function_access_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#sql_function_attr.
    def enterSql_function_attr(self, ctx:TeradataSQLParser.Sql_function_attrContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#sql_function_attr.
    def exitSql_function_attr(self, ctx:TeradataSQLParser.Sql_function_attrContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#table_spec.
    def enterTable_spec(self, ctx:TeradataSQLParser.Table_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#table_spec.
    def exitTable_spec(self, ctx:TeradataSQLParser.Table_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#table_function_parameter_spec.
    def enterTable_function_parameter_spec(self, ctx:TeradataSQLParser.Table_function_parameter_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#table_function_parameter_spec.
    def exitTable_function_parameter_spec(self, ctx:TeradataSQLParser.Table_function_parameter_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#table_function_language_spec.
    def enterTable_function_language_spec(self, ctx:TeradataSQLParser.Table_function_language_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#table_function_language_spec.
    def exitTable_function_language_spec(self, ctx:TeradataSQLParser.Table_function_language_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#table_function_attr.
    def enterTable_function_attr(self, ctx:TeradataSQLParser.Table_function_attrContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#table_function_attr.
    def exitTable_function_attr(self, ctx:TeradataSQLParser.Table_function_attrContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#table_function_parameter_style.
    def enterTable_function_parameter_style(self, ctx:TeradataSQLParser.Table_function_parameter_styleContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#table_function_parameter_style.
    def exitTable_function_parameter_style(self, ctx:TeradataSQLParser.Table_function_parameter_styleContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#external_function_parameter_spec.
    def enterExternal_function_parameter_spec(self, ctx:TeradataSQLParser.External_function_parameter_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#external_function_parameter_spec.
    def exitExternal_function_parameter_spec(self, ctx:TeradataSQLParser.External_function_parameter_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#external_function_language_spec.
    def enterExternal_function_language_spec(self, ctx:TeradataSQLParser.External_function_language_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#external_function_language_spec.
    def exitExternal_function_language_spec(self, ctx:TeradataSQLParser.External_function_language_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#external_function_attr.
    def enterExternal_function_attr(self, ctx:TeradataSQLParser.External_function_attrContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#external_function_attr.
    def exitExternal_function_attr(self, ctx:TeradataSQLParser.External_function_attrContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#external_function_parameter_style.
    def enterExternal_function_parameter_style(self, ctx:TeradataSQLParser.External_function_parameter_styleContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#external_function_parameter_style.
    def exitExternal_function_parameter_style(self, ctx:TeradataSQLParser.External_function_parameter_styleContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#no_sql.
    def enterNo_sql(self, ctx:TeradataSQLParser.No_sqlContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#no_sql.
    def exitNo_sql(self, ctx:TeradataSQLParser.No_sqlContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#create_replace_macro_stat.
    def enterCreate_replace_macro_stat(self, ctx:TeradataSQLParser.Create_replace_macro_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#create_replace_macro_stat.
    def exitCreate_replace_macro_stat(self, ctx:TeradataSQLParser.Create_replace_macro_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#macro_parameter.
    def enterMacro_parameter(self, ctx:TeradataSQLParser.Macro_parameterContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#macro_parameter.
    def exitMacro_parameter(self, ctx:TeradataSQLParser.Macro_parameterContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#create_replace_procedure_stat.
    def enterCreate_replace_procedure_stat(self, ctx:TeradataSQLParser.Create_replace_procedure_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#create_replace_procedure_stat.
    def exitCreate_replace_procedure_stat(self, ctx:TeradataSQLParser.Create_replace_procedure_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#create_replace_procedure_sql_form_stat.
    def enterCreate_replace_procedure_sql_form_stat(self, ctx:TeradataSQLParser.Create_replace_procedure_sql_form_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#create_replace_procedure_sql_form_stat.
    def exitCreate_replace_procedure_sql_form_stat(self, ctx:TeradataSQLParser.Create_replace_procedure_sql_form_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#parameter_spec.
    def enterParameter_spec(self, ctx:TeradataSQLParser.Parameter_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#parameter_spec.
    def exitParameter_spec(self, ctx:TeradataSQLParser.Parameter_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#sql_data_access_option.
    def enterSql_data_access_option(self, ctx:TeradataSQLParser.Sql_data_access_optionContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#sql_data_access_option.
    def exitSql_data_access_option(self, ctx:TeradataSQLParser.Sql_data_access_optionContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#dynamic_result_sets.
    def enterDynamic_result_sets(self, ctx:TeradataSQLParser.Dynamic_result_setsContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#dynamic_result_sets.
    def exitDynamic_result_sets(self, ctx:TeradataSQLParser.Dynamic_result_setsContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#sql_security_option.
    def enterSql_security_option(self, ctx:TeradataSQLParser.Sql_security_optionContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#sql_security_option.
    def exitSql_security_option(self, ctx:TeradataSQLParser.Sql_security_optionContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#procedure_body.
    def enterProcedure_body(self, ctx:TeradataSQLParser.Procedure_bodyContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#procedure_body.
    def exitProcedure_body(self, ctx:TeradataSQLParser.Procedure_bodyContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#procedure_stat.
    def enterProcedure_stat(self, ctx:TeradataSQLParser.Procedure_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#procedure_stat.
    def exitProcedure_stat(self, ctx:TeradataSQLParser.Procedure_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#procedure_data_stat.
    def enterProcedure_data_stat(self, ctx:TeradataSQLParser.Procedure_data_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#procedure_data_stat.
    def exitProcedure_data_stat(self, ctx:TeradataSQLParser.Procedure_data_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#procedure_dml_stat.
    def enterProcedure_dml_stat(self, ctx:TeradataSQLParser.Procedure_dml_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#procedure_dml_stat.
    def exitProcedure_dml_stat(self, ctx:TeradataSQLParser.Procedure_dml_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#procedure_ddl_stat.
    def enterProcedure_ddl_stat(self, ctx:TeradataSQLParser.Procedure_ddl_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#procedure_ddl_stat.
    def exitProcedure_ddl_stat(self, ctx:TeradataSQLParser.Procedure_ddl_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#procedure_dcl_stat.
    def enterProcedure_dcl_stat(self, ctx:TeradataSQLParser.Procedure_dcl_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#procedure_dcl_stat.
    def exitProcedure_dcl_stat(self, ctx:TeradataSQLParser.Procedure_dcl_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#compound_stat.
    def enterCompound_stat(self, ctx:TeradataSQLParser.Compound_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#compound_stat.
    def exitCompound_stat(self, ctx:TeradataSQLParser.Compound_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#procedure_cursor_control_stat.
    def enterProcedure_cursor_control_stat(self, ctx:TeradataSQLParser.Procedure_cursor_control_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#procedure_cursor_control_stat.
    def exitProcedure_cursor_control_stat(self, ctx:TeradataSQLParser.Procedure_cursor_control_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#assignment_stat.
    def enterAssignment_stat(self, ctx:TeradataSQLParser.Assignment_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#assignment_stat.
    def exitAssignment_stat(self, ctx:TeradataSQLParser.Assignment_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#condition_stat.
    def enterCondition_stat(self, ctx:TeradataSQLParser.Condition_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#condition_stat.
    def exitCondition_stat(self, ctx:TeradataSQLParser.Condition_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#iteration_stat.
    def enterIteration_stat(self, ctx:TeradataSQLParser.Iteration_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#iteration_stat.
    def exitIteration_stat(self, ctx:TeradataSQLParser.Iteration_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#diagnostic_stat.
    def enterDiagnostic_stat(self, ctx:TeradataSQLParser.Diagnostic_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#diagnostic_stat.
    def exitDiagnostic_stat(self, ctx:TeradataSQLParser.Diagnostic_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#print_stat.
    def enterPrint_stat(self, ctx:TeradataSQLParser.Print_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#print_stat.
    def exitPrint_stat(self, ctx:TeradataSQLParser.Print_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#local_declaration.
    def enterLocal_declaration(self, ctx:TeradataSQLParser.Local_declarationContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#local_declaration.
    def exitLocal_declaration(self, ctx:TeradataSQLParser.Local_declarationContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#cursor_declaration.
    def enterCursor_declaration(self, ctx:TeradataSQLParser.Cursor_declarationContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#cursor_declaration.
    def exitCursor_declaration(self, ctx:TeradataSQLParser.Cursor_declarationContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#condition_handler.
    def enterCondition_handler(self, ctx:TeradataSQLParser.Condition_handlerContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#condition_handler.
    def exitCondition_handler(self, ctx:TeradataSQLParser.Condition_handlerContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#allocate_stat.
    def enterAllocate_stat(self, ctx:TeradataSQLParser.Allocate_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#allocate_stat.
    def exitAllocate_stat(self, ctx:TeradataSQLParser.Allocate_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#close_stat.
    def enterClose_stat(self, ctx:TeradataSQLParser.Close_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#close_stat.
    def exitClose_stat(self, ctx:TeradataSQLParser.Close_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#deallocate_prepare_stat.
    def enterDeallocate_prepare_stat(self, ctx:TeradataSQLParser.Deallocate_prepare_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#deallocate_prepare_stat.
    def exitDeallocate_prepare_stat(self, ctx:TeradataSQLParser.Deallocate_prepare_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#positioned_delete_stat.
    def enterPositioned_delete_stat(self, ctx:TeradataSQLParser.Positioned_delete_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#positioned_delete_stat.
    def exitPositioned_delete_stat(self, ctx:TeradataSQLParser.Positioned_delete_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#positioned_update_stat.
    def enterPositioned_update_stat(self, ctx:TeradataSQLParser.Positioned_update_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#positioned_update_stat.
    def exitPositioned_update_stat(self, ctx:TeradataSQLParser.Positioned_update_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#execute_statement_stat.
    def enterExecute_statement_stat(self, ctx:TeradataSQLParser.Execute_statement_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#execute_statement_stat.
    def exitExecute_statement_stat(self, ctx:TeradataSQLParser.Execute_statement_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#execute_immediate_stat.
    def enterExecute_immediate_stat(self, ctx:TeradataSQLParser.Execute_immediate_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#execute_immediate_stat.
    def exitExecute_immediate_stat(self, ctx:TeradataSQLParser.Execute_immediate_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#fetch_stat.
    def enterFetch_stat(self, ctx:TeradataSQLParser.Fetch_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#fetch_stat.
    def exitFetch_stat(self, ctx:TeradataSQLParser.Fetch_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#open_stat.
    def enterOpen_stat(self, ctx:TeradataSQLParser.Open_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#open_stat.
    def exitOpen_stat(self, ctx:TeradataSQLParser.Open_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#prepare_stat.
    def enterPrepare_stat(self, ctx:TeradataSQLParser.Prepare_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#prepare_stat.
    def exitPrepare_stat(self, ctx:TeradataSQLParser.Prepare_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#case_stat.
    def enterCase_stat(self, ctx:TeradataSQLParser.Case_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#case_stat.
    def exitCase_stat(self, ctx:TeradataSQLParser.Case_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#when_operand_clause.
    def enterWhen_operand_clause(self, ctx:TeradataSQLParser.When_operand_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#when_operand_clause.
    def exitWhen_operand_clause(self, ctx:TeradataSQLParser.When_operand_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#when_condition_clause.
    def enterWhen_condition_clause(self, ctx:TeradataSQLParser.When_condition_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#when_condition_clause.
    def exitWhen_condition_clause(self, ctx:TeradataSQLParser.When_condition_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#if_stat.
    def enterIf_stat(self, ctx:TeradataSQLParser.If_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#if_stat.
    def exitIf_stat(self, ctx:TeradataSQLParser.If_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#while_stat.
    def enterWhile_stat(self, ctx:TeradataSQLParser.While_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#while_stat.
    def exitWhile_stat(self, ctx:TeradataSQLParser.While_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#loop_stat.
    def enterLoop_stat(self, ctx:TeradataSQLParser.Loop_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#loop_stat.
    def exitLoop_stat(self, ctx:TeradataSQLParser.Loop_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#for_stat.
    def enterFor_stat(self, ctx:TeradataSQLParser.For_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#for_stat.
    def exitFor_stat(self, ctx:TeradataSQLParser.For_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#repeat_stat.
    def enterRepeat_stat(self, ctx:TeradataSQLParser.Repeat_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#repeat_stat.
    def exitRepeat_stat(self, ctx:TeradataSQLParser.Repeat_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#diagnostic_statement_assignment.
    def enterDiagnostic_statement_assignment(self, ctx:TeradataSQLParser.Diagnostic_statement_assignmentContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#diagnostic_statement_assignment.
    def exitDiagnostic_statement_assignment(self, ctx:TeradataSQLParser.Diagnostic_statement_assignmentContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#diagnostic_condition_assignment.
    def enterDiagnostic_condition_assignment(self, ctx:TeradataSQLParser.Diagnostic_condition_assignmentContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#diagnostic_condition_assignment.
    def exitDiagnostic_condition_assignment(self, ctx:TeradataSQLParser.Diagnostic_condition_assignmentContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#condition_information_item.
    def enterCondition_information_item(self, ctx:TeradataSQLParser.Condition_information_itemContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#condition_information_item.
    def exitCondition_information_item(self, ctx:TeradataSQLParser.Condition_information_itemContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#statement_information_item.
    def enterStatement_information_item(self, ctx:TeradataSQLParser.Statement_information_itemContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#statement_information_item.
    def exitStatement_information_item(self, ctx:TeradataSQLParser.Statement_information_itemContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#signal_spec.
    def enterSignal_spec(self, ctx:TeradataSQLParser.Signal_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#signal_spec.
    def exitSignal_spec(self, ctx:TeradataSQLParser.Signal_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#sqlstate_spec.
    def enterSqlstate_spec(self, ctx:TeradataSQLParser.Sqlstate_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#sqlstate_spec.
    def exitSqlstate_spec(self, ctx:TeradataSQLParser.Sqlstate_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#create_replace_view_stat.
    def enterCreate_replace_view_stat(self, ctx:TeradataSQLParser.Create_replace_view_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#create_replace_view_stat.
    def exitCreate_replace_view_stat(self, ctx:TeradataSQLParser.Create_replace_view_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#as_of_clause.
    def enterAs_of_clause(self, ctx:TeradataSQLParser.As_of_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#as_of_clause.
    def exitAs_of_clause(self, ctx:TeradataSQLParser.As_of_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#create_database_stat.
    def enterCreate_database_stat(self, ctx:TeradataSQLParser.Create_database_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#create_database_stat.
    def exitCreate_database_stat(self, ctx:TeradataSQLParser.Create_database_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#database_attribute.
    def enterDatabase_attribute(self, ctx:TeradataSQLParser.Database_attributeContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#database_attribute.
    def exitDatabase_attribute(self, ctx:TeradataSQLParser.Database_attributeContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#create_index_stat.
    def enterCreate_index_stat(self, ctx:TeradataSQLParser.Create_index_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#create_index_stat.
    def exitCreate_index_stat(self, ctx:TeradataSQLParser.Create_index_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#index_spec.
    def enterIndex_spec(self, ctx:TeradataSQLParser.Index_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#index_spec.
    def exitIndex_spec(self, ctx:TeradataSQLParser.Index_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#create_join_index_stat.
    def enterCreate_join_index_stat(self, ctx:TeradataSQLParser.Create_join_index_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#create_join_index_stat.
    def exitCreate_join_index_stat(self, ctx:TeradataSQLParser.Create_join_index_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#join_index_select_clause.
    def enterJoin_index_select_clause(self, ctx:TeradataSQLParser.Join_index_select_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#join_index_select_clause.
    def exitJoin_index_select_clause(self, ctx:TeradataSQLParser.Join_index_select_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#ji_selection.
    def enterJi_selection(self, ctx:TeradataSQLParser.Ji_selectionContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#ji_selection.
    def exitJi_selection(self, ctx:TeradataSQLParser.Ji_selectionContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#aggregation_clause.
    def enterAggregation_clause(self, ctx:TeradataSQLParser.Aggregation_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#aggregation_clause.
    def exitAggregation_clause(self, ctx:TeradataSQLParser.Aggregation_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#ji_source.
    def enterJi_source(self, ctx:TeradataSQLParser.Ji_sourceContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#ji_source.
    def exitJi_source(self, ctx:TeradataSQLParser.Ji_sourceContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#ji_joined_table.
    def enterJi_joined_table(self, ctx:TeradataSQLParser.Ji_joined_tableContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#ji_joined_table.
    def exitJi_joined_table(self, ctx:TeradataSQLParser.Ji_joined_tableContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#ji_grouping_or_ordering_spec.
    def enterJi_grouping_or_ordering_spec(self, ctx:TeradataSQLParser.Ji_grouping_or_ordering_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#ji_grouping_or_ordering_spec.
    def exitJi_grouping_or_ordering_spec(self, ctx:TeradataSQLParser.Ji_grouping_or_ordering_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#create_profile_stat.
    def enterCreate_profile_stat(self, ctx:TeradataSQLParser.Create_profile_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#create_profile_stat.
    def exitCreate_profile_stat(self, ctx:TeradataSQLParser.Create_profile_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#profile_attribute.
    def enterProfile_attribute(self, ctx:TeradataSQLParser.Profile_attributeContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#profile_attribute.
    def exitProfile_attribute(self, ctx:TeradataSQLParser.Profile_attributeContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#password_attribute.
    def enterPassword_attribute(self, ctx:TeradataSQLParser.Password_attributeContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#password_attribute.
    def exitPassword_attribute(self, ctx:TeradataSQLParser.Password_attributeContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#create_foreign_server_stat.
    def enterCreate_foreign_server_stat(self, ctx:TeradataSQLParser.Create_foreign_server_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#create_foreign_server_stat.
    def exitCreate_foreign_server_stat(self, ctx:TeradataSQLParser.Create_foreign_server_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#foreign_server_external_security_clause.
    def enterForeign_server_external_security_clause(self, ctx:TeradataSQLParser.Foreign_server_external_security_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#foreign_server_external_security_clause.
    def exitForeign_server_external_security_clause(self, ctx:TeradataSQLParser.Foreign_server_external_security_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#foreign_server_using_clause.
    def enterForeign_server_using_clause(self, ctx:TeradataSQLParser.Foreign_server_using_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#foreign_server_using_clause.
    def exitForeign_server_using_clause(self, ctx:TeradataSQLParser.Foreign_server_using_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#foreign_server_using_option.
    def enterForeign_server_using_option(self, ctx:TeradataSQLParser.Foreign_server_using_optionContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#foreign_server_using_option.
    def exitForeign_server_using_option(self, ctx:TeradataSQLParser.Foreign_server_using_optionContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#foreign_server_operator_option.
    def enterForeign_server_operator_option(self, ctx:TeradataSQLParser.Foreign_server_operator_optionContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#foreign_server_operator_option.
    def exitForeign_server_operator_option(self, ctx:TeradataSQLParser.Foreign_server_operator_optionContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#do_import_with.
    def enterDo_import_with(self, ctx:TeradataSQLParser.Do_import_withContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#do_import_with.
    def exitDo_import_with(self, ctx:TeradataSQLParser.Do_import_withContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#do_export_with.
    def enterDo_export_with(self, ctx:TeradataSQLParser.Do_export_withContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#do_export_with.
    def exitDo_export_with(self, ctx:TeradataSQLParser.Do_export_withContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#foreign_server_with_clause.
    def enterForeign_server_with_clause(self, ctx:TeradataSQLParser.Foreign_server_with_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#foreign_server_with_clause.
    def exitForeign_server_with_clause(self, ctx:TeradataSQLParser.Foreign_server_with_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#foreign_server_option_name.
    def enterForeign_server_option_name(self, ctx:TeradataSQLParser.Foreign_server_option_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#foreign_server_option_name.
    def exitForeign_server_option_name(self, ctx:TeradataSQLParser.Foreign_server_option_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#create_hash_index_stat.
    def enterCreate_hash_index_stat(self, ctx:TeradataSQLParser.Create_hash_index_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#create_hash_index_stat.
    def exitCreate_hash_index_stat(self, ctx:TeradataSQLParser.Create_hash_index_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#create_role_stat.
    def enterCreate_role_stat(self, ctx:TeradataSQLParser.Create_role_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#create_role_stat.
    def exitCreate_role_stat(self, ctx:TeradataSQLParser.Create_role_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#create_table_stat.
    def enterCreate_table_stat(self, ctx:TeradataSQLParser.Create_table_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#create_table_stat.
    def exitCreate_table_stat(self, ctx:TeradataSQLParser.Create_table_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#create_table_primary_form_stat.
    def enterCreate_table_primary_form_stat(self, ctx:TeradataSQLParser.Create_table_primary_form_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#create_table_primary_form_stat.
    def exitCreate_table_primary_form_stat(self, ctx:TeradataSQLParser.Create_table_primary_form_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#create_table_as_stat.
    def enterCreate_table_as_stat(self, ctx:TeradataSQLParser.Create_table_as_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#create_table_as_stat.
    def exitCreate_table_as_stat(self, ctx:TeradataSQLParser.Create_table_as_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#create_queue_table_stat.
    def enterCreate_queue_table_stat(self, ctx:TeradataSQLParser.Create_queue_table_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#create_queue_table_stat.
    def exitCreate_queue_table_stat(self, ctx:TeradataSQLParser.Create_queue_table_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#create_global_temporary_trace_table_stat.
    def enterCreate_global_temporary_trace_table_stat(self, ctx:TeradataSQLParser.Create_global_temporary_trace_table_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#create_global_temporary_trace_table_stat.
    def exitCreate_global_temporary_trace_table_stat(self, ctx:TeradataSQLParser.Create_global_temporary_trace_table_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#create_foreign_table_stat.
    def enterCreate_foreign_table_stat(self, ctx:TeradataSQLParser.Create_foreign_table_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#create_foreign_table_stat.
    def exitCreate_foreign_table_stat(self, ctx:TeradataSQLParser.Create_foreign_table_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#create_error_table_stat.
    def enterCreate_error_table_stat(self, ctx:TeradataSQLParser.Create_error_table_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#create_error_table_stat.
    def exitCreate_error_table_stat(self, ctx:TeradataSQLParser.Create_error_table_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#table_kind.
    def enterTable_kind(self, ctx:TeradataSQLParser.Table_kindContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#table_kind.
    def exitTable_kind(self, ctx:TeradataSQLParser.Table_kindContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#table_option.
    def enterTable_option(self, ctx:TeradataSQLParser.Table_optionContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#table_option.
    def exitTable_option(self, ctx:TeradataSQLParser.Table_optionContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#column_definition.
    def enterColumn_definition(self, ctx:TeradataSQLParser.Column_definitionContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#column_definition.
    def exitColumn_definition(self, ctx:TeradataSQLParser.Column_definitionContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#ctas_column_definition.
    def enterCtas_column_definition(self, ctx:TeradataSQLParser.Ctas_column_definitionContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#ctas_column_definition.
    def exitCtas_column_definition(self, ctx:TeradataSQLParser.Ctas_column_definitionContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#index_definition.
    def enterIndex_definition(self, ctx:TeradataSQLParser.Index_definitionContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#index_definition.
    def exitIndex_definition(self, ctx:TeradataSQLParser.Index_definitionContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#qits_definition.
    def enterQits_definition(self, ctx:TeradataSQLParser.Qits_definitionContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#qits_definition.
    def exitQits_definition(self, ctx:TeradataSQLParser.Qits_definitionContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#foreign_table_external_security_clause.
    def enterForeign_table_external_security_clause(self, ctx:TeradataSQLParser.Foreign_table_external_security_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#foreign_table_external_security_clause.
    def exitForeign_table_external_security_clause(self, ctx:TeradataSQLParser.Foreign_table_external_security_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#location_column.
    def enterLocation_column(self, ctx:TeradataSQLParser.Location_columnContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#location_column.
    def exitLocation_column(self, ctx:TeradataSQLParser.Location_columnContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#payload_column.
    def enterPayload_column(self, ctx:TeradataSQLParser.Payload_columnContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#payload_column.
    def exitPayload_column(self, ctx:TeradataSQLParser.Payload_columnContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#foreign_table_option.
    def enterForeign_table_option(self, ctx:TeradataSQLParser.Foreign_table_optionContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#foreign_table_option.
    def exitForeign_table_option(self, ctx:TeradataSQLParser.Foreign_table_optionContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#table_preservation.
    def enterTable_preservation(self, ctx:TeradataSQLParser.Table_preservationContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#table_preservation.
    def exitTable_preservation(self, ctx:TeradataSQLParser.Table_preservationContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#mergeblockratio.
    def enterMergeblockratio(self, ctx:TeradataSQLParser.MergeblockratioContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#mergeblockratio.
    def exitMergeblockratio(self, ctx:TeradataSQLParser.MergeblockratioContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#datablocksize.
    def enterDatablocksize(self, ctx:TeradataSQLParser.DatablocksizeContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#datablocksize.
    def exitDatablocksize(self, ctx:TeradataSQLParser.DatablocksizeContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#block_compression.
    def enterBlock_compression(self, ctx:TeradataSQLParser.Block_compressionContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#block_compression.
    def exitBlock_compression(self, ctx:TeradataSQLParser.Block_compressionContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#table_isolated_loading.
    def enterTable_isolated_loading(self, ctx:TeradataSQLParser.Table_isolated_loadingContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#table_isolated_loading.
    def exitTable_isolated_loading(self, ctx:TeradataSQLParser.Table_isolated_loadingContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#column_attribute.
    def enterColumn_attribute(self, ctx:TeradataSQLParser.Column_attributeContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#column_attribute.
    def exitColumn_attribute(self, ctx:TeradataSQLParser.Column_attributeContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#column_storage_attribute.
    def enterColumn_storage_attribute(self, ctx:TeradataSQLParser.Column_storage_attributeContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#column_storage_attribute.
    def exitColumn_storage_attribute(self, ctx:TeradataSQLParser.Column_storage_attributeContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#compressed_value.
    def enterCompressed_value(self, ctx:TeradataSQLParser.Compressed_valueContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#compressed_value.
    def exitCompressed_value(self, ctx:TeradataSQLParser.Compressed_valueContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#column_constraint_attribute.
    def enterColumn_constraint_attribute(self, ctx:TeradataSQLParser.Column_constraint_attributeContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#column_constraint_attribute.
    def exitColumn_constraint_attribute(self, ctx:TeradataSQLParser.Column_constraint_attributeContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#auto_column_attribute.
    def enterAuto_column_attribute(self, ctx:TeradataSQLParser.Auto_column_attributeContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#auto_column_attribute.
    def exitAuto_column_attribute(self, ctx:TeradataSQLParser.Auto_column_attributeContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#identity_column_attribute.
    def enterIdentity_column_attribute(self, ctx:TeradataSQLParser.Identity_column_attributeContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#identity_column_attribute.
    def exitIdentity_column_attribute(self, ctx:TeradataSQLParser.Identity_column_attributeContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#id_column_value.
    def enterId_column_value(self, ctx:TeradataSQLParser.Id_column_valueContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#id_column_value.
    def exitId_column_value(self, ctx:TeradataSQLParser.Id_column_valueContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#normalize_option.
    def enterNormalize_option(self, ctx:TeradataSQLParser.Normalize_optionContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#normalize_option.
    def exitNormalize_option(self, ctx:TeradataSQLParser.Normalize_optionContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#table_constraint.
    def enterTable_constraint(self, ctx:TeradataSQLParser.Table_constraintContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#table_constraint.
    def exitTable_constraint(self, ctx:TeradataSQLParser.Table_constraintContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#references.
    def enterReferences(self, ctx:TeradataSQLParser.ReferencesContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#references.
    def exitReferences(self, ctx:TeradataSQLParser.ReferencesContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#partitioning_level.
    def enterPartitioning_level(self, ctx:TeradataSQLParser.Partitioning_levelContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#partitioning_level.
    def exitPartitioning_level(self, ctx:TeradataSQLParser.Partitioning_levelContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#column_partition.
    def enterColumn_partition(self, ctx:TeradataSQLParser.Column_partitionContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#column_partition.
    def exitColumn_partition(self, ctx:TeradataSQLParser.Column_partitionContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#create_type_stat.
    def enterCreate_type_stat(self, ctx:TeradataSQLParser.Create_type_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#create_type_stat.
    def exitCreate_type_stat(self, ctx:TeradataSQLParser.Create_type_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#create_type_structured_form_stat.
    def enterCreate_type_structured_form_stat(self, ctx:TeradataSQLParser.Create_type_structured_form_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#create_type_structured_form_stat.
    def exitCreate_type_structured_form_stat(self, ctx:TeradataSQLParser.Create_type_structured_form_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#create_type_distinct_form_stat.
    def enterCreate_type_distinct_form_stat(self, ctx:TeradataSQLParser.Create_type_distinct_form_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#create_type_distinct_form_stat.
    def exitCreate_type_distinct_form_stat(self, ctx:TeradataSQLParser.Create_type_distinct_form_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#create_type_array_form_stat.
    def enterCreate_type_array_form_stat(self, ctx:TeradataSQLParser.Create_type_array_form_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#create_type_array_form_stat.
    def exitCreate_type_array_form_stat(self, ctx:TeradataSQLParser.Create_type_array_form_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#create_type_one_dimensional_array_form_stat.
    def enterCreate_type_one_dimensional_array_form_stat(self, ctx:TeradataSQLParser.Create_type_one_dimensional_array_form_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#create_type_one_dimensional_array_form_stat.
    def exitCreate_type_one_dimensional_array_form_stat(self, ctx:TeradataSQLParser.Create_type_one_dimensional_array_form_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#create_type_one_dimensional_varray_form_stat.
    def enterCreate_type_one_dimensional_varray_form_stat(self, ctx:TeradataSQLParser.Create_type_one_dimensional_varray_form_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#create_type_one_dimensional_varray_form_stat.
    def exitCreate_type_one_dimensional_varray_form_stat(self, ctx:TeradataSQLParser.Create_type_one_dimensional_varray_form_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#create_type_multidimensional_array_form_stat.
    def enterCreate_type_multidimensional_array_form_stat(self, ctx:TeradataSQLParser.Create_type_multidimensional_array_form_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#create_type_multidimensional_array_form_stat.
    def exitCreate_type_multidimensional_array_form_stat(self, ctx:TeradataSQLParser.Create_type_multidimensional_array_form_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#create_type_multidimensional_varray_form_stat.
    def enterCreate_type_multidimensional_varray_form_stat(self, ctx:TeradataSQLParser.Create_type_multidimensional_varray_form_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#create_type_multidimensional_varray_form_stat.
    def exitCreate_type_multidimensional_varray_form_stat(self, ctx:TeradataSQLParser.Create_type_multidimensional_varray_form_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#type_attribute_spec.
    def enterType_attribute_spec(self, ctx:TeradataSQLParser.Type_attribute_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#type_attribute_spec.
    def exitType_attribute_spec(self, ctx:TeradataSQLParser.Type_attribute_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#structured_method_spec.
    def enterStructured_method_spec(self, ctx:TeradataSQLParser.Structured_method_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#structured_method_spec.
    def exitStructured_method_spec(self, ctx:TeradataSQLParser.Structured_method_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#distinct_method_spec.
    def enterDistinct_method_spec(self, ctx:TeradataSQLParser.Distinct_method_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#distinct_method_spec.
    def exitDistinct_method_spec(self, ctx:TeradataSQLParser.Distinct_method_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#method_parameter_spec.
    def enterMethod_parameter_spec(self, ctx:TeradataSQLParser.Method_parameter_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#method_parameter_spec.
    def exitMethod_parameter_spec(self, ctx:TeradataSQLParser.Method_parameter_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#returns_parameter_spec.
    def enterReturns_parameter_spec(self, ctx:TeradataSQLParser.Returns_parameter_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#returns_parameter_spec.
    def exitReturns_parameter_spec(self, ctx:TeradataSQLParser.Returns_parameter_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#method_language_spec.
    def enterMethod_language_spec(self, ctx:TeradataSQLParser.Method_language_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#method_language_spec.
    def exitMethod_language_spec(self, ctx:TeradataSQLParser.Method_language_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#method_attr.
    def enterMethod_attr(self, ctx:TeradataSQLParser.Method_attrContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#method_attr.
    def exitMethod_attr(self, ctx:TeradataSQLParser.Method_attrContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#multidimensional_array_dimension.
    def enterMultidimensional_array_dimension(self, ctx:TeradataSQLParser.Multidimensional_array_dimensionContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#multidimensional_array_dimension.
    def exitMultidimensional_array_dimension(self, ctx:TeradataSQLParser.Multidimensional_array_dimensionContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#multidimensional_varray_dimension.
    def enterMultidimensional_varray_dimension(self, ctx:TeradataSQLParser.Multidimensional_varray_dimensionContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#multidimensional_varray_dimension.
    def exitMultidimensional_varray_dimension(self, ctx:TeradataSQLParser.Multidimensional_varray_dimensionContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#array_bounds.
    def enterArray_bounds(self, ctx:TeradataSQLParser.Array_boundsContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#array_bounds.
    def exitArray_bounds(self, ctx:TeradataSQLParser.Array_boundsContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#bound.
    def enterBound(self, ctx:TeradataSQLParser.BoundContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#bound.
    def exitBound(self, ctx:TeradataSQLParser.BoundContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#create_user_stat.
    def enterCreate_user_stat(self, ctx:TeradataSQLParser.Create_user_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#create_user_stat.
    def exitCreate_user_stat(self, ctx:TeradataSQLParser.Create_user_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#user_attribute.
    def enterUser_attribute(self, ctx:TeradataSQLParser.User_attributeContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#user_attribute.
    def exitUser_attribute(self, ctx:TeradataSQLParser.User_attributeContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#transform_specification.
    def enterTransform_specification(self, ctx:TeradataSQLParser.Transform_specificationContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#transform_specification.
    def exitTransform_specification(self, ctx:TeradataSQLParser.Transform_specificationContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#user_constraint.
    def enterUser_constraint(self, ctx:TeradataSQLParser.User_constraintContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#user_constraint.
    def exitUser_constraint(self, ctx:TeradataSQLParser.User_constraintContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#database_stat.
    def enterDatabase_stat(self, ctx:TeradataSQLParser.Database_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#database_stat.
    def exitDatabase_stat(self, ctx:TeradataSQLParser.Database_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#delete_database_stat.
    def enterDelete_database_stat(self, ctx:TeradataSQLParser.Delete_database_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#delete_database_stat.
    def exitDelete_database_stat(self, ctx:TeradataSQLParser.Delete_database_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#delete_user_stat.
    def enterDelete_user_stat(self, ctx:TeradataSQLParser.Delete_user_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#delete_user_stat.
    def exitDelete_user_stat(self, ctx:TeradataSQLParser.Delete_user_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#drop_authorization_stat.
    def enterDrop_authorization_stat(self, ctx:TeradataSQLParser.Drop_authorization_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#drop_authorization_stat.
    def exitDrop_authorization_stat(self, ctx:TeradataSQLParser.Drop_authorization_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#drop_cast_stat.
    def enterDrop_cast_stat(self, ctx:TeradataSQLParser.Drop_cast_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#drop_cast_stat.
    def exitDrop_cast_stat(self, ctx:TeradataSQLParser.Drop_cast_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#drop_constraint_stat.
    def enterDrop_constraint_stat(self, ctx:TeradataSQLParser.Drop_constraint_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#drop_constraint_stat.
    def exitDrop_constraint_stat(self, ctx:TeradataSQLParser.Drop_constraint_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#drop_database_stat.
    def enterDrop_database_stat(self, ctx:TeradataSQLParser.Drop_database_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#drop_database_stat.
    def exitDrop_database_stat(self, ctx:TeradataSQLParser.Drop_database_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#drop_error_table_stat.
    def enterDrop_error_table_stat(self, ctx:TeradataSQLParser.Drop_error_table_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#drop_error_table_stat.
    def exitDrop_error_table_stat(self, ctx:TeradataSQLParser.Drop_error_table_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#drop_foreign_server_stat.
    def enterDrop_foreign_server_stat(self, ctx:TeradataSQLParser.Drop_foreign_server_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#drop_foreign_server_stat.
    def exitDrop_foreign_server_stat(self, ctx:TeradataSQLParser.Drop_foreign_server_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#drop_function_stat.
    def enterDrop_function_stat(self, ctx:TeradataSQLParser.Drop_function_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#drop_function_stat.
    def exitDrop_function_stat(self, ctx:TeradataSQLParser.Drop_function_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#drop_function_mapping_stat.
    def enterDrop_function_mapping_stat(self, ctx:TeradataSQLParser.Drop_function_mapping_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#drop_function_mapping_stat.
    def exitDrop_function_mapping_stat(self, ctx:TeradataSQLParser.Drop_function_mapping_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#drop_index_stat.
    def enterDrop_index_stat(self, ctx:TeradataSQLParser.Drop_index_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#drop_index_stat.
    def exitDrop_index_stat(self, ctx:TeradataSQLParser.Drop_index_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#drop_glop_set_stat.
    def enterDrop_glop_set_stat(self, ctx:TeradataSQLParser.Drop_glop_set_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#drop_glop_set_stat.
    def exitDrop_glop_set_stat(self, ctx:TeradataSQLParser.Drop_glop_set_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#drop_join_index_stat.
    def enterDrop_join_index_stat(self, ctx:TeradataSQLParser.Drop_join_index_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#drop_join_index_stat.
    def exitDrop_join_index_stat(self, ctx:TeradataSQLParser.Drop_join_index_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#drop_hash_index_stat.
    def enterDrop_hash_index_stat(self, ctx:TeradataSQLParser.Drop_hash_index_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#drop_hash_index_stat.
    def exitDrop_hash_index_stat(self, ctx:TeradataSQLParser.Drop_hash_index_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#drop_macro_stat.
    def enterDrop_macro_stat(self, ctx:TeradataSQLParser.Drop_macro_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#drop_macro_stat.
    def exitDrop_macro_stat(self, ctx:TeradataSQLParser.Drop_macro_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#drop_map_stat.
    def enterDrop_map_stat(self, ctx:TeradataSQLParser.Drop_map_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#drop_map_stat.
    def exitDrop_map_stat(self, ctx:TeradataSQLParser.Drop_map_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#drop_method_stat.
    def enterDrop_method_stat(self, ctx:TeradataSQLParser.Drop_method_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#drop_method_stat.
    def exitDrop_method_stat(self, ctx:TeradataSQLParser.Drop_method_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#drop_ordering_stat.
    def enterDrop_ordering_stat(self, ctx:TeradataSQLParser.Drop_ordering_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#drop_ordering_stat.
    def exitDrop_ordering_stat(self, ctx:TeradataSQLParser.Drop_ordering_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#drop_procedure_stat.
    def enterDrop_procedure_stat(self, ctx:TeradataSQLParser.Drop_procedure_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#drop_procedure_stat.
    def exitDrop_procedure_stat(self, ctx:TeradataSQLParser.Drop_procedure_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#drop_profile_stat.
    def enterDrop_profile_stat(self, ctx:TeradataSQLParser.Drop_profile_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#drop_profile_stat.
    def exitDrop_profile_stat(self, ctx:TeradataSQLParser.Drop_profile_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#drop_replication_group_stat.
    def enterDrop_replication_group_stat(self, ctx:TeradataSQLParser.Drop_replication_group_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#drop_replication_group_stat.
    def exitDrop_replication_group_stat(self, ctx:TeradataSQLParser.Drop_replication_group_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#drop_replication_ruleset_stat.
    def enterDrop_replication_ruleset_stat(self, ctx:TeradataSQLParser.Drop_replication_ruleset_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#drop_replication_ruleset_stat.
    def exitDrop_replication_ruleset_stat(self, ctx:TeradataSQLParser.Drop_replication_ruleset_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#drop_role_stat.
    def enterDrop_role_stat(self, ctx:TeradataSQLParser.Drop_role_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#drop_role_stat.
    def exitDrop_role_stat(self, ctx:TeradataSQLParser.Drop_role_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#drop_schema_stat.
    def enterDrop_schema_stat(self, ctx:TeradataSQLParser.Drop_schema_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#drop_schema_stat.
    def exitDrop_schema_stat(self, ctx:TeradataSQLParser.Drop_schema_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#drop_statistics_optimizer_form_stat.
    def enterDrop_statistics_optimizer_form_stat(self, ctx:TeradataSQLParser.Drop_statistics_optimizer_form_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#drop_statistics_optimizer_form_stat.
    def exitDrop_statistics_optimizer_form_stat(self, ctx:TeradataSQLParser.Drop_statistics_optimizer_form_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#drop_table_stat.
    def enterDrop_table_stat(self, ctx:TeradataSQLParser.Drop_table_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#drop_table_stat.
    def exitDrop_table_stat(self, ctx:TeradataSQLParser.Drop_table_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#drop_transform_stat.
    def enterDrop_transform_stat(self, ctx:TeradataSQLParser.Drop_transform_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#drop_transform_stat.
    def exitDrop_transform_stat(self, ctx:TeradataSQLParser.Drop_transform_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#drop_trigger_stat.
    def enterDrop_trigger_stat(self, ctx:TeradataSQLParser.Drop_trigger_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#drop_trigger_stat.
    def exitDrop_trigger_stat(self, ctx:TeradataSQLParser.Drop_trigger_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#drop_type_stat.
    def enterDrop_type_stat(self, ctx:TeradataSQLParser.Drop_type_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#drop_type_stat.
    def exitDrop_type_stat(self, ctx:TeradataSQLParser.Drop_type_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#drop_user_stat.
    def enterDrop_user_stat(self, ctx:TeradataSQLParser.Drop_user_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#drop_user_stat.
    def exitDrop_user_stat(self, ctx:TeradataSQLParser.Drop_user_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#drop_view_stat.
    def enterDrop_view_stat(self, ctx:TeradataSQLParser.Drop_view_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#drop_view_stat.
    def exitDrop_view_stat(self, ctx:TeradataSQLParser.Drop_view_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#drop_zone_stat.
    def enterDrop_zone_stat(self, ctx:TeradataSQLParser.Drop_zone_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#drop_zone_stat.
    def exitDrop_zone_stat(self, ctx:TeradataSQLParser.Drop_zone_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#end_isolated_loading_stat.
    def enterEnd_isolated_loading_stat(self, ctx:TeradataSQLParser.End_isolated_loading_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#end_isolated_loading_stat.
    def exitEnd_isolated_loading_stat(self, ctx:TeradataSQLParser.End_isolated_loading_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#end_logging_stat.
    def enterEnd_logging_stat(self, ctx:TeradataSQLParser.End_logging_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#end_logging_stat.
    def exitEnd_logging_stat(self, ctx:TeradataSQLParser.End_logging_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#end_query_capture_stat.
    def enterEnd_query_capture_stat(self, ctx:TeradataSQLParser.End_query_capture_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#end_query_capture_stat.
    def exitEnd_query_capture_stat(self, ctx:TeradataSQLParser.End_query_capture_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#end_query_logging_stat.
    def enterEnd_query_logging_stat(self, ctx:TeradataSQLParser.End_query_logging_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#end_query_logging_stat.
    def exitEnd_query_logging_stat(self, ctx:TeradataSQLParser.End_query_logging_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#end_query_logging_on_items.
    def enterEnd_query_logging_on_items(self, ctx:TeradataSQLParser.End_query_logging_on_itemsContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#end_query_logging_on_items.
    def exitEnd_query_logging_on_items(self, ctx:TeradataSQLParser.End_query_logging_on_itemsContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#end_query_logging_all_rules.
    def enterEnd_query_logging_all_rules(self, ctx:TeradataSQLParser.End_query_logging_all_rulesContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#end_query_logging_all_rules.
    def exitEnd_query_logging_all_rules(self, ctx:TeradataSQLParser.End_query_logging_all_rulesContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#flush_query_logging_stat.
    def enterFlush_query_logging_stat(self, ctx:TeradataSQLParser.Flush_query_logging_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#flush_query_logging_stat.
    def exitFlush_query_logging_stat(self, ctx:TeradataSQLParser.Flush_query_logging_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#flush_option.
    def enterFlush_option(self, ctx:TeradataSQLParser.Flush_optionContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#flush_option.
    def exitFlush_option(self, ctx:TeradataSQLParser.Flush_optionContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#HelpOnlineStat.
    def enterHelpOnlineStat(self, ctx:TeradataSQLParser.HelpOnlineStatContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#HelpOnlineStat.
    def exitHelpOnlineStat(self, ctx:TeradataSQLParser.HelpOnlineStatContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#HelpColumnListStat.
    def enterHelpColumnListStat(self, ctx:TeradataSQLParser.HelpColumnListStatContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#HelpColumnListStat.
    def exitHelpColumnListStat(self, ctx:TeradataSQLParser.HelpColumnListStatContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#HelpColumnFromStat.
    def enterHelpColumnFromStat(self, ctx:TeradataSQLParser.HelpColumnFromStatContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#HelpColumnFromStat.
    def exitHelpColumnFromStat(self, ctx:TeradataSQLParser.HelpColumnFromStatContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#HelpColumnAllFromStat.
    def enterHelpColumnAllFromStat(self, ctx:TeradataSQLParser.HelpColumnAllFromStatContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#HelpColumnAllFromStat.
    def exitHelpColumnAllFromStat(self, ctx:TeradataSQLParser.HelpColumnAllFromStatContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#HelpColumnFromErrorTableStat.
    def enterHelpColumnFromErrorTableStat(self, ctx:TeradataSQLParser.HelpColumnFromErrorTableStatContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#HelpColumnFromErrorTableStat.
    def exitHelpColumnFromErrorTableStat(self, ctx:TeradataSQLParser.HelpColumnFromErrorTableStatContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#HelpConstraintStat.
    def enterHelpConstraintStat(self, ctx:TeradataSQLParser.HelpConstraintStatContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#HelpConstraintStat.
    def exitHelpConstraintStat(self, ctx:TeradataSQLParser.HelpConstraintStatContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#HelpTableStat.
    def enterHelpTableStat(self, ctx:TeradataSQLParser.HelpTableStatContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#HelpTableStat.
    def exitHelpTableStat(self, ctx:TeradataSQLParser.HelpTableStatContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#HelpErrorTableStat.
    def enterHelpErrorTableStat(self, ctx:TeradataSQLParser.HelpErrorTableStatContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#HelpErrorTableStat.
    def exitHelpErrorTableStat(self, ctx:TeradataSQLParser.HelpErrorTableStatContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#HelpVolatileTableStat.
    def enterHelpVolatileTableStat(self, ctx:TeradataSQLParser.HelpVolatileTableStatContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#HelpVolatileTableStat.
    def exitHelpVolatileTableStat(self, ctx:TeradataSQLParser.HelpVolatileTableStatContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#HelpViewStat.
    def enterHelpViewStat(self, ctx:TeradataSQLParser.HelpViewStatContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#HelpViewStat.
    def exitHelpViewStat(self, ctx:TeradataSQLParser.HelpViewStatContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#HelpIndexStat.
    def enterHelpIndexStat(self, ctx:TeradataSQLParser.HelpIndexStatContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#HelpIndexStat.
    def exitHelpIndexStat(self, ctx:TeradataSQLParser.HelpIndexStatContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#HelpJoinIndexStat.
    def enterHelpJoinIndexStat(self, ctx:TeradataSQLParser.HelpJoinIndexStatContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#HelpJoinIndexStat.
    def exitHelpJoinIndexStat(self, ctx:TeradataSQLParser.HelpJoinIndexStatContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#HelpHashIndexStat.
    def enterHelpHashIndexStat(self, ctx:TeradataSQLParser.HelpHashIndexStatContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#HelpHashIndexStat.
    def exitHelpHashIndexStat(self, ctx:TeradataSQLParser.HelpHashIndexStatContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#HelpProcedureStat.
    def enterHelpProcedureStat(self, ctx:TeradataSQLParser.HelpProcedureStatContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#HelpProcedureStat.
    def exitHelpProcedureStat(self, ctx:TeradataSQLParser.HelpProcedureStatContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#HelpFunctionStat.
    def enterHelpFunctionStat(self, ctx:TeradataSQLParser.HelpFunctionStatContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#HelpFunctionStat.
    def exitHelpFunctionStat(self, ctx:TeradataSQLParser.HelpFunctionStatContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#HelpSpecificFunctionStat.
    def enterHelpSpecificFunctionStat(self, ctx:TeradataSQLParser.HelpSpecificFunctionStatContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#HelpSpecificFunctionStat.
    def exitHelpSpecificFunctionStat(self, ctx:TeradataSQLParser.HelpSpecificFunctionStatContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#HelpMethodStat.
    def enterHelpMethodStat(self, ctx:TeradataSQLParser.HelpMethodStatContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#HelpMethodStat.
    def exitHelpMethodStat(self, ctx:TeradataSQLParser.HelpMethodStatContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#HelpSpecificMethodStat.
    def enterHelpSpecificMethodStat(self, ctx:TeradataSQLParser.HelpSpecificMethodStatContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#HelpSpecificMethodStat.
    def exitHelpSpecificMethodStat(self, ctx:TeradataSQLParser.HelpSpecificMethodStatContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#HelpTypeStat.
    def enterHelpTypeStat(self, ctx:TeradataSQLParser.HelpTypeStatContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#HelpTypeStat.
    def exitHelpTypeStat(self, ctx:TeradataSQLParser.HelpTypeStatContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#HelpStorageFormatSchemaStat.
    def enterHelpStorageFormatSchemaStat(self, ctx:TeradataSQLParser.HelpStorageFormatSchemaStatContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#HelpStorageFormatSchemaStat.
    def exitHelpStorageFormatSchemaStat(self, ctx:TeradataSQLParser.HelpStorageFormatSchemaStatContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#HelpCastStat.
    def enterHelpCastStat(self, ctx:TeradataSQLParser.HelpCastStatContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#HelpCastStat.
    def exitHelpCastStat(self, ctx:TeradataSQLParser.HelpCastStatContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#HelpTransformStat.
    def enterHelpTransformStat(self, ctx:TeradataSQLParser.HelpTransformStatContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#HelpTransformStat.
    def exitHelpTransformStat(self, ctx:TeradataSQLParser.HelpTransformStatContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#HelpDatabaseStat.
    def enterHelpDatabaseStat(self, ctx:TeradataSQLParser.HelpDatabaseStatContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#HelpDatabaseStat.
    def exitHelpDatabaseStat(self, ctx:TeradataSQLParser.HelpDatabaseStatContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#HelpUserStat.
    def enterHelpUserStat(self, ctx:TeradataSQLParser.HelpUserStatContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#HelpUserStat.
    def exitHelpUserStat(self, ctx:TeradataSQLParser.HelpUserStatContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#HelpTriggerStat.
    def enterHelpTriggerStat(self, ctx:TeradataSQLParser.HelpTriggerStatContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#HelpTriggerStat.
    def exitHelpTriggerStat(self, ctx:TeradataSQLParser.HelpTriggerStatContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#HelpForeignServer.
    def enterHelpForeignServer(self, ctx:TeradataSQLParser.HelpForeignServerContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#HelpForeignServer.
    def exitHelpForeignServer(self, ctx:TeradataSQLParser.HelpForeignServerContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#HelpForeignDatabase.
    def enterHelpForeignDatabase(self, ctx:TeradataSQLParser.HelpForeignDatabaseContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#HelpForeignDatabase.
    def exitHelpForeignDatabase(self, ctx:TeradataSQLParser.HelpForeignDatabaseContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#HelpForeignTable.
    def enterHelpForeignTable(self, ctx:TeradataSQLParser.HelpForeignTableContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#HelpForeignTable.
    def exitHelpForeignTable(self, ctx:TeradataSQLParser.HelpForeignTableContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#HelpForeignFunction.
    def enterHelpForeignFunction(self, ctx:TeradataSQLParser.HelpForeignFunctionContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#HelpForeignFunction.
    def exitHelpForeignFunction(self, ctx:TeradataSQLParser.HelpForeignFunctionContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#help_statistics_optimimizer_form_stat.
    def enterHelp_statistics_optimimizer_form_stat(self, ctx:TeradataSQLParser.Help_statistics_optimimizer_form_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#help_statistics_optimimizer_form_stat.
    def exitHelp_statistics_optimimizer_form_stat(self, ctx:TeradataSQLParser.Help_statistics_optimimizer_form_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#help_statistics_qcd_form_stat.
    def enterHelp_statistics_qcd_form_stat(self, ctx:TeradataSQLParser.Help_statistics_qcd_form_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#help_statistics_qcd_form_stat.
    def exitHelp_statistics_qcd_form_stat(self, ctx:TeradataSQLParser.Help_statistics_qcd_form_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#incremental_restore_allow_write_stat.
    def enterIncremental_restore_allow_write_stat(self, ctx:TeradataSQLParser.Incremental_restore_allow_write_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#incremental_restore_allow_write_stat.
    def exitIncremental_restore_allow_write_stat(self, ctx:TeradataSQLParser.Incremental_restore_allow_write_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#logging_incremental_archive_off_stat.
    def enterLogging_incremental_archive_off_stat(self, ctx:TeradataSQLParser.Logging_incremental_archive_off_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#logging_incremental_archive_off_stat.
    def exitLogging_incremental_archive_off_stat(self, ctx:TeradataSQLParser.Logging_incremental_archive_off_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#logging_incremental_archive_on_stat.
    def enterLogging_incremental_archive_on_stat(self, ctx:TeradataSQLParser.Logging_incremental_archive_on_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#logging_incremental_archive_on_stat.
    def exitLogging_incremental_archive_on_stat(self, ctx:TeradataSQLParser.Logging_incremental_archive_on_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#modify_database_stat.
    def enterModify_database_stat(self, ctx:TeradataSQLParser.Modify_database_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#modify_database_stat.
    def exitModify_database_stat(self, ctx:TeradataSQLParser.Modify_database_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#modified_database_attribute.
    def enterModified_database_attribute(self, ctx:TeradataSQLParser.Modified_database_attributeContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#modified_database_attribute.
    def exitModified_database_attribute(self, ctx:TeradataSQLParser.Modified_database_attributeContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#modify_profile_stat.
    def enterModify_profile_stat(self, ctx:TeradataSQLParser.Modify_profile_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#modify_profile_stat.
    def exitModify_profile_stat(self, ctx:TeradataSQLParser.Modify_profile_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#modify_user_stat.
    def enterModify_user_stat(self, ctx:TeradataSQLParser.Modify_user_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#modify_user_stat.
    def exitModify_user_stat(self, ctx:TeradataSQLParser.Modify_user_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#modify_user_attribute.
    def enterModify_user_attribute(self, ctx:TeradataSQLParser.Modify_user_attributeContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#modify_user_attribute.
    def exitModify_user_attribute(self, ctx:TeradataSQLParser.Modify_user_attributeContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#rename_function_stat.
    def enterRename_function_stat(self, ctx:TeradataSQLParser.Rename_function_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#rename_function_stat.
    def exitRename_function_stat(self, ctx:TeradataSQLParser.Rename_function_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#rename_procedure_stat.
    def enterRename_procedure_stat(self, ctx:TeradataSQLParser.Rename_procedure_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#rename_procedure_stat.
    def exitRename_procedure_stat(self, ctx:TeradataSQLParser.Rename_procedure_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#rename_macro_stat.
    def enterRename_macro_stat(self, ctx:TeradataSQLParser.Rename_macro_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#rename_macro_stat.
    def exitRename_macro_stat(self, ctx:TeradataSQLParser.Rename_macro_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#rename_table_stat.
    def enterRename_table_stat(self, ctx:TeradataSQLParser.Rename_table_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#rename_table_stat.
    def exitRename_table_stat(self, ctx:TeradataSQLParser.Rename_table_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#rename_trigger_stat.
    def enterRename_trigger_stat(self, ctx:TeradataSQLParser.Rename_trigger_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#rename_trigger_stat.
    def exitRename_trigger_stat(self, ctx:TeradataSQLParser.Rename_trigger_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#rename_view_stat.
    def enterRename_view_stat(self, ctx:TeradataSQLParser.Rename_view_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#rename_view_stat.
    def exitRename_view_stat(self, ctx:TeradataSQLParser.Rename_view_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#replace_query_logging_stat.
    def enterReplace_query_logging_stat(self, ctx:TeradataSQLParser.Replace_query_logging_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#replace_query_logging_stat.
    def exitReplace_query_logging_stat(self, ctx:TeradataSQLParser.Replace_query_logging_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#set_session_stat.
    def enterSet_session_stat(self, ctx:TeradataSQLParser.Set_session_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#set_session_stat.
    def exitSet_session_stat(self, ctx:TeradataSQLParser.Set_session_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#collation_sequence.
    def enterCollation_sequence(self, ctx:TeradataSQLParser.Collation_sequenceContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#collation_sequence.
    def exitCollation_sequence(self, ctx:TeradataSQLParser.Collation_sequenceContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#session_constraint.
    def enterSession_constraint(self, ctx:TeradataSQLParser.Session_constraintContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#session_constraint.
    def exitSession_constraint(self, ctx:TeradataSQLParser.Session_constraintContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#isolation_level.
    def enterIsolation_level(self, ctx:TeradataSQLParser.Isolation_levelContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#isolation_level.
    def exitIsolation_level(self, ctx:TeradataSQLParser.Isolation_levelContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#session_debug_spec.
    def enterSession_debug_spec(self, ctx:TeradataSQLParser.Session_debug_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#session_debug_spec.
    def exitSession_debug_spec(self, ctx:TeradataSQLParser.Session_debug_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#trace_enabling_spec.
    def enterTrace_enabling_spec(self, ctx:TeradataSQLParser.Trace_enabling_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#trace_enabling_spec.
    def exitTrace_enabling_spec(self, ctx:TeradataSQLParser.Trace_enabling_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#set_role_stat.
    def enterSet_role_stat(self, ctx:TeradataSQLParser.Set_role_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#set_role_stat.
    def exitSet_role_stat(self, ctx:TeradataSQLParser.Set_role_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#set_query_band_stat.
    def enterSet_query_band_stat(self, ctx:TeradataSQLParser.Set_query_band_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#set_query_band_stat.
    def exitSet_query_band_stat(self, ctx:TeradataSQLParser.Set_query_band_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#ShowHashIndexStat.
    def enterShowHashIndexStat(self, ctx:TeradataSQLParser.ShowHashIndexStatContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#ShowHashIndexStat.
    def exitShowHashIndexStat(self, ctx:TeradataSQLParser.ShowHashIndexStatContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#ShowJoinIndexStat.
    def enterShowJoinIndexStat(self, ctx:TeradataSQLParser.ShowJoinIndexStatContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#ShowJoinIndexStat.
    def exitShowJoinIndexStat(self, ctx:TeradataSQLParser.ShowJoinIndexStatContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#ShowMacroStat.
    def enterShowMacroStat(self, ctx:TeradataSQLParser.ShowMacroStatContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#ShowMacroStat.
    def exitShowMacroStat(self, ctx:TeradataSQLParser.ShowMacroStatContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#ShowTableStat.
    def enterShowTableStat(self, ctx:TeradataSQLParser.ShowTableStatContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#ShowTableStat.
    def exitShowTableStat(self, ctx:TeradataSQLParser.ShowTableStatContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#ShowErrorTableStat.
    def enterShowErrorTableStat(self, ctx:TeradataSQLParser.ShowErrorTableStatContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#ShowErrorTableStat.
    def exitShowErrorTableStat(self, ctx:TeradataSQLParser.ShowErrorTableStatContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#ShowTriggerStat.
    def enterShowTriggerStat(self, ctx:TeradataSQLParser.ShowTriggerStatContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#ShowTriggerStat.
    def exitShowTriggerStat(self, ctx:TeradataSQLParser.ShowTriggerStatContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#ShowViewStat.
    def enterShowViewStat(self, ctx:TeradataSQLParser.ShowViewStatContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#ShowViewStat.
    def exitShowViewStat(self, ctx:TeradataSQLParser.ShowViewStatContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#ShowProcedureStat.
    def enterShowProcedureStat(self, ctx:TeradataSQLParser.ShowProcedureStatContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#ShowProcedureStat.
    def exitShowProcedureStat(self, ctx:TeradataSQLParser.ShowProcedureStatContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#ShowSpecificFunctionStat.
    def enterShowSpecificFunctionStat(self, ctx:TeradataSQLParser.ShowSpecificFunctionStatContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#ShowSpecificFunctionStat.
    def exitShowSpecificFunctionStat(self, ctx:TeradataSQLParser.ShowSpecificFunctionStatContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#ShowFunctionStat.
    def enterShowFunctionStat(self, ctx:TeradataSQLParser.ShowFunctionStatContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#ShowFunctionStat.
    def exitShowFunctionStat(self, ctx:TeradataSQLParser.ShowFunctionStatContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#ShowSpecificMethodStat.
    def enterShowSpecificMethodStat(self, ctx:TeradataSQLParser.ShowSpecificMethodStatContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#ShowSpecificMethodStat.
    def exitShowSpecificMethodStat(self, ctx:TeradataSQLParser.ShowSpecificMethodStatContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#ShowMethodStat.
    def enterShowMethodStat(self, ctx:TeradataSQLParser.ShowMethodStatContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#ShowMethodStat.
    def exitShowMethodStat(self, ctx:TeradataSQLParser.ShowMethodStatContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#ShowCastStat.
    def enterShowCastStat(self, ctx:TeradataSQLParser.ShowCastStatContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#ShowCastStat.
    def exitShowCastStat(self, ctx:TeradataSQLParser.ShowCastStatContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#ShowTypeStat.
    def enterShowTypeStat(self, ctx:TeradataSQLParser.ShowTypeStatContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#ShowTypeStat.
    def exitShowTypeStat(self, ctx:TeradataSQLParser.ShowTypeStatContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#ShowStorageFormatSchemaStat.
    def enterShowStorageFormatSchemaStat(self, ctx:TeradataSQLParser.ShowStorageFormatSchemaStatContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#ShowStorageFormatSchemaStat.
    def exitShowStorageFormatSchemaStat(self, ctx:TeradataSQLParser.ShowStorageFormatSchemaStatContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#ShowFileStat.
    def enterShowFileStat(self, ctx:TeradataSQLParser.ShowFileStatContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#ShowFileStat.
    def exitShowFileStat(self, ctx:TeradataSQLParser.ShowFileStatContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#ShowConstraintStat.
    def enterShowConstraintStat(self, ctx:TeradataSQLParser.ShowConstraintStatContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#ShowConstraintStat.
    def exitShowConstraintStat(self, ctx:TeradataSQLParser.ShowConstraintStatContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#ShowAuthorizationStat.
    def enterShowAuthorizationStat(self, ctx:TeradataSQLParser.ShowAuthorizationStatContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#ShowAuthorizationStat.
    def exitShowAuthorizationStat(self, ctx:TeradataSQLParser.ShowAuthorizationStatContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#ShowGlopSetStat.
    def enterShowGlopSetStat(self, ctx:TeradataSQLParser.ShowGlopSetStatContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#ShowGlopSetStat.
    def exitShowGlopSetStat(self, ctx:TeradataSQLParser.ShowGlopSetStatContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#ShowForeignServer.
    def enterShowForeignServer(self, ctx:TeradataSQLParser.ShowForeignServerContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#ShowForeignServer.
    def exitShowForeignServer(self, ctx:TeradataSQLParser.ShowForeignServerContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#show_query_logging_stat.
    def enterShow_query_logging_stat(self, ctx:TeradataSQLParser.Show_query_logging_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#show_query_logging_stat.
    def exitShow_query_logging_stat(self, ctx:TeradataSQLParser.Show_query_logging_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#show_request_stat.
    def enterShow_request_stat(self, ctx:TeradataSQLParser.Show_request_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#show_request_stat.
    def exitShow_request_stat(self, ctx:TeradataSQLParser.Show_request_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#show_statistics_optimizer_form_stat.
    def enterShow_statistics_optimizer_form_stat(self, ctx:TeradataSQLParser.Show_statistics_optimizer_form_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#show_statistics_optimizer_form_stat.
    def exitShow_statistics_optimizer_form_stat(self, ctx:TeradataSQLParser.Show_statistics_optimizer_form_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#show_statistics_qcd_form_stat.
    def enterShow_statistics_qcd_form_stat(self, ctx:TeradataSQLParser.Show_statistics_qcd_form_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#show_statistics_qcd_form_stat.
    def exitShow_statistics_qcd_form_stat(self, ctx:TeradataSQLParser.Show_statistics_qcd_form_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#show_stats_target_spec.
    def enterShow_stats_target_spec(self, ctx:TeradataSQLParser.Show_stats_target_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#show_stats_target_spec.
    def exitShow_stats_target_spec(self, ctx:TeradataSQLParser.Show_stats_target_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#method.
    def enterMethod(self, ctx:TeradataSQLParser.MethodContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#method.
    def exitMethod(self, ctx:TeradataSQLParser.MethodContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#index_loading.
    def enterIndex_loading(self, ctx:TeradataSQLParser.Index_loadingContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#index_loading.
    def exitIndex_loading(self, ctx:TeradataSQLParser.Index_loadingContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#index_ordering.
    def enterIndex_ordering(self, ctx:TeradataSQLParser.Index_orderingContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#index_ordering.
    def exitIndex_ordering(self, ctx:TeradataSQLParser.Index_orderingContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#table_option_index_form.
    def enterTable_option_index_form(self, ctx:TeradataSQLParser.Table_option_index_formContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#table_option_index_form.
    def exitTable_option_index_form(self, ctx:TeradataSQLParser.Table_option_index_formContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#map_spec.
    def enterMap_spec(self, ctx:TeradataSQLParser.Map_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#map_spec.
    def exitMap_spec(self, ctx:TeradataSQLParser.Map_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#database_size_spec.
    def enterDatabase_size_spec(self, ctx:TeradataSQLParser.Database_size_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#database_size_spec.
    def exitDatabase_size_spec(self, ctx:TeradataSQLParser.Database_size_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#skew_spec.
    def enterSkew_spec(self, ctx:TeradataSQLParser.Skew_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#skew_spec.
    def exitSkew_spec(self, ctx:TeradataSQLParser.Skew_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#database_default_map.
    def enterDatabase_default_map(self, ctx:TeradataSQLParser.Database_default_mapContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#database_default_map.
    def exitDatabase_default_map(self, ctx:TeradataSQLParser.Database_default_mapContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#fallback_protection.
    def enterFallback_protection(self, ctx:TeradataSQLParser.Fallback_protectionContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#fallback_protection.
    def exitFallback_protection(self, ctx:TeradataSQLParser.Fallback_protectionContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#before_journal.
    def enterBefore_journal(self, ctx:TeradataSQLParser.Before_journalContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#before_journal.
    def exitBefore_journal(self, ctx:TeradataSQLParser.Before_journalContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#after_journal.
    def enterAfter_journal(self, ctx:TeradataSQLParser.After_journalContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#after_journal.
    def exitAfter_journal(self, ctx:TeradataSQLParser.After_journalContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#default_journal_table.
    def enterDefault_journal_table(self, ctx:TeradataSQLParser.Default_journal_tableContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#default_journal_table.
    def exitDefault_journal_table(self, ctx:TeradataSQLParser.Default_journal_tableContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#drop_default_journal_table.
    def enterDrop_default_journal_table(self, ctx:TeradataSQLParser.Drop_default_journal_tableContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#drop_default_journal_table.
    def exitDrop_default_journal_table(self, ctx:TeradataSQLParser.Drop_default_journal_tableContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#password.
    def enterPassword(self, ctx:TeradataSQLParser.PasswordContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#password.
    def exitPassword(self, ctx:TeradataSQLParser.PasswordContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#dml_stat.
    def enterDml_stat(self, ctx:TeradataSQLParser.Dml_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#dml_stat.
    def exitDml_stat(self, ctx:TeradataSQLParser.Dml_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#select_stat.
    def enterSelect_stat(self, ctx:TeradataSQLParser.Select_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#select_stat.
    def exitSelect_stat(self, ctx:TeradataSQLParser.Select_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#select_and_consume_stat.
    def enterSelect_and_consume_stat(self, ctx:TeradataSQLParser.Select_and_consume_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#select_and_consume_stat.
    def exitSelect_and_consume_stat(self, ctx:TeradataSQLParser.Select_and_consume_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#delete_stat.
    def enterDelete_stat(self, ctx:TeradataSQLParser.Delete_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#delete_stat.
    def exitDelete_stat(self, ctx:TeradataSQLParser.Delete_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#delete_table_spec.
    def enterDelete_table_spec(self, ctx:TeradataSQLParser.Delete_table_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#delete_table_spec.
    def exitDelete_table_spec(self, ctx:TeradataSQLParser.Delete_table_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#insert_stat.
    def enterInsert_stat(self, ctx:TeradataSQLParser.Insert_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#insert_stat.
    def exitInsert_stat(self, ctx:TeradataSQLParser.Insert_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#hash_by.
    def enterHash_by(self, ctx:TeradataSQLParser.Hash_byContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#hash_by.
    def exitHash_by(self, ctx:TeradataSQLParser.Hash_byContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#local_order_by.
    def enterLocal_order_by(self, ctx:TeradataSQLParser.Local_order_byContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#local_order_by.
    def exitLocal_order_by(self, ctx:TeradataSQLParser.Local_order_byContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#update_stat.
    def enterUpdate_stat(self, ctx:TeradataSQLParser.Update_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#update_stat.
    def exitUpdate_stat(self, ctx:TeradataSQLParser.Update_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#update_basic_form_stat.
    def enterUpdate_basic_form_stat(self, ctx:TeradataSQLParser.Update_basic_form_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#update_basic_form_stat.
    def exitUpdate_basic_form_stat(self, ctx:TeradataSQLParser.Update_basic_form_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#update_with_from_stat.
    def enterUpdate_with_from_stat(self, ctx:TeradataSQLParser.Update_with_from_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#update_with_from_stat.
    def exitUpdate_with_from_stat(self, ctx:TeradataSQLParser.Update_with_from_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#update_upsert_form_stat.
    def enterUpdate_upsert_form_stat(self, ctx:TeradataSQLParser.Update_upsert_form_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#update_upsert_form_stat.
    def exitUpdate_upsert_form_stat(self, ctx:TeradataSQLParser.Update_upsert_form_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#update_table_spec.
    def enterUpdate_table_spec(self, ctx:TeradataSQLParser.Update_table_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#update_table_spec.
    def exitUpdate_table_spec(self, ctx:TeradataSQLParser.Update_table_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#merge_stat.
    def enterMerge_stat(self, ctx:TeradataSQLParser.Merge_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#merge_stat.
    def exitMerge_stat(self, ctx:TeradataSQLParser.Merge_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#when_matched.
    def enterWhen_matched(self, ctx:TeradataSQLParser.When_matchedContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#when_matched.
    def exitWhen_matched(self, ctx:TeradataSQLParser.When_matchedContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#when_not_matched.
    def enterWhen_not_matched(self, ctx:TeradataSQLParser.When_not_matchedContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#when_not_matched.
    def exitWhen_not_matched(self, ctx:TeradataSQLParser.When_not_matchedContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#collect_demographics_stat.
    def enterCollect_demographics_stat(self, ctx:TeradataSQLParser.Collect_demographics_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#collect_demographics_stat.
    def exitCollect_demographics_stat(self, ctx:TeradataSQLParser.Collect_demographics_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#collect_statistics_qcd_form_stat.
    def enterCollect_statistics_qcd_form_stat(self, ctx:TeradataSQLParser.Collect_statistics_qcd_form_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#collect_statistics_qcd_form_stat.
    def exitCollect_statistics_qcd_form_stat(self, ctx:TeradataSQLParser.Collect_statistics_qcd_form_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#qcd_stats_target_spec.
    def enterQcd_stats_target_spec(self, ctx:TeradataSQLParser.Qcd_stats_target_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#qcd_stats_target_spec.
    def exitQcd_stats_target_spec(self, ctx:TeradataSQLParser.Qcd_stats_target_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#drop_statistics_qcd_form_stat.
    def enterDrop_statistics_qcd_form_stat(self, ctx:TeradataSQLParser.Drop_statistics_qcd_form_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#drop_statistics_qcd_form_stat.
    def exitDrop_statistics_qcd_form_stat(self, ctx:TeradataSQLParser.Drop_statistics_qcd_form_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#dump_explain_stat.
    def enterDump_explain_stat(self, ctx:TeradataSQLParser.Dump_explain_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#dump_explain_stat.
    def exitDump_explain_stat(self, ctx:TeradataSQLParser.Dump_explain_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#initiate_index_analysis_stat.
    def enterInitiate_index_analysis_stat(self, ctx:TeradataSQLParser.Initiate_index_analysis_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#initiate_index_analysis_stat.
    def exitInitiate_index_analysis_stat(self, ctx:TeradataSQLParser.Initiate_index_analysis_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#index_analysis_set_spec.
    def enterIndex_analysis_set_spec(self, ctx:TeradataSQLParser.Index_analysis_set_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#index_analysis_set_spec.
    def exitIndex_analysis_set_spec(self, ctx:TeradataSQLParser.Index_analysis_set_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#index_analysis_boundary_option.
    def enterIndex_analysis_boundary_option(self, ctx:TeradataSQLParser.Index_analysis_boundary_optionContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#index_analysis_boundary_option.
    def exitIndex_analysis_boundary_option(self, ctx:TeradataSQLParser.Index_analysis_boundary_optionContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#initiate_partition_analysis_stat.
    def enterInitiate_partition_analysis_stat(self, ctx:TeradataSQLParser.Initiate_partition_analysis_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#initiate_partition_analysis_stat.
    def exitInitiate_partition_analysis_stat(self, ctx:TeradataSQLParser.Initiate_partition_analysis_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#insert_explain_stat.
    def enterInsert_explain_stat(self, ctx:TeradataSQLParser.Insert_explain_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#insert_explain_stat.
    def exitInsert_explain_stat(self, ctx:TeradataSQLParser.Insert_explain_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#restart_index_analysis_stat.
    def enterRestart_index_analysis_stat(self, ctx:TeradataSQLParser.Restart_index_analysis_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#restart_index_analysis_stat.
    def exitRestart_index_analysis_stat(self, ctx:TeradataSQLParser.Restart_index_analysis_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#call_stat.
    def enterCall_stat(self, ctx:TeradataSQLParser.Call_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#call_stat.
    def exitCall_stat(self, ctx:TeradataSQLParser.Call_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#argument.
    def enterArgument(self, ctx:TeradataSQLParser.ArgumentContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#argument.
    def exitArgument(self, ctx:TeradataSQLParser.ArgumentContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#execute_stat.
    def enterExecute_stat(self, ctx:TeradataSQLParser.Execute_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#execute_stat.
    def exitExecute_stat(self, ctx:TeradataSQLParser.Execute_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#commit_stat.
    def enterCommit_stat(self, ctx:TeradataSQLParser.Commit_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#commit_stat.
    def exitCommit_stat(self, ctx:TeradataSQLParser.Commit_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#rollback_stat.
    def enterRollback_stat(self, ctx:TeradataSQLParser.Rollback_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#rollback_stat.
    def exitRollback_stat(self, ctx:TeradataSQLParser.Rollback_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#abort_stat.
    def enterAbort_stat(self, ctx:TeradataSQLParser.Abort_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#abort_stat.
    def exitAbort_stat(self, ctx:TeradataSQLParser.Abort_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#begin_transaction_stat.
    def enterBegin_transaction_stat(self, ctx:TeradataSQLParser.Begin_transaction_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#begin_transaction_stat.
    def exitBegin_transaction_stat(self, ctx:TeradataSQLParser.Begin_transaction_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#end_transaction_stat.
    def enterEnd_transaction_stat(self, ctx:TeradataSQLParser.End_transaction_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#end_transaction_stat.
    def exitEnd_transaction_stat(self, ctx:TeradataSQLParser.End_transaction_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#locking_stat.
    def enterLocking_stat(self, ctx:TeradataSQLParser.Locking_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#locking_stat.
    def exitLocking_stat(self, ctx:TeradataSQLParser.Locking_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#comment_retrieving_stat.
    def enterComment_retrieving_stat(self, ctx:TeradataSQLParser.Comment_retrieving_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#comment_retrieving_stat.
    def exitComment_retrieving_stat(self, ctx:TeradataSQLParser.Comment_retrieving_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#checkpoint_stat.
    def enterCheckpoint_stat(self, ctx:TeradataSQLParser.Checkpoint_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#checkpoint_stat.
    def exitCheckpoint_stat(self, ctx:TeradataSQLParser.Checkpoint_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#echo_stat.
    def enterEcho_stat(self, ctx:TeradataSQLParser.Echo_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#echo_stat.
    def exitEcho_stat(self, ctx:TeradataSQLParser.Echo_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#null_stat.
    def enterNull_stat(self, ctx:TeradataSQLParser.Null_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#null_stat.
    def exitNull_stat(self, ctx:TeradataSQLParser.Null_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#set_spec.
    def enterSet_spec(self, ctx:TeradataSQLParser.Set_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#set_spec.
    def exitSet_spec(self, ctx:TeradataSQLParser.Set_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#with_isolated_loading.
    def enterWith_isolated_loading(self, ctx:TeradataSQLParser.With_isolated_loadingContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#with_isolated_loading.
    def exitWith_isolated_loading(self, ctx:TeradataSQLParser.With_isolated_loadingContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#logging_errors.
    def enterLogging_errors(self, ctx:TeradataSQLParser.Logging_errorsContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#logging_errors.
    def exitLogging_errors(self, ctx:TeradataSQLParser.Logging_errorsContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#object_kind.
    def enterObject_kind(self, ctx:TeradataSQLParser.Object_kindContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#object_kind.
    def exitObject_kind(self, ctx:TeradataSQLParser.Object_kindContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#explained_sql_request.
    def enterExplained_sql_request(self, ctx:TeradataSQLParser.Explained_sql_requestContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#explained_sql_request.
    def exitExplained_sql_request(self, ctx:TeradataSQLParser.Explained_sql_requestContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#limit_sql_clause.
    def enterLimit_sql_clause(self, ctx:TeradataSQLParser.Limit_sql_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#limit_sql_clause.
    def exitLimit_sql_clause(self, ctx:TeradataSQLParser.Limit_sql_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#analysis_time_limit_clause.
    def enterAnalysis_time_limit_clause(self, ctx:TeradataSQLParser.Analysis_time_limit_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#analysis_time_limit_clause.
    def exitAnalysis_time_limit_clause(self, ctx:TeradataSQLParser.Analysis_time_limit_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#data_type.
    def enterData_type(self, ctx:TeradataSQLParser.Data_typeContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#data_type.
    def exitData_type(self, ctx:TeradataSQLParser.Data_typeContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#variable_data_type.
    def enterVariable_data_type(self, ctx:TeradataSQLParser.Variable_data_typeContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#variable_data_type.
    def exitVariable_data_type(self, ctx:TeradataSQLParser.Variable_data_typeContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#external_function_data_type.
    def enterExternal_function_data_type(self, ctx:TeradataSQLParser.External_function_data_typeContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#external_function_data_type.
    def exitExternal_function_data_type(self, ctx:TeradataSQLParser.External_function_data_typeContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#numeric_data_type.
    def enterNumeric_data_type(self, ctx:TeradataSQLParser.Numeric_data_typeContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#numeric_data_type.
    def exitNumeric_data_type(self, ctx:TeradataSQLParser.Numeric_data_typeContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#char_data_type.
    def enterChar_data_type(self, ctx:TeradataSQLParser.Char_data_typeContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#char_data_type.
    def exitChar_data_type(self, ctx:TeradataSQLParser.Char_data_typeContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#precisionless_char_data_type.
    def enterPrecisionless_char_data_type(self, ctx:TeradataSQLParser.Precisionless_char_data_typeContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#precisionless_char_data_type.
    def exitPrecisionless_char_data_type(self, ctx:TeradataSQLParser.Precisionless_char_data_typeContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#lob_as_locator_data_type.
    def enterLob_as_locator_data_type(self, ctx:TeradataSQLParser.Lob_as_locator_data_typeContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#lob_as_locator_data_type.
    def exitLob_as_locator_data_type(self, ctx:TeradataSQLParser.Lob_as_locator_data_typeContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#binary_data_type.
    def enterBinary_data_type(self, ctx:TeradataSQLParser.Binary_data_typeContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#binary_data_type.
    def exitBinary_data_type(self, ctx:TeradataSQLParser.Binary_data_typeContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#datetime_type.
    def enterDatetime_type(self, ctx:TeradataSQLParser.Datetime_typeContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#datetime_type.
    def exitDatetime_type(self, ctx:TeradataSQLParser.Datetime_typeContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#period_type.
    def enterPeriod_type(self, ctx:TeradataSQLParser.Period_typeContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#period_type.
    def exitPeriod_type(self, ctx:TeradataSQLParser.Period_typeContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#udt_type.
    def enterUdt_type(self, ctx:TeradataSQLParser.Udt_typeContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#udt_type.
    def exitUdt_type(self, ctx:TeradataSQLParser.Udt_typeContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#data_type_attribute.
    def enterData_type_attribute(self, ctx:TeradataSQLParser.Data_type_attributeContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#data_type_attribute.
    def exitData_type_attribute(self, ctx:TeradataSQLParser.Data_type_attributeContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#default_value_control_phrase.
    def enterDefault_value_control_phrase(self, ctx:TeradataSQLParser.Default_value_control_phraseContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#default_value_control_phrase.
    def exitDefault_value_control_phrase(self, ctx:TeradataSQLParser.Default_value_control_phraseContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#default_value.
    def enterDefault_value(self, ctx:TeradataSQLParser.Default_valueContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#default_value.
    def exitDefault_value(self, ctx:TeradataSQLParser.Default_valueContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#column_naming_phrase.
    def enterColumn_naming_phrase(self, ctx:TeradataSQLParser.Column_naming_phraseContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#column_naming_phrase.
    def exitColumn_naming_phrase(self, ctx:TeradataSQLParser.Column_naming_phraseContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#sysudtlib.
    def enterSysudtlib(self, ctx:TeradataSQLParser.SysudtlibContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#sysudtlib.
    def exitSysudtlib(self, ctx:TeradataSQLParser.SysudtlibContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#interval_period_spec.
    def enterInterval_period_spec(self, ctx:TeradataSQLParser.Interval_period_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#interval_period_spec.
    def exitInterval_period_spec(self, ctx:TeradataSQLParser.Interval_period_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#type_precision.
    def enterType_precision(self, ctx:TeradataSQLParser.Type_precisionContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#type_precision.
    def exitType_precision(self, ctx:TeradataSQLParser.Type_precisionContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#max_length_k_m_g.
    def enterMax_length_k_m_g(self, ctx:TeradataSQLParser.Max_length_k_m_gContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#max_length_k_m_g.
    def exitMax_length_k_m_g(self, ctx:TeradataSQLParser.Max_length_k_m_gContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#max_length_k_m.
    def enterMax_length_k_m(self, ctx:TeradataSQLParser.Max_length_k_mContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#max_length_k_m.
    def exitMax_length_k_m(self, ctx:TeradataSQLParser.Max_length_k_mContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#character_set_phrase.
    def enterCharacter_set_phrase(self, ctx:TeradataSQLParser.Character_set_phraseContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#character_set_phrase.
    def exitCharacter_set_phrase(self, ctx:TeradataSQLParser.Character_set_phraseContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#uppercase_phrase.
    def enterUppercase_phrase(self, ctx:TeradataSQLParser.Uppercase_phraseContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#uppercase_phrase.
    def exitUppercase_phrase(self, ctx:TeradataSQLParser.Uppercase_phraseContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#casespecific_phrase.
    def enterCasespecific_phrase(self, ctx:TeradataSQLParser.Casespecific_phraseContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#casespecific_phrase.
    def exitCasespecific_phrase(self, ctx:TeradataSQLParser.Casespecific_phraseContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#format_phrase.
    def enterFormat_phrase(self, ctx:TeradataSQLParser.Format_phraseContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#format_phrase.
    def exitFormat_phrase(self, ctx:TeradataSQLParser.Format_phraseContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#title_phrase.
    def enterTitle_phrase(self, ctx:TeradataSQLParser.Title_phraseContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#title_phrase.
    def exitTitle_phrase(self, ctx:TeradataSQLParser.Title_phraseContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#named_phrase.
    def enterNamed_phrase(self, ctx:TeradataSQLParser.Named_phraseContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#named_phrase.
    def exitNamed_phrase(self, ctx:TeradataSQLParser.Named_phraseContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#latin_unicode_character_set_phrase.
    def enterLatin_unicode_character_set_phrase(self, ctx:TeradataSQLParser.Latin_unicode_character_set_phraseContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#latin_unicode_character_set_phrase.
    def exitLatin_unicode_character_set_phrase(self, ctx:TeradataSQLParser.Latin_unicode_character_set_phraseContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#inline_length.
    def enterInline_length(self, ctx:TeradataSQLParser.Inline_lengthContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#inline_length.
    def exitInline_length(self, ctx:TeradataSQLParser.Inline_lengthContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#json_storage_format.
    def enterJson_storage_format(self, ctx:TeradataSQLParser.Json_storage_formatContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#json_storage_format.
    def exitJson_storage_format(self, ctx:TeradataSQLParser.Json_storage_formatContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#dataset_storage_format_clause.
    def enterDataset_storage_format_clause(self, ctx:TeradataSQLParser.Dataset_storage_format_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#dataset_storage_format_clause.
    def exitDataset_storage_format_clause(self, ctx:TeradataSQLParser.Dataset_storage_format_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#dataset_storage_format.
    def enterDataset_storage_format(self, ctx:TeradataSQLParser.Dataset_storage_formatContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#dataset_storage_format.
    def exitDataset_storage_format(self, ctx:TeradataSQLParser.Dataset_storage_formatContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#with_schema.
    def enterWith_schema(self, ctx:TeradataSQLParser.With_schemaContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#with_schema.
    def exitWith_schema(self, ctx:TeradataSQLParser.With_schemaContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#with_time_zone.
    def enterWith_time_zone(self, ctx:TeradataSQLParser.With_time_zoneContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#with_time_zone.
    def exitWith_time_zone(self, ctx:TeradataSQLParser.With_time_zoneContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#literal.
    def enterLiteral(self, ctx:TeradataSQLParser.LiteralContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#literal.
    def exitLiteral(self, ctx:TeradataSQLParser.LiteralContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#hex_byte_literal.
    def enterHex_byte_literal(self, ctx:TeradataSQLParser.Hex_byte_literalContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#hex_byte_literal.
    def exitHex_byte_literal(self, ctx:TeradataSQLParser.Hex_byte_literalContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#char_string_literal.
    def enterChar_string_literal(self, ctx:TeradataSQLParser.Char_string_literalContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#char_string_literal.
    def exitChar_string_literal(self, ctx:TeradataSQLParser.Char_string_literalContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#unicode_char_string_literal.
    def enterUnicode_char_string_literal(self, ctx:TeradataSQLParser.Unicode_char_string_literalContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#unicode_char_string_literal.
    def exitUnicode_char_string_literal(self, ctx:TeradataSQLParser.Unicode_char_string_literalContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#hex_char_string_literal.
    def enterHex_char_string_literal(self, ctx:TeradataSQLParser.Hex_char_string_literalContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#hex_char_string_literal.
    def exitHex_char_string_literal(self, ctx:TeradataSQLParser.Hex_char_string_literalContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#integer_literal.
    def enterInteger_literal(self, ctx:TeradataSQLParser.Integer_literalContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#integer_literal.
    def exitInteger_literal(self, ctx:TeradataSQLParser.Integer_literalContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#hex_integer_literal.
    def enterHex_integer_literal(self, ctx:TeradataSQLParser.Hex_integer_literalContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#hex_integer_literal.
    def exitHex_integer_literal(self, ctx:TeradataSQLParser.Hex_integer_literalContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#float_literal.
    def enterFloat_literal(self, ctx:TeradataSQLParser.Float_literalContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#float_literal.
    def exitFloat_literal(self, ctx:TeradataSQLParser.Float_literalContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#character_set_prefix.
    def enterCharacter_set_prefix(self, ctx:TeradataSQLParser.Character_set_prefixContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#character_set_prefix.
    def exitCharacter_set_prefix(self, ctx:TeradataSQLParser.Character_set_prefixContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#date_literal.
    def enterDate_literal(self, ctx:TeradataSQLParser.Date_literalContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#date_literal.
    def exitDate_literal(self, ctx:TeradataSQLParser.Date_literalContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#time_literal.
    def enterTime_literal(self, ctx:TeradataSQLParser.Time_literalContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#time_literal.
    def exitTime_literal(self, ctx:TeradataSQLParser.Time_literalContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#timestamp_literal.
    def enterTimestamp_literal(self, ctx:TeradataSQLParser.Timestamp_literalContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#timestamp_literal.
    def exitTimestamp_literal(self, ctx:TeradataSQLParser.Timestamp_literalContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#interval_literal.
    def enterInterval_literal(self, ctx:TeradataSQLParser.Interval_literalContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#interval_literal.
    def exitInterval_literal(self, ctx:TeradataSQLParser.Interval_literalContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#interval_qualifier.
    def enterInterval_qualifier(self, ctx:TeradataSQLParser.Interval_qualifierContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#interval_qualifier.
    def exitInterval_qualifier(self, ctx:TeradataSQLParser.Interval_qualifierContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#period_literal.
    def enterPeriod_literal(self, ctx:TeradataSQLParser.Period_literalContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#period_literal.
    def exitPeriod_literal(self, ctx:TeradataSQLParser.Period_literalContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#column_name.
    def enterColumn_name(self, ctx:TeradataSQLParser.Column_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#column_name.
    def exitColumn_name(self, ctx:TeradataSQLParser.Column_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#unqualified_column_name.
    def enterUnqualified_column_name(self, ctx:TeradataSQLParser.Unqualified_column_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#unqualified_column_name.
    def exitUnqualified_column_name(self, ctx:TeradataSQLParser.Unqualified_column_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#unqualified_name.
    def enterUnqualified_name(self, ctx:TeradataSQLParser.Unqualified_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#unqualified_name.
    def exitUnqualified_name(self, ctx:TeradataSQLParser.Unqualified_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#object_name.
    def enterObject_name(self, ctx:TeradataSQLParser.Object_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#object_name.
    def exitObject_name(self, ctx:TeradataSQLParser.Object_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#table_name.
    def enterTable_name(self, ctx:TeradataSQLParser.Table_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#table_name.
    def exitTable_name(self, ctx:TeradataSQLParser.Table_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#procedure_name.
    def enterProcedure_name(self, ctx:TeradataSQLParser.Procedure_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#procedure_name.
    def exitProcedure_name(self, ctx:TeradataSQLParser.Procedure_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#function_name.
    def enterFunction_name(self, ctx:TeradataSQLParser.Function_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#function_name.
    def exitFunction_name(self, ctx:TeradataSQLParser.Function_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#macro_name.
    def enterMacro_name(self, ctx:TeradataSQLParser.Macro_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#macro_name.
    def exitMacro_name(self, ctx:TeradataSQLParser.Macro_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#database_name.
    def enterDatabase_name(self, ctx:TeradataSQLParser.Database_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#database_name.
    def exitDatabase_name(self, ctx:TeradataSQLParser.Database_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#user_name.
    def enterUser_name(self, ctx:TeradataSQLParser.User_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#user_name.
    def exitUser_name(self, ctx:TeradataSQLParser.User_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#role_name.
    def enterRole_name(self, ctx:TeradataSQLParser.Role_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#role_name.
    def exitRole_name(self, ctx:TeradataSQLParser.Role_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#profile_name.
    def enterProfile_name(self, ctx:TeradataSQLParser.Profile_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#profile_name.
    def exitProfile_name(self, ctx:TeradataSQLParser.Profile_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#alias_name.
    def enterAlias_name(self, ctx:TeradataSQLParser.Alias_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#alias_name.
    def exitAlias_name(self, ctx:TeradataSQLParser.Alias_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#variable_name.
    def enterVariable_name(self, ctx:TeradataSQLParser.Variable_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#variable_name.
    def exitVariable_name(self, ctx:TeradataSQLParser.Variable_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#parameter_name.
    def enterParameter_name(self, ctx:TeradataSQLParser.Parameter_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#parameter_name.
    def exitParameter_name(self, ctx:TeradataSQLParser.Parameter_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#label_name.
    def enterLabel_name(self, ctx:TeradataSQLParser.Label_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#label_name.
    def exitLabel_name(self, ctx:TeradataSQLParser.Label_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#condition_name.
    def enterCondition_name(self, ctx:TeradataSQLParser.Condition_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#condition_name.
    def exitCondition_name(self, ctx:TeradataSQLParser.Condition_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#cursor_name.
    def enterCursor_name(self, ctx:TeradataSQLParser.Cursor_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#cursor_name.
    def exitCursor_name(self, ctx:TeradataSQLParser.Cursor_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#statement_name.
    def enterStatement_name(self, ctx:TeradataSQLParser.Statement_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#statement_name.
    def exitStatement_name(self, ctx:TeradataSQLParser.Statement_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#statistics_name.
    def enterStatistics_name(self, ctx:TeradataSQLParser.Statistics_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#statistics_name.
    def exitStatistics_name(self, ctx:TeradataSQLParser.Statistics_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#udt_name.
    def enterUdt_name(self, ctx:TeradataSQLParser.Udt_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#udt_name.
    def exitUdt_name(self, ctx:TeradataSQLParser.Udt_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#attribute_name.
    def enterAttribute_name(self, ctx:TeradataSQLParser.Attribute_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#attribute_name.
    def exitAttribute_name(self, ctx:TeradataSQLParser.Attribute_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#method_name.
    def enterMethod_name(self, ctx:TeradataSQLParser.Method_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#method_name.
    def exitMethod_name(self, ctx:TeradataSQLParser.Method_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#anchor_name.
    def enterAnchor_name(self, ctx:TeradataSQLParser.Anchor_nameContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#anchor_name.
    def exitAnchor_name(self, ctx:TeradataSQLParser.Anchor_nameContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#nonreserved_word.
    def enterNonreserved_word(self, ctx:TeradataSQLParser.Nonreserved_wordContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#nonreserved_word.
    def exitNonreserved_word(self, ctx:TeradataSQLParser.Nonreserved_wordContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#query_expr.
    def enterQuery_expr(self, ctx:TeradataSQLParser.Query_exprContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#query_expr.
    def exitQuery_expr(self, ctx:TeradataSQLParser.Query_exprContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#query_term.
    def enterQuery_term(self, ctx:TeradataSQLParser.Query_termContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#query_term.
    def exitQuery_term(self, ctx:TeradataSQLParser.Query_termContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#with_deleted_rows.
    def enterWith_deleted_rows(self, ctx:TeradataSQLParser.With_deleted_rowsContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#with_deleted_rows.
    def exitWith_deleted_rows(self, ctx:TeradataSQLParser.With_deleted_rowsContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#as_json.
    def enterAs_json(self, ctx:TeradataSQLParser.As_jsonContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#as_json.
    def exitAs_json(self, ctx:TeradataSQLParser.As_jsonContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#select_list.
    def enterSelect_list(self, ctx:TeradataSQLParser.Select_listContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#select_list.
    def exitSelect_list(self, ctx:TeradataSQLParser.Select_listContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#top_n.
    def enterTop_n(self, ctx:TeradataSQLParser.Top_nContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#top_n.
    def exitTop_n(self, ctx:TeradataSQLParser.Top_nContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#normalize.
    def enterNormalize(self, ctx:TeradataSQLParser.NormalizeContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#normalize.
    def exitNormalize(self, ctx:TeradataSQLParser.NormalizeContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#all_operator.
    def enterAll_operator(self, ctx:TeradataSQLParser.All_operatorContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#all_operator.
    def exitAll_operator(self, ctx:TeradataSQLParser.All_operatorContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#selected_columns.
    def enterSelected_columns(self, ctx:TeradataSQLParser.Selected_columnsContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#selected_columns.
    def exitSelected_columns(self, ctx:TeradataSQLParser.Selected_columnsContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#selected_column.
    def enterSelected_column(self, ctx:TeradataSQLParser.Selected_columnContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#selected_column.
    def exitSelected_column(self, ctx:TeradataSQLParser.Selected_columnContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#into_clause.
    def enterInto_clause(self, ctx:TeradataSQLParser.Into_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#into_clause.
    def exitInto_clause(self, ctx:TeradataSQLParser.Into_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#from_clause.
    def enterFrom_clause(self, ctx:TeradataSQLParser.From_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#from_clause.
    def exitFrom_clause(self, ctx:TeradataSQLParser.From_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#from_spec.
    def enterFrom_spec(self, ctx:TeradataSQLParser.From_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#from_spec.
    def exitFrom_spec(self, ctx:TeradataSQLParser.From_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#join_source_spec.
    def enterJoin_source_spec(self, ctx:TeradataSQLParser.Join_source_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#join_source_spec.
    def exitJoin_source_spec(self, ctx:TeradataSQLParser.Join_source_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#join_joined_spec.
    def enterJoin_joined_spec(self, ctx:TeradataSQLParser.Join_joined_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#join_joined_spec.
    def exitJoin_joined_spec(self, ctx:TeradataSQLParser.Join_joined_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#from_pivot_spec.
    def enterFrom_pivot_spec(self, ctx:TeradataSQLParser.From_pivot_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#from_pivot_spec.
    def exitFrom_pivot_spec(self, ctx:TeradataSQLParser.From_pivot_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#from_unpivot_spec.
    def enterFrom_unpivot_spec(self, ctx:TeradataSQLParser.From_unpivot_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#from_unpivot_spec.
    def exitFrom_unpivot_spec(self, ctx:TeradataSQLParser.From_unpivot_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#table_reference.
    def enterTable_reference(self, ctx:TeradataSQLParser.Table_referenceContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#table_reference.
    def exitTable_reference(self, ctx:TeradataSQLParser.Table_referenceContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#join_clause.
    def enterJoin_clause(self, ctx:TeradataSQLParser.Join_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#join_clause.
    def exitJoin_clause(self, ctx:TeradataSQLParser.Join_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#join_on_clause.
    def enterJoin_on_clause(self, ctx:TeradataSQLParser.Join_on_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#join_on_clause.
    def exitJoin_on_clause(self, ctx:TeradataSQLParser.Join_on_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#foreign_table_reference.
    def enterForeign_table_reference(self, ctx:TeradataSQLParser.Foreign_table_referenceContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#foreign_table_reference.
    def exitForeign_table_reference(self, ctx:TeradataSQLParser.Foreign_table_referenceContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#foreign_function_reference.
    def enterForeign_function_reference(self, ctx:TeradataSQLParser.Foreign_function_referenceContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#foreign_function_reference.
    def exitForeign_function_reference(self, ctx:TeradataSQLParser.Foreign_function_referenceContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#foreign_on_clause.
    def enterForeign_on_clause(self, ctx:TeradataSQLParser.Foreign_on_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#foreign_on_clause.
    def exitForeign_on_clause(self, ctx:TeradataSQLParser.Foreign_on_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#exported_data.
    def enterExported_data(self, ctx:TeradataSQLParser.Exported_dataContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#exported_data.
    def exitExported_data(self, ctx:TeradataSQLParser.Exported_dataContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#foreign_using_clause.
    def enterForeign_using_clause(self, ctx:TeradataSQLParser.Foreign_using_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#foreign_using_clause.
    def exitForeign_using_clause(self, ctx:TeradataSQLParser.Foreign_using_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#foreign_parameter.
    def enterForeign_parameter(self, ctx:TeradataSQLParser.Foreign_parameterContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#foreign_parameter.
    def exitForeign_parameter(self, ctx:TeradataSQLParser.Foreign_parameterContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#foreign_returns_clause.
    def enterForeign_returns_clause(self, ctx:TeradataSQLParser.Foreign_returns_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#foreign_returns_clause.
    def exitForeign_returns_clause(self, ctx:TeradataSQLParser.Foreign_returns_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#server_name_reference.
    def enterServer_name_reference(self, ctx:TeradataSQLParser.Server_name_referenceContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#server_name_reference.
    def exitServer_name_reference(self, ctx:TeradataSQLParser.Server_name_referenceContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#table_function_reference.
    def enterTable_function_reference(self, ctx:TeradataSQLParser.Table_function_referenceContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#table_function_reference.
    def exitTable_function_reference(self, ctx:TeradataSQLParser.Table_function_referenceContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#udt_table_function.
    def enterUdt_table_function(self, ctx:TeradataSQLParser.Udt_table_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#udt_table_function.
    def exitUdt_table_function(self, ctx:TeradataSQLParser.Udt_table_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#unnest_table_function.
    def enterUnnest_table_function(self, ctx:TeradataSQLParser.Unnest_table_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#unnest_table_function.
    def exitUnnest_table_function(self, ctx:TeradataSQLParser.Unnest_table_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#table_function_returns_clause.
    def enterTable_function_returns_clause(self, ctx:TeradataSQLParser.Table_function_returns_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#table_function_returns_clause.
    def exitTable_function_returns_clause(self, ctx:TeradataSQLParser.Table_function_returns_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#table_function_local_order_by_clause.
    def enterTable_function_local_order_by_clause(self, ctx:TeradataSQLParser.Table_function_local_order_by_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#table_function_local_order_by_clause.
    def exitTable_function_local_order_by_clause(self, ctx:TeradataSQLParser.Table_function_local_order_by_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#table_function_hash_by_clause.
    def enterTable_function_hash_by_clause(self, ctx:TeradataSQLParser.Table_function_hash_by_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#table_function_hash_by_clause.
    def exitTable_function_hash_by_clause(self, ctx:TeradataSQLParser.Table_function_hash_by_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#table_operator_reference.
    def enterTable_operator_reference(self, ctx:TeradataSQLParser.Table_operator_referenceContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#table_operator_reference.
    def exitTable_operator_reference(self, ctx:TeradataSQLParser.Table_operator_referenceContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#xmltable_operator.
    def enterXmltable_operator(self, ctx:TeradataSQLParser.Xmltable_operatorContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#xmltable_operator.
    def exitXmltable_operator(self, ctx:TeradataSQLParser.Xmltable_operatorContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#calcmatrix_table_operator.
    def enterCalcmatrix_table_operator(self, ctx:TeradataSQLParser.Calcmatrix_table_operatorContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#calcmatrix_table_operator.
    def exitCalcmatrix_table_operator(self, ctx:TeradataSQLParser.Calcmatrix_table_operatorContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#read_nos_table_operator.
    def enterRead_nos_table_operator(self, ctx:TeradataSQLParser.Read_nos_table_operatorContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#read_nos_table_operator.
    def exitRead_nos_table_operator(self, ctx:TeradataSQLParser.Read_nos_table_operatorContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#script_table_operator.
    def enterScript_table_operator(self, ctx:TeradataSQLParser.Script_table_operatorContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#script_table_operator.
    def exitScript_table_operator(self, ctx:TeradataSQLParser.Script_table_operatorContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#td_unpivot_table_operator.
    def enterTd_unpivot_table_operator(self, ctx:TeradataSQLParser.Td_unpivot_table_operatorContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#td_unpivot_table_operator.
    def exitTd_unpivot_table_operator(self, ctx:TeradataSQLParser.Td_unpivot_table_operatorContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#write_nos_table_operator.
    def enterWrite_nos_table_operator(self, ctx:TeradataSQLParser.Write_nos_table_operatorContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#write_nos_table_operator.
    def exitWrite_nos_table_operator(self, ctx:TeradataSQLParser.Write_nos_table_operatorContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#json_table_table_operator.
    def enterJson_table_table_operator(self, ctx:TeradataSQLParser.Json_table_table_operatorContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#json_table_table_operator.
    def exitJson_table_table_operator(self, ctx:TeradataSQLParser.Json_table_table_operatorContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#json_keys_table_operator.
    def enterJson_keys_table_operator(self, ctx:TeradataSQLParser.Json_keys_table_operatorContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#json_keys_table_operator.
    def exitJson_keys_table_operator(self, ctx:TeradataSQLParser.Json_keys_table_operatorContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#json_shred_table_operator.
    def enterJson_shred_table_operator(self, ctx:TeradataSQLParser.Json_shred_table_operatorContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#json_shred_table_operator.
    def exitJson_shred_table_operator(self, ctx:TeradataSQLParser.Json_shred_table_operatorContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#generic_table_operator.
    def enterGeneric_table_operator(self, ctx:TeradataSQLParser.Generic_table_operatorContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#generic_table_operator.
    def exitGeneric_table_operator(self, ctx:TeradataSQLParser.Generic_table_operatorContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#table_operator_on_clause.
    def enterTable_operator_on_clause(self, ctx:TeradataSQLParser.Table_operator_on_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#table_operator_on_clause.
    def exitTable_operator_on_clause(self, ctx:TeradataSQLParser.Table_operator_on_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#table_operator_execute_clause.
    def enterTable_operator_execute_clause(self, ctx:TeradataSQLParser.Table_operator_execute_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#table_operator_execute_clause.
    def exitTable_operator_execute_clause(self, ctx:TeradataSQLParser.Table_operator_execute_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#table_operator_out_table_clause.
    def enterTable_operator_out_table_clause(self, ctx:TeradataSQLParser.Table_operator_out_table_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#table_operator_out_table_clause.
    def exitTable_operator_out_table_clause(self, ctx:TeradataSQLParser.Table_operator_out_table_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#table_operator_using_clause.
    def enterTable_operator_using_clause(self, ctx:TeradataSQLParser.Table_operator_using_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#table_operator_using_clause.
    def exitTable_operator_using_clause(self, ctx:TeradataSQLParser.Table_operator_using_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#table_operator_using_spec.
    def enterTable_operator_using_spec(self, ctx:TeradataSQLParser.Table_operator_using_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#table_operator_using_spec.
    def exitTable_operator_using_spec(self, ctx:TeradataSQLParser.Table_operator_using_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#json_keys_using_name_value_pair.
    def enterJson_keys_using_name_value_pair(self, ctx:TeradataSQLParser.Json_keys_using_name_value_pairContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#json_keys_using_name_value_pair.
    def exitJson_keys_using_name_value_pair(self, ctx:TeradataSQLParser.Json_keys_using_name_value_pairContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#hash_or_partition_by.
    def enterHash_or_partition_by(self, ctx:TeradataSQLParser.Hash_or_partition_byContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#hash_or_partition_by.
    def exitHash_or_partition_by(self, ctx:TeradataSQLParser.Hash_or_partition_byContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#subquery_reference.
    def enterSubquery_reference(self, ctx:TeradataSQLParser.Subquery_referenceContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#subquery_reference.
    def exitSubquery_reference(self, ctx:TeradataSQLParser.Subquery_referenceContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#location.
    def enterLocation(self, ctx:TeradataSQLParser.LocationContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#location.
    def exitLocation(self, ctx:TeradataSQLParser.LocationContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#read_nos_option.
    def enterRead_nos_option(self, ctx:TeradataSQLParser.Read_nos_optionContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#read_nos_option.
    def exitRead_nos_option(self, ctx:TeradataSQLParser.Read_nos_optionContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#write_nos_option.
    def enterWrite_nos_option(self, ctx:TeradataSQLParser.Write_nos_optionContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#write_nos_option.
    def exitWrite_nos_option(self, ctx:TeradataSQLParser.Write_nos_optionContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#with_clause.
    def enterWith_clause(self, ctx:TeradataSQLParser.With_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#with_clause.
    def exitWith_clause(self, ctx:TeradataSQLParser.With_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#with_clause_by_phrase.
    def enterWith_clause_by_phrase(self, ctx:TeradataSQLParser.With_clause_by_phraseContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#with_clause_by_phrase.
    def exitWith_clause_by_phrase(self, ctx:TeradataSQLParser.With_clause_by_phraseContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#with_clause_title_phrase.
    def enterWith_clause_title_phrase(self, ctx:TeradataSQLParser.With_clause_title_phraseContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#with_clause_title_phrase.
    def exitWith_clause_title_phrase(self, ctx:TeradataSQLParser.With_clause_title_phraseContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#where_clause.
    def enterWhere_clause(self, ctx:TeradataSQLParser.Where_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#where_clause.
    def exitWhere_clause(self, ctx:TeradataSQLParser.Where_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#group_by_clause.
    def enterGroup_by_clause(self, ctx:TeradataSQLParser.Group_by_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#group_by_clause.
    def exitGroup_by_clause(self, ctx:TeradataSQLParser.Group_by_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#group_by_spec.
    def enterGroup_by_spec(self, ctx:TeradataSQLParser.Group_by_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#group_by_spec.
    def exitGroup_by_spec(self, ctx:TeradataSQLParser.Group_by_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#ordinary_grouping_set.
    def enterOrdinary_grouping_set(self, ctx:TeradataSQLParser.Ordinary_grouping_setContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#ordinary_grouping_set.
    def exitOrdinary_grouping_set(self, ctx:TeradataSQLParser.Ordinary_grouping_setContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#ordinary_grouping_set_parenthesized.
    def enterOrdinary_grouping_set_parenthesized(self, ctx:TeradataSQLParser.Ordinary_grouping_set_parenthesizedContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#ordinary_grouping_set_parenthesized.
    def exitOrdinary_grouping_set_parenthesized(self, ctx:TeradataSQLParser.Ordinary_grouping_set_parenthesizedContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#empty_grouping_set.
    def enterEmpty_grouping_set(self, ctx:TeradataSQLParser.Empty_grouping_setContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#empty_grouping_set.
    def exitEmpty_grouping_set(self, ctx:TeradataSQLParser.Empty_grouping_setContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#rollup_option.
    def enterRollup_option(self, ctx:TeradataSQLParser.Rollup_optionContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#rollup_option.
    def exitRollup_option(self, ctx:TeradataSQLParser.Rollup_optionContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#cube_option.
    def enterCube_option(self, ctx:TeradataSQLParser.Cube_optionContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#cube_option.
    def exitCube_option(self, ctx:TeradataSQLParser.Cube_optionContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#grouping_sets_option.
    def enterGrouping_sets_option(self, ctx:TeradataSQLParser.Grouping_sets_optionContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#grouping_sets_option.
    def exitGrouping_sets_option(self, ctx:TeradataSQLParser.Grouping_sets_optionContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#grouping_sets_spec.
    def enterGrouping_sets_spec(self, ctx:TeradataSQLParser.Grouping_sets_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#grouping_sets_spec.
    def exitGrouping_sets_spec(self, ctx:TeradataSQLParser.Grouping_sets_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#having_clause.
    def enterHaving_clause(self, ctx:TeradataSQLParser.Having_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#having_clause.
    def exitHaving_clause(self, ctx:TeradataSQLParser.Having_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#qualify_clause.
    def enterQualify_clause(self, ctx:TeradataSQLParser.Qualify_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#qualify_clause.
    def exitQualify_clause(self, ctx:TeradataSQLParser.Qualify_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#sample_clause.
    def enterSample_clause(self, ctx:TeradataSQLParser.Sample_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#sample_clause.
    def exitSample_clause(self, ctx:TeradataSQLParser.Sample_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#sample_fraction_description.
    def enterSample_fraction_description(self, ctx:TeradataSQLParser.Sample_fraction_descriptionContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#sample_fraction_description.
    def exitSample_fraction_description(self, ctx:TeradataSQLParser.Sample_fraction_descriptionContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#sample_count_description.
    def enterSample_count_description(self, ctx:TeradataSQLParser.Sample_count_descriptionContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#sample_count_description.
    def exitSample_count_description(self, ctx:TeradataSQLParser.Sample_count_descriptionContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#sample_when_clause.
    def enterSample_when_clause(self, ctx:TeradataSQLParser.Sample_when_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#sample_when_clause.
    def exitSample_when_clause(self, ctx:TeradataSQLParser.Sample_when_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#expand_on_clause.
    def enterExpand_on_clause(self, ctx:TeradataSQLParser.Expand_on_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#expand_on_clause.
    def exitExpand_on_clause(self, ctx:TeradataSQLParser.Expand_on_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#order_by_clause.
    def enterOrder_by_clause(self, ctx:TeradataSQLParser.Order_by_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#order_by_clause.
    def exitOrder_by_clause(self, ctx:TeradataSQLParser.Order_by_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#order_by_spec_full.
    def enterOrder_by_spec_full(self, ctx:TeradataSQLParser.Order_by_spec_fullContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#order_by_spec_full.
    def exitOrder_by_spec_full(self, ctx:TeradataSQLParser.Order_by_spec_fullContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#order_by_spec_asc_desc_only.
    def enterOrder_by_spec_asc_desc_only(self, ctx:TeradataSQLParser.Order_by_spec_asc_desc_onlyContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#order_by_spec_asc_desc_only.
    def exitOrder_by_spec_asc_desc_only(self, ctx:TeradataSQLParser.Order_by_spec_asc_desc_onlyContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#with_check_option.
    def enterWith_check_option(self, ctx:TeradataSQLParser.With_check_optionContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#with_check_option.
    def exitWith_check_option(self, ctx:TeradataSQLParser.With_check_optionContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#PeriodMeets.
    def enterPeriodMeets(self, ctx:TeradataSQLParser.PeriodMeetsContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#PeriodMeets.
    def exitPeriodMeets(self, ctx:TeradataSQLParser.PeriodMeetsContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#PeriodImmediatelySucceeds.
    def enterPeriodImmediatelySucceeds(self, ctx:TeradataSQLParser.PeriodImmediatelySucceedsContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#PeriodImmediatelySucceeds.
    def exitPeriodImmediatelySucceeds(self, ctx:TeradataSQLParser.PeriodImmediatelySucceedsContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#PeriodEquals.
    def enterPeriodEquals(self, ctx:TeradataSQLParser.PeriodEqualsContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#PeriodEquals.
    def exitPeriodEquals(self, ctx:TeradataSQLParser.PeriodEqualsContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#ScalarComparelist.
    def enterScalarComparelist(self, ctx:TeradataSQLParser.ScalarComparelistContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#ScalarComparelist.
    def exitScalarComparelist(self, ctx:TeradataSQLParser.ScalarComparelistContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#TupleInSubquery.
    def enterTupleInSubquery(self, ctx:TeradataSQLParser.TupleInSubqueryContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#TupleInSubquery.
    def exitTupleInSubquery(self, ctx:TeradataSQLParser.TupleInSubqueryContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#LogicalOr.
    def enterLogicalOr(self, ctx:TeradataSQLParser.LogicalOrContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#LogicalOr.
    def exitLogicalOr(self, ctx:TeradataSQLParser.LogicalOrContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#ScalarInScalar.
    def enterScalarInScalar(self, ctx:TeradataSQLParser.ScalarInScalarContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#ScalarInScalar.
    def exitScalarInScalar(self, ctx:TeradataSQLParser.ScalarInScalarContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#ScalarCompareScalar.
    def enterScalarCompareScalar(self, ctx:TeradataSQLParser.ScalarCompareScalarContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#ScalarCompareScalar.
    def exitScalarCompareScalar(self, ctx:TeradataSQLParser.ScalarCompareScalarContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#LogicalNot.
    def enterLogicalNot(self, ctx:TeradataSQLParser.LogicalNotContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#LogicalNot.
    def exitLogicalNot(self, ctx:TeradataSQLParser.LogicalNotContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#TupleComparelist.
    def enterTupleComparelist(self, ctx:TeradataSQLParser.TupleComparelistContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#TupleComparelist.
    def exitTupleComparelist(self, ctx:TeradataSQLParser.TupleComparelistContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#ScalarInList.
    def enterScalarInList(self, ctx:TeradataSQLParser.ScalarInListContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#ScalarInList.
    def exitScalarInList(self, ctx:TeradataSQLParser.ScalarInListContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#TupleLikeList.
    def enterTupleLikeList(self, ctx:TeradataSQLParser.TupleLikeListContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#TupleLikeList.
    def exitTupleLikeList(self, ctx:TeradataSQLParser.TupleLikeListContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#LogicalAnd.
    def enterLogicalAnd(self, ctx:TeradataSQLParser.LogicalAndContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#LogicalAnd.
    def exitLogicalAnd(self, ctx:TeradataSQLParser.LogicalAndContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#ScalarInSubquery.
    def enterScalarInSubquery(self, ctx:TeradataSQLParser.ScalarInSubqueryContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#ScalarInSubquery.
    def exitScalarInSubquery(self, ctx:TeradataSQLParser.ScalarInSubqueryContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#PeriodContains.
    def enterPeriodContains(self, ctx:TeradataSQLParser.PeriodContainsContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#PeriodContains.
    def exitPeriodContains(self, ctx:TeradataSQLParser.PeriodContainsContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#PeriodOverlaps.
    def enterPeriodOverlaps(self, ctx:TeradataSQLParser.PeriodOverlapsContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#PeriodOverlaps.
    def exitPeriodOverlaps(self, ctx:TeradataSQLParser.PeriodOverlapsContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#Between.
    def enterBetween(self, ctx:TeradataSQLParser.BetweenContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#Between.
    def exitBetween(self, ctx:TeradataSQLParser.BetweenContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#ParenthesizedLogicalExpr.
    def enterParenthesizedLogicalExpr(self, ctx:TeradataSQLParser.ParenthesizedLogicalExprContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#ParenthesizedLogicalExpr.
    def exitParenthesizedLogicalExpr(self, ctx:TeradataSQLParser.ParenthesizedLogicalExprContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#PeriodImmediatelyPrecedes.
    def enterPeriodImmediatelyPrecedes(self, ctx:TeradataSQLParser.PeriodImmediatelyPrecedesContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#PeriodImmediatelyPrecedes.
    def exitPeriodImmediatelyPrecedes(self, ctx:TeradataSQLParser.PeriodImmediatelyPrecedesContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#NullCheck.
    def enterNullCheck(self, ctx:TeradataSQLParser.NullCheckContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#NullCheck.
    def exitNullCheck(self, ctx:TeradataSQLParser.NullCheckContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#PeriodPrecedes.
    def enterPeriodPrecedes(self, ctx:TeradataSQLParser.PeriodPrecedesContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#PeriodPrecedes.
    def exitPeriodPrecedes(self, ctx:TeradataSQLParser.PeriodPrecedesContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#Exists.
    def enterExists(self, ctx:TeradataSQLParser.ExistsContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#Exists.
    def exitExists(self, ctx:TeradataSQLParser.ExistsContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#PeriodSucceeds.
    def enterPeriodSucceeds(self, ctx:TeradataSQLParser.PeriodSucceedsContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#PeriodSucceeds.
    def exitPeriodSucceeds(self, ctx:TeradataSQLParser.PeriodSucceedsContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#ScalarLikeList.
    def enterScalarLikeList(self, ctx:TeradataSQLParser.ScalarLikeListContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#ScalarLikeList.
    def exitScalarLikeList(self, ctx:TeradataSQLParser.ScalarLikeListContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#ScalarLikeScalar.
    def enterScalarLikeScalar(self, ctx:TeradataSQLParser.ScalarLikeScalarContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#ScalarLikeScalar.
    def exitScalarLikeScalar(self, ctx:TeradataSQLParser.ScalarLikeScalarContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#JsonMetadata.
    def enterJsonMetadata(self, ctx:TeradataSQLParser.JsonMetadataContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#JsonMetadata.
    def exitJsonMetadata(self, ctx:TeradataSQLParser.JsonMetadataContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#JsonAsBson.
    def enterJsonAsBson(self, ctx:TeradataSQLParser.JsonAsBsonContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#JsonAsBson.
    def exitJsonAsBson(self, ctx:TeradataSQLParser.JsonAsBsonContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#VariantTypeConstructor.
    def enterVariantTypeConstructor(self, ctx:TeradataSQLParser.VariantTypeConstructorContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#VariantTypeConstructor.
    def exitVariantTypeConstructor(self, ctx:TeradataSQLParser.VariantTypeConstructorContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#XMLExtract.
    def enterXMLExtract(self, ctx:TeradataSQLParser.XMLExtractContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#XMLExtract.
    def exitXMLExtract(self, ctx:TeradataSQLParser.XMLExtractContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#ArrayComparison.
    def enterArrayComparison(self, ctx:TeradataSQLParser.ArrayComparisonContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#ArrayComparison.
    def exitArrayComparison(self, ctx:TeradataSQLParser.ArrayComparisonContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#ArrayGet.
    def enterArrayGet(self, ctx:TeradataSQLParser.ArrayGetContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#ArrayGet.
    def exitArrayGet(self, ctx:TeradataSQLParser.ArrayGetContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#XMLConstructor.
    def enterXMLConstructor(self, ctx:TeradataSQLParser.XMLConstructorContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#XMLConstructor.
    def exitXMLConstructor(self, ctx:TeradataSQLParser.XMLConstructorContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#UDTMethodInvocation.
    def enterUDTMethodInvocation(self, ctx:TeradataSQLParser.UDTMethodInvocationContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#UDTMethodInvocation.
    def exitUDTMethodInvocation(self, ctx:TeradataSQLParser.UDTMethodInvocationContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#JsonExtractLargeValue.
    def enterJsonExtractLargeValue(self, ctx:TeradataSQLParser.JsonExtractLargeValueContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#JsonExtractLargeValue.
    def exitJsonExtractLargeValue(self, ctx:TeradataSQLParser.JsonExtractLargeValueContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#JsonRecursiveDescendSlice.
    def enterJsonRecursiveDescendSlice(self, ctx:TeradataSQLParser.JsonRecursiveDescendSliceContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#JsonRecursiveDescendSlice.
    def exitJsonRecursiveDescendSlice(self, ctx:TeradataSQLParser.JsonRecursiveDescendSliceContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#FunctionInvocation.
    def enterFunctionInvocation(self, ctx:TeradataSQLParser.FunctionInvocationContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#FunctionInvocation.
    def exitFunctionInvocation(self, ctx:TeradataSQLParser.FunctionInvocationContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#ScalarSubquery.
    def enterScalarSubquery(self, ctx:TeradataSQLParser.ScalarSubqueryContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#ScalarSubquery.
    def exitScalarSubquery(self, ctx:TeradataSQLParser.ScalarSubqueryContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#JsonExistValue.
    def enterJsonExistValue(self, ctx:TeradataSQLParser.JsonExistValueContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#JsonExistValue.
    def exitJsonExistValue(self, ctx:TeradataSQLParser.JsonExistValueContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#Modulo.
    def enterModulo(self, ctx:TeradataSQLParser.ModuloContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#Modulo.
    def exitModulo(self, ctx:TeradataSQLParser.ModuloContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#JsonExtractValue.
    def enterJsonExtractValue(self, ctx:TeradataSQLParser.JsonExtractValueContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#JsonExtractValue.
    def exitJsonExtractValue(self, ctx:TeradataSQLParser.JsonExtractValueContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#XMLCreateSchemaBasedXML.
    def enterXMLCreateSchemaBasedXML(self, ctx:TeradataSQLParser.XMLCreateSchemaBasedXMLContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#XMLCreateSchemaBasedXML.
    def exitXMLCreateSchemaBasedXML(self, ctx:TeradataSQLParser.XMLCreateSchemaBasedXMLContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#ArrayUpdate.
    def enterArrayUpdate(self, ctx:TeradataSQLParser.ArrayUpdateContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#ArrayUpdate.
    def exitArrayUpdate(self, ctx:TeradataSQLParser.ArrayUpdateContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#JsonExtract.
    def enterJsonExtract(self, ctx:TeradataSQLParser.JsonExtractContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#JsonExtract.
    def exitJsonExtract(self, ctx:TeradataSQLParser.JsonExtractContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#MultDiv.
    def enterMultDiv(self, ctx:TeradataSQLParser.MultDivContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#MultDiv.
    def exitMultDiv(self, ctx:TeradataSQLParser.MultDivContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#PeriodIntersect.
    def enterPeriodIntersect(self, ctx:TeradataSQLParser.PeriodIntersectContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#PeriodIntersect.
    def exitPeriodIntersect(self, ctx:TeradataSQLParser.PeriodIntersectContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#IntervalExprParenthesized.
    def enterIntervalExprParenthesized(self, ctx:TeradataSQLParser.IntervalExprParenthesizedContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#IntervalExprParenthesized.
    def exitIntervalExprParenthesized(self, ctx:TeradataSQLParser.IntervalExprParenthesizedContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#JsonRecursiveDescendAllArrayElements.
    def enterJsonRecursiveDescendAllArrayElements(self, ctx:TeradataSQLParser.JsonRecursiveDescendAllArrayElementsContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#JsonRecursiveDescendAllArrayElements.
    def exitJsonRecursiveDescendAllArrayElements(self, ctx:TeradataSQLParser.JsonRecursiveDescendAllArrayElementsContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#UnaryPlusMinus.
    def enterUnaryPlusMinus(self, ctx:TeradataSQLParser.UnaryPlusMinusContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#UnaryPlusMinus.
    def exitUnaryPlusMinus(self, ctx:TeradataSQLParser.UnaryPlusMinusContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#Concatenation.
    def enterConcatenation(self, ctx:TeradataSQLParser.ConcatenationContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#Concatenation.
    def exitConcatenation(self, ctx:TeradataSQLParser.ConcatenationContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#PeriodDiff.
    def enterPeriodDiff(self, ctx:TeradataSQLParser.PeriodDiffContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#PeriodDiff.
    def exitPeriodDiff(self, ctx:TeradataSQLParser.PeriodDiffContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#ArrayOmethodWithoudArgs.
    def enterArrayOmethodWithoudArgs(self, ctx:TeradataSQLParser.ArrayOmethodWithoudArgsContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#ArrayOmethodWithoudArgs.
    def exitArrayOmethodWithoudArgs(self, ctx:TeradataSQLParser.ArrayOmethodWithoudArgsContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#PartitioningExpr.
    def enterPartitioningExpr(self, ctx:TeradataSQLParser.PartitioningExprContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#PartitioningExpr.
    def exitPartitioningExpr(self, ctx:TeradataSQLParser.PartitioningExprContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#XMLExistNode.
    def enterXMLExistNode(self, ctx:TeradataSQLParser.XMLExistNodeContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#XMLExistNode.
    def exitXMLExistNode(self, ctx:TeradataSQLParser.XMLExistNodeContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#JsonRecursiveDescendArrayElementReference.
    def enterJsonRecursiveDescendArrayElementReference(self, ctx:TeradataSQLParser.JsonRecursiveDescendArrayElementReferenceContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#JsonRecursiveDescendArrayElementReference.
    def exitJsonRecursiveDescendArrayElementReference(self, ctx:TeradataSQLParser.JsonRecursiveDescendArrayElementReferenceContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#DataTypeConversion.
    def enterDataTypeConversion(self, ctx:TeradataSQLParser.DataTypeConversionContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#DataTypeConversion.
    def exitDataTypeConversion(self, ctx:TeradataSQLParser.DataTypeConversionContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#JsonRecursiveDescendObjectMember.
    def enterJsonRecursiveDescendObjectMember(self, ctx:TeradataSQLParser.JsonRecursiveDescendObjectMemberContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#JsonRecursiveDescendObjectMember.
    def exitJsonRecursiveDescendObjectMember(self, ctx:TeradataSQLParser.JsonRecursiveDescendObjectMemberContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#IntervalExpr.
    def enterIntervalExpr(self, ctx:TeradataSQLParser.IntervalExprContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#IntervalExpr.
    def exitIntervalExpr(self, ctx:TeradataSQLParser.IntervalExprContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#Exponentiation.
    def enterExponentiation(self, ctx:TeradataSQLParser.ExponentiationContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#Exponentiation.
    def exitExponentiation(self, ctx:TeradataSQLParser.ExponentiationContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#XMLIsSchemaValidated.
    def enterXMLIsSchemaValidated(self, ctx:TeradataSQLParser.XMLIsSchemaValidatedContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#XMLIsSchemaValidated.
    def exitXMLIsSchemaValidated(self, ctx:TeradataSQLParser.XMLIsSchemaValidatedContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#JSONConstructor.
    def enterJSONConstructor(self, ctx:TeradataSQLParser.JSONConstructorContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#JSONConstructor.
    def exitJSONConstructor(self, ctx:TeradataSQLParser.JSONConstructorContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#JsonSlice.
    def enterJsonSlice(self, ctx:TeradataSQLParser.JsonSliceContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#JsonSlice.
    def exitJsonSlice(self, ctx:TeradataSQLParser.JsonSliceContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#XMLIsSchemaValid.
    def enterXMLIsSchemaValid(self, ctx:TeradataSQLParser.XMLIsSchemaValidContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#XMLIsSchemaValid.
    def exitXMLIsSchemaValid(self, ctx:TeradataSQLParser.XMLIsSchemaValidContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#ArrayAggregation.
    def enterArrayAggregation(self, ctx:TeradataSQLParser.ArrayAggregationContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#ArrayAggregation.
    def exitArrayAggregation(self, ctx:TeradataSQLParser.ArrayAggregationContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#ArrayUpdateStride.
    def enterArrayUpdateStride(self, ctx:TeradataSQLParser.ArrayUpdateStrideContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#ArrayUpdateStride.
    def exitArrayUpdateStride(self, ctx:TeradataSQLParser.ArrayUpdateStrideContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#LiteralExpr.
    def enterLiteralExpr(self, ctx:TeradataSQLParser.LiteralExprContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#LiteralExpr.
    def exitLiteralExpr(self, ctx:TeradataSQLParser.LiteralExprContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#ArrayOmethodWithArg.
    def enterArrayOmethodWithArg(self, ctx:TeradataSQLParser.ArrayOmethodWithArgContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#ArrayOmethodWithArg.
    def exitArrayOmethodWithArg(self, ctx:TeradataSQLParser.ArrayOmethodWithArgContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#JsonRecursiveDescendAllObjectMembers.
    def enterJsonRecursiveDescendAllObjectMembers(self, ctx:TeradataSQLParser.JsonRecursiveDescendAllObjectMembersContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#JsonRecursiveDescendAllObjectMembers.
    def exitJsonRecursiveDescendAllObjectMembers(self, ctx:TeradataSQLParser.JsonRecursiveDescendAllObjectMembersContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#XMLCreateNonSchemaBasedXML.
    def enterXMLCreateNonSchemaBasedXML(self, ctx:TeradataSQLParser.XMLCreateNonSchemaBasedXMLContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#XMLCreateNonSchemaBasedXML.
    def exitXMLCreateNonSchemaBasedXML(self, ctx:TeradataSQLParser.XMLCreateNonSchemaBasedXMLContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#VariableReference.
    def enterVariableReference(self, ctx:TeradataSQLParser.VariableReferenceContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#VariableReference.
    def exitVariableReference(self, ctx:TeradataSQLParser.VariableReferenceContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#AddSub.
    def enterAddSub(self, ctx:TeradataSQLParser.AddSubContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#AddSub.
    def exitAddSub(self, ctx:TeradataSQLParser.AddSubContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#JsonObjectMember.
    def enterJsonObjectMember(self, ctx:TeradataSQLParser.JsonObjectMemberContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#JsonObjectMember.
    def exitJsonObjectMember(self, ctx:TeradataSQLParser.JsonObjectMemberContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#JsonAllElements.
    def enterJsonAllElements(self, ctx:TeradataSQLParser.JsonAllElementsContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#JsonAllElements.
    def exitJsonAllElements(self, ctx:TeradataSQLParser.JsonAllElementsContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#ArrayOextend.
    def enterArrayOextend(self, ctx:TeradataSQLParser.ArrayOextendContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#ArrayOextend.
    def exitArrayOextend(self, ctx:TeradataSQLParser.ArrayOextendContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#ArrayArithmetic.
    def enterArrayArithmetic(self, ctx:TeradataSQLParser.ArrayArithmeticContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#ArrayArithmetic.
    def exitArrayArithmetic(self, ctx:TeradataSQLParser.ArrayArithmeticContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#UDTConstructor.
    def enterUDTConstructor(self, ctx:TeradataSQLParser.UDTConstructorContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#UDTConstructor.
    def exitUDTConstructor(self, ctx:TeradataSQLParser.UDTConstructorContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#XMLTransform.
    def enterXMLTransform(self, ctx:TeradataSQLParser.XMLTransformContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#XMLTransform.
    def exitXMLTransform(self, ctx:TeradataSQLParser.XMLTransformContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#DateTimeExpr.
    def enterDateTimeExpr(self, ctx:TeradataSQLParser.DateTimeExprContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#DateTimeExpr.
    def exitDateTimeExpr(self, ctx:TeradataSQLParser.DateTimeExprContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#ColumnName.
    def enterColumnName(self, ctx:TeradataSQLParser.ColumnNameContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#ColumnName.
    def exitColumnName(self, ctx:TeradataSQLParser.ColumnNameContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#ArrayOtrim.
    def enterArrayOtrim(self, ctx:TeradataSQLParser.ArrayOtrimContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#ArrayOtrim.
    def exitArrayOtrim(self, ctx:TeradataSQLParser.ArrayOtrimContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#CursorVariableReference.
    def enterCursorVariableReference(self, ctx:TeradataSQLParser.CursorVariableReferenceContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#CursorVariableReference.
    def exitCursorVariableReference(self, ctx:TeradataSQLParser.CursorVariableReferenceContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#Parenthesized.
    def enterParenthesized(self, ctx:TeradataSQLParser.ParenthesizedContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#Parenthesized.
    def exitParenthesized(self, ctx:TeradataSQLParser.ParenthesizedContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#JsonAsBsonText.
    def enterJsonAsBsonText(self, ctx:TeradataSQLParser.JsonAsBsonTextContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#JsonAsBsonText.
    def exitJsonAsBsonText(self, ctx:TeradataSQLParser.JsonAsBsonTextContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#AttributeModification.
    def enterAttributeModification(self, ctx:TeradataSQLParser.AttributeModificationContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#AttributeModification.
    def exitAttributeModification(self, ctx:TeradataSQLParser.AttributeModificationContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#JsonCombine.
    def enterJsonCombine(self, ctx:TeradataSQLParser.JsonCombineContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#JsonCombine.
    def exitJsonCombine(self, ctx:TeradataSQLParser.JsonCombineContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#XMLIsDocument.
    def enterXMLIsDocument(self, ctx:TeradataSQLParser.XMLIsDocumentContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#XMLIsDocument.
    def exitXMLIsDocument(self, ctx:TeradataSQLParser.XMLIsDocumentContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#MacroParameterReference.
    def enterMacroParameterReference(self, ctx:TeradataSQLParser.MacroParameterReferenceContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#MacroParameterReference.
    def exitMacroParameterReference(self, ctx:TeradataSQLParser.MacroParameterReferenceContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#XMLIsContent.
    def enterXMLIsContent(self, ctx:TeradataSQLParser.XMLIsContentContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#XMLIsContent.
    def exitXMLIsContent(self, ctx:TeradataSQLParser.XMLIsContentContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#ArrayElementReference.
    def enterArrayElementReference(self, ctx:TeradataSQLParser.ArrayElementReferenceContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#ArrayElementReference.
    def exitArrayElementReference(self, ctx:TeradataSQLParser.ArrayElementReferenceContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#ArrayCardinality.
    def enterArrayCardinality(self, ctx:TeradataSQLParser.ArrayCardinalityContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#ArrayCardinality.
    def exitArrayCardinality(self, ctx:TeradataSQLParser.ArrayCardinalityContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#CaseExpr.
    def enterCaseExpr(self, ctx:TeradataSQLParser.CaseExprContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#CaseExpr.
    def exitCaseExpr(self, ctx:TeradataSQLParser.CaseExprContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#JsonKeycount.
    def enterJsonKeycount(self, ctx:TeradataSQLParser.JsonKeycountContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#JsonKeycount.
    def exitJsonKeycount(self, ctx:TeradataSQLParser.JsonKeycountContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#JsonAllObjectMembers.
    def enterJsonAllObjectMembers(self, ctx:TeradataSQLParser.JsonAllObjectMembersContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#JsonAllObjectMembers.
    def exitJsonAllObjectMembers(self, ctx:TeradataSQLParser.JsonAllObjectMembersContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#tuple.
    def enterTuple(self, ctx:TeradataSQLParser.TupleContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#tuple.
    def exitTuple(self, ctx:TeradataSQLParser.TupleContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#tuple_attribute.
    def enterTuple_attribute(self, ctx:TeradataSQLParser.Tuple_attributeContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#tuple_attribute.
    def exitTuple_attribute(self, ctx:TeradataSQLParser.Tuple_attributeContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#case_expr.
    def enterCase_expr(self, ctx:TeradataSQLParser.Case_exprContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#case_expr.
    def exitCase_expr(self, ctx:TeradataSQLParser.Case_exprContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#valued_case_expr.
    def enterValued_case_expr(self, ctx:TeradataSQLParser.Valued_case_exprContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#valued_case_expr.
    def exitValued_case_expr(self, ctx:TeradataSQLParser.Valued_case_exprContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#searched_case_expr.
    def enterSearched_case_expr(self, ctx:TeradataSQLParser.Searched_case_exprContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#searched_case_expr.
    def exitSearched_case_expr(self, ctx:TeradataSQLParser.Searched_case_exprContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#coalesce_expr.
    def enterCoalesce_expr(self, ctx:TeradataSQLParser.Coalesce_exprContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#coalesce_expr.
    def exitCoalesce_expr(self, ctx:TeradataSQLParser.Coalesce_exprContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#nullif_expr.
    def enterNullif_expr(self, ctx:TeradataSQLParser.Nullif_exprContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#nullif_expr.
    def exitNullif_expr(self, ctx:TeradataSQLParser.Nullif_exprContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#interval_expr_base.
    def enterInterval_expr_base(self, ctx:TeradataSQLParser.Interval_expr_baseContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#interval_expr_base.
    def exitInterval_expr_base(self, ctx:TeradataSQLParser.Interval_expr_baseContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#interval_expr_parenthesized.
    def enterInterval_expr_parenthesized(self, ctx:TeradataSQLParser.Interval_expr_parenthesizedContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#interval_expr_parenthesized.
    def exitInterval_expr_parenthesized(self, ctx:TeradataSQLParser.Interval_expr_parenthesizedContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#interval_expr_start_end_phrase.
    def enterInterval_expr_start_end_phrase(self, ctx:TeradataSQLParser.Interval_expr_start_end_phraseContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#interval_expr_start_end_phrase.
    def exitInterval_expr_start_end_phrase(self, ctx:TeradataSQLParser.Interval_expr_start_end_phraseContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#function_invocation.
    def enterFunction_invocation(self, ctx:TeradataSQLParser.Function_invocationContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#function_invocation.
    def exitFunction_invocation(self, ctx:TeradataSQLParser.Function_invocationContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#AggOneArg.
    def enterAggOneArg(self, ctx:TeradataSQLParser.AggOneArgContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#AggOneArg.
    def exitAggOneArg(self, ctx:TeradataSQLParser.AggOneArgContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#AggTwoArgs.
    def enterAggTwoArgs(self, ctx:TeradataSQLParser.AggTwoArgsContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#AggTwoArgs.
    def exitAggTwoArgs(self, ctx:TeradataSQLParser.AggTwoArgsContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#AggCount.
    def enterAggCount(self, ctx:TeradataSQLParser.AggCountContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#AggCount.
    def exitAggCount(self, ctx:TeradataSQLParser.AggCountContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#Grouping.
    def enterGrouping(self, ctx:TeradataSQLParser.GroupingContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#Grouping.
    def exitGrouping(self, ctx:TeradataSQLParser.GroupingContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#ListAgg.
    def enterListAgg(self, ctx:TeradataSQLParser.ListAggContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#ListAgg.
    def exitListAgg(self, ctx:TeradataSQLParser.ListAggContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#analytic_function.
    def enterAnalytic_function(self, ctx:TeradataSQLParser.Analytic_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#analytic_function.
    def exitAnalytic_function(self, ctx:TeradataSQLParser.Analytic_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#arithmetic_function.
    def enterArithmetic_function(self, ctx:TeradataSQLParser.Arithmetic_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#arithmetic_function.
    def exitArithmetic_function(self, ctx:TeradataSQLParser.Arithmetic_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#array_function.
    def enterArray_function(self, ctx:TeradataSQLParser.Array_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#array_function.
    def exitArray_function(self, ctx:TeradataSQLParser.Array_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#attribute_function.
    def enterAttribute_function(self, ctx:TeradataSQLParser.Attribute_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#attribute_function.
    def exitAttribute_function(self, ctx:TeradataSQLParser.Attribute_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#byte_function.
    def enterByte_function(self, ctx:TeradataSQLParser.Byte_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#byte_function.
    def exitByte_function(self, ctx:TeradataSQLParser.Byte_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#builtin_function.
    def enterBuiltin_function(self, ctx:TeradataSQLParser.Builtin_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#builtin_function.
    def exitBuiltin_function(self, ctx:TeradataSQLParser.Builtin_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#calendar_function.
    def enterCalendar_function(self, ctx:TeradataSQLParser.Calendar_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#calendar_function.
    def exitCalendar_function(self, ctx:TeradataSQLParser.Calendar_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#comparison_function.
    def enterComparison_function(self, ctx:TeradataSQLParser.Comparison_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#comparison_function.
    def exitComparison_function(self, ctx:TeradataSQLParser.Comparison_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#compression_function.
    def enterCompression_function(self, ctx:TeradataSQLParser.Compression_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#compression_function.
    def exitCompression_function(self, ctx:TeradataSQLParser.Compression_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#conversion_function.
    def enterConversion_function(self, ctx:TeradataSQLParser.Conversion_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#conversion_function.
    def exitConversion_function(self, ctx:TeradataSQLParser.Conversion_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#date_function.
    def enterDate_function(self, ctx:TeradataSQLParser.Date_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#date_function.
    def exitDate_function(self, ctx:TeradataSQLParser.Date_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#hash_function.
    def enterHash_function(self, ctx:TeradataSQLParser.Hash_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#hash_function.
    def exitHash_function(self, ctx:TeradataSQLParser.Hash_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#lob_function.
    def enterLob_function(self, ctx:TeradataSQLParser.Lob_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#lob_function.
    def exitLob_function(self, ctx:TeradataSQLParser.Lob_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#map_function.
    def enterMap_function(self, ctx:TeradataSQLParser.Map_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#map_function.
    def exitMap_function(self, ctx:TeradataSQLParser.Map_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#nvl_funtion.
    def enterNvl_funtion(self, ctx:TeradataSQLParser.Nvl_funtionContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#nvl_funtion.
    def exitNvl_funtion(self, ctx:TeradataSQLParser.Nvl_funtionContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#period_function.
    def enterPeriod_function(self, ctx:TeradataSQLParser.Period_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#period_function.
    def exitPeriod_function(self, ctx:TeradataSQLParser.Period_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#regexp_function.
    def enterRegexp_function(self, ctx:TeradataSQLParser.Regexp_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#regexp_function.
    def exitRegexp_function(self, ctx:TeradataSQLParser.Regexp_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#string_function.
    def enterString_function(self, ctx:TeradataSQLParser.String_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#string_function.
    def exitString_function(self, ctx:TeradataSQLParser.String_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#json_function.
    def enterJson_function(self, ctx:TeradataSQLParser.Json_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#json_function.
    def exitJson_function(self, ctx:TeradataSQLParser.Json_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#xml_function.
    def enterXml_function(self, ctx:TeradataSQLParser.Xml_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#xml_function.
    def exitXml_function(self, ctx:TeradataSQLParser.Xml_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#other_function.
    def enterOther_function(self, ctx:TeradataSQLParser.Other_functionContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#other_function.
    def exitOther_function(self, ctx:TeradataSQLParser.Other_functionContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#partitioning_expr.
    def enterPartitioning_expr(self, ctx:TeradataSQLParser.Partitioning_exprContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#partitioning_expr.
    def exitPartitioning_expr(self, ctx:TeradataSQLParser.Partitioning_exprContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#td_sysfnlib.
    def enterTd_sysfnlib(self, ctx:TeradataSQLParser.Td_sysfnlibContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#td_sysfnlib.
    def exitTd_sysfnlib(self, ctx:TeradataSQLParser.Td_sysfnlibContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#td_sysxml.
    def enterTd_sysxml(self, ctx:TeradataSQLParser.Td_sysxmlContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#td_sysxml.
    def exitTd_sysxml(self, ctx:TeradataSQLParser.Td_sysxmlContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#syslib.
    def enterSyslib(self, ctx:TeradataSQLParser.SyslibContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#syslib.
    def exitSyslib(self, ctx:TeradataSQLParser.SyslibContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#td_server_db.
    def enterTd_server_db(self, ctx:TeradataSQLParser.Td_server_dbContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#td_server_db.
    def exitTd_server_db(self, ctx:TeradataSQLParser.Td_server_dbContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#translation_mapping.
    def enterTranslation_mapping(self, ctx:TeradataSQLParser.Translation_mappingContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#translation_mapping.
    def exitTranslation_mapping(self, ctx:TeradataSQLParser.Translation_mappingContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#attribute_modification.
    def enterAttribute_modification(self, ctx:TeradataSQLParser.Attribute_modificationContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#attribute_modification.
    def exitAttribute_modification(self, ctx:TeradataSQLParser.Attribute_modificationContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#returns_clause.
    def enterReturns_clause(self, ctx:TeradataSQLParser.Returns_clauseContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#returns_clause.
    def exitReturns_clause(self, ctx:TeradataSQLParser.Returns_clauseContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#attribute_modification_option.
    def enterAttribute_modification_option(self, ctx:TeradataSQLParser.Attribute_modification_optionContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#attribute_modification_option.
    def exitAttribute_modification_option(self, ctx:TeradataSQLParser.Attribute_modification_optionContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#teradata_type_conversion.
    def enterTeradata_type_conversion(self, ctx:TeradataSQLParser.Teradata_type_conversionContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#teradata_type_conversion.
    def exitTeradata_type_conversion(self, ctx:TeradataSQLParser.Teradata_type_conversionContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#teradata_type_conversion_data_attribute.
    def enterTeradata_type_conversion_data_attribute(self, ctx:TeradataSQLParser.Teradata_type_conversion_data_attributeContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#teradata_type_conversion_data_attribute.
    def exitTeradata_type_conversion_data_attribute(self, ctx:TeradataSQLParser.Teradata_type_conversion_data_attributeContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#case_spec.
    def enterCase_spec(self, ctx:TeradataSQLParser.Case_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#case_spec.
    def exitCase_spec(self, ctx:TeradataSQLParser.Case_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#range_expr.
    def enterRange_expr(self, ctx:TeradataSQLParser.Range_exprContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#range_expr.
    def exitRange_expr(self, ctx:TeradataSQLParser.Range_exprContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#range_list.
    def enterRange_list(self, ctx:TeradataSQLParser.Range_listContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#range_list.
    def exitRange_list(self, ctx:TeradataSQLParser.Range_listContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#range_expr_1.
    def enterRange_expr_1(self, ctx:TeradataSQLParser.Range_expr_1Context):
        pass

    # Exit a parse tree produced by TeradataSQLParser#range_expr_1.
    def exitRange_expr_1(self, ctx:TeradataSQLParser.Range_expr_1Context):
        pass


    # Enter a parse tree produced by TeradataSQLParser#range_expr_2.
    def enterRange_expr_2(self, ctx:TeradataSQLParser.Range_expr_2Context):
        pass

    # Exit a parse tree produced by TeradataSQLParser#range_expr_2.
    def exitRange_expr_2(self, ctx:TeradataSQLParser.Range_expr_2Context):
        pass


    # Enter a parse tree produced by TeradataSQLParser#range_expr_3.
    def enterRange_expr_3(self, ctx:TeradataSQLParser.Range_expr_3Context):
        pass

    # Exit a parse tree produced by TeradataSQLParser#range_expr_3.
    def exitRange_expr_3(self, ctx:TeradataSQLParser.Range_expr_3Context):
        pass


    # Enter a parse tree produced by TeradataSQLParser#range_spec.
    def enterRange_spec(self, ctx:TeradataSQLParser.Range_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#range_spec.
    def exitRange_spec(self, ctx:TeradataSQLParser.Range_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#hash_bucket_number_expr.
    def enterHash_bucket_number_expr(self, ctx:TeradataSQLParser.Hash_bucket_number_exprContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#hash_bucket_number_expr.
    def exitHash_bucket_number_expr(self, ctx:TeradataSQLParser.Hash_bucket_number_exprContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#window_spec.
    def enterWindow_spec(self, ctx:TeradataSQLParser.Window_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#window_spec.
    def exitWindow_spec(self, ctx:TeradataSQLParser.Window_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#window_spec_without_rows.
    def enterWindow_spec_without_rows(self, ctx:TeradataSQLParser.Window_spec_without_rowsContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#window_spec_without_rows.
    def exitWindow_spec_without_rows(self, ctx:TeradataSQLParser.Window_spec_without_rowsContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#window_spec_with_ties.
    def enterWindow_spec_with_ties(self, ctx:TeradataSQLParser.Window_spec_with_tiesContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#window_spec_with_ties.
    def exitWindow_spec_with_ties(self, ctx:TeradataSQLParser.Window_spec_with_tiesContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#window_partition_by.
    def enterWindow_partition_by(self, ctx:TeradataSQLParser.Window_partition_byContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#window_partition_by.
    def exitWindow_partition_by(self, ctx:TeradataSQLParser.Window_partition_byContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#window_order_by.
    def enterWindow_order_by(self, ctx:TeradataSQLParser.Window_order_byContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#window_order_by.
    def exitWindow_order_by(self, ctx:TeradataSQLParser.Window_order_byContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#window_rows.
    def enterWindow_rows(self, ctx:TeradataSQLParser.Window_rowsContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#window_rows.
    def exitWindow_rows(self, ctx:TeradataSQLParser.Window_rowsContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#json_param_spec.
    def enterJson_param_spec(self, ctx:TeradataSQLParser.Json_param_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#json_param_spec.
    def exitJson_param_spec(self, ctx:TeradataSQLParser.Json_param_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#xml_query_argument.
    def enterXml_query_argument(self, ctx:TeradataSQLParser.Xml_query_argumentContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#xml_query_argument.
    def exitXml_query_argument(self, ctx:TeradataSQLParser.Xml_query_argumentContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#xml_query_variable_spec.
    def enterXml_query_variable_spec(self, ctx:TeradataSQLParser.Xml_query_variable_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#xml_query_variable_spec.
    def exitXml_query_variable_spec(self, ctx:TeradataSQLParser.Xml_query_variable_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#xml_attribute_declaration.
    def enterXml_attribute_declaration(self, ctx:TeradataSQLParser.Xml_attribute_declarationContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#xml_attribute_declaration.
    def exitXml_attribute_declaration(self, ctx:TeradataSQLParser.Xml_attribute_declarationContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#xml_attribute_spec.
    def enterXml_attribute_spec(self, ctx:TeradataSQLParser.Xml_attribute_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#xml_attribute_spec.
    def exitXml_attribute_spec(self, ctx:TeradataSQLParser.Xml_attribute_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#xml_forest_element_spec.
    def enterXml_forest_element_spec(self, ctx:TeradataSQLParser.Xml_forest_element_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#xml_forest_element_spec.
    def exitXml_forest_element_spec(self, ctx:TeradataSQLParser.Xml_forest_element_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#xml_value_declaration.
    def enterXml_value_declaration(self, ctx:TeradataSQLParser.Xml_value_declarationContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#xml_value_declaration.
    def exitXml_value_declaration(self, ctx:TeradataSQLParser.Xml_value_declarationContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#xml_namespace_declaration.
    def enterXml_namespace_declaration(self, ctx:TeradataSQLParser.Xml_namespace_declarationContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#xml_namespace_declaration.
    def exitXml_namespace_declaration(self, ctx:TeradataSQLParser.Xml_namespace_declarationContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#xml_namespace_spec.
    def enterXml_namespace_spec(self, ctx:TeradataSQLParser.Xml_namespace_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#xml_namespace_spec.
    def exitXml_namespace_spec(self, ctx:TeradataSQLParser.Xml_namespace_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#xml_columns_spec.
    def enterXml_columns_spec(self, ctx:TeradataSQLParser.Xml_columns_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#xml_columns_spec.
    def exitXml_columns_spec(self, ctx:TeradataSQLParser.Xml_columns_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#xml_regular_column_definition.
    def enterXml_regular_column_definition(self, ctx:TeradataSQLParser.Xml_regular_column_definitionContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#xml_regular_column_definition.
    def exitXml_regular_column_definition(self, ctx:TeradataSQLParser.Xml_regular_column_definitionContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#xml_encoding.
    def enterXml_encoding(self, ctx:TeradataSQLParser.Xml_encodingContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#xml_encoding.
    def exitXml_encoding(self, ctx:TeradataSQLParser.Xml_encodingContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#xml_query_on_empty.
    def enterXml_query_on_empty(self, ctx:TeradataSQLParser.Xml_query_on_emptyContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#xml_query_on_empty.
    def exitXml_query_on_empty(self, ctx:TeradataSQLParser.Xml_query_on_emptyContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#xml_returning_spec.
    def enterXml_returning_spec(self, ctx:TeradataSQLParser.Xml_returning_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#xml_returning_spec.
    def exitXml_returning_spec(self, ctx:TeradataSQLParser.Xml_returning_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#xml_content_option_spec.
    def enterXml_content_option_spec(self, ctx:TeradataSQLParser.Xml_content_option_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#xml_content_option_spec.
    def exitXml_content_option_spec(self, ctx:TeradataSQLParser.Xml_content_option_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#ignore_respect_nulls.
    def enterIgnore_respect_nulls(self, ctx:TeradataSQLParser.Ignore_respect_nullsContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#ignore_respect_nulls.
    def exitIgnore_respect_nulls(self, ctx:TeradataSQLParser.Ignore_respect_nullsContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#number_of_rows.
    def enterNumber_of_rows(self, ctx:TeradataSQLParser.Number_of_rowsContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#number_of_rows.
    def exitNumber_of_rows(self, ctx:TeradataSQLParser.Number_of_rowsContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#with_ties.
    def enterWith_ties(self, ctx:TeradataSQLParser.With_tiesContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#with_ties.
    def exitWith_ties(self, ctx:TeradataSQLParser.With_tiesContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#pivot.
    def enterPivot(self, ctx:TeradataSQLParser.PivotContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#pivot.
    def exitPivot(self, ctx:TeradataSQLParser.PivotContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#pivot_spec.
    def enterPivot_spec(self, ctx:TeradataSQLParser.Pivot_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#pivot_spec.
    def exitPivot_spec(self, ctx:TeradataSQLParser.Pivot_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#pivot_with_phrase.
    def enterPivot_with_phrase(self, ctx:TeradataSQLParser.Pivot_with_phraseContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#pivot_with_phrase.
    def exitPivot_with_phrase(self, ctx:TeradataSQLParser.Pivot_with_phraseContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#pivot_agg_func_spec.
    def enterPivot_agg_func_spec(self, ctx:TeradataSQLParser.Pivot_agg_func_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#pivot_agg_func_spec.
    def exitPivot_agg_func_spec(self, ctx:TeradataSQLParser.Pivot_agg_func_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#pivot_for_phrase.
    def enterPivot_for_phrase(self, ctx:TeradataSQLParser.Pivot_for_phraseContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#pivot_for_phrase.
    def exitPivot_for_phrase(self, ctx:TeradataSQLParser.Pivot_for_phraseContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#pivot_with_spec.
    def enterPivot_with_spec(self, ctx:TeradataSQLParser.Pivot_with_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#pivot_with_spec.
    def exitPivot_with_spec(self, ctx:TeradataSQLParser.Pivot_with_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#pivot_expr_spec_scalar.
    def enterPivot_expr_spec_scalar(self, ctx:TeradataSQLParser.Pivot_expr_spec_scalarContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#pivot_expr_spec_scalar.
    def exitPivot_expr_spec_scalar(self, ctx:TeradataSQLParser.Pivot_expr_spec_scalarContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#pivot_expr_spec_list.
    def enterPivot_expr_spec_list(self, ctx:TeradataSQLParser.Pivot_expr_spec_listContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#pivot_expr_spec_list.
    def exitPivot_expr_spec_list(self, ctx:TeradataSQLParser.Pivot_expr_spec_listContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#unpivot.
    def enterUnpivot(self, ctx:TeradataSQLParser.UnpivotContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#unpivot.
    def exitUnpivot(self, ctx:TeradataSQLParser.UnpivotContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#unpivot_spec.
    def enterUnpivot_spec(self, ctx:TeradataSQLParser.Unpivot_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#unpivot_spec.
    def exitUnpivot_spec(self, ctx:TeradataSQLParser.Unpivot_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#unpivot_column_name_spec_single.
    def enterUnpivot_column_name_spec_single(self, ctx:TeradataSQLParser.Unpivot_column_name_spec_singleContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#unpivot_column_name_spec_single.
    def exitUnpivot_column_name_spec_single(self, ctx:TeradataSQLParser.Unpivot_column_name_spec_singleContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#unpivot_column_name_spec_list.
    def enterUnpivot_column_name_spec_list(self, ctx:TeradataSQLParser.Unpivot_column_name_spec_listContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#unpivot_column_name_spec_list.
    def exitUnpivot_column_name_spec_list(self, ctx:TeradataSQLParser.Unpivot_column_name_spec_listContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#at_timezone.
    def enterAt_timezone(self, ctx:TeradataSQLParser.At_timezoneContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#at_timezone.
    def exitAt_timezone(self, ctx:TeradataSQLParser.At_timezoneContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#elements_list.
    def enterElements_list(self, ctx:TeradataSQLParser.Elements_listContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#elements_list.
    def exitElements_list(self, ctx:TeradataSQLParser.Elements_listContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#scalar_expr_list.
    def enterScalar_expr_list(self, ctx:TeradataSQLParser.Scalar_expr_listContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#scalar_expr_list.
    def exitScalar_expr_list(self, ctx:TeradataSQLParser.Scalar_expr_listContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#scalar_expr_list_comma_separated.
    def enterScalar_expr_list_comma_separated(self, ctx:TeradataSQLParser.Scalar_expr_list_comma_separatedContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#scalar_expr_list_comma_separated.
    def exitScalar_expr_list_comma_separated(self, ctx:TeradataSQLParser.Scalar_expr_list_comma_separatedContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#column_list.
    def enterColumn_list(self, ctx:TeradataSQLParser.Column_listContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#column_list.
    def exitColumn_list(self, ctx:TeradataSQLParser.Column_listContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#subquery.
    def enterSubquery(self, ctx:TeradataSQLParser.SubqueryContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#subquery.
    def exitSubquery(self, ctx:TeradataSQLParser.SubqueryContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#column_spec.
    def enterColumn_spec(self, ctx:TeradataSQLParser.Column_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#column_spec.
    def exitColumn_spec(self, ctx:TeradataSQLParser.Column_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#variable_reference.
    def enterVariable_reference(self, ctx:TeradataSQLParser.Variable_referenceContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#variable_reference.
    def exitVariable_reference(self, ctx:TeradataSQLParser.Variable_referenceContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#cursor_variable_reference.
    def enterCursor_variable_reference(self, ctx:TeradataSQLParser.Cursor_variable_referenceContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#cursor_variable_reference.
    def exitCursor_variable_reference(self, ctx:TeradataSQLParser.Cursor_variable_referenceContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#macro_parameter_reference.
    def enterMacro_parameter_reference(self, ctx:TeradataSQLParser.Macro_parameter_referenceContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#macro_parameter_reference.
    def exitMacro_parameter_reference(self, ctx:TeradataSQLParser.Macro_parameter_referenceContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#array_scope_reference.
    def enterArray_scope_reference(self, ctx:TeradataSQLParser.Array_scope_referenceContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#array_scope_reference.
    def exitArray_scope_reference(self, ctx:TeradataSQLParser.Array_scope_referenceContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#comparison_operator.
    def enterComparison_operator(self, ctx:TeradataSQLParser.Comparison_operatorContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#comparison_operator.
    def exitComparison_operator(self, ctx:TeradataSQLParser.Comparison_operatorContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#quantifier.
    def enterQuantifier(self, ctx:TeradataSQLParser.QuantifierContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#quantifier.
    def exitQuantifier(self, ctx:TeradataSQLParser.QuantifierContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#request_modifier.
    def enterRequest_modifier(self, ctx:TeradataSQLParser.Request_modifierContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#request_modifier.
    def exitRequest_modifier(self, ctx:TeradataSQLParser.Request_modifierContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#locking_request_modifier.
    def enterLocking_request_modifier(self, ctx:TeradataSQLParser.Locking_request_modifierContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#locking_request_modifier.
    def exitLocking_request_modifier(self, ctx:TeradataSQLParser.Locking_request_modifierContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#locking_spec.
    def enterLocking_spec(self, ctx:TeradataSQLParser.Locking_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#locking_spec.
    def exitLocking_spec(self, ctx:TeradataSQLParser.Locking_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#lock_type.
    def enterLock_type(self, ctx:TeradataSQLParser.Lock_typeContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#lock_type.
    def exitLock_type(self, ctx:TeradataSQLParser.Lock_typeContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#with_request_modifier.
    def enterWith_request_modifier(self, ctx:TeradataSQLParser.With_request_modifierContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#with_request_modifier.
    def exitWith_request_modifier(self, ctx:TeradataSQLParser.With_request_modifierContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#cte_spec.
    def enterCte_spec(self, ctx:TeradataSQLParser.Cte_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#cte_spec.
    def exitCte_spec(self, ctx:TeradataSQLParser.Cte_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#regular_cte_spec.
    def enterRegular_cte_spec(self, ctx:TeradataSQLParser.Regular_cte_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#regular_cte_spec.
    def exitRegular_cte_spec(self, ctx:TeradataSQLParser.Regular_cte_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#recursive_cte_spec.
    def enterRecursive_cte_spec(self, ctx:TeradataSQLParser.Recursive_cte_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#recursive_cte_spec.
    def exitRecursive_cte_spec(self, ctx:TeradataSQLParser.Recursive_cte_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#using_request_modifier.
    def enterUsing_request_modifier(self, ctx:TeradataSQLParser.Using_request_modifierContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#using_request_modifier.
    def exitUsing_request_modifier(self, ctx:TeradataSQLParser.Using_request_modifierContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#using_spec.
    def enterUsing_spec(self, ctx:TeradataSQLParser.Using_specContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#using_spec.
    def exitUsing_spec(self, ctx:TeradataSQLParser.Using_specContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#explain_request_modifier.
    def enterExplain_request_modifier(self, ctx:TeradataSQLParser.Explain_request_modifierContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#explain_request_modifier.
    def exitExplain_request_modifier(self, ctx:TeradataSQLParser.Explain_request_modifierContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#dcl_stat.
    def enterDcl_stat(self, ctx:TeradataSQLParser.Dcl_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#dcl_stat.
    def exitDcl_stat(self, ctx:TeradataSQLParser.Dcl_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#give_stat.
    def enterGive_stat(self, ctx:TeradataSQLParser.Give_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#give_stat.
    def exitGive_stat(self, ctx:TeradataSQLParser.Give_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#grant_stat.
    def enterGrant_stat(self, ctx:TeradataSQLParser.Grant_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#grant_stat.
    def exitGrant_stat(self, ctx:TeradataSQLParser.Grant_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#grant_monitor_stat.
    def enterGrant_monitor_stat(self, ctx:TeradataSQLParser.Grant_monitor_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#grant_monitor_stat.
    def exitGrant_monitor_stat(self, ctx:TeradataSQLParser.Grant_monitor_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#grant_role_stat.
    def enterGrant_role_stat(self, ctx:TeradataSQLParser.Grant_role_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#grant_role_stat.
    def exitGrant_role_stat(self, ctx:TeradataSQLParser.Grant_role_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#grant_sql_form_stat.
    def enterGrant_sql_form_stat(self, ctx:TeradataSQLParser.Grant_sql_form_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#grant_sql_form_stat.
    def exitGrant_sql_form_stat(self, ctx:TeradataSQLParser.Grant_sql_form_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#grant_connect_through_stat.
    def enterGrant_connect_through_stat(self, ctx:TeradataSQLParser.Grant_connect_through_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#grant_connect_through_stat.
    def exitGrant_connect_through_stat(self, ctx:TeradataSQLParser.Grant_connect_through_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#grant_logon_stat.
    def enterGrant_logon_stat(self, ctx:TeradataSQLParser.Grant_logon_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#grant_logon_stat.
    def exitGrant_logon_stat(self, ctx:TeradataSQLParser.Grant_logon_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#grant_map_stat.
    def enterGrant_map_stat(self, ctx:TeradataSQLParser.Grant_map_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#grant_map_stat.
    def exitGrant_map_stat(self, ctx:TeradataSQLParser.Grant_map_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#grant_zone_stat.
    def enterGrant_zone_stat(self, ctx:TeradataSQLParser.Grant_zone_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#grant_zone_stat.
    def exitGrant_zone_stat(self, ctx:TeradataSQLParser.Grant_zone_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#grant_zone_override_stat.
    def enterGrant_zone_override_stat(self, ctx:TeradataSQLParser.Grant_zone_override_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#grant_zone_override_stat.
    def exitGrant_zone_override_stat(self, ctx:TeradataSQLParser.Grant_zone_override_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#revoke_stat.
    def enterRevoke_stat(self, ctx:TeradataSQLParser.Revoke_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#revoke_stat.
    def exitRevoke_stat(self, ctx:TeradataSQLParser.Revoke_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#revoke_monitor_stat.
    def enterRevoke_monitor_stat(self, ctx:TeradataSQLParser.Revoke_monitor_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#revoke_monitor_stat.
    def exitRevoke_monitor_stat(self, ctx:TeradataSQLParser.Revoke_monitor_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#revoke_role_stat.
    def enterRevoke_role_stat(self, ctx:TeradataSQLParser.Revoke_role_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#revoke_role_stat.
    def exitRevoke_role_stat(self, ctx:TeradataSQLParser.Revoke_role_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#revoke_sql_form_stat.
    def enterRevoke_sql_form_stat(self, ctx:TeradataSQLParser.Revoke_sql_form_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#revoke_sql_form_stat.
    def exitRevoke_sql_form_stat(self, ctx:TeradataSQLParser.Revoke_sql_form_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#revoke_connect_through_stat.
    def enterRevoke_connect_through_stat(self, ctx:TeradataSQLParser.Revoke_connect_through_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#revoke_connect_through_stat.
    def exitRevoke_connect_through_stat(self, ctx:TeradataSQLParser.Revoke_connect_through_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#revoke_logon_stat.
    def enterRevoke_logon_stat(self, ctx:TeradataSQLParser.Revoke_logon_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#revoke_logon_stat.
    def exitRevoke_logon_stat(self, ctx:TeradataSQLParser.Revoke_logon_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#revoke_map_stat.
    def enterRevoke_map_stat(self, ctx:TeradataSQLParser.Revoke_map_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#revoke_map_stat.
    def exitRevoke_map_stat(self, ctx:TeradataSQLParser.Revoke_map_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#revoke_zone_stat.
    def enterRevoke_zone_stat(self, ctx:TeradataSQLParser.Revoke_zone_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#revoke_zone_stat.
    def exitRevoke_zone_stat(self, ctx:TeradataSQLParser.Revoke_zone_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#revoke_zone_override_stat.
    def enterRevoke_zone_override_stat(self, ctx:TeradataSQLParser.Revoke_zone_override_statContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#revoke_zone_override_stat.
    def exitRevoke_zone_override_stat(self, ctx:TeradataSQLParser.Revoke_zone_override_statContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#privilege.
    def enterPrivilege(self, ctx:TeradataSQLParser.PrivilegeContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#privilege.
    def exitPrivilege(self, ctx:TeradataSQLParser.PrivilegeContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#privilege_object.
    def enterPrivilege_object(self, ctx:TeradataSQLParser.Privilege_objectContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#privilege_object.
    def exitPrivilege_object(self, ctx:TeradataSQLParser.Privilege_objectContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#map_privilege.
    def enterMap_privilege(self, ctx:TeradataSQLParser.Map_privilegeContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#map_privilege.
    def exitMap_privilege(self, ctx:TeradataSQLParser.Map_privilegeContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#role_privilege.
    def enterRole_privilege(self, ctx:TeradataSQLParser.Role_privilegeContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#role_privilege.
    def exitRole_privilege(self, ctx:TeradataSQLParser.Role_privilegeContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#profile_privilege.
    def enterProfile_privilege(self, ctx:TeradataSQLParser.Profile_privilegeContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#profile_privilege.
    def exitProfile_privilege(self, ctx:TeradataSQLParser.Profile_privilegeContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#zone_privilege.
    def enterZone_privilege(self, ctx:TeradataSQLParser.Zone_privilegeContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#zone_privilege.
    def exitZone_privilege(self, ctx:TeradataSQLParser.Zone_privilegeContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#monitor_privilege.
    def enterMonitor_privilege(self, ctx:TeradataSQLParser.Monitor_privilegeContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#monitor_privilege.
    def exitMonitor_privilege(self, ctx:TeradataSQLParser.Monitor_privilegeContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#grantee.
    def enterGrantee(self, ctx:TeradataSQLParser.GranteeContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#grantee.
    def exitGrantee(self, ctx:TeradataSQLParser.GranteeContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#revokee.
    def enterRevokee(self, ctx:TeradataSQLParser.RevokeeContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#revokee.
    def exitRevokee(self, ctx:TeradataSQLParser.RevokeeContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#function_parameter.
    def enterFunction_parameter(self, ctx:TeradataSQLParser.Function_parameterContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#function_parameter.
    def exitFunction_parameter(self, ctx:TeradataSQLParser.Function_parameterContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#with_admin_option.
    def enterWith_admin_option(self, ctx:TeradataSQLParser.With_admin_optionContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#with_admin_option.
    def exitWith_admin_option(self, ctx:TeradataSQLParser.With_admin_optionContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#with_grant_option.
    def enterWith_grant_option(self, ctx:TeradataSQLParser.With_grant_optionContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#with_grant_option.
    def exitWith_grant_option(self, ctx:TeradataSQLParser.With_grant_optionContext):
        pass


    # Enter a parse tree produced by TeradataSQLParser#grant_option_for.
    def enterGrant_option_for(self, ctx:TeradataSQLParser.Grant_option_forContext):
        pass

    # Exit a parse tree produced by TeradataSQLParser#grant_option_for.
    def exitGrant_option_for(self, ctx:TeradataSQLParser.Grant_option_forContext):
        pass



del TeradataSQLParser