# Generated from sql/snowflake/SnowflakeParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SnowflakeParser import SnowflakeParser
else:
    from SnowflakeParser import SnowflakeParser

# This class defines a complete listener for a parse tree produced by SnowflakeParser.
class SnowflakeParserListener(ParseTreeListener):

    # Enter a parse tree produced by SnowflakeParser#snowflake_file.
    def enterSnowflake_file(self, ctx:SnowflakeParser.Snowflake_fileContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#snowflake_file.
    def exitSnowflake_file(self, ctx:SnowflakeParser.Snowflake_fileContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#batch.
    def enterBatch(self, ctx:SnowflakeParser.BatchContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#batch.
    def exitBatch(self, ctx:SnowflakeParser.BatchContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#sql_command.
    def enterSql_command(self, ctx:SnowflakeParser.Sql_commandContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#sql_command.
    def exitSql_command(self, ctx:SnowflakeParser.Sql_commandContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#ddl_command.
    def enterDdl_command(self, ctx:SnowflakeParser.Ddl_commandContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#ddl_command.
    def exitDdl_command(self, ctx:SnowflakeParser.Ddl_commandContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#dml_command.
    def enterDml_command(self, ctx:SnowflakeParser.Dml_commandContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#dml_command.
    def exitDml_command(self, ctx:SnowflakeParser.Dml_commandContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#insert_statement.
    def enterInsert_statement(self, ctx:SnowflakeParser.Insert_statementContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#insert_statement.
    def exitInsert_statement(self, ctx:SnowflakeParser.Insert_statementContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#insert_multi_table_statement.
    def enterInsert_multi_table_statement(self, ctx:SnowflakeParser.Insert_multi_table_statementContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#insert_multi_table_statement.
    def exitInsert_multi_table_statement(self, ctx:SnowflakeParser.Insert_multi_table_statementContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#into_clause2.
    def enterInto_clause2(self, ctx:SnowflakeParser.Into_clause2Context):
        pass

    # Exit a parse tree produced by SnowflakeParser#into_clause2.
    def exitInto_clause2(self, ctx:SnowflakeParser.Into_clause2Context):
        pass


    # Enter a parse tree produced by SnowflakeParser#values_list.
    def enterValues_list(self, ctx:SnowflakeParser.Values_listContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#values_list.
    def exitValues_list(self, ctx:SnowflakeParser.Values_listContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#value_item.
    def enterValue_item(self, ctx:SnowflakeParser.Value_itemContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#value_item.
    def exitValue_item(self, ctx:SnowflakeParser.Value_itemContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#merge_statement.
    def enterMerge_statement(self, ctx:SnowflakeParser.Merge_statementContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#merge_statement.
    def exitMerge_statement(self, ctx:SnowflakeParser.Merge_statementContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#merge_matches.
    def enterMerge_matches(self, ctx:SnowflakeParser.Merge_matchesContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#merge_matches.
    def exitMerge_matches(self, ctx:SnowflakeParser.Merge_matchesContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#merge_cond.
    def enterMerge_cond(self, ctx:SnowflakeParser.Merge_condContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#merge_cond.
    def exitMerge_cond(self, ctx:SnowflakeParser.Merge_condContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#merge_update_delete.
    def enterMerge_update_delete(self, ctx:SnowflakeParser.Merge_update_deleteContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#merge_update_delete.
    def exitMerge_update_delete(self, ctx:SnowflakeParser.Merge_update_deleteContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#merge_insert.
    def enterMerge_insert(self, ctx:SnowflakeParser.Merge_insertContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#merge_insert.
    def exitMerge_insert(self, ctx:SnowflakeParser.Merge_insertContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#update_statement.
    def enterUpdate_statement(self, ctx:SnowflakeParser.Update_statementContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#update_statement.
    def exitUpdate_statement(self, ctx:SnowflakeParser.Update_statementContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#table_or_query.
    def enterTable_or_query(self, ctx:SnowflakeParser.Table_or_queryContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#table_or_query.
    def exitTable_or_query(self, ctx:SnowflakeParser.Table_or_queryContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#delete_statement.
    def enterDelete_statement(self, ctx:SnowflakeParser.Delete_statementContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#delete_statement.
    def exitDelete_statement(self, ctx:SnowflakeParser.Delete_statementContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#values_builder.
    def enterValues_builder(self, ctx:SnowflakeParser.Values_builderContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#values_builder.
    def exitValues_builder(self, ctx:SnowflakeParser.Values_builderContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#other_command.
    def enterOther_command(self, ctx:SnowflakeParser.Other_commandContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#other_command.
    def exitOther_command(self, ctx:SnowflakeParser.Other_commandContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#begin_txn.
    def enterBegin_txn(self, ctx:SnowflakeParser.Begin_txnContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#begin_txn.
    def exitBegin_txn(self, ctx:SnowflakeParser.Begin_txnContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#copy_into_table.
    def enterCopy_into_table(self, ctx:SnowflakeParser.Copy_into_tableContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#copy_into_table.
    def exitCopy_into_table(self, ctx:SnowflakeParser.Copy_into_tableContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#external_location.
    def enterExternal_location(self, ctx:SnowflakeParser.External_locationContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#external_location.
    def exitExternal_location(self, ctx:SnowflakeParser.External_locationContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#files.
    def enterFiles(self, ctx:SnowflakeParser.FilesContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#files.
    def exitFiles(self, ctx:SnowflakeParser.FilesContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#file_format.
    def enterFile_format(self, ctx:SnowflakeParser.File_formatContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#file_format.
    def exitFile_format(self, ctx:SnowflakeParser.File_formatContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#format_name.
    def enterFormat_name(self, ctx:SnowflakeParser.Format_nameContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#format_name.
    def exitFormat_name(self, ctx:SnowflakeParser.Format_nameContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#format_type.
    def enterFormat_type(self, ctx:SnowflakeParser.Format_typeContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#format_type.
    def exitFormat_type(self, ctx:SnowflakeParser.Format_typeContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#stage_file_format.
    def enterStage_file_format(self, ctx:SnowflakeParser.Stage_file_formatContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#stage_file_format.
    def exitStage_file_format(self, ctx:SnowflakeParser.Stage_file_formatContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#copy_into_location.
    def enterCopy_into_location(self, ctx:SnowflakeParser.Copy_into_locationContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#copy_into_location.
    def exitCopy_into_location(self, ctx:SnowflakeParser.Copy_into_locationContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#comment.
    def enterComment(self, ctx:SnowflakeParser.CommentContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#comment.
    def exitComment(self, ctx:SnowflakeParser.CommentContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#function_signature.
    def enterFunction_signature(self, ctx:SnowflakeParser.Function_signatureContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#function_signature.
    def exitFunction_signature(self, ctx:SnowflakeParser.Function_signatureContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#commit.
    def enterCommit(self, ctx:SnowflakeParser.CommitContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#commit.
    def exitCommit(self, ctx:SnowflakeParser.CommitContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#execute_immediate.
    def enterExecute_immediate(self, ctx:SnowflakeParser.Execute_immediateContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#execute_immediate.
    def exitExecute_immediate(self, ctx:SnowflakeParser.Execute_immediateContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#execute_task.
    def enterExecute_task(self, ctx:SnowflakeParser.Execute_taskContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#execute_task.
    def exitExecute_task(self, ctx:SnowflakeParser.Execute_taskContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#explain.
    def enterExplain(self, ctx:SnowflakeParser.ExplainContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#explain.
    def exitExplain(self, ctx:SnowflakeParser.ExplainContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#parallel.
    def enterParallel(self, ctx:SnowflakeParser.ParallelContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#parallel.
    def exitParallel(self, ctx:SnowflakeParser.ParallelContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#get_dml.
    def enterGet_dml(self, ctx:SnowflakeParser.Get_dmlContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#get_dml.
    def exitGet_dml(self, ctx:SnowflakeParser.Get_dmlContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#grant_ownership.
    def enterGrant_ownership(self, ctx:SnowflakeParser.Grant_ownershipContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#grant_ownership.
    def exitGrant_ownership(self, ctx:SnowflakeParser.Grant_ownershipContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#grant_to_role.
    def enterGrant_to_role(self, ctx:SnowflakeParser.Grant_to_roleContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#grant_to_role.
    def exitGrant_to_role(self, ctx:SnowflakeParser.Grant_to_roleContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#global_privileges.
    def enterGlobal_privileges(self, ctx:SnowflakeParser.Global_privilegesContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#global_privileges.
    def exitGlobal_privileges(self, ctx:SnowflakeParser.Global_privilegesContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#global_privilege.
    def enterGlobal_privilege(self, ctx:SnowflakeParser.Global_privilegeContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#global_privilege.
    def exitGlobal_privilege(self, ctx:SnowflakeParser.Global_privilegeContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#account_object_privileges.
    def enterAccount_object_privileges(self, ctx:SnowflakeParser.Account_object_privilegesContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#account_object_privileges.
    def exitAccount_object_privileges(self, ctx:SnowflakeParser.Account_object_privilegesContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#account_object_privilege.
    def enterAccount_object_privilege(self, ctx:SnowflakeParser.Account_object_privilegeContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#account_object_privilege.
    def exitAccount_object_privilege(self, ctx:SnowflakeParser.Account_object_privilegeContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#schema_privileges.
    def enterSchema_privileges(self, ctx:SnowflakeParser.Schema_privilegesContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#schema_privileges.
    def exitSchema_privileges(self, ctx:SnowflakeParser.Schema_privilegesContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#schema_privilege.
    def enterSchema_privilege(self, ctx:SnowflakeParser.Schema_privilegeContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#schema_privilege.
    def exitSchema_privilege(self, ctx:SnowflakeParser.Schema_privilegeContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#schema_object_privileges.
    def enterSchema_object_privileges(self, ctx:SnowflakeParser.Schema_object_privilegesContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#schema_object_privileges.
    def exitSchema_object_privileges(self, ctx:SnowflakeParser.Schema_object_privilegesContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#schema_object_privilege.
    def enterSchema_object_privilege(self, ctx:SnowflakeParser.Schema_object_privilegeContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#schema_object_privilege.
    def exitSchema_object_privilege(self, ctx:SnowflakeParser.Schema_object_privilegeContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#grant_to_share.
    def enterGrant_to_share(self, ctx:SnowflakeParser.Grant_to_shareContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#grant_to_share.
    def exitGrant_to_share(self, ctx:SnowflakeParser.Grant_to_shareContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#object_privilege.
    def enterObject_privilege(self, ctx:SnowflakeParser.Object_privilegeContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#object_privilege.
    def exitObject_privilege(self, ctx:SnowflakeParser.Object_privilegeContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#grant_role.
    def enterGrant_role(self, ctx:SnowflakeParser.Grant_roleContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#grant_role.
    def exitGrant_role(self, ctx:SnowflakeParser.Grant_roleContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#role_name.
    def enterRole_name(self, ctx:SnowflakeParser.Role_nameContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#role_name.
    def exitRole_name(self, ctx:SnowflakeParser.Role_nameContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#system_defined_role.
    def enterSystem_defined_role(self, ctx:SnowflakeParser.System_defined_roleContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#system_defined_role.
    def exitSystem_defined_role(self, ctx:SnowflakeParser.System_defined_roleContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#list.
    def enterList(self, ctx:SnowflakeParser.ListContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#list.
    def exitList(self, ctx:SnowflakeParser.ListContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#user_stage.
    def enterUser_stage(self, ctx:SnowflakeParser.User_stageContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#user_stage.
    def exitUser_stage(self, ctx:SnowflakeParser.User_stageContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#table_stage.
    def enterTable_stage(self, ctx:SnowflakeParser.Table_stageContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#table_stage.
    def exitTable_stage(self, ctx:SnowflakeParser.Table_stageContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#named_stage.
    def enterNamed_stage(self, ctx:SnowflakeParser.Named_stageContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#named_stage.
    def exitNamed_stage(self, ctx:SnowflakeParser.Named_stageContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#stage_path.
    def enterStage_path(self, ctx:SnowflakeParser.Stage_pathContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#stage_path.
    def exitStage_path(self, ctx:SnowflakeParser.Stage_pathContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#put.
    def enterPut(self, ctx:SnowflakeParser.PutContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#put.
    def exitPut(self, ctx:SnowflakeParser.PutContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#remove.
    def enterRemove(self, ctx:SnowflakeParser.RemoveContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#remove.
    def exitRemove(self, ctx:SnowflakeParser.RemoveContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#revoke_from_role.
    def enterRevoke_from_role(self, ctx:SnowflakeParser.Revoke_from_roleContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#revoke_from_role.
    def exitRevoke_from_role(self, ctx:SnowflakeParser.Revoke_from_roleContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#revoke_from_share.
    def enterRevoke_from_share(self, ctx:SnowflakeParser.Revoke_from_shareContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#revoke_from_share.
    def exitRevoke_from_share(self, ctx:SnowflakeParser.Revoke_from_shareContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#revoke_role.
    def enterRevoke_role(self, ctx:SnowflakeParser.Revoke_roleContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#revoke_role.
    def exitRevoke_role(self, ctx:SnowflakeParser.Revoke_roleContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#rollback.
    def enterRollback(self, ctx:SnowflakeParser.RollbackContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#rollback.
    def exitRollback(self, ctx:SnowflakeParser.RollbackContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#set.
    def enterSet(self, ctx:SnowflakeParser.SetContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#set.
    def exitSet(self, ctx:SnowflakeParser.SetContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#truncate_materialized_view.
    def enterTruncate_materialized_view(self, ctx:SnowflakeParser.Truncate_materialized_viewContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#truncate_materialized_view.
    def exitTruncate_materialized_view(self, ctx:SnowflakeParser.Truncate_materialized_viewContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#truncate_table.
    def enterTruncate_table(self, ctx:SnowflakeParser.Truncate_tableContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#truncate_table.
    def exitTruncate_table(self, ctx:SnowflakeParser.Truncate_tableContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#unset.
    def enterUnset(self, ctx:SnowflakeParser.UnsetContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#unset.
    def exitUnset(self, ctx:SnowflakeParser.UnsetContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#alter_command.
    def enterAlter_command(self, ctx:SnowflakeParser.Alter_commandContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#alter_command.
    def exitAlter_command(self, ctx:SnowflakeParser.Alter_commandContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#account_params.
    def enterAccount_params(self, ctx:SnowflakeParser.Account_paramsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#account_params.
    def exitAccount_params(self, ctx:SnowflakeParser.Account_paramsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#object_params.
    def enterObject_params(self, ctx:SnowflakeParser.Object_paramsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#object_params.
    def exitObject_params(self, ctx:SnowflakeParser.Object_paramsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#default_ddl_collation.
    def enterDefault_ddl_collation(self, ctx:SnowflakeParser.Default_ddl_collationContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#default_ddl_collation.
    def exitDefault_ddl_collation(self, ctx:SnowflakeParser.Default_ddl_collationContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#object_properties.
    def enterObject_properties(self, ctx:SnowflakeParser.Object_propertiesContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#object_properties.
    def exitObject_properties(self, ctx:SnowflakeParser.Object_propertiesContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#session_params.
    def enterSession_params(self, ctx:SnowflakeParser.Session_paramsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#session_params.
    def exitSession_params(self, ctx:SnowflakeParser.Session_paramsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#alter_account.
    def enterAlter_account(self, ctx:SnowflakeParser.Alter_accountContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#alter_account.
    def exitAlter_account(self, ctx:SnowflakeParser.Alter_accountContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#enabled_true_false.
    def enterEnabled_true_false(self, ctx:SnowflakeParser.Enabled_true_falseContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#enabled_true_false.
    def exitEnabled_true_false(self, ctx:SnowflakeParser.Enabled_true_falseContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#alter_alert.
    def enterAlter_alert(self, ctx:SnowflakeParser.Alter_alertContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#alter_alert.
    def exitAlter_alert(self, ctx:SnowflakeParser.Alter_alertContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#resume_suspend.
    def enterResume_suspend(self, ctx:SnowflakeParser.Resume_suspendContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#resume_suspend.
    def exitResume_suspend(self, ctx:SnowflakeParser.Resume_suspendContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#alert_set_clause.
    def enterAlert_set_clause(self, ctx:SnowflakeParser.Alert_set_clauseContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#alert_set_clause.
    def exitAlert_set_clause(self, ctx:SnowflakeParser.Alert_set_clauseContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#alert_unset_clause.
    def enterAlert_unset_clause(self, ctx:SnowflakeParser.Alert_unset_clauseContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#alert_unset_clause.
    def exitAlert_unset_clause(self, ctx:SnowflakeParser.Alert_unset_clauseContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#alter_api_integration.
    def enterAlter_api_integration(self, ctx:SnowflakeParser.Alter_api_integrationContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#alter_api_integration.
    def exitAlter_api_integration(self, ctx:SnowflakeParser.Alter_api_integrationContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#api_integration_property.
    def enterApi_integration_property(self, ctx:SnowflakeParser.Api_integration_propertyContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#api_integration_property.
    def exitApi_integration_property(self, ctx:SnowflakeParser.Api_integration_propertyContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#alter_connection.
    def enterAlter_connection(self, ctx:SnowflakeParser.Alter_connectionContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#alter_connection.
    def exitAlter_connection(self, ctx:SnowflakeParser.Alter_connectionContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#alter_database.
    def enterAlter_database(self, ctx:SnowflakeParser.Alter_databaseContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#alter_database.
    def exitAlter_database(self, ctx:SnowflakeParser.Alter_databaseContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#database_property.
    def enterDatabase_property(self, ctx:SnowflakeParser.Database_propertyContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#database_property.
    def exitDatabase_property(self, ctx:SnowflakeParser.Database_propertyContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#account_id_list.
    def enterAccount_id_list(self, ctx:SnowflakeParser.Account_id_listContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#account_id_list.
    def exitAccount_id_list(self, ctx:SnowflakeParser.Account_id_listContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#alter_dataset.
    def enterAlter_dataset(self, ctx:SnowflakeParser.Alter_datasetContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#alter_dataset.
    def exitAlter_dataset(self, ctx:SnowflakeParser.Alter_datasetContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#alter_dynamic_table.
    def enterAlter_dynamic_table(self, ctx:SnowflakeParser.Alter_dynamic_tableContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#alter_dynamic_table.
    def exitAlter_dynamic_table(self, ctx:SnowflakeParser.Alter_dynamic_tableContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#id_list.
    def enterId_list(self, ctx:SnowflakeParser.Id_listContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#id_list.
    def exitId_list(self, ctx:SnowflakeParser.Id_listContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#alter_external_table.
    def enterAlter_external_table(self, ctx:SnowflakeParser.Alter_external_tableContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#alter_external_table.
    def exitAlter_external_table(self, ctx:SnowflakeParser.Alter_external_tableContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#ignore_edition_check.
    def enterIgnore_edition_check(self, ctx:SnowflakeParser.Ignore_edition_checkContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#ignore_edition_check.
    def exitIgnore_edition_check(self, ctx:SnowflakeParser.Ignore_edition_checkContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#replication_schedule.
    def enterReplication_schedule(self, ctx:SnowflakeParser.Replication_scheduleContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#replication_schedule.
    def exitReplication_schedule(self, ctx:SnowflakeParser.Replication_scheduleContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#db_name_list.
    def enterDb_name_list(self, ctx:SnowflakeParser.Db_name_listContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#db_name_list.
    def exitDb_name_list(self, ctx:SnowflakeParser.Db_name_listContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#share_name_list.
    def enterShare_name_list(self, ctx:SnowflakeParser.Share_name_listContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#share_name_list.
    def exitShare_name_list(self, ctx:SnowflakeParser.Share_name_listContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#full_acct_list.
    def enterFull_acct_list(self, ctx:SnowflakeParser.Full_acct_listContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#full_acct_list.
    def exitFull_acct_list(self, ctx:SnowflakeParser.Full_acct_listContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#alter_failover_group.
    def enterAlter_failover_group(self, ctx:SnowflakeParser.Alter_failover_groupContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#alter_failover_group.
    def exitAlter_failover_group(self, ctx:SnowflakeParser.Alter_failover_groupContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#alter_file_format.
    def enterAlter_file_format(self, ctx:SnowflakeParser.Alter_file_formatContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#alter_file_format.
    def exitAlter_file_format(self, ctx:SnowflakeParser.Alter_file_formatContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#alter_function.
    def enterAlter_function(self, ctx:SnowflakeParser.Alter_functionContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#alter_function.
    def exitAlter_function(self, ctx:SnowflakeParser.Alter_functionContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#alter_function_signature.
    def enterAlter_function_signature(self, ctx:SnowflakeParser.Alter_function_signatureContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#alter_function_signature.
    def exitAlter_function_signature(self, ctx:SnowflakeParser.Alter_function_signatureContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#data_type_list.
    def enterData_type_list(self, ctx:SnowflakeParser.Data_type_listContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#data_type_list.
    def exitData_type_list(self, ctx:SnowflakeParser.Data_type_listContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#alter_git_repository.
    def enterAlter_git_repository(self, ctx:SnowflakeParser.Alter_git_repositoryContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#alter_git_repository.
    def exitAlter_git_repository(self, ctx:SnowflakeParser.Alter_git_repositoryContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#alter_git_set_opts.
    def enterAlter_git_set_opts(self, ctx:SnowflakeParser.Alter_git_set_optsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#alter_git_set_opts.
    def exitAlter_git_set_opts(self, ctx:SnowflakeParser.Alter_git_set_optsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#alter_git_unset_opts.
    def enterAlter_git_unset_opts(self, ctx:SnowflakeParser.Alter_git_unset_optsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#alter_git_unset_opts.
    def exitAlter_git_unset_opts(self, ctx:SnowflakeParser.Alter_git_unset_optsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#alter_masking_policy.
    def enterAlter_masking_policy(self, ctx:SnowflakeParser.Alter_masking_policyContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#alter_masking_policy.
    def exitAlter_masking_policy(self, ctx:SnowflakeParser.Alter_masking_policyContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#alter_materialized_view.
    def enterAlter_materialized_view(self, ctx:SnowflakeParser.Alter_materialized_viewContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#alter_materialized_view.
    def exitAlter_materialized_view(self, ctx:SnowflakeParser.Alter_materialized_viewContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#alter_network_policy.
    def enterAlter_network_policy(self, ctx:SnowflakeParser.Alter_network_policyContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#alter_network_policy.
    def exitAlter_network_policy(self, ctx:SnowflakeParser.Alter_network_policyContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#alter_notification_integration.
    def enterAlter_notification_integration(self, ctx:SnowflakeParser.Alter_notification_integrationContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#alter_notification_integration.
    def exitAlter_notification_integration(self, ctx:SnowflakeParser.Alter_notification_integrationContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#alter_pipe.
    def enterAlter_pipe(self, ctx:SnowflakeParser.Alter_pipeContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#alter_pipe.
    def exitAlter_pipe(self, ctx:SnowflakeParser.Alter_pipeContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#alter_procedure.
    def enterAlter_procedure(self, ctx:SnowflakeParser.Alter_procedureContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#alter_procedure.
    def exitAlter_procedure(self, ctx:SnowflakeParser.Alter_procedureContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#alter_replication_group.
    def enterAlter_replication_group(self, ctx:SnowflakeParser.Alter_replication_groupContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#alter_replication_group.
    def exitAlter_replication_group(self, ctx:SnowflakeParser.Alter_replication_groupContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#credit_quota.
    def enterCredit_quota(self, ctx:SnowflakeParser.Credit_quotaContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#credit_quota.
    def exitCredit_quota(self, ctx:SnowflakeParser.Credit_quotaContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#frequency.
    def enterFrequency(self, ctx:SnowflakeParser.FrequencyContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#frequency.
    def exitFrequency(self, ctx:SnowflakeParser.FrequencyContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#notify_users.
    def enterNotify_users(self, ctx:SnowflakeParser.Notify_usersContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#notify_users.
    def exitNotify_users(self, ctx:SnowflakeParser.Notify_usersContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#triggerDefinition.
    def enterTriggerDefinition(self, ctx:SnowflakeParser.TriggerDefinitionContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#triggerDefinition.
    def exitTriggerDefinition(self, ctx:SnowflakeParser.TriggerDefinitionContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#alter_resource_monitor.
    def enterAlter_resource_monitor(self, ctx:SnowflakeParser.Alter_resource_monitorContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#alter_resource_monitor.
    def exitAlter_resource_monitor(self, ctx:SnowflakeParser.Alter_resource_monitorContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#alter_role.
    def enterAlter_role(self, ctx:SnowflakeParser.Alter_roleContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#alter_role.
    def exitAlter_role(self, ctx:SnowflakeParser.Alter_roleContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#alter_row_access_policy.
    def enterAlter_row_access_policy(self, ctx:SnowflakeParser.Alter_row_access_policyContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#alter_row_access_policy.
    def exitAlter_row_access_policy(self, ctx:SnowflakeParser.Alter_row_access_policyContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#alter_schema.
    def enterAlter_schema(self, ctx:SnowflakeParser.Alter_schemaContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#alter_schema.
    def exitAlter_schema(self, ctx:SnowflakeParser.Alter_schemaContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#schema_property.
    def enterSchema_property(self, ctx:SnowflakeParser.Schema_propertyContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#schema_property.
    def exitSchema_property(self, ctx:SnowflakeParser.Schema_propertyContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#alter_sequence.
    def enterAlter_sequence(self, ctx:SnowflakeParser.Alter_sequenceContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#alter_sequence.
    def exitAlter_sequence(self, ctx:SnowflakeParser.Alter_sequenceContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#alter_secret.
    def enterAlter_secret(self, ctx:SnowflakeParser.Alter_secretContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#alter_secret.
    def exitAlter_secret(self, ctx:SnowflakeParser.Alter_secretContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#secret_opts.
    def enterSecret_opts(self, ctx:SnowflakeParser.Secret_optsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#secret_opts.
    def exitSecret_opts(self, ctx:SnowflakeParser.Secret_optsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#secret_set_opts.
    def enterSecret_set_opts(self, ctx:SnowflakeParser.Secret_set_optsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#secret_set_opts.
    def exitSecret_set_opts(self, ctx:SnowflakeParser.Secret_set_optsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#secret_oauth_client_creds_opts.
    def enterSecret_oauth_client_creds_opts(self, ctx:SnowflakeParser.Secret_oauth_client_creds_optsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#secret_oauth_client_creds_opts.
    def exitSecret_oauth_client_creds_opts(self, ctx:SnowflakeParser.Secret_oauth_client_creds_optsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#secret_oauth_auth_code_opts.
    def enterSecret_oauth_auth_code_opts(self, ctx:SnowflakeParser.Secret_oauth_auth_code_optsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#secret_oauth_auth_code_opts.
    def exitSecret_oauth_auth_code_opts(self, ctx:SnowflakeParser.Secret_oauth_auth_code_optsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#secret_api_auth_opts.
    def enterSecret_api_auth_opts(self, ctx:SnowflakeParser.Secret_api_auth_optsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#secret_api_auth_opts.
    def exitSecret_api_auth_opts(self, ctx:SnowflakeParser.Secret_api_auth_optsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#secret_basic_auth_opts.
    def enterSecret_basic_auth_opts(self, ctx:SnowflakeParser.Secret_basic_auth_optsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#secret_basic_auth_opts.
    def exitSecret_basic_auth_opts(self, ctx:SnowflakeParser.Secret_basic_auth_optsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#secret_generic_string_opts.
    def enterSecret_generic_string_opts(self, ctx:SnowflakeParser.Secret_generic_string_optsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#secret_generic_string_opts.
    def exitSecret_generic_string_opts(self, ctx:SnowflakeParser.Secret_generic_string_optsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#alter_security_integration_external_oauth.
    def enterAlter_security_integration_external_oauth(self, ctx:SnowflakeParser.Alter_security_integration_external_oauthContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#alter_security_integration_external_oauth.
    def exitAlter_security_integration_external_oauth(self, ctx:SnowflakeParser.Alter_security_integration_external_oauthContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#security_integration_external_oauth_property.
    def enterSecurity_integration_external_oauth_property(self, ctx:SnowflakeParser.Security_integration_external_oauth_propertyContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#security_integration_external_oauth_property.
    def exitSecurity_integration_external_oauth_property(self, ctx:SnowflakeParser.Security_integration_external_oauth_propertyContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#alter_security_integration_snowflake_oauth.
    def enterAlter_security_integration_snowflake_oauth(self, ctx:SnowflakeParser.Alter_security_integration_snowflake_oauthContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#alter_security_integration_snowflake_oauth.
    def exitAlter_security_integration_snowflake_oauth(self, ctx:SnowflakeParser.Alter_security_integration_snowflake_oauthContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#security_integration_snowflake_oauth_property.
    def enterSecurity_integration_snowflake_oauth_property(self, ctx:SnowflakeParser.Security_integration_snowflake_oauth_propertyContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#security_integration_snowflake_oauth_property.
    def exitSecurity_integration_snowflake_oauth_property(self, ctx:SnowflakeParser.Security_integration_snowflake_oauth_propertyContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#alter_security_integration_saml2.
    def enterAlter_security_integration_saml2(self, ctx:SnowflakeParser.Alter_security_integration_saml2Context):
        pass

    # Exit a parse tree produced by SnowflakeParser#alter_security_integration_saml2.
    def exitAlter_security_integration_saml2(self, ctx:SnowflakeParser.Alter_security_integration_saml2Context):
        pass


    # Enter a parse tree produced by SnowflakeParser#alter_security_integration_scim.
    def enterAlter_security_integration_scim(self, ctx:SnowflakeParser.Alter_security_integration_scimContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#alter_security_integration_scim.
    def exitAlter_security_integration_scim(self, ctx:SnowflakeParser.Alter_security_integration_scimContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#security_integration_scim_property.
    def enterSecurity_integration_scim_property(self, ctx:SnowflakeParser.Security_integration_scim_propertyContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#security_integration_scim_property.
    def exitSecurity_integration_scim_property(self, ctx:SnowflakeParser.Security_integration_scim_propertyContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#alter_session.
    def enterAlter_session(self, ctx:SnowflakeParser.Alter_sessionContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#alter_session.
    def exitAlter_session(self, ctx:SnowflakeParser.Alter_sessionContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#alter_session_policy.
    def enterAlter_session_policy(self, ctx:SnowflakeParser.Alter_session_policyContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#alter_session_policy.
    def exitAlter_session_policy(self, ctx:SnowflakeParser.Alter_session_policyContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#alter_password_policy.
    def enterAlter_password_policy(self, ctx:SnowflakeParser.Alter_password_policyContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#alter_password_policy.
    def exitAlter_password_policy(self, ctx:SnowflakeParser.Alter_password_policyContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#alter_share.
    def enterAlter_share(self, ctx:SnowflakeParser.Alter_shareContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#alter_share.
    def exitAlter_share(self, ctx:SnowflakeParser.Alter_shareContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#alter_storage_integration.
    def enterAlter_storage_integration(self, ctx:SnowflakeParser.Alter_storage_integrationContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#alter_storage_integration.
    def exitAlter_storage_integration(self, ctx:SnowflakeParser.Alter_storage_integrationContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#alter_stream.
    def enterAlter_stream(self, ctx:SnowflakeParser.Alter_streamContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#alter_stream.
    def exitAlter_stream(self, ctx:SnowflakeParser.Alter_streamContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#alter_table.
    def enterAlter_table(self, ctx:SnowflakeParser.Alter_tableContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#alter_table.
    def exitAlter_table(self, ctx:SnowflakeParser.Alter_tableContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#rls_operations.
    def enterRls_operations(self, ctx:SnowflakeParser.Rls_operationsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#rls_operations.
    def exitRls_operations(self, ctx:SnowflakeParser.Rls_operationsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#clustering_action.
    def enterClustering_action(self, ctx:SnowflakeParser.Clustering_actionContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#clustering_action.
    def exitClustering_action(self, ctx:SnowflakeParser.Clustering_actionContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#table_column_action.
    def enterTable_column_action(self, ctx:SnowflakeParser.Table_column_actionContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#table_column_action.
    def exitTable_column_action(self, ctx:SnowflakeParser.Table_column_actionContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#alter_column_clause.
    def enterAlter_column_clause(self, ctx:SnowflakeParser.Alter_column_clauseContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#alter_column_clause.
    def exitAlter_column_clause(self, ctx:SnowflakeParser.Alter_column_clauseContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#inline_constraint.
    def enterInline_constraint(self, ctx:SnowflakeParser.Inline_constraintContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#inline_constraint.
    def exitInline_constraint(self, ctx:SnowflakeParser.Inline_constraintContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#enforced_not_enforced.
    def enterEnforced_not_enforced(self, ctx:SnowflakeParser.Enforced_not_enforcedContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#enforced_not_enforced.
    def exitEnforced_not_enforced(self, ctx:SnowflakeParser.Enforced_not_enforcedContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#deferrable_not_deferrable.
    def enterDeferrable_not_deferrable(self, ctx:SnowflakeParser.Deferrable_not_deferrableContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#deferrable_not_deferrable.
    def exitDeferrable_not_deferrable(self, ctx:SnowflakeParser.Deferrable_not_deferrableContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#initially_deferred_or_immediate.
    def enterInitially_deferred_or_immediate(self, ctx:SnowflakeParser.Initially_deferred_or_immediateContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#initially_deferred_or_immediate.
    def exitInitially_deferred_or_immediate(self, ctx:SnowflakeParser.Initially_deferred_or_immediateContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#common_constraint_properties.
    def enterCommon_constraint_properties(self, ctx:SnowflakeParser.Common_constraint_propertiesContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#common_constraint_properties.
    def exitCommon_constraint_properties(self, ctx:SnowflakeParser.Common_constraint_propertiesContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#on_update.
    def enterOn_update(self, ctx:SnowflakeParser.On_updateContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#on_update.
    def exitOn_update(self, ctx:SnowflakeParser.On_updateContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#on_delete.
    def enterOn_delete(self, ctx:SnowflakeParser.On_deleteContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#on_delete.
    def exitOn_delete(self, ctx:SnowflakeParser.On_deleteContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#foreign_key_match.
    def enterForeign_key_match(self, ctx:SnowflakeParser.Foreign_key_matchContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#foreign_key_match.
    def exitForeign_key_match(self, ctx:SnowflakeParser.Foreign_key_matchContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#on_action.
    def enterOn_action(self, ctx:SnowflakeParser.On_actionContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#on_action.
    def exitOn_action(self, ctx:SnowflakeParser.On_actionContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#constraint_properties.
    def enterConstraint_properties(self, ctx:SnowflakeParser.Constraint_propertiesContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#constraint_properties.
    def exitConstraint_properties(self, ctx:SnowflakeParser.Constraint_propertiesContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#ext_table_column_action.
    def enterExt_table_column_action(self, ctx:SnowflakeParser.Ext_table_column_actionContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#ext_table_column_action.
    def exitExt_table_column_action(self, ctx:SnowflakeParser.Ext_table_column_actionContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#constraint_action.
    def enterConstraint_action(self, ctx:SnowflakeParser.Constraint_actionContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#constraint_action.
    def exitConstraint_action(self, ctx:SnowflakeParser.Constraint_actionContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#search_optimization_action.
    def enterSearch_optimization_action(self, ctx:SnowflakeParser.Search_optimization_actionContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#search_optimization_action.
    def exitSearch_optimization_action(self, ctx:SnowflakeParser.Search_optimization_actionContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#search_method_with_target.
    def enterSearch_method_with_target(self, ctx:SnowflakeParser.Search_method_with_targetContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#search_method_with_target.
    def exitSearch_method_with_target(self, ctx:SnowflakeParser.Search_method_with_targetContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#alter_table_alter_column.
    def enterAlter_table_alter_column(self, ctx:SnowflakeParser.Alter_table_alter_columnContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#alter_table_alter_column.
    def exitAlter_table_alter_column(self, ctx:SnowflakeParser.Alter_table_alter_columnContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#alter_column_decl_list.
    def enterAlter_column_decl_list(self, ctx:SnowflakeParser.Alter_column_decl_listContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#alter_column_decl_list.
    def exitAlter_column_decl_list(self, ctx:SnowflakeParser.Alter_column_decl_listContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#alter_column_decl.
    def enterAlter_column_decl(self, ctx:SnowflakeParser.Alter_column_declContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#alter_column_decl.
    def exitAlter_column_decl(self, ctx:SnowflakeParser.Alter_column_declContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#alter_column_opts.
    def enterAlter_column_opts(self, ctx:SnowflakeParser.Alter_column_optsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#alter_column_opts.
    def exitAlter_column_opts(self, ctx:SnowflakeParser.Alter_column_optsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#column_set_tags.
    def enterColumn_set_tags(self, ctx:SnowflakeParser.Column_set_tagsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#column_set_tags.
    def exitColumn_set_tags(self, ctx:SnowflakeParser.Column_set_tagsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#column_unset_tags.
    def enterColumn_unset_tags(self, ctx:SnowflakeParser.Column_unset_tagsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#column_unset_tags.
    def exitColumn_unset_tags(self, ctx:SnowflakeParser.Column_unset_tagsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#alter_tag.
    def enterAlter_tag(self, ctx:SnowflakeParser.Alter_tagContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#alter_tag.
    def exitAlter_tag(self, ctx:SnowflakeParser.Alter_tagContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#alter_task.
    def enterAlter_task(self, ctx:SnowflakeParser.Alter_taskContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#alter_task.
    def exitAlter_task(self, ctx:SnowflakeParser.Alter_taskContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#alter_user.
    def enterAlter_user(self, ctx:SnowflakeParser.Alter_userContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#alter_user.
    def exitAlter_user(self, ctx:SnowflakeParser.Alter_userContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#alter_view.
    def enterAlter_view(self, ctx:SnowflakeParser.Alter_viewContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#alter_view.
    def exitAlter_view(self, ctx:SnowflakeParser.Alter_viewContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#alter_modify.
    def enterAlter_modify(self, ctx:SnowflakeParser.Alter_modifyContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#alter_modify.
    def exitAlter_modify(self, ctx:SnowflakeParser.Alter_modifyContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#alter_warehouse.
    def enterAlter_warehouse(self, ctx:SnowflakeParser.Alter_warehouseContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#alter_warehouse.
    def exitAlter_warehouse(self, ctx:SnowflakeParser.Alter_warehouseContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#alter_connection_opts.
    def enterAlter_connection_opts(self, ctx:SnowflakeParser.Alter_connection_optsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#alter_connection_opts.
    def exitAlter_connection_opts(self, ctx:SnowflakeParser.Alter_connection_optsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#alter_user_opts.
    def enterAlter_user_opts(self, ctx:SnowflakeParser.Alter_user_optsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#alter_user_opts.
    def exitAlter_user_opts(self, ctx:SnowflakeParser.Alter_user_optsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#alter_tag_opts.
    def enterAlter_tag_opts(self, ctx:SnowflakeParser.Alter_tag_optsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#alter_tag_opts.
    def exitAlter_tag_opts(self, ctx:SnowflakeParser.Alter_tag_optsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#alter_network_policy_opts.
    def enterAlter_network_policy_opts(self, ctx:SnowflakeParser.Alter_network_policy_optsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#alter_network_policy_opts.
    def exitAlter_network_policy_opts(self, ctx:SnowflakeParser.Alter_network_policy_optsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#alter_warehouse_opts.
    def enterAlter_warehouse_opts(self, ctx:SnowflakeParser.Alter_warehouse_optsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#alter_warehouse_opts.
    def exitAlter_warehouse_opts(self, ctx:SnowflakeParser.Alter_warehouse_optsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#alter_account_opts.
    def enterAlter_account_opts(self, ctx:SnowflakeParser.Alter_account_optsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#alter_account_opts.
    def exitAlter_account_opts(self, ctx:SnowflakeParser.Alter_account_optsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#set_tags.
    def enterSet_tags(self, ctx:SnowflakeParser.Set_tagsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#set_tags.
    def exitSet_tags(self, ctx:SnowflakeParser.Set_tagsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#tag_decl_list.
    def enterTag_decl_list(self, ctx:SnowflakeParser.Tag_decl_listContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#tag_decl_list.
    def exitTag_decl_list(self, ctx:SnowflakeParser.Tag_decl_listContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#unset_tags.
    def enterUnset_tags(self, ctx:SnowflakeParser.Unset_tagsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#unset_tags.
    def exitUnset_tags(self, ctx:SnowflakeParser.Unset_tagsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#tag_list.
    def enterTag_list(self, ctx:SnowflakeParser.Tag_listContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#tag_list.
    def exitTag_list(self, ctx:SnowflakeParser.Tag_listContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#create_command.
    def enterCreate_command(self, ctx:SnowflakeParser.Create_commandContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#create_command.
    def exitCreate_command(self, ctx:SnowflakeParser.Create_commandContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#create_account.
    def enterCreate_account(self, ctx:SnowflakeParser.Create_accountContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#create_account.
    def exitCreate_account(self, ctx:SnowflakeParser.Create_accountContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#create_alert.
    def enterCreate_alert(self, ctx:SnowflakeParser.Create_alertContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#create_alert.
    def exitCreate_alert(self, ctx:SnowflakeParser.Create_alertContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#alert_condition.
    def enterAlert_condition(self, ctx:SnowflakeParser.Alert_conditionContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#alert_condition.
    def exitAlert_condition(self, ctx:SnowflakeParser.Alert_conditionContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#alert_action.
    def enterAlert_action(self, ctx:SnowflakeParser.Alert_actionContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#alert_action.
    def exitAlert_action(self, ctx:SnowflakeParser.Alert_actionContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#create_api_integration.
    def enterCreate_api_integration(self, ctx:SnowflakeParser.Create_api_integrationContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#create_api_integration.
    def exitCreate_api_integration(self, ctx:SnowflakeParser.Create_api_integrationContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#create_object_clone.
    def enterCreate_object_clone(self, ctx:SnowflakeParser.Create_object_cloneContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#create_object_clone.
    def exitCreate_object_clone(self, ctx:SnowflakeParser.Create_object_cloneContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#create_connection.
    def enterCreate_connection(self, ctx:SnowflakeParser.Create_connectionContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#create_connection.
    def exitCreate_connection(self, ctx:SnowflakeParser.Create_connectionContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#create_database.
    def enterCreate_database(self, ctx:SnowflakeParser.Create_databaseContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#create_database.
    def exitCreate_database(self, ctx:SnowflakeParser.Create_databaseContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#clone_at_before.
    def enterClone_at_before(self, ctx:SnowflakeParser.Clone_at_beforeContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#clone_at_before.
    def exitClone_at_before(self, ctx:SnowflakeParser.Clone_at_beforeContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#at_before1.
    def enterAt_before1(self, ctx:SnowflakeParser.At_before1Context):
        pass

    # Exit a parse tree produced by SnowflakeParser#at_before1.
    def exitAt_before1(self, ctx:SnowflakeParser.At_before1Context):
        pass


    # Enter a parse tree produced by SnowflakeParser#header_decl.
    def enterHeader_decl(self, ctx:SnowflakeParser.Header_declContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#header_decl.
    def exitHeader_decl(self, ctx:SnowflakeParser.Header_declContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#compression_type.
    def enterCompression_type(self, ctx:SnowflakeParser.Compression_typeContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#compression_type.
    def exitCompression_type(self, ctx:SnowflakeParser.Compression_typeContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#compression.
    def enterCompression(self, ctx:SnowflakeParser.CompressionContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#compression.
    def exitCompression(self, ctx:SnowflakeParser.CompressionContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#create_dataset.
    def enterCreate_dataset(self, ctx:SnowflakeParser.Create_datasetContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#create_dataset.
    def exitCreate_dataset(self, ctx:SnowflakeParser.Create_datasetContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#create_dynamic_table.
    def enterCreate_dynamic_table(self, ctx:SnowflakeParser.Create_dynamic_tableContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#create_dynamic_table.
    def exitCreate_dynamic_table(self, ctx:SnowflakeParser.Create_dynamic_tableContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#dynamic_table_params.
    def enterDynamic_table_params(self, ctx:SnowflakeParser.Dynamic_table_paramsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#dynamic_table_params.
    def exitDynamic_table_params(self, ctx:SnowflakeParser.Dynamic_table_paramsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#dynamic_table_settable_params.
    def enterDynamic_table_settable_params(self, ctx:SnowflakeParser.Dynamic_table_settable_paramsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#dynamic_table_settable_params.
    def exitDynamic_table_settable_params(self, ctx:SnowflakeParser.Dynamic_table_settable_paramsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#dynamic_table_unsettable_params.
    def enterDynamic_table_unsettable_params(self, ctx:SnowflakeParser.Dynamic_table_unsettable_paramsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#dynamic_table_unsettable_params.
    def exitDynamic_table_unsettable_params(self, ctx:SnowflakeParser.Dynamic_table_unsettable_paramsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#data_retention_params.
    def enterData_retention_params(self, ctx:SnowflakeParser.Data_retention_paramsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#data_retention_params.
    def exitData_retention_params(self, ctx:SnowflakeParser.Data_retention_paramsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#set_data_retention_params.
    def enterSet_data_retention_params(self, ctx:SnowflakeParser.Set_data_retention_paramsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#set_data_retention_params.
    def exitSet_data_retention_params(self, ctx:SnowflakeParser.Set_data_retention_paramsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#create_event_table.
    def enterCreate_event_table(self, ctx:SnowflakeParser.Create_event_tableContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#create_event_table.
    def exitCreate_event_table(self, ctx:SnowflakeParser.Create_event_tableContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#create_external_function.
    def enterCreate_external_function(self, ctx:SnowflakeParser.Create_external_functionContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#create_external_function.
    def exitCreate_external_function(self, ctx:SnowflakeParser.Create_external_functionContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#create_external_table.
    def enterCreate_external_table(self, ctx:SnowflakeParser.Create_external_tableContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#create_external_table.
    def exitCreate_external_table(self, ctx:SnowflakeParser.Create_external_tableContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#external_table_column_decl.
    def enterExternal_table_column_decl(self, ctx:SnowflakeParser.External_table_column_declContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#external_table_column_decl.
    def exitExternal_table_column_decl(self, ctx:SnowflakeParser.External_table_column_declContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#external_table_column_decl_list.
    def enterExternal_table_column_decl_list(self, ctx:SnowflakeParser.External_table_column_decl_listContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#external_table_column_decl_list.
    def exitExternal_table_column_decl_list(self, ctx:SnowflakeParser.External_table_column_decl_listContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#full_acct.
    def enterFull_acct(self, ctx:SnowflakeParser.Full_acctContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#full_acct.
    def exitFull_acct(self, ctx:SnowflakeParser.Full_acctContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#integration_type_name.
    def enterIntegration_type_name(self, ctx:SnowflakeParser.Integration_type_nameContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#integration_type_name.
    def exitIntegration_type_name(self, ctx:SnowflakeParser.Integration_type_nameContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#create_failover_group.
    def enterCreate_failover_group(self, ctx:SnowflakeParser.Create_failover_groupContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#create_failover_group.
    def exitCreate_failover_group(self, ctx:SnowflakeParser.Create_failover_groupContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#type_fileformat.
    def enterType_fileformat(self, ctx:SnowflakeParser.Type_fileformatContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#type_fileformat.
    def exitType_fileformat(self, ctx:SnowflakeParser.Type_fileformatContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#create_file_format.
    def enterCreate_file_format(self, ctx:SnowflakeParser.Create_file_formatContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#create_file_format.
    def exitCreate_file_format(self, ctx:SnowflakeParser.Create_file_formatContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#arg_decl.
    def enterArg_decl(self, ctx:SnowflakeParser.Arg_declContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#arg_decl.
    def exitArg_decl(self, ctx:SnowflakeParser.Arg_declContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#arg_default_value_clause.
    def enterArg_default_value_clause(self, ctx:SnowflakeParser.Arg_default_value_clauseContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#arg_default_value_clause.
    def exitArg_default_value_clause(self, ctx:SnowflakeParser.Arg_default_value_clauseContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#col_decl.
    def enterCol_decl(self, ctx:SnowflakeParser.Col_declContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#col_decl.
    def exitCol_decl(self, ctx:SnowflakeParser.Col_declContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#virtual_column_decl.
    def enterVirtual_column_decl(self, ctx:SnowflakeParser.Virtual_column_declContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#virtual_column_decl.
    def exitVirtual_column_decl(self, ctx:SnowflakeParser.Virtual_column_declContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#function_definition.
    def enterFunction_definition(self, ctx:SnowflakeParser.Function_definitionContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#function_definition.
    def exitFunction_definition(self, ctx:SnowflakeParser.Function_definitionContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#create_function.
    def enterCreate_function(self, ctx:SnowflakeParser.Create_functionContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#create_function.
    def exitCreate_function(self, ctx:SnowflakeParser.Create_functionContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#create_git_repository.
    def enterCreate_git_repository(self, ctx:SnowflakeParser.Create_git_repositoryContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#create_git_repository.
    def exitCreate_git_repository(self, ctx:SnowflakeParser.Create_git_repositoryContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#create_git_opts.
    def enterCreate_git_opts(self, ctx:SnowflakeParser.Create_git_optsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#create_git_opts.
    def exitCreate_git_opts(self, ctx:SnowflakeParser.Create_git_optsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#create_managed_account.
    def enterCreate_managed_account(self, ctx:SnowflakeParser.Create_managed_accountContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#create_managed_account.
    def exitCreate_managed_account(self, ctx:SnowflakeParser.Create_managed_accountContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#create_masking_policy.
    def enterCreate_masking_policy(self, ctx:SnowflakeParser.Create_masking_policyContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#create_masking_policy.
    def exitCreate_masking_policy(self, ctx:SnowflakeParser.Create_masking_policyContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#tag_decl.
    def enterTag_decl(self, ctx:SnowflakeParser.Tag_declContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#tag_decl.
    def exitTag_decl(self, ctx:SnowflakeParser.Tag_declContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#column_list_in_parentheses.
    def enterColumn_list_in_parentheses(self, ctx:SnowflakeParser.Column_list_in_parenthesesContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#column_list_in_parentheses.
    def exitColumn_list_in_parentheses(self, ctx:SnowflakeParser.Column_list_in_parenthesesContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#create_materialized_view.
    def enterCreate_materialized_view(self, ctx:SnowflakeParser.Create_materialized_viewContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#create_materialized_view.
    def exitCreate_materialized_view(self, ctx:SnowflakeParser.Create_materialized_viewContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#create_network_policy.
    def enterCreate_network_policy(self, ctx:SnowflakeParser.Create_network_policyContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#create_network_policy.
    def exitCreate_network_policy(self, ctx:SnowflakeParser.Create_network_policyContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#cloud_provider_params_auto.
    def enterCloud_provider_params_auto(self, ctx:SnowflakeParser.Cloud_provider_params_autoContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#cloud_provider_params_auto.
    def exitCloud_provider_params_auto(self, ctx:SnowflakeParser.Cloud_provider_params_autoContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#cloud_provider_params_push.
    def enterCloud_provider_params_push(self, ctx:SnowflakeParser.Cloud_provider_params_pushContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#cloud_provider_params_push.
    def exitCloud_provider_params_push(self, ctx:SnowflakeParser.Cloud_provider_params_pushContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#create_notification_integration.
    def enterCreate_notification_integration(self, ctx:SnowflakeParser.Create_notification_integrationContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#create_notification_integration.
    def exitCreate_notification_integration(self, ctx:SnowflakeParser.Create_notification_integrationContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#create_pipe.
    def enterCreate_pipe(self, ctx:SnowflakeParser.Create_pipeContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#create_pipe.
    def exitCreate_pipe(self, ctx:SnowflakeParser.Create_pipeContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#caller_owner.
    def enterCaller_owner(self, ctx:SnowflakeParser.Caller_ownerContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#caller_owner.
    def exitCaller_owner(self, ctx:SnowflakeParser.Caller_ownerContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#executa_as.
    def enterExecuta_as(self, ctx:SnowflakeParser.Executa_asContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#executa_as.
    def exitExecuta_as(self, ctx:SnowflakeParser.Executa_asContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#procedure_definition.
    def enterProcedure_definition(self, ctx:SnowflakeParser.Procedure_definitionContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#procedure_definition.
    def exitProcedure_definition(self, ctx:SnowflakeParser.Procedure_definitionContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#not_null.
    def enterNot_null(self, ctx:SnowflakeParser.Not_nullContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#not_null.
    def exitNot_null(self, ctx:SnowflakeParser.Not_nullContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#create_procedure.
    def enterCreate_procedure(self, ctx:SnowflakeParser.Create_procedureContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#create_procedure.
    def exitCreate_procedure(self, ctx:SnowflakeParser.Create_procedureContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#create_replication_group.
    def enterCreate_replication_group(self, ctx:SnowflakeParser.Create_replication_groupContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#create_replication_group.
    def exitCreate_replication_group(self, ctx:SnowflakeParser.Create_replication_groupContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#create_resource_monitor.
    def enterCreate_resource_monitor(self, ctx:SnowflakeParser.Create_resource_monitorContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#create_resource_monitor.
    def exitCreate_resource_monitor(self, ctx:SnowflakeParser.Create_resource_monitorContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#create_role.
    def enterCreate_role(self, ctx:SnowflakeParser.Create_roleContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#create_role.
    def exitCreate_role(self, ctx:SnowflakeParser.Create_roleContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#create_row_access_policy.
    def enterCreate_row_access_policy(self, ctx:SnowflakeParser.Create_row_access_policyContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#create_row_access_policy.
    def exitCreate_row_access_policy(self, ctx:SnowflakeParser.Create_row_access_policyContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#create_schema.
    def enterCreate_schema(self, ctx:SnowflakeParser.Create_schemaContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#create_schema.
    def exitCreate_schema(self, ctx:SnowflakeParser.Create_schemaContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#create_secret.
    def enterCreate_secret(self, ctx:SnowflakeParser.Create_secretContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#create_secret.
    def exitCreate_secret(self, ctx:SnowflakeParser.Create_secretContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#create_security_integration_external_oauth.
    def enterCreate_security_integration_external_oauth(self, ctx:SnowflakeParser.Create_security_integration_external_oauthContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#create_security_integration_external_oauth.
    def exitCreate_security_integration_external_oauth(self, ctx:SnowflakeParser.Create_security_integration_external_oauthContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#implicit_none.
    def enterImplicit_none(self, ctx:SnowflakeParser.Implicit_noneContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#implicit_none.
    def exitImplicit_none(self, ctx:SnowflakeParser.Implicit_noneContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#create_security_integration_snowflake_oauth.
    def enterCreate_security_integration_snowflake_oauth(self, ctx:SnowflakeParser.Create_security_integration_snowflake_oauthContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#create_security_integration_snowflake_oauth.
    def exitCreate_security_integration_snowflake_oauth(self, ctx:SnowflakeParser.Create_security_integration_snowflake_oauthContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#create_security_integration_saml2.
    def enterCreate_security_integration_saml2(self, ctx:SnowflakeParser.Create_security_integration_saml2Context):
        pass

    # Exit a parse tree produced by SnowflakeParser#create_security_integration_saml2.
    def exitCreate_security_integration_saml2(self, ctx:SnowflakeParser.Create_security_integration_saml2Context):
        pass


    # Enter a parse tree produced by SnowflakeParser#create_security_integration_scim.
    def enterCreate_security_integration_scim(self, ctx:SnowflakeParser.Create_security_integration_scimContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#create_security_integration_scim.
    def exitCreate_security_integration_scim(self, ctx:SnowflakeParser.Create_security_integration_scimContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#network_policy.
    def enterNetwork_policy(self, ctx:SnowflakeParser.Network_policyContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#network_policy.
    def exitNetwork_policy(self, ctx:SnowflakeParser.Network_policyContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#partner_application.
    def enterPartner_application(self, ctx:SnowflakeParser.Partner_applicationContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#partner_application.
    def exitPartner_application(self, ctx:SnowflakeParser.Partner_applicationContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#start_with.
    def enterStart_with(self, ctx:SnowflakeParser.Start_withContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#start_with.
    def exitStart_with(self, ctx:SnowflakeParser.Start_withContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#increment_by.
    def enterIncrement_by(self, ctx:SnowflakeParser.Increment_byContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#increment_by.
    def exitIncrement_by(self, ctx:SnowflakeParser.Increment_byContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#create_sequence.
    def enterCreate_sequence(self, ctx:SnowflakeParser.Create_sequenceContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#create_sequence.
    def exitCreate_sequence(self, ctx:SnowflakeParser.Create_sequenceContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#create_session_policy.
    def enterCreate_session_policy(self, ctx:SnowflakeParser.Create_session_policyContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#create_session_policy.
    def exitCreate_session_policy(self, ctx:SnowflakeParser.Create_session_policyContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#session_policy_params.
    def enterSession_policy_params(self, ctx:SnowflakeParser.Session_policy_paramsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#session_policy_params.
    def exitSession_policy_params(self, ctx:SnowflakeParser.Session_policy_paramsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#session_policy_param_name.
    def enterSession_policy_param_name(self, ctx:SnowflakeParser.Session_policy_param_nameContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#session_policy_param_name.
    def exitSession_policy_param_name(self, ctx:SnowflakeParser.Session_policy_param_nameContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#create_password_policy.
    def enterCreate_password_policy(self, ctx:SnowflakeParser.Create_password_policyContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#create_password_policy.
    def exitCreate_password_policy(self, ctx:SnowflakeParser.Create_password_policyContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#password_policy_params.
    def enterPassword_policy_params(self, ctx:SnowflakeParser.Password_policy_paramsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#password_policy_params.
    def exitPassword_policy_params(self, ctx:SnowflakeParser.Password_policy_paramsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#password_policy_param_name.
    def enterPassword_policy_param_name(self, ctx:SnowflakeParser.Password_policy_param_nameContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#password_policy_param_name.
    def exitPassword_policy_param_name(self, ctx:SnowflakeParser.Password_policy_param_nameContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#create_share.
    def enterCreate_share(self, ctx:SnowflakeParser.Create_shareContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#create_share.
    def exitCreate_share(self, ctx:SnowflakeParser.Create_shareContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#character.
    def enterCharacter(self, ctx:SnowflakeParser.CharacterContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#character.
    def exitCharacter(self, ctx:SnowflakeParser.CharacterContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#format_type_options.
    def enterFormat_type_options(self, ctx:SnowflakeParser.Format_type_optionsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#format_type_options.
    def exitFormat_type_options(self, ctx:SnowflakeParser.Format_type_optionsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#copy_options.
    def enterCopy_options(self, ctx:SnowflakeParser.Copy_optionsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#copy_options.
    def exitCopy_options(self, ctx:SnowflakeParser.Copy_optionsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#stage_encryption_opts_internal.
    def enterStage_encryption_opts_internal(self, ctx:SnowflakeParser.Stage_encryption_opts_internalContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#stage_encryption_opts_internal.
    def exitStage_encryption_opts_internal(self, ctx:SnowflakeParser.Stage_encryption_opts_internalContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#stage_type.
    def enterStage_type(self, ctx:SnowflakeParser.Stage_typeContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#stage_type.
    def exitStage_type(self, ctx:SnowflakeParser.Stage_typeContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#stage_master_key.
    def enterStage_master_key(self, ctx:SnowflakeParser.Stage_master_keyContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#stage_master_key.
    def exitStage_master_key(self, ctx:SnowflakeParser.Stage_master_keyContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#stage_kms_key.
    def enterStage_kms_key(self, ctx:SnowflakeParser.Stage_kms_keyContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#stage_kms_key.
    def exitStage_kms_key(self, ctx:SnowflakeParser.Stage_kms_keyContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#stage_encryption_opts_aws.
    def enterStage_encryption_opts_aws(self, ctx:SnowflakeParser.Stage_encryption_opts_awsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#stage_encryption_opts_aws.
    def exitStage_encryption_opts_aws(self, ctx:SnowflakeParser.Stage_encryption_opts_awsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#aws_token.
    def enterAws_token(self, ctx:SnowflakeParser.Aws_tokenContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#aws_token.
    def exitAws_token(self, ctx:SnowflakeParser.Aws_tokenContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#aws_key_id.
    def enterAws_key_id(self, ctx:SnowflakeParser.Aws_key_idContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#aws_key_id.
    def exitAws_key_id(self, ctx:SnowflakeParser.Aws_key_idContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#aws_secret_key.
    def enterAws_secret_key(self, ctx:SnowflakeParser.Aws_secret_keyContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#aws_secret_key.
    def exitAws_secret_key(self, ctx:SnowflakeParser.Aws_secret_keyContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#aws_role.
    def enterAws_role(self, ctx:SnowflakeParser.Aws_roleContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#aws_role.
    def exitAws_role(self, ctx:SnowflakeParser.Aws_roleContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#azure_encryption_value.
    def enterAzure_encryption_value(self, ctx:SnowflakeParser.Azure_encryption_valueContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#azure_encryption_value.
    def exitAzure_encryption_value(self, ctx:SnowflakeParser.Azure_encryption_valueContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#stage_encryption_opts_az.
    def enterStage_encryption_opts_az(self, ctx:SnowflakeParser.Stage_encryption_opts_azContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#stage_encryption_opts_az.
    def exitStage_encryption_opts_az(self, ctx:SnowflakeParser.Stage_encryption_opts_azContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#storage_integration_eq_id.
    def enterStorage_integration_eq_id(self, ctx:SnowflakeParser.Storage_integration_eq_idContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#storage_integration_eq_id.
    def exitStorage_integration_eq_id(self, ctx:SnowflakeParser.Storage_integration_eq_idContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#az_credential_or_storage_integration.
    def enterAz_credential_or_storage_integration(self, ctx:SnowflakeParser.Az_credential_or_storage_integrationContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#az_credential_or_storage_integration.
    def exitAz_credential_or_storage_integration(self, ctx:SnowflakeParser.Az_credential_or_storage_integrationContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#gcp_encryption_value.
    def enterGcp_encryption_value(self, ctx:SnowflakeParser.Gcp_encryption_valueContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#gcp_encryption_value.
    def exitGcp_encryption_value(self, ctx:SnowflakeParser.Gcp_encryption_valueContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#stage_encryption_opts_gcp.
    def enterStage_encryption_opts_gcp(self, ctx:SnowflakeParser.Stage_encryption_opts_gcpContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#stage_encryption_opts_gcp.
    def exitStage_encryption_opts_gcp(self, ctx:SnowflakeParser.Stage_encryption_opts_gcpContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#aws_credential_or_storage_integration.
    def enterAws_credential_or_storage_integration(self, ctx:SnowflakeParser.Aws_credential_or_storage_integrationContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#aws_credential_or_storage_integration.
    def exitAws_credential_or_storage_integration(self, ctx:SnowflakeParser.Aws_credential_or_storage_integrationContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#external_stage_params.
    def enterExternal_stage_params(self, ctx:SnowflakeParser.External_stage_paramsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#external_stage_params.
    def exitExternal_stage_params(self, ctx:SnowflakeParser.External_stage_paramsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#true_false.
    def enterTrue_false(self, ctx:SnowflakeParser.True_falseContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#true_false.
    def exitTrue_false(self, ctx:SnowflakeParser.True_falseContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#enable.
    def enterEnable(self, ctx:SnowflakeParser.EnableContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#enable.
    def exitEnable(self, ctx:SnowflakeParser.EnableContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#refresh_on_create.
    def enterRefresh_on_create(self, ctx:SnowflakeParser.Refresh_on_createContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#refresh_on_create.
    def exitRefresh_on_create(self, ctx:SnowflakeParser.Refresh_on_createContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#auto_refresh.
    def enterAuto_refresh(self, ctx:SnowflakeParser.Auto_refreshContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#auto_refresh.
    def exitAuto_refresh(self, ctx:SnowflakeParser.Auto_refreshContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#notification_integration.
    def enterNotification_integration(self, ctx:SnowflakeParser.Notification_integrationContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#notification_integration.
    def exitNotification_integration(self, ctx:SnowflakeParser.Notification_integrationContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#directory_table_internal_params.
    def enterDirectory_table_internal_params(self, ctx:SnowflakeParser.Directory_table_internal_paramsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#directory_table_internal_params.
    def exitDirectory_table_internal_params(self, ctx:SnowflakeParser.Directory_table_internal_paramsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#directory_table_external_params.
    def enterDirectory_table_external_params(self, ctx:SnowflakeParser.Directory_table_external_paramsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#directory_table_external_params.
    def exitDirectory_table_external_params(self, ctx:SnowflakeParser.Directory_table_external_paramsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#create_stage.
    def enterCreate_stage(self, ctx:SnowflakeParser.Create_stageContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#create_stage.
    def exitCreate_stage(self, ctx:SnowflakeParser.Create_stageContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#alter_stage.
    def enterAlter_stage(self, ctx:SnowflakeParser.Alter_stageContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#alter_stage.
    def exitAlter_stage(self, ctx:SnowflakeParser.Alter_stageContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#drop_stage.
    def enterDrop_stage(self, ctx:SnowflakeParser.Drop_stageContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#drop_stage.
    def exitDrop_stage(self, ctx:SnowflakeParser.Drop_stageContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#describe_stage.
    def enterDescribe_stage(self, ctx:SnowflakeParser.Describe_stageContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#describe_stage.
    def exitDescribe_stage(self, ctx:SnowflakeParser.Describe_stageContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#show_stages.
    def enterShow_stages(self, ctx:SnowflakeParser.Show_stagesContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#show_stages.
    def exitShow_stages(self, ctx:SnowflakeParser.Show_stagesContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#cloud_provider_params.
    def enterCloud_provider_params(self, ctx:SnowflakeParser.Cloud_provider_paramsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#cloud_provider_params.
    def exitCloud_provider_params(self, ctx:SnowflakeParser.Cloud_provider_paramsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#cloud_provider_params2.
    def enterCloud_provider_params2(self, ctx:SnowflakeParser.Cloud_provider_params2Context):
        pass

    # Exit a parse tree produced by SnowflakeParser#cloud_provider_params2.
    def exitCloud_provider_params2(self, ctx:SnowflakeParser.Cloud_provider_params2Context):
        pass


    # Enter a parse tree produced by SnowflakeParser#cloud_provider_params3.
    def enterCloud_provider_params3(self, ctx:SnowflakeParser.Cloud_provider_params3Context):
        pass

    # Exit a parse tree produced by SnowflakeParser#cloud_provider_params3.
    def exitCloud_provider_params3(self, ctx:SnowflakeParser.Cloud_provider_params3Context):
        pass


    # Enter a parse tree produced by SnowflakeParser#create_storage_integration.
    def enterCreate_storage_integration(self, ctx:SnowflakeParser.Create_storage_integrationContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#create_storage_integration.
    def exitCreate_storage_integration(self, ctx:SnowflakeParser.Create_storage_integrationContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#copy_grants.
    def enterCopy_grants(self, ctx:SnowflakeParser.Copy_grantsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#copy_grants.
    def exitCopy_grants(self, ctx:SnowflakeParser.Copy_grantsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#append_only.
    def enterAppend_only(self, ctx:SnowflakeParser.Append_onlyContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#append_only.
    def exitAppend_only(self, ctx:SnowflakeParser.Append_onlyContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#insert_only.
    def enterInsert_only(self, ctx:SnowflakeParser.Insert_onlyContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#insert_only.
    def exitInsert_only(self, ctx:SnowflakeParser.Insert_onlyContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#show_initial_rows.
    def enterShow_initial_rows(self, ctx:SnowflakeParser.Show_initial_rowsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#show_initial_rows.
    def exitShow_initial_rows(self, ctx:SnowflakeParser.Show_initial_rowsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#stream_time.
    def enterStream_time(self, ctx:SnowflakeParser.Stream_timeContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#stream_time.
    def exitStream_time(self, ctx:SnowflakeParser.Stream_timeContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#create_stream.
    def enterCreate_stream(self, ctx:SnowflakeParser.Create_streamContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#create_stream.
    def exitCreate_stream(self, ctx:SnowflakeParser.Create_streamContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#temporary.
    def enterTemporary(self, ctx:SnowflakeParser.TemporaryContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#temporary.
    def exitTemporary(self, ctx:SnowflakeParser.TemporaryContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#table_type.
    def enterTable_type(self, ctx:SnowflakeParser.Table_typeContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#table_type.
    def exitTable_type(self, ctx:SnowflakeParser.Table_typeContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#with_tags.
    def enterWith_tags(self, ctx:SnowflakeParser.With_tagsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#with_tags.
    def exitWith_tags(self, ctx:SnowflakeParser.With_tagsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#with_row_access_policy.
    def enterWith_row_access_policy(self, ctx:SnowflakeParser.With_row_access_policyContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#with_row_access_policy.
    def exitWith_row_access_policy(self, ctx:SnowflakeParser.With_row_access_policyContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#cluster_by.
    def enterCluster_by(self, ctx:SnowflakeParser.Cluster_byContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#cluster_by.
    def exitCluster_by(self, ctx:SnowflakeParser.Cluster_byContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#change_tracking.
    def enterChange_tracking(self, ctx:SnowflakeParser.Change_trackingContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#change_tracking.
    def exitChange_tracking(self, ctx:SnowflakeParser.Change_trackingContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#with_masking_policy.
    def enterWith_masking_policy(self, ctx:SnowflakeParser.With_masking_policyContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#with_masking_policy.
    def exitWith_masking_policy(self, ctx:SnowflakeParser.With_masking_policyContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#collate.
    def enterCollate(self, ctx:SnowflakeParser.CollateContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#collate.
    def exitCollate(self, ctx:SnowflakeParser.CollateContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#order_noorder.
    def enterOrder_noorder(self, ctx:SnowflakeParser.Order_noorderContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#order_noorder.
    def exitOrder_noorder(self, ctx:SnowflakeParser.Order_noorderContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#default_value.
    def enterDefault_value(self, ctx:SnowflakeParser.Default_valueContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#default_value.
    def exitDefault_value(self, ctx:SnowflakeParser.Default_valueContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#foreign_key.
    def enterForeign_key(self, ctx:SnowflakeParser.Foreign_keyContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#foreign_key.
    def exitForeign_key(self, ctx:SnowflakeParser.Foreign_keyContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#primary_key.
    def enterPrimary_key(self, ctx:SnowflakeParser.Primary_keyContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#primary_key.
    def exitPrimary_key(self, ctx:SnowflakeParser.Primary_keyContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#out_of_line_constraint.
    def enterOut_of_line_constraint(self, ctx:SnowflakeParser.Out_of_line_constraintContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#out_of_line_constraint.
    def exitOut_of_line_constraint(self, ctx:SnowflakeParser.Out_of_line_constraintContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#full_col_decl.
    def enterFull_col_decl(self, ctx:SnowflakeParser.Full_col_declContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#full_col_decl.
    def exitFull_col_decl(self, ctx:SnowflakeParser.Full_col_declContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#materialized_col_decl.
    def enterMaterialized_col_decl(self, ctx:SnowflakeParser.Materialized_col_declContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#materialized_col_decl.
    def exitMaterialized_col_decl(self, ctx:SnowflakeParser.Materialized_col_declContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#materialized_col_decl_list.
    def enterMaterialized_col_decl_list(self, ctx:SnowflakeParser.Materialized_col_decl_listContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#materialized_col_decl_list.
    def exitMaterialized_col_decl_list(self, ctx:SnowflakeParser.Materialized_col_decl_listContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#column_decl_item.
    def enterColumn_decl_item(self, ctx:SnowflakeParser.Column_decl_itemContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#column_decl_item.
    def exitColumn_decl_item(self, ctx:SnowflakeParser.Column_decl_itemContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#column_decl_item_list.
    def enterColumn_decl_item_list(self, ctx:SnowflakeParser.Column_decl_item_listContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#column_decl_item_list.
    def exitColumn_decl_item_list(self, ctx:SnowflakeParser.Column_decl_item_listContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#create_table.
    def enterCreate_table(self, ctx:SnowflakeParser.Create_tableContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#create_table.
    def exitCreate_table(self, ctx:SnowflakeParser.Create_tableContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#column_decl_item_list_paren.
    def enterColumn_decl_item_list_paren(self, ctx:SnowflakeParser.Column_decl_item_list_parenContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#column_decl_item_list_paren.
    def exitColumn_decl_item_list_paren(self, ctx:SnowflakeParser.Column_decl_item_list_parenContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#create_table_clause.
    def enterCreate_table_clause(self, ctx:SnowflakeParser.Create_table_clauseContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#create_table_clause.
    def exitCreate_table_clause(self, ctx:SnowflakeParser.Create_table_clauseContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#create_table_as_select.
    def enterCreate_table_as_select(self, ctx:SnowflakeParser.Create_table_as_selectContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#create_table_as_select.
    def exitCreate_table_as_select(self, ctx:SnowflakeParser.Create_table_as_selectContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#create_table_like.
    def enterCreate_table_like(self, ctx:SnowflakeParser.Create_table_likeContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#create_table_like.
    def exitCreate_table_like(self, ctx:SnowflakeParser.Create_table_likeContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#create_tag.
    def enterCreate_tag(self, ctx:SnowflakeParser.Create_tagContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#create_tag.
    def exitCreate_tag(self, ctx:SnowflakeParser.Create_tagContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#tag_allowed_values.
    def enterTag_allowed_values(self, ctx:SnowflakeParser.Tag_allowed_valuesContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#tag_allowed_values.
    def exitTag_allowed_values(self, ctx:SnowflakeParser.Tag_allowed_valuesContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#session_parameter.
    def enterSession_parameter(self, ctx:SnowflakeParser.Session_parameterContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#session_parameter.
    def exitSession_parameter(self, ctx:SnowflakeParser.Session_parameterContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#session_parameter_list.
    def enterSession_parameter_list(self, ctx:SnowflakeParser.Session_parameter_listContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#session_parameter_list.
    def exitSession_parameter_list(self, ctx:SnowflakeParser.Session_parameter_listContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#session_params_list.
    def enterSession_params_list(self, ctx:SnowflakeParser.Session_params_listContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#session_params_list.
    def exitSession_params_list(self, ctx:SnowflakeParser.Session_params_listContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#create_task.
    def enterCreate_task(self, ctx:SnowflakeParser.Create_taskContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#create_task.
    def exitCreate_task(self, ctx:SnowflakeParser.Create_taskContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#task_parameters.
    def enterTask_parameters(self, ctx:SnowflakeParser.Task_parametersContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#task_parameters.
    def exitTask_parameters(self, ctx:SnowflakeParser.Task_parametersContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#task_compute.
    def enterTask_compute(self, ctx:SnowflakeParser.Task_computeContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#task_compute.
    def exitTask_compute(self, ctx:SnowflakeParser.Task_computeContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#task_schedule.
    def enterTask_schedule(self, ctx:SnowflakeParser.Task_scheduleContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#task_schedule.
    def exitTask_schedule(self, ctx:SnowflakeParser.Task_scheduleContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#task_timeout.
    def enterTask_timeout(self, ctx:SnowflakeParser.Task_timeoutContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#task_timeout.
    def exitTask_timeout(self, ctx:SnowflakeParser.Task_timeoutContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#task_suspend_after_failure_number.
    def enterTask_suspend_after_failure_number(self, ctx:SnowflakeParser.Task_suspend_after_failure_numberContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#task_suspend_after_failure_number.
    def exitTask_suspend_after_failure_number(self, ctx:SnowflakeParser.Task_suspend_after_failure_numberContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#task_error_integration.
    def enterTask_error_integration(self, ctx:SnowflakeParser.Task_error_integrationContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#task_error_integration.
    def exitTask_error_integration(self, ctx:SnowflakeParser.Task_error_integrationContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#task_overlap.
    def enterTask_overlap(self, ctx:SnowflakeParser.Task_overlapContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#task_overlap.
    def exitTask_overlap(self, ctx:SnowflakeParser.Task_overlapContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#sql.
    def enterSql(self, ctx:SnowflakeParser.SqlContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#sql.
    def exitSql(self, ctx:SnowflakeParser.SqlContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#call.
    def enterCall(self, ctx:SnowflakeParser.CallContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#call.
    def exitCall(self, ctx:SnowflakeParser.CallContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#create_user.
    def enterCreate_user(self, ctx:SnowflakeParser.Create_userContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#create_user.
    def exitCreate_user(self, ctx:SnowflakeParser.Create_userContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#view_col.
    def enterView_col(self, ctx:SnowflakeParser.View_colContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#view_col.
    def exitView_col(self, ctx:SnowflakeParser.View_colContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#create_view.
    def enterCreate_view(self, ctx:SnowflakeParser.Create_viewContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#create_view.
    def exitCreate_view(self, ctx:SnowflakeParser.Create_viewContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#create_warehouse.
    def enterCreate_warehouse(self, ctx:SnowflakeParser.Create_warehouseContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#create_warehouse.
    def exitCreate_warehouse(self, ctx:SnowflakeParser.Create_warehouseContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#wh_common_size.
    def enterWh_common_size(self, ctx:SnowflakeParser.Wh_common_sizeContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#wh_common_size.
    def exitWh_common_size(self, ctx:SnowflakeParser.Wh_common_sizeContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#wh_extra_size.
    def enterWh_extra_size(self, ctx:SnowflakeParser.Wh_extra_sizeContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#wh_extra_size.
    def exitWh_extra_size(self, ctx:SnowflakeParser.Wh_extra_sizeContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#wh_properties.
    def enterWh_properties(self, ctx:SnowflakeParser.Wh_propertiesContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#wh_properties.
    def exitWh_properties(self, ctx:SnowflakeParser.Wh_propertiesContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#wh_params.
    def enterWh_params(self, ctx:SnowflakeParser.Wh_paramsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#wh_params.
    def exitWh_params(self, ctx:SnowflakeParser.Wh_paramsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#trigger_definition.
    def enterTrigger_definition(self, ctx:SnowflakeParser.Trigger_definitionContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#trigger_definition.
    def exitTrigger_definition(self, ctx:SnowflakeParser.Trigger_definitionContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#object_type_name.
    def enterObject_type_name(self, ctx:SnowflakeParser.Object_type_nameContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#object_type_name.
    def exitObject_type_name(self, ctx:SnowflakeParser.Object_type_nameContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#object_type_plural.
    def enterObject_type_plural(self, ctx:SnowflakeParser.Object_type_pluralContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#object_type_plural.
    def exitObject_type_plural(self, ctx:SnowflakeParser.Object_type_pluralContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#drop_command.
    def enterDrop_command(self, ctx:SnowflakeParser.Drop_commandContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#drop_command.
    def exitDrop_command(self, ctx:SnowflakeParser.Drop_commandContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#drop_object.
    def enterDrop_object(self, ctx:SnowflakeParser.Drop_objectContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#drop_object.
    def exitDrop_object(self, ctx:SnowflakeParser.Drop_objectContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#drop_alert.
    def enterDrop_alert(self, ctx:SnowflakeParser.Drop_alertContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#drop_alert.
    def exitDrop_alert(self, ctx:SnowflakeParser.Drop_alertContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#drop_connection.
    def enterDrop_connection(self, ctx:SnowflakeParser.Drop_connectionContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#drop_connection.
    def exitDrop_connection(self, ctx:SnowflakeParser.Drop_connectionContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#drop_database.
    def enterDrop_database(self, ctx:SnowflakeParser.Drop_databaseContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#drop_database.
    def exitDrop_database(self, ctx:SnowflakeParser.Drop_databaseContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#drop_dynamic_table.
    def enterDrop_dynamic_table(self, ctx:SnowflakeParser.Drop_dynamic_tableContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#drop_dynamic_table.
    def exitDrop_dynamic_table(self, ctx:SnowflakeParser.Drop_dynamic_tableContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#drop_external_table.
    def enterDrop_external_table(self, ctx:SnowflakeParser.Drop_external_tableContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#drop_external_table.
    def exitDrop_external_table(self, ctx:SnowflakeParser.Drop_external_tableContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#drop_failover_group.
    def enterDrop_failover_group(self, ctx:SnowflakeParser.Drop_failover_groupContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#drop_failover_group.
    def exitDrop_failover_group(self, ctx:SnowflakeParser.Drop_failover_groupContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#drop_file_format.
    def enterDrop_file_format(self, ctx:SnowflakeParser.Drop_file_formatContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#drop_file_format.
    def exitDrop_file_format(self, ctx:SnowflakeParser.Drop_file_formatContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#drop_function.
    def enterDrop_function(self, ctx:SnowflakeParser.Drop_functionContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#drop_function.
    def exitDrop_function(self, ctx:SnowflakeParser.Drop_functionContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#drop_git_repository.
    def enterDrop_git_repository(self, ctx:SnowflakeParser.Drop_git_repositoryContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#drop_git_repository.
    def exitDrop_git_repository(self, ctx:SnowflakeParser.Drop_git_repositoryContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#drop_integration.
    def enterDrop_integration(self, ctx:SnowflakeParser.Drop_integrationContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#drop_integration.
    def exitDrop_integration(self, ctx:SnowflakeParser.Drop_integrationContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#drop_managed_account.
    def enterDrop_managed_account(self, ctx:SnowflakeParser.Drop_managed_accountContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#drop_managed_account.
    def exitDrop_managed_account(self, ctx:SnowflakeParser.Drop_managed_accountContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#drop_masking_policy.
    def enterDrop_masking_policy(self, ctx:SnowflakeParser.Drop_masking_policyContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#drop_masking_policy.
    def exitDrop_masking_policy(self, ctx:SnowflakeParser.Drop_masking_policyContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#drop_materialized_view.
    def enterDrop_materialized_view(self, ctx:SnowflakeParser.Drop_materialized_viewContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#drop_materialized_view.
    def exitDrop_materialized_view(self, ctx:SnowflakeParser.Drop_materialized_viewContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#drop_network_policy.
    def enterDrop_network_policy(self, ctx:SnowflakeParser.Drop_network_policyContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#drop_network_policy.
    def exitDrop_network_policy(self, ctx:SnowflakeParser.Drop_network_policyContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#drop_pipe.
    def enterDrop_pipe(self, ctx:SnowflakeParser.Drop_pipeContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#drop_pipe.
    def exitDrop_pipe(self, ctx:SnowflakeParser.Drop_pipeContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#drop_procedure.
    def enterDrop_procedure(self, ctx:SnowflakeParser.Drop_procedureContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#drop_procedure.
    def exitDrop_procedure(self, ctx:SnowflakeParser.Drop_procedureContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#drop_replication_group.
    def enterDrop_replication_group(self, ctx:SnowflakeParser.Drop_replication_groupContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#drop_replication_group.
    def exitDrop_replication_group(self, ctx:SnowflakeParser.Drop_replication_groupContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#drop_resource_monitor.
    def enterDrop_resource_monitor(self, ctx:SnowflakeParser.Drop_resource_monitorContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#drop_resource_monitor.
    def exitDrop_resource_monitor(self, ctx:SnowflakeParser.Drop_resource_monitorContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#drop_role.
    def enterDrop_role(self, ctx:SnowflakeParser.Drop_roleContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#drop_role.
    def exitDrop_role(self, ctx:SnowflakeParser.Drop_roleContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#drop_row_access_policy.
    def enterDrop_row_access_policy(self, ctx:SnowflakeParser.Drop_row_access_policyContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#drop_row_access_policy.
    def exitDrop_row_access_policy(self, ctx:SnowflakeParser.Drop_row_access_policyContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#drop_schema.
    def enterDrop_schema(self, ctx:SnowflakeParser.Drop_schemaContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#drop_schema.
    def exitDrop_schema(self, ctx:SnowflakeParser.Drop_schemaContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#drop_secret.
    def enterDrop_secret(self, ctx:SnowflakeParser.Drop_secretContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#drop_secret.
    def exitDrop_secret(self, ctx:SnowflakeParser.Drop_secretContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#drop_sequence.
    def enterDrop_sequence(self, ctx:SnowflakeParser.Drop_sequenceContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#drop_sequence.
    def exitDrop_sequence(self, ctx:SnowflakeParser.Drop_sequenceContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#drop_session_policy.
    def enterDrop_session_policy(self, ctx:SnowflakeParser.Drop_session_policyContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#drop_session_policy.
    def exitDrop_session_policy(self, ctx:SnowflakeParser.Drop_session_policyContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#drop_password_policy.
    def enterDrop_password_policy(self, ctx:SnowflakeParser.Drop_password_policyContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#drop_password_policy.
    def exitDrop_password_policy(self, ctx:SnowflakeParser.Drop_password_policyContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#drop_share.
    def enterDrop_share(self, ctx:SnowflakeParser.Drop_shareContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#drop_share.
    def exitDrop_share(self, ctx:SnowflakeParser.Drop_shareContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#drop_stream.
    def enterDrop_stream(self, ctx:SnowflakeParser.Drop_streamContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#drop_stream.
    def exitDrop_stream(self, ctx:SnowflakeParser.Drop_streamContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#drop_table.
    def enterDrop_table(self, ctx:SnowflakeParser.Drop_tableContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#drop_table.
    def exitDrop_table(self, ctx:SnowflakeParser.Drop_tableContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#drop_tag.
    def enterDrop_tag(self, ctx:SnowflakeParser.Drop_tagContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#drop_tag.
    def exitDrop_tag(self, ctx:SnowflakeParser.Drop_tagContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#drop_task.
    def enterDrop_task(self, ctx:SnowflakeParser.Drop_taskContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#drop_task.
    def exitDrop_task(self, ctx:SnowflakeParser.Drop_taskContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#drop_user.
    def enterDrop_user(self, ctx:SnowflakeParser.Drop_userContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#drop_user.
    def exitDrop_user(self, ctx:SnowflakeParser.Drop_userContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#drop_view.
    def enterDrop_view(self, ctx:SnowflakeParser.Drop_viewContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#drop_view.
    def exitDrop_view(self, ctx:SnowflakeParser.Drop_viewContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#drop_warehouse.
    def enterDrop_warehouse(self, ctx:SnowflakeParser.Drop_warehouseContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#drop_warehouse.
    def exitDrop_warehouse(self, ctx:SnowflakeParser.Drop_warehouseContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#cascade_restrict.
    def enterCascade_restrict(self, ctx:SnowflakeParser.Cascade_restrictContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#cascade_restrict.
    def exitCascade_restrict(self, ctx:SnowflakeParser.Cascade_restrictContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#arg_types.
    def enterArg_types(self, ctx:SnowflakeParser.Arg_typesContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#arg_types.
    def exitArg_types(self, ctx:SnowflakeParser.Arg_typesContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#undrop_command.
    def enterUndrop_command(self, ctx:SnowflakeParser.Undrop_commandContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#undrop_command.
    def exitUndrop_command(self, ctx:SnowflakeParser.Undrop_commandContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#undrop_database.
    def enterUndrop_database(self, ctx:SnowflakeParser.Undrop_databaseContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#undrop_database.
    def exitUndrop_database(self, ctx:SnowflakeParser.Undrop_databaseContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#undrop_schema.
    def enterUndrop_schema(self, ctx:SnowflakeParser.Undrop_schemaContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#undrop_schema.
    def exitUndrop_schema(self, ctx:SnowflakeParser.Undrop_schemaContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#undrop_table.
    def enterUndrop_table(self, ctx:SnowflakeParser.Undrop_tableContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#undrop_table.
    def exitUndrop_table(self, ctx:SnowflakeParser.Undrop_tableContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#undrop_tag.
    def enterUndrop_tag(self, ctx:SnowflakeParser.Undrop_tagContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#undrop_tag.
    def exitUndrop_tag(self, ctx:SnowflakeParser.Undrop_tagContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#use_command.
    def enterUse_command(self, ctx:SnowflakeParser.Use_commandContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#use_command.
    def exitUse_command(self, ctx:SnowflakeParser.Use_commandContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#use_database.
    def enterUse_database(self, ctx:SnowflakeParser.Use_databaseContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#use_database.
    def exitUse_database(self, ctx:SnowflakeParser.Use_databaseContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#use_role.
    def enterUse_role(self, ctx:SnowflakeParser.Use_roleContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#use_role.
    def exitUse_role(self, ctx:SnowflakeParser.Use_roleContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#use_schema.
    def enterUse_schema(self, ctx:SnowflakeParser.Use_schemaContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#use_schema.
    def exitUse_schema(self, ctx:SnowflakeParser.Use_schemaContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#use_secondary_roles.
    def enterUse_secondary_roles(self, ctx:SnowflakeParser.Use_secondary_rolesContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#use_secondary_roles.
    def exitUse_secondary_roles(self, ctx:SnowflakeParser.Use_secondary_rolesContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#use_warehouse.
    def enterUse_warehouse(self, ctx:SnowflakeParser.Use_warehouseContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#use_warehouse.
    def exitUse_warehouse(self, ctx:SnowflakeParser.Use_warehouseContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#comment_clause.
    def enterComment_clause(self, ctx:SnowflakeParser.Comment_clauseContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#comment_clause.
    def exitComment_clause(self, ctx:SnowflakeParser.Comment_clauseContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#inline_comment_clause.
    def enterInline_comment_clause(self, ctx:SnowflakeParser.Inline_comment_clauseContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#inline_comment_clause.
    def exitInline_comment_clause(self, ctx:SnowflakeParser.Inline_comment_clauseContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#if_suspended.
    def enterIf_suspended(self, ctx:SnowflakeParser.If_suspendedContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#if_suspended.
    def exitIf_suspended(self, ctx:SnowflakeParser.If_suspendedContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#if_exists.
    def enterIf_exists(self, ctx:SnowflakeParser.If_existsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#if_exists.
    def exitIf_exists(self, ctx:SnowflakeParser.If_existsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#if_not_exists.
    def enterIf_not_exists(self, ctx:SnowflakeParser.If_not_existsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#if_not_exists.
    def exitIf_not_exists(self, ctx:SnowflakeParser.If_not_existsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#or_replace.
    def enterOr_replace(self, ctx:SnowflakeParser.Or_replaceContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#or_replace.
    def exitOr_replace(self, ctx:SnowflakeParser.Or_replaceContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#or_alter.
    def enterOr_alter(self, ctx:SnowflakeParser.Or_alterContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#or_alter.
    def exitOr_alter(self, ctx:SnowflakeParser.Or_alterContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#describe.
    def enterDescribe(self, ctx:SnowflakeParser.DescribeContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#describe.
    def exitDescribe(self, ctx:SnowflakeParser.DescribeContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#describe_command.
    def enterDescribe_command(self, ctx:SnowflakeParser.Describe_commandContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#describe_command.
    def exitDescribe_command(self, ctx:SnowflakeParser.Describe_commandContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#describe_alert.
    def enterDescribe_alert(self, ctx:SnowflakeParser.Describe_alertContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#describe_alert.
    def exitDescribe_alert(self, ctx:SnowflakeParser.Describe_alertContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#describe_database.
    def enterDescribe_database(self, ctx:SnowflakeParser.Describe_databaseContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#describe_database.
    def exitDescribe_database(self, ctx:SnowflakeParser.Describe_databaseContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#describe_dynamic_table.
    def enterDescribe_dynamic_table(self, ctx:SnowflakeParser.Describe_dynamic_tableContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#describe_dynamic_table.
    def exitDescribe_dynamic_table(self, ctx:SnowflakeParser.Describe_dynamic_tableContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#describe_event_table.
    def enterDescribe_event_table(self, ctx:SnowflakeParser.Describe_event_tableContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#describe_event_table.
    def exitDescribe_event_table(self, ctx:SnowflakeParser.Describe_event_tableContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#describe_external_table.
    def enterDescribe_external_table(self, ctx:SnowflakeParser.Describe_external_tableContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#describe_external_table.
    def exitDescribe_external_table(self, ctx:SnowflakeParser.Describe_external_tableContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#describe_file_format.
    def enterDescribe_file_format(self, ctx:SnowflakeParser.Describe_file_formatContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#describe_file_format.
    def exitDescribe_file_format(self, ctx:SnowflakeParser.Describe_file_formatContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#describe_function.
    def enterDescribe_function(self, ctx:SnowflakeParser.Describe_functionContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#describe_function.
    def exitDescribe_function(self, ctx:SnowflakeParser.Describe_functionContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#describe_git_repository.
    def enterDescribe_git_repository(self, ctx:SnowflakeParser.Describe_git_repositoryContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#describe_git_repository.
    def exitDescribe_git_repository(self, ctx:SnowflakeParser.Describe_git_repositoryContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#describe_integration.
    def enterDescribe_integration(self, ctx:SnowflakeParser.Describe_integrationContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#describe_integration.
    def exitDescribe_integration(self, ctx:SnowflakeParser.Describe_integrationContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#describe_masking_policy.
    def enterDescribe_masking_policy(self, ctx:SnowflakeParser.Describe_masking_policyContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#describe_masking_policy.
    def exitDescribe_masking_policy(self, ctx:SnowflakeParser.Describe_masking_policyContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#describe_materialized_view.
    def enterDescribe_materialized_view(self, ctx:SnowflakeParser.Describe_materialized_viewContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#describe_materialized_view.
    def exitDescribe_materialized_view(self, ctx:SnowflakeParser.Describe_materialized_viewContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#describe_network_policy.
    def enterDescribe_network_policy(self, ctx:SnowflakeParser.Describe_network_policyContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#describe_network_policy.
    def exitDescribe_network_policy(self, ctx:SnowflakeParser.Describe_network_policyContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#describe_pipe.
    def enterDescribe_pipe(self, ctx:SnowflakeParser.Describe_pipeContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#describe_pipe.
    def exitDescribe_pipe(self, ctx:SnowflakeParser.Describe_pipeContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#describe_procedure.
    def enterDescribe_procedure(self, ctx:SnowflakeParser.Describe_procedureContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#describe_procedure.
    def exitDescribe_procedure(self, ctx:SnowflakeParser.Describe_procedureContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#describe_result.
    def enterDescribe_result(self, ctx:SnowflakeParser.Describe_resultContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#describe_result.
    def exitDescribe_result(self, ctx:SnowflakeParser.Describe_resultContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#describe_row_access_policy.
    def enterDescribe_row_access_policy(self, ctx:SnowflakeParser.Describe_row_access_policyContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#describe_row_access_policy.
    def exitDescribe_row_access_policy(self, ctx:SnowflakeParser.Describe_row_access_policyContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#describe_schema.
    def enterDescribe_schema(self, ctx:SnowflakeParser.Describe_schemaContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#describe_schema.
    def exitDescribe_schema(self, ctx:SnowflakeParser.Describe_schemaContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#describe_search_optimization.
    def enterDescribe_search_optimization(self, ctx:SnowflakeParser.Describe_search_optimizationContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#describe_search_optimization.
    def exitDescribe_search_optimization(self, ctx:SnowflakeParser.Describe_search_optimizationContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#describe_sequence.
    def enterDescribe_sequence(self, ctx:SnowflakeParser.Describe_sequenceContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#describe_sequence.
    def exitDescribe_sequence(self, ctx:SnowflakeParser.Describe_sequenceContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#describe_session_policy.
    def enterDescribe_session_policy(self, ctx:SnowflakeParser.Describe_session_policyContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#describe_session_policy.
    def exitDescribe_session_policy(self, ctx:SnowflakeParser.Describe_session_policyContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#describe_password_policy.
    def enterDescribe_password_policy(self, ctx:SnowflakeParser.Describe_password_policyContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#describe_password_policy.
    def exitDescribe_password_policy(self, ctx:SnowflakeParser.Describe_password_policyContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#describe_share.
    def enterDescribe_share(self, ctx:SnowflakeParser.Describe_shareContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#describe_share.
    def exitDescribe_share(self, ctx:SnowflakeParser.Describe_shareContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#describe_stream.
    def enterDescribe_stream(self, ctx:SnowflakeParser.Describe_streamContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#describe_stream.
    def exitDescribe_stream(self, ctx:SnowflakeParser.Describe_streamContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#describe_table.
    def enterDescribe_table(self, ctx:SnowflakeParser.Describe_tableContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#describe_table.
    def exitDescribe_table(self, ctx:SnowflakeParser.Describe_tableContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#describe_task.
    def enterDescribe_task(self, ctx:SnowflakeParser.Describe_taskContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#describe_task.
    def exitDescribe_task(self, ctx:SnowflakeParser.Describe_taskContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#describe_transaction.
    def enterDescribe_transaction(self, ctx:SnowflakeParser.Describe_transactionContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#describe_transaction.
    def exitDescribe_transaction(self, ctx:SnowflakeParser.Describe_transactionContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#describe_user.
    def enterDescribe_user(self, ctx:SnowflakeParser.Describe_userContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#describe_user.
    def exitDescribe_user(self, ctx:SnowflakeParser.Describe_userContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#describe_view.
    def enterDescribe_view(self, ctx:SnowflakeParser.Describe_viewContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#describe_view.
    def exitDescribe_view(self, ctx:SnowflakeParser.Describe_viewContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#describe_warehouse.
    def enterDescribe_warehouse(self, ctx:SnowflakeParser.Describe_warehouseContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#describe_warehouse.
    def exitDescribe_warehouse(self, ctx:SnowflakeParser.Describe_warehouseContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#show_command.
    def enterShow_command(self, ctx:SnowflakeParser.Show_commandContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#show_command.
    def exitShow_command(self, ctx:SnowflakeParser.Show_commandContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#show_alerts.
    def enterShow_alerts(self, ctx:SnowflakeParser.Show_alertsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#show_alerts.
    def exitShow_alerts(self, ctx:SnowflakeParser.Show_alertsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#show_channels.
    def enterShow_channels(self, ctx:SnowflakeParser.Show_channelsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#show_channels.
    def exitShow_channels(self, ctx:SnowflakeParser.Show_channelsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#show_columns.
    def enterShow_columns(self, ctx:SnowflakeParser.Show_columnsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#show_columns.
    def exitShow_columns(self, ctx:SnowflakeParser.Show_columnsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#show_connections.
    def enterShow_connections(self, ctx:SnowflakeParser.Show_connectionsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#show_connections.
    def exitShow_connections(self, ctx:SnowflakeParser.Show_connectionsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#starts_with.
    def enterStarts_with(self, ctx:SnowflakeParser.Starts_withContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#starts_with.
    def exitStarts_with(self, ctx:SnowflakeParser.Starts_withContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#limit_rows.
    def enterLimit_rows(self, ctx:SnowflakeParser.Limit_rowsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#limit_rows.
    def exitLimit_rows(self, ctx:SnowflakeParser.Limit_rowsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#show_databases.
    def enterShow_databases(self, ctx:SnowflakeParser.Show_databasesContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#show_databases.
    def exitShow_databases(self, ctx:SnowflakeParser.Show_databasesContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#show_databases_in_failover_group.
    def enterShow_databases_in_failover_group(self, ctx:SnowflakeParser.Show_databases_in_failover_groupContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#show_databases_in_failover_group.
    def exitShow_databases_in_failover_group(self, ctx:SnowflakeParser.Show_databases_in_failover_groupContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#show_databases_in_replication_group.
    def enterShow_databases_in_replication_group(self, ctx:SnowflakeParser.Show_databases_in_replication_groupContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#show_databases_in_replication_group.
    def exitShow_databases_in_replication_group(self, ctx:SnowflakeParser.Show_databases_in_replication_groupContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#show_datasets.
    def enterShow_datasets(self, ctx:SnowflakeParser.Show_datasetsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#show_datasets.
    def exitShow_datasets(self, ctx:SnowflakeParser.Show_datasetsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#show_delegated_authorizations.
    def enterShow_delegated_authorizations(self, ctx:SnowflakeParser.Show_delegated_authorizationsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#show_delegated_authorizations.
    def exitShow_delegated_authorizations(self, ctx:SnowflakeParser.Show_delegated_authorizationsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#show_dynamic_tables.
    def enterShow_dynamic_tables(self, ctx:SnowflakeParser.Show_dynamic_tablesContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#show_dynamic_tables.
    def exitShow_dynamic_tables(self, ctx:SnowflakeParser.Show_dynamic_tablesContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#show_event_tables.
    def enterShow_event_tables(self, ctx:SnowflakeParser.Show_event_tablesContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#show_event_tables.
    def exitShow_event_tables(self, ctx:SnowflakeParser.Show_event_tablesContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#show_external_functions.
    def enterShow_external_functions(self, ctx:SnowflakeParser.Show_external_functionsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#show_external_functions.
    def exitShow_external_functions(self, ctx:SnowflakeParser.Show_external_functionsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#show_external_tables.
    def enterShow_external_tables(self, ctx:SnowflakeParser.Show_external_tablesContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#show_external_tables.
    def exitShow_external_tables(self, ctx:SnowflakeParser.Show_external_tablesContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#show_failover_groups.
    def enterShow_failover_groups(self, ctx:SnowflakeParser.Show_failover_groupsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#show_failover_groups.
    def exitShow_failover_groups(self, ctx:SnowflakeParser.Show_failover_groupsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#show_file_formats.
    def enterShow_file_formats(self, ctx:SnowflakeParser.Show_file_formatsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#show_file_formats.
    def exitShow_file_formats(self, ctx:SnowflakeParser.Show_file_formatsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#show_functions.
    def enterShow_functions(self, ctx:SnowflakeParser.Show_functionsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#show_functions.
    def exitShow_functions(self, ctx:SnowflakeParser.Show_functionsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#show_git_branches.
    def enterShow_git_branches(self, ctx:SnowflakeParser.Show_git_branchesContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#show_git_branches.
    def exitShow_git_branches(self, ctx:SnowflakeParser.Show_git_branchesContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#show_git_repositories.
    def enterShow_git_repositories(self, ctx:SnowflakeParser.Show_git_repositoriesContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#show_git_repositories.
    def exitShow_git_repositories(self, ctx:SnowflakeParser.Show_git_repositoriesContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#show_git_tags.
    def enterShow_git_tags(self, ctx:SnowflakeParser.Show_git_tagsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#show_git_tags.
    def exitShow_git_tags(self, ctx:SnowflakeParser.Show_git_tagsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#show_global_accounts.
    def enterShow_global_accounts(self, ctx:SnowflakeParser.Show_global_accountsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#show_global_accounts.
    def exitShow_global_accounts(self, ctx:SnowflakeParser.Show_global_accountsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#show_grants.
    def enterShow_grants(self, ctx:SnowflakeParser.Show_grantsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#show_grants.
    def exitShow_grants(self, ctx:SnowflakeParser.Show_grantsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#show_grants_opts.
    def enterShow_grants_opts(self, ctx:SnowflakeParser.Show_grants_optsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#show_grants_opts.
    def exitShow_grants_opts(self, ctx:SnowflakeParser.Show_grants_optsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#show_integrations.
    def enterShow_integrations(self, ctx:SnowflakeParser.Show_integrationsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#show_integrations.
    def exitShow_integrations(self, ctx:SnowflakeParser.Show_integrationsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#show_locks.
    def enterShow_locks(self, ctx:SnowflakeParser.Show_locksContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#show_locks.
    def exitShow_locks(self, ctx:SnowflakeParser.Show_locksContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#show_managed_accounts.
    def enterShow_managed_accounts(self, ctx:SnowflakeParser.Show_managed_accountsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#show_managed_accounts.
    def exitShow_managed_accounts(self, ctx:SnowflakeParser.Show_managed_accountsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#show_masking_policies.
    def enterShow_masking_policies(self, ctx:SnowflakeParser.Show_masking_policiesContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#show_masking_policies.
    def exitShow_masking_policies(self, ctx:SnowflakeParser.Show_masking_policiesContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#in_obj.
    def enterIn_obj(self, ctx:SnowflakeParser.In_objContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#in_obj.
    def exitIn_obj(self, ctx:SnowflakeParser.In_objContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#in_obj_2.
    def enterIn_obj_2(self, ctx:SnowflakeParser.In_obj_2Context):
        pass

    # Exit a parse tree produced by SnowflakeParser#in_obj_2.
    def exitIn_obj_2(self, ctx:SnowflakeParser.In_obj_2Context):
        pass


    # Enter a parse tree produced by SnowflakeParser#show_materialized_views.
    def enterShow_materialized_views(self, ctx:SnowflakeParser.Show_materialized_viewsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#show_materialized_views.
    def exitShow_materialized_views(self, ctx:SnowflakeParser.Show_materialized_viewsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#show_network_policies.
    def enterShow_network_policies(self, ctx:SnowflakeParser.Show_network_policiesContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#show_network_policies.
    def exitShow_network_policies(self, ctx:SnowflakeParser.Show_network_policiesContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#show_objects.
    def enterShow_objects(self, ctx:SnowflakeParser.Show_objectsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#show_objects.
    def exitShow_objects(self, ctx:SnowflakeParser.Show_objectsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#show_organization_accounts.
    def enterShow_organization_accounts(self, ctx:SnowflakeParser.Show_organization_accountsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#show_organization_accounts.
    def exitShow_organization_accounts(self, ctx:SnowflakeParser.Show_organization_accountsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#in_for.
    def enterIn_for(self, ctx:SnowflakeParser.In_forContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#in_for.
    def exitIn_for(self, ctx:SnowflakeParser.In_forContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#show_parameters.
    def enterShow_parameters(self, ctx:SnowflakeParser.Show_parametersContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#show_parameters.
    def exitShow_parameters(self, ctx:SnowflakeParser.Show_parametersContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#show_pipes.
    def enterShow_pipes(self, ctx:SnowflakeParser.Show_pipesContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#show_pipes.
    def exitShow_pipes(self, ctx:SnowflakeParser.Show_pipesContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#show_primary_keys.
    def enterShow_primary_keys(self, ctx:SnowflakeParser.Show_primary_keysContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#show_primary_keys.
    def exitShow_primary_keys(self, ctx:SnowflakeParser.Show_primary_keysContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#show_procedures.
    def enterShow_procedures(self, ctx:SnowflakeParser.Show_proceduresContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#show_procedures.
    def exitShow_procedures(self, ctx:SnowflakeParser.Show_proceduresContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#show_regions.
    def enterShow_regions(self, ctx:SnowflakeParser.Show_regionsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#show_regions.
    def exitShow_regions(self, ctx:SnowflakeParser.Show_regionsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#show_replication_accounts.
    def enterShow_replication_accounts(self, ctx:SnowflakeParser.Show_replication_accountsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#show_replication_accounts.
    def exitShow_replication_accounts(self, ctx:SnowflakeParser.Show_replication_accountsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#show_replication_databases.
    def enterShow_replication_databases(self, ctx:SnowflakeParser.Show_replication_databasesContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#show_replication_databases.
    def exitShow_replication_databases(self, ctx:SnowflakeParser.Show_replication_databasesContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#show_replication_groups.
    def enterShow_replication_groups(self, ctx:SnowflakeParser.Show_replication_groupsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#show_replication_groups.
    def exitShow_replication_groups(self, ctx:SnowflakeParser.Show_replication_groupsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#show_resource_monitors.
    def enterShow_resource_monitors(self, ctx:SnowflakeParser.Show_resource_monitorsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#show_resource_monitors.
    def exitShow_resource_monitors(self, ctx:SnowflakeParser.Show_resource_monitorsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#show_roles.
    def enterShow_roles(self, ctx:SnowflakeParser.Show_rolesContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#show_roles.
    def exitShow_roles(self, ctx:SnowflakeParser.Show_rolesContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#show_row_access_policies.
    def enterShow_row_access_policies(self, ctx:SnowflakeParser.Show_row_access_policiesContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#show_row_access_policies.
    def exitShow_row_access_policies(self, ctx:SnowflakeParser.Show_row_access_policiesContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#show_schemas.
    def enterShow_schemas(self, ctx:SnowflakeParser.Show_schemasContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#show_schemas.
    def exitShow_schemas(self, ctx:SnowflakeParser.Show_schemasContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#show_secrets.
    def enterShow_secrets(self, ctx:SnowflakeParser.Show_secretsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#show_secrets.
    def exitShow_secrets(self, ctx:SnowflakeParser.Show_secretsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#show_sequences.
    def enterShow_sequences(self, ctx:SnowflakeParser.Show_sequencesContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#show_sequences.
    def exitShow_sequences(self, ctx:SnowflakeParser.Show_sequencesContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#show_session_policies.
    def enterShow_session_policies(self, ctx:SnowflakeParser.Show_session_policiesContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#show_session_policies.
    def exitShow_session_policies(self, ctx:SnowflakeParser.Show_session_policiesContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#show_password_policies.
    def enterShow_password_policies(self, ctx:SnowflakeParser.Show_password_policiesContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#show_password_policies.
    def exitShow_password_policies(self, ctx:SnowflakeParser.Show_password_policiesContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#show_shares.
    def enterShow_shares(self, ctx:SnowflakeParser.Show_sharesContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#show_shares.
    def exitShow_shares(self, ctx:SnowflakeParser.Show_sharesContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#show_shares_in_failover_group.
    def enterShow_shares_in_failover_group(self, ctx:SnowflakeParser.Show_shares_in_failover_groupContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#show_shares_in_failover_group.
    def exitShow_shares_in_failover_group(self, ctx:SnowflakeParser.Show_shares_in_failover_groupContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#show_shares_in_replication_group.
    def enterShow_shares_in_replication_group(self, ctx:SnowflakeParser.Show_shares_in_replication_groupContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#show_shares_in_replication_group.
    def exitShow_shares_in_replication_group(self, ctx:SnowflakeParser.Show_shares_in_replication_groupContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#show_streams.
    def enterShow_streams(self, ctx:SnowflakeParser.Show_streamsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#show_streams.
    def exitShow_streams(self, ctx:SnowflakeParser.Show_streamsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#show_tables.
    def enterShow_tables(self, ctx:SnowflakeParser.Show_tablesContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#show_tables.
    def exitShow_tables(self, ctx:SnowflakeParser.Show_tablesContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#show_tags.
    def enterShow_tags(self, ctx:SnowflakeParser.Show_tagsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#show_tags.
    def exitShow_tags(self, ctx:SnowflakeParser.Show_tagsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#show_tasks.
    def enterShow_tasks(self, ctx:SnowflakeParser.Show_tasksContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#show_tasks.
    def exitShow_tasks(self, ctx:SnowflakeParser.Show_tasksContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#show_transactions.
    def enterShow_transactions(self, ctx:SnowflakeParser.Show_transactionsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#show_transactions.
    def exitShow_transactions(self, ctx:SnowflakeParser.Show_transactionsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#show_user_functions.
    def enterShow_user_functions(self, ctx:SnowflakeParser.Show_user_functionsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#show_user_functions.
    def exitShow_user_functions(self, ctx:SnowflakeParser.Show_user_functionsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#show_users.
    def enterShow_users(self, ctx:SnowflakeParser.Show_usersContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#show_users.
    def exitShow_users(self, ctx:SnowflakeParser.Show_usersContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#show_variables.
    def enterShow_variables(self, ctx:SnowflakeParser.Show_variablesContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#show_variables.
    def exitShow_variables(self, ctx:SnowflakeParser.Show_variablesContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#show_versions_in_dataset.
    def enterShow_versions_in_dataset(self, ctx:SnowflakeParser.Show_versions_in_datasetContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#show_versions_in_dataset.
    def exitShow_versions_in_dataset(self, ctx:SnowflakeParser.Show_versions_in_datasetContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#show_views.
    def enterShow_views(self, ctx:SnowflakeParser.Show_viewsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#show_views.
    def exitShow_views(self, ctx:SnowflakeParser.Show_viewsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#show_warehouses.
    def enterShow_warehouses(self, ctx:SnowflakeParser.Show_warehousesContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#show_warehouses.
    def exitShow_warehouses(self, ctx:SnowflakeParser.Show_warehousesContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#like_pattern.
    def enterLike_pattern(self, ctx:SnowflakeParser.Like_patternContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#like_pattern.
    def exitLike_pattern(self, ctx:SnowflakeParser.Like_patternContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#account_identifier.
    def enterAccount_identifier(self, ctx:SnowflakeParser.Account_identifierContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#account_identifier.
    def exitAccount_identifier(self, ctx:SnowflakeParser.Account_identifierContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#schema_name.
    def enterSchema_name(self, ctx:SnowflakeParser.Schema_nameContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#schema_name.
    def exitSchema_name(self, ctx:SnowflakeParser.Schema_nameContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#object_type.
    def enterObject_type(self, ctx:SnowflakeParser.Object_typeContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#object_type.
    def exitObject_type(self, ctx:SnowflakeParser.Object_typeContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#object_type_list.
    def enterObject_type_list(self, ctx:SnowflakeParser.Object_type_listContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#object_type_list.
    def exitObject_type_list(self, ctx:SnowflakeParser.Object_type_listContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#tag_value.
    def enterTag_value(self, ctx:SnowflakeParser.Tag_valueContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#tag_value.
    def exitTag_value(self, ctx:SnowflakeParser.Tag_valueContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#arg_data_type.
    def enterArg_data_type(self, ctx:SnowflakeParser.Arg_data_typeContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#arg_data_type.
    def exitArg_data_type(self, ctx:SnowflakeParser.Arg_data_typeContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#arg_name.
    def enterArg_name(self, ctx:SnowflakeParser.Arg_nameContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#arg_name.
    def exitArg_name(self, ctx:SnowflakeParser.Arg_nameContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#param_name.
    def enterParam_name(self, ctx:SnowflakeParser.Param_nameContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#param_name.
    def exitParam_name(self, ctx:SnowflakeParser.Param_nameContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#region_group_id.
    def enterRegion_group_id(self, ctx:SnowflakeParser.Region_group_idContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#region_group_id.
    def exitRegion_group_id(self, ctx:SnowflakeParser.Region_group_idContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#snowflake_region_id.
    def enterSnowflake_region_id(self, ctx:SnowflakeParser.Snowflake_region_idContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#snowflake_region_id.
    def exitSnowflake_region_id(self, ctx:SnowflakeParser.Snowflake_region_idContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#string.
    def enterString(self, ctx:SnowflakeParser.StringContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#string.
    def exitString(self, ctx:SnowflakeParser.StringContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#string_list.
    def enterString_list(self, ctx:SnowflakeParser.String_listContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#string_list.
    def exitString_list(self, ctx:SnowflakeParser.String_listContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#id_fn.
    def enterId_fn(self, ctx:SnowflakeParser.Id_fnContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#id_fn.
    def exitId_fn(self, ctx:SnowflakeParser.Id_fnContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#id_.
    def enterId_(self, ctx:SnowflakeParser.Id_Context):
        pass

    # Exit a parse tree produced by SnowflakeParser#id_.
    def exitId_(self, ctx:SnowflakeParser.Id_Context):
        pass


    # Enter a parse tree produced by SnowflakeParser#keyword.
    def enterKeyword(self, ctx:SnowflakeParser.KeywordContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#keyword.
    def exitKeyword(self, ctx:SnowflakeParser.KeywordContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#non_reserved_words.
    def enterNon_reserved_words(self, ctx:SnowflakeParser.Non_reserved_wordsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#non_reserved_words.
    def exitNon_reserved_words(self, ctx:SnowflakeParser.Non_reserved_wordsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#builtin_function.
    def enterBuiltin_function(self, ctx:SnowflakeParser.Builtin_functionContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#builtin_function.
    def exitBuiltin_function(self, ctx:SnowflakeParser.Builtin_functionContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#unary_or_binary_builtin_function.
    def enterUnary_or_binary_builtin_function(self, ctx:SnowflakeParser.Unary_or_binary_builtin_functionContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#unary_or_binary_builtin_function.
    def exitUnary_or_binary_builtin_function(self, ctx:SnowflakeParser.Unary_or_binary_builtin_functionContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#binary_builtin_function.
    def enterBinary_builtin_function(self, ctx:SnowflakeParser.Binary_builtin_functionContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#binary_builtin_function.
    def exitBinary_builtin_function(self, ctx:SnowflakeParser.Binary_builtin_functionContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#binary_or_ternary_builtin_function.
    def enterBinary_or_ternary_builtin_function(self, ctx:SnowflakeParser.Binary_or_ternary_builtin_functionContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#binary_or_ternary_builtin_function.
    def exitBinary_or_ternary_builtin_function(self, ctx:SnowflakeParser.Binary_or_ternary_builtin_functionContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#ternary_builtin_function.
    def enterTernary_builtin_function(self, ctx:SnowflakeParser.Ternary_builtin_functionContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#ternary_builtin_function.
    def exitTernary_builtin_function(self, ctx:SnowflakeParser.Ternary_builtin_functionContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#list_function.
    def enterList_function(self, ctx:SnowflakeParser.List_functionContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#list_function.
    def exitList_function(self, ctx:SnowflakeParser.List_functionContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#pattern.
    def enterPattern(self, ctx:SnowflakeParser.PatternContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#pattern.
    def exitPattern(self, ctx:SnowflakeParser.PatternContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#column_name.
    def enterColumn_name(self, ctx:SnowflakeParser.Column_nameContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#column_name.
    def exitColumn_name(self, ctx:SnowflakeParser.Column_nameContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#column_list.
    def enterColumn_list(self, ctx:SnowflakeParser.Column_listContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#column_list.
    def exitColumn_list(self, ctx:SnowflakeParser.Column_listContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#column_list_with_comment.
    def enterColumn_list_with_comment(self, ctx:SnowflakeParser.Column_list_with_commentContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#column_list_with_comment.
    def exitColumn_list_with_comment(self, ctx:SnowflakeParser.Column_list_with_commentContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#object_name.
    def enterObject_name(self, ctx:SnowflakeParser.Object_nameContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#object_name.
    def exitObject_name(self, ctx:SnowflakeParser.Object_nameContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#object_name_or_identifier.
    def enterObject_name_or_identifier(self, ctx:SnowflakeParser.Object_name_or_identifierContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#object_name_or_identifier.
    def exitObject_name_or_identifier(self, ctx:SnowflakeParser.Object_name_or_identifierContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#num.
    def enterNum(self, ctx:SnowflakeParser.NumContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#num.
    def exitNum(self, ctx:SnowflakeParser.NumContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#expr_list.
    def enterExpr_list(self, ctx:SnowflakeParser.Expr_listContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#expr_list.
    def exitExpr_list(self, ctx:SnowflakeParser.Expr_listContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#expr_list_sorted.
    def enterExpr_list_sorted(self, ctx:SnowflakeParser.Expr_list_sortedContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#expr_list_sorted.
    def exitExpr_list_sorted(self, ctx:SnowflakeParser.Expr_list_sortedContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#expr.
    def enterExpr(self, ctx:SnowflakeParser.ExprContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#expr.
    def exitExpr(self, ctx:SnowflakeParser.ExprContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#iff_expr.
    def enterIff_expr(self, ctx:SnowflakeParser.Iff_exprContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#iff_expr.
    def exitIff_expr(self, ctx:SnowflakeParser.Iff_exprContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#trim_expression.
    def enterTrim_expression(self, ctx:SnowflakeParser.Trim_expressionContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#trim_expression.
    def exitTrim_expression(self, ctx:SnowflakeParser.Trim_expressionContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#try_cast_expr.
    def enterTry_cast_expr(self, ctx:SnowflakeParser.Try_cast_exprContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#try_cast_expr.
    def exitTry_cast_expr(self, ctx:SnowflakeParser.Try_cast_exprContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#cast_expr.
    def enterCast_expr(self, ctx:SnowflakeParser.Cast_exprContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#cast_expr.
    def exitCast_expr(self, ctx:SnowflakeParser.Cast_exprContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#json_literal.
    def enterJson_literal(self, ctx:SnowflakeParser.Json_literalContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#json_literal.
    def exitJson_literal(self, ctx:SnowflakeParser.Json_literalContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#kv_pair.
    def enterKv_pair(self, ctx:SnowflakeParser.Kv_pairContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#kv_pair.
    def exitKv_pair(self, ctx:SnowflakeParser.Kv_pairContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#value.
    def enterValue(self, ctx:SnowflakeParser.ValueContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#value.
    def exitValue(self, ctx:SnowflakeParser.ValueContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#arr_literal.
    def enterArr_literal(self, ctx:SnowflakeParser.Arr_literalContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#arr_literal.
    def exitArr_literal(self, ctx:SnowflakeParser.Arr_literalContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#data_type_size.
    def enterData_type_size(self, ctx:SnowflakeParser.Data_type_sizeContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#data_type_size.
    def exitData_type_size(self, ctx:SnowflakeParser.Data_type_sizeContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#data_type.
    def enterData_type(self, ctx:SnowflakeParser.Data_typeContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#data_type.
    def exitData_type(self, ctx:SnowflakeParser.Data_typeContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#primitive_expression.
    def enterPrimitive_expression(self, ctx:SnowflakeParser.Primitive_expressionContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#primitive_expression.
    def exitPrimitive_expression(self, ctx:SnowflakeParser.Primitive_expressionContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#order_by_expr.
    def enterOrder_by_expr(self, ctx:SnowflakeParser.Order_by_exprContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#order_by_expr.
    def exitOrder_by_expr(self, ctx:SnowflakeParser.Order_by_exprContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#asc_desc.
    def enterAsc_desc(self, ctx:SnowflakeParser.Asc_descContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#asc_desc.
    def exitAsc_desc(self, ctx:SnowflakeParser.Asc_descContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#over_clause.
    def enterOver_clause(self, ctx:SnowflakeParser.Over_clauseContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#over_clause.
    def exitOver_clause(self, ctx:SnowflakeParser.Over_clauseContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#function_call.
    def enterFunction_call(self, ctx:SnowflakeParser.Function_callContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#function_call.
    def exitFunction_call(self, ctx:SnowflakeParser.Function_callContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#param_assoc_list.
    def enterParam_assoc_list(self, ctx:SnowflakeParser.Param_assoc_listContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#param_assoc_list.
    def exitParam_assoc_list(self, ctx:SnowflakeParser.Param_assoc_listContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#param_assoc.
    def enterParam_assoc(self, ctx:SnowflakeParser.Param_assocContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#param_assoc.
    def exitParam_assoc(self, ctx:SnowflakeParser.Param_assocContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#ignore_or_repect_nulls.
    def enterIgnore_or_repect_nulls(self, ctx:SnowflakeParser.Ignore_or_repect_nullsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#ignore_or_repect_nulls.
    def exitIgnore_or_repect_nulls(self, ctx:SnowflakeParser.Ignore_or_repect_nullsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#ranking_windowed_function.
    def enterRanking_windowed_function(self, ctx:SnowflakeParser.Ranking_windowed_functionContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#ranking_windowed_function.
    def exitRanking_windowed_function(self, ctx:SnowflakeParser.Ranking_windowed_functionContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#aggregate_function.
    def enterAggregate_function(self, ctx:SnowflakeParser.Aggregate_functionContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#aggregate_function.
    def exitAggregate_function(self, ctx:SnowflakeParser.Aggregate_functionContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#literal.
    def enterLiteral(self, ctx:SnowflakeParser.LiteralContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#literal.
    def exitLiteral(self, ctx:SnowflakeParser.LiteralContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#sign.
    def enterSign(self, ctx:SnowflakeParser.SignContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#sign.
    def exitSign(self, ctx:SnowflakeParser.SignContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#full_column_name.
    def enterFull_column_name(self, ctx:SnowflakeParser.Full_column_nameContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#full_column_name.
    def exitFull_column_name(self, ctx:SnowflakeParser.Full_column_nameContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#bracket_expression.
    def enterBracket_expression(self, ctx:SnowflakeParser.Bracket_expressionContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#bracket_expression.
    def exitBracket_expression(self, ctx:SnowflakeParser.Bracket_expressionContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#case_expression.
    def enterCase_expression(self, ctx:SnowflakeParser.Case_expressionContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#case_expression.
    def exitCase_expression(self, ctx:SnowflakeParser.Case_expressionContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#switch_search_condition_section.
    def enterSwitch_search_condition_section(self, ctx:SnowflakeParser.Switch_search_condition_sectionContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#switch_search_condition_section.
    def exitSwitch_search_condition_section(self, ctx:SnowflakeParser.Switch_search_condition_sectionContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#switch_section.
    def enterSwitch_section(self, ctx:SnowflakeParser.Switch_sectionContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#switch_section.
    def exitSwitch_section(self, ctx:SnowflakeParser.Switch_sectionContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#query_statement.
    def enterQuery_statement(self, ctx:SnowflakeParser.Query_statementContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#query_statement.
    def exitQuery_statement(self, ctx:SnowflakeParser.Query_statementContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#with_expression.
    def enterWith_expression(self, ctx:SnowflakeParser.With_expressionContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#with_expression.
    def exitWith_expression(self, ctx:SnowflakeParser.With_expressionContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#common_table_expression.
    def enterCommon_table_expression(self, ctx:SnowflakeParser.Common_table_expressionContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#common_table_expression.
    def exitCommon_table_expression(self, ctx:SnowflakeParser.Common_table_expressionContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#select_statement.
    def enterSelect_statement(self, ctx:SnowflakeParser.Select_statementContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#select_statement.
    def exitSelect_statement(self, ctx:SnowflakeParser.Select_statementContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#set_operators.
    def enterSet_operators(self, ctx:SnowflakeParser.Set_operatorsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#set_operators.
    def exitSet_operators(self, ctx:SnowflakeParser.Set_operatorsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#select_statement_in_parentheses.
    def enterSelect_statement_in_parentheses(self, ctx:SnowflakeParser.Select_statement_in_parenthesesContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#select_statement_in_parentheses.
    def exitSelect_statement_in_parentheses(self, ctx:SnowflakeParser.Select_statement_in_parenthesesContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#select_optional_clauses.
    def enterSelect_optional_clauses(self, ctx:SnowflakeParser.Select_optional_clausesContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#select_optional_clauses.
    def exitSelect_optional_clauses(self, ctx:SnowflakeParser.Select_optional_clausesContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#select_clause.
    def enterSelect_clause(self, ctx:SnowflakeParser.Select_clauseContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#select_clause.
    def exitSelect_clause(self, ctx:SnowflakeParser.Select_clauseContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#select_top_clause.
    def enterSelect_top_clause(self, ctx:SnowflakeParser.Select_top_clauseContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#select_top_clause.
    def exitSelect_top_clause(self, ctx:SnowflakeParser.Select_top_clauseContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#select_list_no_top.
    def enterSelect_list_no_top(self, ctx:SnowflakeParser.Select_list_no_topContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#select_list_no_top.
    def exitSelect_list_no_top(self, ctx:SnowflakeParser.Select_list_no_topContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#select_list_top.
    def enterSelect_list_top(self, ctx:SnowflakeParser.Select_list_topContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#select_list_top.
    def exitSelect_list_top(self, ctx:SnowflakeParser.Select_list_topContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#select_list.
    def enterSelect_list(self, ctx:SnowflakeParser.Select_listContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#select_list.
    def exitSelect_list(self, ctx:SnowflakeParser.Select_listContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#select_list_elem.
    def enterSelect_list_elem(self, ctx:SnowflakeParser.Select_list_elemContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#select_list_elem.
    def exitSelect_list_elem(self, ctx:SnowflakeParser.Select_list_elemContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#column_elem_star.
    def enterColumn_elem_star(self, ctx:SnowflakeParser.Column_elem_starContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#column_elem_star.
    def exitColumn_elem_star(self, ctx:SnowflakeParser.Column_elem_starContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#column_elem.
    def enterColumn_elem(self, ctx:SnowflakeParser.Column_elemContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#column_elem.
    def exitColumn_elem(self, ctx:SnowflakeParser.Column_elemContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#object_name_or_alias.
    def enterObject_name_or_alias(self, ctx:SnowflakeParser.Object_name_or_aliasContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#object_name_or_alias.
    def exitObject_name_or_alias(self, ctx:SnowflakeParser.Object_name_or_aliasContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#exclude_clause.
    def enterExclude_clause(self, ctx:SnowflakeParser.Exclude_clauseContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#exclude_clause.
    def exitExclude_clause(self, ctx:SnowflakeParser.Exclude_clauseContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#as_alias.
    def enterAs_alias(self, ctx:SnowflakeParser.As_aliasContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#as_alias.
    def exitAs_alias(self, ctx:SnowflakeParser.As_aliasContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#expression_elem.
    def enterExpression_elem(self, ctx:SnowflakeParser.Expression_elemContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#expression_elem.
    def exitExpression_elem(self, ctx:SnowflakeParser.Expression_elemContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#column_position.
    def enterColumn_position(self, ctx:SnowflakeParser.Column_positionContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#column_position.
    def exitColumn_position(self, ctx:SnowflakeParser.Column_positionContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#all_distinct.
    def enterAll_distinct(self, ctx:SnowflakeParser.All_distinctContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#all_distinct.
    def exitAll_distinct(self, ctx:SnowflakeParser.All_distinctContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#top_clause.
    def enterTop_clause(self, ctx:SnowflakeParser.Top_clauseContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#top_clause.
    def exitTop_clause(self, ctx:SnowflakeParser.Top_clauseContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#into_clause.
    def enterInto_clause(self, ctx:SnowflakeParser.Into_clauseContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#into_clause.
    def exitInto_clause(self, ctx:SnowflakeParser.Into_clauseContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#var_list.
    def enterVar_list(self, ctx:SnowflakeParser.Var_listContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#var_list.
    def exitVar_list(self, ctx:SnowflakeParser.Var_listContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#var.
    def enterVar(self, ctx:SnowflakeParser.VarContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#var.
    def exitVar(self, ctx:SnowflakeParser.VarContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#from_clause.
    def enterFrom_clause(self, ctx:SnowflakeParser.From_clauseContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#from_clause.
    def exitFrom_clause(self, ctx:SnowflakeParser.From_clauseContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#table_sources.
    def enterTable_sources(self, ctx:SnowflakeParser.Table_sourcesContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#table_sources.
    def exitTable_sources(self, ctx:SnowflakeParser.Table_sourcesContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#table_source.
    def enterTable_source(self, ctx:SnowflakeParser.Table_sourceContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#table_source.
    def exitTable_source(self, ctx:SnowflakeParser.Table_sourceContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#table_source_item_joined.
    def enterTable_source_item_joined(self, ctx:SnowflakeParser.Table_source_item_joinedContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#table_source_item_joined.
    def exitTable_source_item_joined(self, ctx:SnowflakeParser.Table_source_item_joinedContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#object_ref.
    def enterObject_ref(self, ctx:SnowflakeParser.Object_refContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#object_ref.
    def exitObject_ref(self, ctx:SnowflakeParser.Object_refContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#flatten_table_option.
    def enterFlatten_table_option(self, ctx:SnowflakeParser.Flatten_table_optionContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#flatten_table_option.
    def exitFlatten_table_option(self, ctx:SnowflakeParser.Flatten_table_optionContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#flatten_table.
    def enterFlatten_table(self, ctx:SnowflakeParser.Flatten_tableContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#flatten_table.
    def exitFlatten_table(self, ctx:SnowflakeParser.Flatten_tableContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#splited_table.
    def enterSplited_table(self, ctx:SnowflakeParser.Splited_tableContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#splited_table.
    def exitSplited_table(self, ctx:SnowflakeParser.Splited_tableContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#prior_list.
    def enterPrior_list(self, ctx:SnowflakeParser.Prior_listContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#prior_list.
    def exitPrior_list(self, ctx:SnowflakeParser.Prior_listContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#prior_item.
    def enterPrior_item(self, ctx:SnowflakeParser.Prior_itemContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#prior_item.
    def exitPrior_item(self, ctx:SnowflakeParser.Prior_itemContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#outer_join.
    def enterOuter_join(self, ctx:SnowflakeParser.Outer_joinContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#outer_join.
    def exitOuter_join(self, ctx:SnowflakeParser.Outer_joinContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#join_type.
    def enterJoin_type(self, ctx:SnowflakeParser.Join_typeContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#join_type.
    def exitJoin_type(self, ctx:SnowflakeParser.Join_typeContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#join_clause.
    def enterJoin_clause(self, ctx:SnowflakeParser.Join_clauseContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#join_clause.
    def exitJoin_clause(self, ctx:SnowflakeParser.Join_clauseContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#at_before.
    def enterAt_before(self, ctx:SnowflakeParser.At_beforeContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#at_before.
    def exitAt_before(self, ctx:SnowflakeParser.At_beforeContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#end.
    def enterEnd(self, ctx:SnowflakeParser.EndContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#end.
    def exitEnd(self, ctx:SnowflakeParser.EndContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#changes.
    def enterChanges(self, ctx:SnowflakeParser.ChangesContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#changes.
    def exitChanges(self, ctx:SnowflakeParser.ChangesContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#default_append_only.
    def enterDefault_append_only(self, ctx:SnowflakeParser.Default_append_onlyContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#default_append_only.
    def exitDefault_append_only(self, ctx:SnowflakeParser.Default_append_onlyContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#partition_by.
    def enterPartition_by(self, ctx:SnowflakeParser.Partition_byContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#partition_by.
    def exitPartition_by(self, ctx:SnowflakeParser.Partition_byContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#alias.
    def enterAlias(self, ctx:SnowflakeParser.AliasContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#alias.
    def exitAlias(self, ctx:SnowflakeParser.AliasContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#expr_alias_list.
    def enterExpr_alias_list(self, ctx:SnowflakeParser.Expr_alias_listContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#expr_alias_list.
    def exitExpr_alias_list(self, ctx:SnowflakeParser.Expr_alias_listContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#measures.
    def enterMeasures(self, ctx:SnowflakeParser.MeasuresContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#measures.
    def exitMeasures(self, ctx:SnowflakeParser.MeasuresContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#match_opts.
    def enterMatch_opts(self, ctx:SnowflakeParser.Match_optsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#match_opts.
    def exitMatch_opts(self, ctx:SnowflakeParser.Match_optsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#row_match.
    def enterRow_match(self, ctx:SnowflakeParser.Row_matchContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#row_match.
    def exitRow_match(self, ctx:SnowflakeParser.Row_matchContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#first_last.
    def enterFirst_last(self, ctx:SnowflakeParser.First_lastContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#first_last.
    def exitFirst_last(self, ctx:SnowflakeParser.First_lastContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#symbol.
    def enterSymbol(self, ctx:SnowflakeParser.SymbolContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#symbol.
    def exitSymbol(self, ctx:SnowflakeParser.SymbolContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#after_match.
    def enterAfter_match(self, ctx:SnowflakeParser.After_matchContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#after_match.
    def exitAfter_match(self, ctx:SnowflakeParser.After_matchContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#symbol_list.
    def enterSymbol_list(self, ctx:SnowflakeParser.Symbol_listContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#symbol_list.
    def exitSymbol_list(self, ctx:SnowflakeParser.Symbol_listContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#define.
    def enterDefine(self, ctx:SnowflakeParser.DefineContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#define.
    def exitDefine(self, ctx:SnowflakeParser.DefineContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#match_recognize.
    def enterMatch_recognize(self, ctx:SnowflakeParser.Match_recognizeContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#match_recognize.
    def exitMatch_recognize(self, ctx:SnowflakeParser.Match_recognizeContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#pivot_unpivot.
    def enterPivot_unpivot(self, ctx:SnowflakeParser.Pivot_unpivotContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#pivot_unpivot.
    def exitPivot_unpivot(self, ctx:SnowflakeParser.Pivot_unpivotContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#column_alias_list_in_brackets.
    def enterColumn_alias_list_in_brackets(self, ctx:SnowflakeParser.Column_alias_list_in_bracketsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#column_alias_list_in_brackets.
    def exitColumn_alias_list_in_brackets(self, ctx:SnowflakeParser.Column_alias_list_in_bracketsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#expr_list_in_parentheses.
    def enterExpr_list_in_parentheses(self, ctx:SnowflakeParser.Expr_list_in_parenthesesContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#expr_list_in_parentheses.
    def exitExpr_list_in_parentheses(self, ctx:SnowflakeParser.Expr_list_in_parenthesesContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#values_table.
    def enterValues_table(self, ctx:SnowflakeParser.Values_tableContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#values_table.
    def exitValues_table(self, ctx:SnowflakeParser.Values_tableContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#values_table_body.
    def enterValues_table_body(self, ctx:SnowflakeParser.Values_table_bodyContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#values_table_body.
    def exitValues_table_body(self, ctx:SnowflakeParser.Values_table_bodyContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#sample_method.
    def enterSample_method(self, ctx:SnowflakeParser.Sample_methodContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#sample_method.
    def exitSample_method(self, ctx:SnowflakeParser.Sample_methodContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#repeatable_seed.
    def enterRepeatable_seed(self, ctx:SnowflakeParser.Repeatable_seedContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#repeatable_seed.
    def exitRepeatable_seed(self, ctx:SnowflakeParser.Repeatable_seedContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#sample_opts.
    def enterSample_opts(self, ctx:SnowflakeParser.Sample_optsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#sample_opts.
    def exitSample_opts(self, ctx:SnowflakeParser.Sample_optsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#sample.
    def enterSample(self, ctx:SnowflakeParser.SampleContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#sample.
    def exitSample(self, ctx:SnowflakeParser.SampleContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#search_condition.
    def enterSearch_condition(self, ctx:SnowflakeParser.Search_conditionContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#search_condition.
    def exitSearch_condition(self, ctx:SnowflakeParser.Search_conditionContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#comparison_operator.
    def enterComparison_operator(self, ctx:SnowflakeParser.Comparison_operatorContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#comparison_operator.
    def exitComparison_operator(self, ctx:SnowflakeParser.Comparison_operatorContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#null_not_null.
    def enterNull_not_null(self, ctx:SnowflakeParser.Null_not_nullContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#null_not_null.
    def exitNull_not_null(self, ctx:SnowflakeParser.Null_not_nullContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#subquery.
    def enterSubquery(self, ctx:SnowflakeParser.SubqueryContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#subquery.
    def exitSubquery(self, ctx:SnowflakeParser.SubqueryContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#predicate.
    def enterPredicate(self, ctx:SnowflakeParser.PredicateContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#predicate.
    def exitPredicate(self, ctx:SnowflakeParser.PredicateContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#where_clause.
    def enterWhere_clause(self, ctx:SnowflakeParser.Where_clauseContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#where_clause.
    def exitWhere_clause(self, ctx:SnowflakeParser.Where_clauseContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#group_by_elem.
    def enterGroup_by_elem(self, ctx:SnowflakeParser.Group_by_elemContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#group_by_elem.
    def exitGroup_by_elem(self, ctx:SnowflakeParser.Group_by_elemContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#group_by_list.
    def enterGroup_by_list(self, ctx:SnowflakeParser.Group_by_listContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#group_by_list.
    def exitGroup_by_list(self, ctx:SnowflakeParser.Group_by_listContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#group_by_clause.
    def enterGroup_by_clause(self, ctx:SnowflakeParser.Group_by_clauseContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#group_by_clause.
    def exitGroup_by_clause(self, ctx:SnowflakeParser.Group_by_clauseContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#having_clause.
    def enterHaving_clause(self, ctx:SnowflakeParser.Having_clauseContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#having_clause.
    def exitHaving_clause(self, ctx:SnowflakeParser.Having_clauseContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#qualify_clause.
    def enterQualify_clause(self, ctx:SnowflakeParser.Qualify_clauseContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#qualify_clause.
    def exitQualify_clause(self, ctx:SnowflakeParser.Qualify_clauseContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#order_item.
    def enterOrder_item(self, ctx:SnowflakeParser.Order_itemContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#order_item.
    def exitOrder_item(self, ctx:SnowflakeParser.Order_itemContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#order_by_clause.
    def enterOrder_by_clause(self, ctx:SnowflakeParser.Order_by_clauseContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#order_by_clause.
    def exitOrder_by_clause(self, ctx:SnowflakeParser.Order_by_clauseContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#row_rows.
    def enterRow_rows(self, ctx:SnowflakeParser.Row_rowsContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#row_rows.
    def exitRow_rows(self, ctx:SnowflakeParser.Row_rowsContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#first_next.
    def enterFirst_next(self, ctx:SnowflakeParser.First_nextContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#first_next.
    def exitFirst_next(self, ctx:SnowflakeParser.First_nextContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#limit_clause.
    def enterLimit_clause(self, ctx:SnowflakeParser.Limit_clauseContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#limit_clause.
    def exitLimit_clause(self, ctx:SnowflakeParser.Limit_clauseContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#round_mode.
    def enterRound_mode(self, ctx:SnowflakeParser.Round_modeContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#round_mode.
    def exitRound_mode(self, ctx:SnowflakeParser.Round_modeContext):
        pass


    # Enter a parse tree produced by SnowflakeParser#round_expr.
    def enterRound_expr(self, ctx:SnowflakeParser.Round_exprContext):
        pass

    # Exit a parse tree produced by SnowflakeParser#round_expr.
    def exitRound_expr(self, ctx:SnowflakeParser.Round_exprContext):
        pass



del SnowflakeParser