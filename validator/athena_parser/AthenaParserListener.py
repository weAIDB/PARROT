# Generated from sql/athena/AthenaParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .AthenaParser import AthenaParser
else:
    from AthenaParser import AthenaParser

# This class defines a complete listener for a parse tree produced by AthenaParser.
class AthenaParserListener(ParseTreeListener):

    # Enter a parse tree produced by AthenaParser#stmt.
    def enterStmt(self, ctx:AthenaParser.StmtContext):
        pass

    # Exit a parse tree produced by AthenaParser#stmt.
    def exitStmt(self, ctx:AthenaParser.StmtContext):
        pass


    # Enter a parse tree produced by AthenaParser#command.
    def enterCommand(self, ctx:AthenaParser.CommandContext):
        pass

    # Exit a parse tree produced by AthenaParser#command.
    def exitCommand(self, ctx:AthenaParser.CommandContext):
        pass


    # Enter a parse tree produced by AthenaParser#ddl_command.
    def enterDdl_command(self, ctx:AthenaParser.Ddl_commandContext):
        pass

    # Exit a parse tree produced by AthenaParser#ddl_command.
    def exitDdl_command(self, ctx:AthenaParser.Ddl_commandContext):
        pass


    # Enter a parse tree produced by AthenaParser#dml_command.
    def enterDml_command(self, ctx:AthenaParser.Dml_commandContext):
        pass

    # Exit a parse tree produced by AthenaParser#dml_command.
    def exitDml_command(self, ctx:AthenaParser.Dml_commandContext):
        pass


    # Enter a parse tree produced by AthenaParser#select.
    def enterSelect(self, ctx:AthenaParser.SelectContext):
        pass

    # Exit a parse tree produced by AthenaParser#select.
    def exitSelect(self, ctx:AthenaParser.SelectContext):
        pass


    # Enter a parse tree produced by AthenaParser#select_statement.
    def enterSelect_statement(self, ctx:AthenaParser.Select_statementContext):
        pass

    # Exit a parse tree produced by AthenaParser#select_statement.
    def exitSelect_statement(self, ctx:AthenaParser.Select_statementContext):
        pass


    # Enter a parse tree produced by AthenaParser#all_distinct.
    def enterAll_distinct(self, ctx:AthenaParser.All_distinctContext):
        pass

    # Exit a parse tree produced by AthenaParser#all_distinct.
    def exitAll_distinct(self, ctx:AthenaParser.All_distinctContext):
        pass


    # Enter a parse tree produced by AthenaParser#order_item.
    def enterOrder_item(self, ctx:AthenaParser.Order_itemContext):
        pass

    # Exit a parse tree produced by AthenaParser#order_item.
    def exitOrder_item(self, ctx:AthenaParser.Order_itemContext):
        pass


    # Enter a parse tree produced by AthenaParser#from_item.
    def enterFrom_item(self, ctx:AthenaParser.From_itemContext):
        pass

    # Exit a parse tree produced by AthenaParser#from_item.
    def exitFrom_item(self, ctx:AthenaParser.From_itemContext):
        pass


    # Enter a parse tree produced by AthenaParser#count.
    def enterCount(self, ctx:AthenaParser.CountContext):
        pass

    # Exit a parse tree produced by AthenaParser#count.
    def exitCount(self, ctx:AthenaParser.CountContext):
        pass


    # Enter a parse tree produced by AthenaParser#with_query.
    def enterWith_query(self, ctx:AthenaParser.With_queryContext):
        pass

    # Exit a parse tree produced by AthenaParser#with_query.
    def exitWith_query(self, ctx:AthenaParser.With_queryContext):
        pass


    # Enter a parse tree produced by AthenaParser#grouping_element.
    def enterGrouping_element(self, ctx:AthenaParser.Grouping_elementContext):
        pass

    # Exit a parse tree produced by AthenaParser#grouping_element.
    def exitGrouping_element(self, ctx:AthenaParser.Grouping_elementContext):
        pass


    # Enter a parse tree produced by AthenaParser#condition.
    def enterCondition(self, ctx:AthenaParser.ConditionContext):
        pass

    # Exit a parse tree produced by AthenaParser#condition.
    def exitCondition(self, ctx:AthenaParser.ConditionContext):
        pass


    # Enter a parse tree produced by AthenaParser#insert_into.
    def enterInsert_into(self, ctx:AthenaParser.Insert_intoContext):
        pass

    # Exit a parse tree produced by AthenaParser#insert_into.
    def exitInsert_into(self, ctx:AthenaParser.Insert_intoContext):
        pass


    # Enter a parse tree produced by AthenaParser#value_list.
    def enterValue_list(self, ctx:AthenaParser.Value_listContext):
        pass

    # Exit a parse tree produced by AthenaParser#value_list.
    def exitValue_list(self, ctx:AthenaParser.Value_listContext):
        pass


    # Enter a parse tree produced by AthenaParser#select_list.
    def enterSelect_list(self, ctx:AthenaParser.Select_listContext):
        pass

    # Exit a parse tree produced by AthenaParser#select_list.
    def exitSelect_list(self, ctx:AthenaParser.Select_listContext):
        pass


    # Enter a parse tree produced by AthenaParser#select_item.
    def enterSelect_item(self, ctx:AthenaParser.Select_itemContext):
        pass

    # Exit a parse tree produced by AthenaParser#select_item.
    def exitSelect_item(self, ctx:AthenaParser.Select_itemContext):
        pass


    # Enter a parse tree produced by AthenaParser#delete_stmt.
    def enterDelete_stmt(self, ctx:AthenaParser.Delete_stmtContext):
        pass

    # Exit a parse tree produced by AthenaParser#delete_stmt.
    def exitDelete_stmt(self, ctx:AthenaParser.Delete_stmtContext):
        pass


    # Enter a parse tree produced by AthenaParser#update.
    def enterUpdate(self, ctx:AthenaParser.UpdateContext):
        pass

    # Exit a parse tree produced by AthenaParser#update.
    def exitUpdate(self, ctx:AthenaParser.UpdateContext):
        pass


    # Enter a parse tree produced by AthenaParser#merge_into.
    def enterMerge_into(self, ctx:AthenaParser.Merge_intoContext):
        pass

    # Exit a parse tree produced by AthenaParser#merge_into.
    def exitMerge_into(self, ctx:AthenaParser.Merge_intoContext):
        pass


    # Enter a parse tree produced by AthenaParser#search_condition.
    def enterSearch_condition(self, ctx:AthenaParser.Search_conditionContext):
        pass

    # Exit a parse tree produced by AthenaParser#search_condition.
    def exitSearch_condition(self, ctx:AthenaParser.Search_conditionContext):
        pass


    # Enter a parse tree produced by AthenaParser#when_clauses.
    def enterWhen_clauses(self, ctx:AthenaParser.When_clausesContext):
        pass

    # Exit a parse tree produced by AthenaParser#when_clauses.
    def exitWhen_clauses(self, ctx:AthenaParser.When_clausesContext):
        pass


    # Enter a parse tree produced by AthenaParser#when_not_matched_clause.
    def enterWhen_not_matched_clause(self, ctx:AthenaParser.When_not_matched_clauseContext):
        pass

    # Exit a parse tree produced by AthenaParser#when_not_matched_clause.
    def exitWhen_not_matched_clause(self, ctx:AthenaParser.When_not_matched_clauseContext):
        pass


    # Enter a parse tree produced by AthenaParser#expression_list_.
    def enterExpression_list_(self, ctx:AthenaParser.Expression_list_Context):
        pass

    # Exit a parse tree produced by AthenaParser#expression_list_.
    def exitExpression_list_(self, ctx:AthenaParser.Expression_list_Context):
        pass


    # Enter a parse tree produced by AthenaParser#column_list.
    def enterColumn_list(self, ctx:AthenaParser.Column_listContext):
        pass

    # Exit a parse tree produced by AthenaParser#column_list.
    def exitColumn_list(self, ctx:AthenaParser.Column_listContext):
        pass


    # Enter a parse tree produced by AthenaParser#when_matched_and_clause.
    def enterWhen_matched_and_clause(self, ctx:AthenaParser.When_matched_and_clauseContext):
        pass

    # Exit a parse tree produced by AthenaParser#when_matched_and_clause.
    def exitWhen_matched_and_clause(self, ctx:AthenaParser.When_matched_and_clauseContext):
        pass


    # Enter a parse tree produced by AthenaParser#when_matched_then_clause.
    def enterWhen_matched_then_clause(self, ctx:AthenaParser.When_matched_then_clauseContext):
        pass

    # Exit a parse tree produced by AthenaParser#when_matched_then_clause.
    def exitWhen_matched_then_clause(self, ctx:AthenaParser.When_matched_then_clauseContext):
        pass


    # Enter a parse tree produced by AthenaParser#update_delete.
    def enterUpdate_delete(self, ctx:AthenaParser.Update_deleteContext):
        pass

    # Exit a parse tree produced by AthenaParser#update_delete.
    def exitUpdate_delete(self, ctx:AthenaParser.Update_deleteContext):
        pass


    # Enter a parse tree produced by AthenaParser#optimize_stmt.
    def enterOptimize_stmt(self, ctx:AthenaParser.Optimize_stmtContext):
        pass

    # Exit a parse tree produced by AthenaParser#optimize_stmt.
    def exitOptimize_stmt(self, ctx:AthenaParser.Optimize_stmtContext):
        pass


    # Enter a parse tree produced by AthenaParser#vacuum.
    def enterVacuum(self, ctx:AthenaParser.VacuumContext):
        pass

    # Exit a parse tree produced by AthenaParser#vacuum.
    def exitVacuum(self, ctx:AthenaParser.VacuumContext):
        pass


    # Enter a parse tree produced by AthenaParser#target_table.
    def enterTarget_table(self, ctx:AthenaParser.Target_tableContext):
        pass

    # Exit a parse tree produced by AthenaParser#target_table.
    def exitTarget_table(self, ctx:AthenaParser.Target_tableContext):
        pass


    # Enter a parse tree produced by AthenaParser#source_table.
    def enterSource_table(self, ctx:AthenaParser.Source_tableContext):
        pass

    # Exit a parse tree produced by AthenaParser#source_table.
    def exitSource_table(self, ctx:AthenaParser.Source_tableContext):
        pass


    # Enter a parse tree produced by AthenaParser#explain.
    def enterExplain(self, ctx:AthenaParser.ExplainContext):
        pass

    # Exit a parse tree produced by AthenaParser#explain.
    def exitExplain(self, ctx:AthenaParser.ExplainContext):
        pass


    # Enter a parse tree produced by AthenaParser#explain_option.
    def enterExplain_option(self, ctx:AthenaParser.Explain_optionContext):
        pass

    # Exit a parse tree produced by AthenaParser#explain_option.
    def exitExplain_option(self, ctx:AthenaParser.Explain_optionContext):
        pass


    # Enter a parse tree produced by AthenaParser#prepare.
    def enterPrepare(self, ctx:AthenaParser.PrepareContext):
        pass

    # Exit a parse tree produced by AthenaParser#prepare.
    def exitPrepare(self, ctx:AthenaParser.PrepareContext):
        pass


    # Enter a parse tree produced by AthenaParser#statement.
    def enterStatement(self, ctx:AthenaParser.StatementContext):
        pass

    # Exit a parse tree produced by AthenaParser#statement.
    def exitStatement(self, ctx:AthenaParser.StatementContext):
        pass


    # Enter a parse tree produced by AthenaParser#execute.
    def enterExecute(self, ctx:AthenaParser.ExecuteContext):
        pass

    # Exit a parse tree produced by AthenaParser#execute.
    def exitExecute(self, ctx:AthenaParser.ExecuteContext):
        pass


    # Enter a parse tree produced by AthenaParser#parameter.
    def enterParameter(self, ctx:AthenaParser.ParameterContext):
        pass

    # Exit a parse tree produced by AthenaParser#parameter.
    def exitParameter(self, ctx:AthenaParser.ParameterContext):
        pass


    # Enter a parse tree produced by AthenaParser#value.
    def enterValue(self, ctx:AthenaParser.ValueContext):
        pass

    # Exit a parse tree produced by AthenaParser#value.
    def exitValue(self, ctx:AthenaParser.ValueContext):
        pass


    # Enter a parse tree produced by AthenaParser#deallocate.
    def enterDeallocate(self, ctx:AthenaParser.DeallocateContext):
        pass

    # Exit a parse tree produced by AthenaParser#deallocate.
    def exitDeallocate(self, ctx:AthenaParser.DeallocateContext):
        pass


    # Enter a parse tree produced by AthenaParser#unload.
    def enterUnload(self, ctx:AthenaParser.UnloadContext):
        pass

    # Exit a parse tree produced by AthenaParser#unload.
    def exitUnload(self, ctx:AthenaParser.UnloadContext):
        pass


    # Enter a parse tree produced by AthenaParser#property_list.
    def enterProperty_list(self, ctx:AthenaParser.Property_listContext):
        pass

    # Exit a parse tree produced by AthenaParser#property_list.
    def exitProperty_list(self, ctx:AthenaParser.Property_listContext):
        pass


    # Enter a parse tree produced by AthenaParser#property_value.
    def enterProperty_value(self, ctx:AthenaParser.Property_valueContext):
        pass

    # Exit a parse tree produced by AthenaParser#property_value.
    def exitProperty_value(self, ctx:AthenaParser.Property_valueContext):
        pass


    # Enter a parse tree produced by AthenaParser#predicate.
    def enterPredicate(self, ctx:AthenaParser.PredicateContext):
        pass

    # Exit a parse tree produced by AthenaParser#predicate.
    def exitPredicate(self, ctx:AthenaParser.PredicateContext):
        pass


    # Enter a parse tree produced by AthenaParser#alter_database.
    def enterAlter_database(self, ctx:AthenaParser.Alter_databaseContext):
        pass

    # Exit a parse tree produced by AthenaParser#alter_database.
    def exitAlter_database(self, ctx:AthenaParser.Alter_databaseContext):
        pass


    # Enter a parse tree produced by AthenaParser#db_schema.
    def enterDb_schema(self, ctx:AthenaParser.Db_schemaContext):
        pass

    # Exit a parse tree produced by AthenaParser#db_schema.
    def exitDb_schema(self, ctx:AthenaParser.Db_schemaContext):
        pass


    # Enter a parse tree produced by AthenaParser#kv_pair.
    def enterKv_pair(self, ctx:AthenaParser.Kv_pairContext):
        pass

    # Exit a parse tree produced by AthenaParser#kv_pair.
    def exitKv_pair(self, ctx:AthenaParser.Kv_pairContext):
        pass


    # Enter a parse tree produced by AthenaParser#alter_table_add_cols.
    def enterAlter_table_add_cols(self, ctx:AthenaParser.Alter_table_add_colsContext):
        pass

    # Exit a parse tree produced by AthenaParser#alter_table_add_cols.
    def exitAlter_table_add_cols(self, ctx:AthenaParser.Alter_table_add_colsContext):
        pass


    # Enter a parse tree produced by AthenaParser#part_col_name_value.
    def enterPart_col_name_value(self, ctx:AthenaParser.Part_col_name_valueContext):
        pass

    # Exit a parse tree produced by AthenaParser#part_col_name_value.
    def exitPart_col_name_value(self, ctx:AthenaParser.Part_col_name_valueContext):
        pass


    # Enter a parse tree produced by AthenaParser#partition_col_name.
    def enterPartition_col_name(self, ctx:AthenaParser.Partition_col_nameContext):
        pass

    # Exit a parse tree produced by AthenaParser#partition_col_name.
    def exitPartition_col_name(self, ctx:AthenaParser.Partition_col_nameContext):
        pass


    # Enter a parse tree produced by AthenaParser#partition_col_value.
    def enterPartition_col_value(self, ctx:AthenaParser.Partition_col_valueContext):
        pass

    # Exit a parse tree produced by AthenaParser#partition_col_value.
    def exitPartition_col_value(self, ctx:AthenaParser.Partition_col_valueContext):
        pass


    # Enter a parse tree produced by AthenaParser#alter_table_add_part.
    def enterAlter_table_add_part(self, ctx:AthenaParser.Alter_table_add_partContext):
        pass

    # Exit a parse tree produced by AthenaParser#alter_table_add_part.
    def exitAlter_table_add_part(self, ctx:AthenaParser.Alter_table_add_partContext):
        pass


    # Enter a parse tree produced by AthenaParser#alter_table_drop_part.
    def enterAlter_table_drop_part(self, ctx:AthenaParser.Alter_table_drop_partContext):
        pass

    # Exit a parse tree produced by AthenaParser#alter_table_drop_part.
    def exitAlter_table_drop_part(self, ctx:AthenaParser.Alter_table_drop_partContext):
        pass


    # Enter a parse tree produced by AthenaParser#partition_spec.
    def enterPartition_spec(self, ctx:AthenaParser.Partition_specContext):
        pass

    # Exit a parse tree produced by AthenaParser#partition_spec.
    def exitPartition_spec(self, ctx:AthenaParser.Partition_specContext):
        pass


    # Enter a parse tree produced by AthenaParser#alter_table_rename_part.
    def enterAlter_table_rename_part(self, ctx:AthenaParser.Alter_table_rename_partContext):
        pass

    # Exit a parse tree produced by AthenaParser#alter_table_rename_part.
    def exitAlter_table_rename_part(self, ctx:AthenaParser.Alter_table_rename_partContext):
        pass


    # Enter a parse tree produced by AthenaParser#alter_table_replace_part.
    def enterAlter_table_replace_part(self, ctx:AthenaParser.Alter_table_replace_partContext):
        pass

    # Exit a parse tree produced by AthenaParser#alter_table_replace_part.
    def exitAlter_table_replace_part(self, ctx:AthenaParser.Alter_table_replace_partContext):
        pass


    # Enter a parse tree produced by AthenaParser#alter_table_set_location.
    def enterAlter_table_set_location(self, ctx:AthenaParser.Alter_table_set_locationContext):
        pass

    # Exit a parse tree produced by AthenaParser#alter_table_set_location.
    def exitAlter_table_set_location(self, ctx:AthenaParser.Alter_table_set_locationContext):
        pass


    # Enter a parse tree produced by AthenaParser#alter_table_set_props.
    def enterAlter_table_set_props(self, ctx:AthenaParser.Alter_table_set_propsContext):
        pass

    # Exit a parse tree produced by AthenaParser#alter_table_set_props.
    def exitAlter_table_set_props(self, ctx:AthenaParser.Alter_table_set_propsContext):
        pass


    # Enter a parse tree produced by AthenaParser#create_database.
    def enterCreate_database(self, ctx:AthenaParser.Create_databaseContext):
        pass

    # Exit a parse tree produced by AthenaParser#create_database.
    def exitCreate_database(self, ctx:AthenaParser.Create_databaseContext):
        pass


    # Enter a parse tree produced by AthenaParser#create_table.
    def enterCreate_table(self, ctx:AthenaParser.Create_tableContext):
        pass

    # Exit a parse tree produced by AthenaParser#create_table.
    def exitCreate_table(self, ctx:AthenaParser.Create_tableContext):
        pass


    # Enter a parse tree produced by AthenaParser#table_comment.
    def enterTable_comment(self, ctx:AthenaParser.Table_commentContext):
        pass

    # Exit a parse tree produced by AthenaParser#table_comment.
    def exitTable_comment(self, ctx:AthenaParser.Table_commentContext):
        pass


    # Enter a parse tree produced by AthenaParser#row_format.
    def enterRow_format(self, ctx:AthenaParser.Row_formatContext):
        pass

    # Exit a parse tree produced by AthenaParser#row_format.
    def exitRow_format(self, ctx:AthenaParser.Row_formatContext):
        pass


    # Enter a parse tree produced by AthenaParser#table_row_format_field_identifier.
    def enterTable_row_format_field_identifier(self, ctx:AthenaParser.Table_row_format_field_identifierContext):
        pass

    # Exit a parse tree produced by AthenaParser#table_row_format_field_identifier.
    def exitTable_row_format_field_identifier(self, ctx:AthenaParser.Table_row_format_field_identifierContext):
        pass


    # Enter a parse tree produced by AthenaParser#table_row_format_coll_items_identifier.
    def enterTable_row_format_coll_items_identifier(self, ctx:AthenaParser.Table_row_format_coll_items_identifierContext):
        pass

    # Exit a parse tree produced by AthenaParser#table_row_format_coll_items_identifier.
    def exitTable_row_format_coll_items_identifier(self, ctx:AthenaParser.Table_row_format_coll_items_identifierContext):
        pass


    # Enter a parse tree produced by AthenaParser#table_row_format_map_keys_identifier.
    def enterTable_row_format_map_keys_identifier(self, ctx:AthenaParser.Table_row_format_map_keys_identifierContext):
        pass

    # Exit a parse tree produced by AthenaParser#table_row_format_map_keys_identifier.
    def exitTable_row_format_map_keys_identifier(self, ctx:AthenaParser.Table_row_format_map_keys_identifierContext):
        pass


    # Enter a parse tree produced by AthenaParser#table_row_format_lines_identifier.
    def enterTable_row_format_lines_identifier(self, ctx:AthenaParser.Table_row_format_lines_identifierContext):
        pass

    # Exit a parse tree produced by AthenaParser#table_row_format_lines_identifier.
    def exitTable_row_format_lines_identifier(self, ctx:AthenaParser.Table_row_format_lines_identifierContext):
        pass


    # Enter a parse tree produced by AthenaParser#table_row_null_format.
    def enterTable_row_null_format(self, ctx:AthenaParser.Table_row_null_formatContext):
        pass

    # Exit a parse tree produced by AthenaParser#table_row_null_format.
    def exitTable_row_null_format(self, ctx:AthenaParser.Table_row_null_formatContext):
        pass


    # Enter a parse tree produced by AthenaParser#file_format.
    def enterFile_format(self, ctx:AthenaParser.File_formatContext):
        pass

    # Exit a parse tree produced by AthenaParser#file_format.
    def exitFile_format(self, ctx:AthenaParser.File_formatContext):
        pass


    # Enter a parse tree produced by AthenaParser#num_buckets.
    def enterNum_buckets(self, ctx:AthenaParser.Num_bucketsContext):
        pass

    # Exit a parse tree produced by AthenaParser#num_buckets.
    def exitNum_buckets(self, ctx:AthenaParser.Num_bucketsContext):
        pass


    # Enter a parse tree produced by AthenaParser#col_def_with_comment.
    def enterCol_def_with_comment(self, ctx:AthenaParser.Col_def_with_commentContext):
        pass

    # Exit a parse tree produced by AthenaParser#col_def_with_comment.
    def exitCol_def_with_comment(self, ctx:AthenaParser.Col_def_with_commentContext):
        pass


    # Enter a parse tree produced by AthenaParser#col_comment.
    def enterCol_comment(self, ctx:AthenaParser.Col_commentContext):
        pass

    # Exit a parse tree produced by AthenaParser#col_comment.
    def exitCol_comment(self, ctx:AthenaParser.Col_commentContext):
        pass


    # Enter a parse tree produced by AthenaParser#create_table_as.
    def enterCreate_table_as(self, ctx:AthenaParser.Create_table_asContext):
        pass

    # Exit a parse tree produced by AthenaParser#create_table_as.
    def exitCreate_table_as(self, ctx:AthenaParser.Create_table_asContext):
        pass


    # Enter a parse tree produced by AthenaParser#property_name.
    def enterProperty_name(self, ctx:AthenaParser.Property_nameContext):
        pass

    # Exit a parse tree produced by AthenaParser#property_name.
    def exitProperty_name(self, ctx:AthenaParser.Property_nameContext):
        pass


    # Enter a parse tree produced by AthenaParser#prop_exp.
    def enterProp_exp(self, ctx:AthenaParser.Prop_expContext):
        pass

    # Exit a parse tree produced by AthenaParser#prop_exp.
    def exitProp_exp(self, ctx:AthenaParser.Prop_expContext):
        pass


    # Enter a parse tree produced by AthenaParser#create_view.
    def enterCreate_view(self, ctx:AthenaParser.Create_viewContext):
        pass

    # Exit a parse tree produced by AthenaParser#create_view.
    def exitCreate_view(self, ctx:AthenaParser.Create_viewContext):
        pass


    # Enter a parse tree produced by AthenaParser#describe.
    def enterDescribe(self, ctx:AthenaParser.DescribeContext):
        pass

    # Exit a parse tree produced by AthenaParser#describe.
    def exitDescribe(self, ctx:AthenaParser.DescribeContext):
        pass


    # Enter a parse tree produced by AthenaParser#field_name.
    def enterField_name(self, ctx:AthenaParser.Field_nameContext):
        pass

    # Exit a parse tree produced by AthenaParser#field_name.
    def exitField_name(self, ctx:AthenaParser.Field_nameContext):
        pass


    # Enter a parse tree produced by AthenaParser#describe_view.
    def enterDescribe_view(self, ctx:AthenaParser.Describe_viewContext):
        pass

    # Exit a parse tree produced by AthenaParser#describe_view.
    def exitDescribe_view(self, ctx:AthenaParser.Describe_viewContext):
        pass


    # Enter a parse tree produced by AthenaParser#drop_database.
    def enterDrop_database(self, ctx:AthenaParser.Drop_databaseContext):
        pass

    # Exit a parse tree produced by AthenaParser#drop_database.
    def exitDrop_database(self, ctx:AthenaParser.Drop_databaseContext):
        pass


    # Enter a parse tree produced by AthenaParser#drop_table.
    def enterDrop_table(self, ctx:AthenaParser.Drop_tableContext):
        pass

    # Exit a parse tree produced by AthenaParser#drop_table.
    def exitDrop_table(self, ctx:AthenaParser.Drop_tableContext):
        pass


    # Enter a parse tree produced by AthenaParser#drop_view.
    def enterDrop_view(self, ctx:AthenaParser.Drop_viewContext):
        pass

    # Exit a parse tree produced by AthenaParser#drop_view.
    def exitDrop_view(self, ctx:AthenaParser.Drop_viewContext):
        pass


    # Enter a parse tree produced by AthenaParser#msck.
    def enterMsck(self, ctx:AthenaParser.MsckContext):
        pass

    # Exit a parse tree produced by AthenaParser#msck.
    def exitMsck(self, ctx:AthenaParser.MsckContext):
        pass


    # Enter a parse tree produced by AthenaParser#show_columns.
    def enterShow_columns(self, ctx:AthenaParser.Show_columnsContext):
        pass

    # Exit a parse tree produced by AthenaParser#show_columns.
    def exitShow_columns(self, ctx:AthenaParser.Show_columnsContext):
        pass


    # Enter a parse tree produced by AthenaParser#show_create_table.
    def enterShow_create_table(self, ctx:AthenaParser.Show_create_tableContext):
        pass

    # Exit a parse tree produced by AthenaParser#show_create_table.
    def exitShow_create_table(self, ctx:AthenaParser.Show_create_tableContext):
        pass


    # Enter a parse tree produced by AthenaParser#show_create_view.
    def enterShow_create_view(self, ctx:AthenaParser.Show_create_viewContext):
        pass

    # Exit a parse tree produced by AthenaParser#show_create_view.
    def exitShow_create_view(self, ctx:AthenaParser.Show_create_viewContext):
        pass


    # Enter a parse tree produced by AthenaParser#show_databases.
    def enterShow_databases(self, ctx:AthenaParser.Show_databasesContext):
        pass

    # Exit a parse tree produced by AthenaParser#show_databases.
    def exitShow_databases(self, ctx:AthenaParser.Show_databasesContext):
        pass


    # Enter a parse tree produced by AthenaParser#show_partitions.
    def enterShow_partitions(self, ctx:AthenaParser.Show_partitionsContext):
        pass

    # Exit a parse tree produced by AthenaParser#show_partitions.
    def exitShow_partitions(self, ctx:AthenaParser.Show_partitionsContext):
        pass


    # Enter a parse tree produced by AthenaParser#show_tables.
    def enterShow_tables(self, ctx:AthenaParser.Show_tablesContext):
        pass

    # Exit a parse tree produced by AthenaParser#show_tables.
    def exitShow_tables(self, ctx:AthenaParser.Show_tablesContext):
        pass


    # Enter a parse tree produced by AthenaParser#show_tblproperties.
    def enterShow_tblproperties(self, ctx:AthenaParser.Show_tblpropertiesContext):
        pass

    # Exit a parse tree produced by AthenaParser#show_tblproperties.
    def exitShow_tblproperties(self, ctx:AthenaParser.Show_tblpropertiesContext):
        pass


    # Enter a parse tree produced by AthenaParser#show_views.
    def enterShow_views(self, ctx:AthenaParser.Show_viewsContext):
        pass

    # Exit a parse tree produced by AthenaParser#show_views.
    def exitShow_views(self, ctx:AthenaParser.Show_viewsContext):
        pass


    # Enter a parse tree produced by AthenaParser#query.
    def enterQuery(self, ctx:AthenaParser.QueryContext):
        pass

    # Exit a parse tree produced by AthenaParser#query.
    def exitQuery(self, ctx:AthenaParser.QueryContext):
        pass


    # Enter a parse tree produced by AthenaParser#true_false.
    def enterTrue_false(self, ctx:AthenaParser.True_falseContext):
        pass

    # Exit a parse tree produced by AthenaParser#true_false.
    def exitTrue_false(self, ctx:AthenaParser.True_falseContext):
        pass


    # Enter a parse tree produced by AthenaParser#boolean_expression.
    def enterBoolean_expression(self, ctx:AthenaParser.Boolean_expressionContext):
        pass

    # Exit a parse tree produced by AthenaParser#boolean_expression.
    def exitBoolean_expression(self, ctx:AthenaParser.Boolean_expressionContext):
        pass


    # Enter a parse tree produced by AthenaParser#pred.
    def enterPred(self, ctx:AthenaParser.PredContext):
        pass

    # Exit a parse tree produced by AthenaParser#pred.
    def exitPred(self, ctx:AthenaParser.PredContext):
        pass


    # Enter a parse tree produced by AthenaParser#table_subquery.
    def enterTable_subquery(self, ctx:AthenaParser.Table_subqueryContext):
        pass

    # Exit a parse tree produced by AthenaParser#table_subquery.
    def exitTable_subquery(self, ctx:AthenaParser.Table_subqueryContext):
        pass


    # Enter a parse tree produced by AthenaParser#comparison_operator.
    def enterComparison_operator(self, ctx:AthenaParser.Comparison_operatorContext):
        pass

    # Exit a parse tree produced by AthenaParser#comparison_operator.
    def exitComparison_operator(self, ctx:AthenaParser.Comparison_operatorContext):
        pass


    # Enter a parse tree produced by AthenaParser#expression.
    def enterExpression(self, ctx:AthenaParser.ExpressionContext):
        pass

    # Exit a parse tree produced by AthenaParser#expression.
    def exitExpression(self, ctx:AthenaParser.ExpressionContext):
        pass


    # Enter a parse tree produced by AthenaParser#case_expression.
    def enterCase_expression(self, ctx:AthenaParser.Case_expressionContext):
        pass

    # Exit a parse tree produced by AthenaParser#case_expression.
    def exitCase_expression(self, ctx:AthenaParser.Case_expressionContext):
        pass


    # Enter a parse tree produced by AthenaParser#when_expression.
    def enterWhen_expression(self, ctx:AthenaParser.When_expressionContext):
        pass

    # Exit a parse tree produced by AthenaParser#when_expression.
    def exitWhen_expression(self, ctx:AthenaParser.When_expressionContext):
        pass


    # Enter a parse tree produced by AthenaParser#primitive_expression.
    def enterPrimitive_expression(self, ctx:AthenaParser.Primitive_expressionContext):
        pass

    # Exit a parse tree produced by AthenaParser#primitive_expression.
    def exitPrimitive_expression(self, ctx:AthenaParser.Primitive_expressionContext):
        pass


    # Enter a parse tree produced by AthenaParser#literal.
    def enterLiteral(self, ctx:AthenaParser.LiteralContext):
        pass

    # Exit a parse tree produced by AthenaParser#literal.
    def exitLiteral(self, ctx:AthenaParser.LiteralContext):
        pass


    # Enter a parse tree produced by AthenaParser#int_number.
    def enterInt_number(self, ctx:AthenaParser.Int_numberContext):
        pass

    # Exit a parse tree produced by AthenaParser#int_number.
    def exitInt_number(self, ctx:AthenaParser.Int_numberContext):
        pass


    # Enter a parse tree produced by AthenaParser#number.
    def enterNumber(self, ctx:AthenaParser.NumberContext):
        pass

    # Exit a parse tree produced by AthenaParser#number.
    def exitNumber(self, ctx:AthenaParser.NumberContext):
        pass


    # Enter a parse tree produced by AthenaParser#data_type.
    def enterData_type(self, ctx:AthenaParser.Data_typeContext):
        pass

    # Exit a parse tree produced by AthenaParser#data_type.
    def exitData_type(self, ctx:AthenaParser.Data_typeContext):
        pass


    # Enter a parse tree produced by AthenaParser#primitive_type.
    def enterPrimitive_type(self, ctx:AthenaParser.Primitive_typeContext):
        pass

    # Exit a parse tree produced by AthenaParser#primitive_type.
    def exitPrimitive_type(self, ctx:AthenaParser.Primitive_typeContext):
        pass


    # Enter a parse tree produced by AthenaParser#precision.
    def enterPrecision(self, ctx:AthenaParser.PrecisionContext):
        pass

    # Exit a parse tree produced by AthenaParser#precision.
    def exitPrecision(self, ctx:AthenaParser.PrecisionContext):
        pass


    # Enter a parse tree produced by AthenaParser#scale.
    def enterScale(self, ctx:AthenaParser.ScaleContext):
        pass

    # Exit a parse tree produced by AthenaParser#scale.
    def exitScale(self, ctx:AthenaParser.ScaleContext):
        pass


    # Enter a parse tree produced by AthenaParser#struct_col_def.
    def enterStruct_col_def(self, ctx:AthenaParser.Struct_col_defContext):
        pass

    # Exit a parse tree produced by AthenaParser#struct_col_def.
    def exitStruct_col_def(self, ctx:AthenaParser.Struct_col_defContext):
        pass


    # Enter a parse tree produced by AthenaParser#col_name.
    def enterCol_name(self, ctx:AthenaParser.Col_nameContext):
        pass

    # Exit a parse tree produced by AthenaParser#col_name.
    def exitCol_name(self, ctx:AthenaParser.Col_nameContext):
        pass


    # Enter a parse tree produced by AthenaParser#db_name.
    def enterDb_name(self, ctx:AthenaParser.Db_nameContext):
        pass

    # Exit a parse tree produced by AthenaParser#db_name.
    def exitDb_name(self, ctx:AthenaParser.Db_nameContext):
        pass


    # Enter a parse tree produced by AthenaParser#database_name.
    def enterDatabase_name(self, ctx:AthenaParser.Database_nameContext):
        pass

    # Exit a parse tree produced by AthenaParser#database_name.
    def exitDatabase_name(self, ctx:AthenaParser.Database_nameContext):
        pass


    # Enter a parse tree produced by AthenaParser#statement_name.
    def enterStatement_name(self, ctx:AthenaParser.Statement_nameContext):
        pass

    # Exit a parse tree produced by AthenaParser#statement_name.
    def exitStatement_name(self, ctx:AthenaParser.Statement_nameContext):
        pass


    # Enter a parse tree produced by AthenaParser#table_name.
    def enterTable_name(self, ctx:AthenaParser.Table_nameContext):
        pass

    # Exit a parse tree produced by AthenaParser#table_name.
    def exitTable_name(self, ctx:AthenaParser.Table_nameContext):
        pass


    # Enter a parse tree produced by AthenaParser#view_name.
    def enterView_name(self, ctx:AthenaParser.View_nameContext):
        pass

    # Exit a parse tree produced by AthenaParser#view_name.
    def exitView_name(self, ctx:AthenaParser.View_nameContext):
        pass


    # Enter a parse tree produced by AthenaParser#destination_table.
    def enterDestination_table(self, ctx:AthenaParser.Destination_tableContext):
        pass

    # Exit a parse tree produced by AthenaParser#destination_table.
    def exitDestination_table(self, ctx:AthenaParser.Destination_tableContext):
        pass


    # Enter a parse tree produced by AthenaParser#string.
    def enterString(self, ctx:AthenaParser.StringContext):
        pass

    # Exit a parse tree produced by AthenaParser#string.
    def exitString(self, ctx:AthenaParser.StringContext):
        pass


    # Enter a parse tree produced by AthenaParser#reg_ex.
    def enterReg_ex(self, ctx:AthenaParser.Reg_exContext):
        pass

    # Exit a parse tree produced by AthenaParser#reg_ex.
    def exitReg_ex(self, ctx:AthenaParser.Reg_exContext):
        pass


    # Enter a parse tree produced by AthenaParser#alias.
    def enterAlias(self, ctx:AthenaParser.AliasContext):
        pass

    # Exit a parse tree produced by AthenaParser#alias.
    def exitAlias(self, ctx:AthenaParser.AliasContext):
        pass


    # Enter a parse tree produced by AthenaParser#target_alias.
    def enterTarget_alias(self, ctx:AthenaParser.Target_aliasContext):
        pass

    # Exit a parse tree produced by AthenaParser#target_alias.
    def exitTarget_alias(self, ctx:AthenaParser.Target_aliasContext):
        pass


    # Enter a parse tree produced by AthenaParser#source_alias.
    def enterSource_alias(self, ctx:AthenaParser.Source_aliasContext):
        pass

    # Exit a parse tree produced by AthenaParser#source_alias.
    def exitSource_alias(self, ctx:AthenaParser.Source_aliasContext):
        pass


    # Enter a parse tree produced by AthenaParser#id_.
    def enterId_(self, ctx:AthenaParser.Id_Context):
        pass

    # Exit a parse tree produced by AthenaParser#id_.
    def exitId_(self, ctx:AthenaParser.Id_Context):
        pass


    # Enter a parse tree produced by AthenaParser#if_not_exists.
    def enterIf_not_exists(self, ctx:AthenaParser.If_not_existsContext):
        pass

    # Exit a parse tree produced by AthenaParser#if_not_exists.
    def exitIf_not_exists(self, ctx:AthenaParser.If_not_existsContext):
        pass


    # Enter a parse tree produced by AthenaParser#if_exists.
    def enterIf_exists(self, ctx:AthenaParser.If_existsContext):
        pass

    # Exit a parse tree produced by AthenaParser#if_exists.
    def exitIf_exists(self, ctx:AthenaParser.If_existsContext):
        pass


    # Enter a parse tree produced by AthenaParser#or_replace.
    def enterOr_replace(self, ctx:AthenaParser.Or_replaceContext):
        pass

    # Exit a parse tree produced by AthenaParser#or_replace.
    def exitOr_replace(self, ctx:AthenaParser.Or_replaceContext):
        pass


    # Enter a parse tree produced by AthenaParser#from_in.
    def enterFrom_in(self, ctx:AthenaParser.From_inContext):
        pass

    # Exit a parse tree produced by AthenaParser#from_in.
    def exitFrom_in(self, ctx:AthenaParser.From_inContext):
        pass



del AthenaParser