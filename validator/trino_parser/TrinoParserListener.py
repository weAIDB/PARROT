# Generated from sql/trino/TrinoParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .TrinoParser import TrinoParser
else:
    from TrinoParser import TrinoParser

# This class defines a complete listener for a parse tree produced by TrinoParser.
class TrinoParserListener(ParseTreeListener):

    # Enter a parse tree produced by TrinoParser#parse.
    def enterParse(self, ctx:TrinoParser.ParseContext):
        pass

    # Exit a parse tree produced by TrinoParser#parse.
    def exitParse(self, ctx:TrinoParser.ParseContext):
        pass


    # Enter a parse tree produced by TrinoParser#statements.
    def enterStatements(self, ctx:TrinoParser.StatementsContext):
        pass

    # Exit a parse tree produced by TrinoParser#statements.
    def exitStatements(self, ctx:TrinoParser.StatementsContext):
        pass


    # Enter a parse tree produced by TrinoParser#singleStatement.
    def enterSingleStatement(self, ctx:TrinoParser.SingleStatementContext):
        pass

    # Exit a parse tree produced by TrinoParser#singleStatement.
    def exitSingleStatement(self, ctx:TrinoParser.SingleStatementContext):
        pass


    # Enter a parse tree produced by TrinoParser#standaloneExpression.
    def enterStandaloneExpression(self, ctx:TrinoParser.StandaloneExpressionContext):
        pass

    # Exit a parse tree produced by TrinoParser#standaloneExpression.
    def exitStandaloneExpression(self, ctx:TrinoParser.StandaloneExpressionContext):
        pass


    # Enter a parse tree produced by TrinoParser#standalonePathSpecification.
    def enterStandalonePathSpecification(self, ctx:TrinoParser.StandalonePathSpecificationContext):
        pass

    # Exit a parse tree produced by TrinoParser#standalonePathSpecification.
    def exitStandalonePathSpecification(self, ctx:TrinoParser.StandalonePathSpecificationContext):
        pass


    # Enter a parse tree produced by TrinoParser#standaloneType.
    def enterStandaloneType(self, ctx:TrinoParser.StandaloneTypeContext):
        pass

    # Exit a parse tree produced by TrinoParser#standaloneType.
    def exitStandaloneType(self, ctx:TrinoParser.StandaloneTypeContext):
        pass


    # Enter a parse tree produced by TrinoParser#standaloneRowPattern.
    def enterStandaloneRowPattern(self, ctx:TrinoParser.StandaloneRowPatternContext):
        pass

    # Exit a parse tree produced by TrinoParser#standaloneRowPattern.
    def exitStandaloneRowPattern(self, ctx:TrinoParser.StandaloneRowPatternContext):
        pass


    # Enter a parse tree produced by TrinoParser#standaloneFunctionSpecification.
    def enterStandaloneFunctionSpecification(self, ctx:TrinoParser.StandaloneFunctionSpecificationContext):
        pass

    # Exit a parse tree produced by TrinoParser#standaloneFunctionSpecification.
    def exitStandaloneFunctionSpecification(self, ctx:TrinoParser.StandaloneFunctionSpecificationContext):
        pass


    # Enter a parse tree produced by TrinoParser#statementDefault.
    def enterStatementDefault(self, ctx:TrinoParser.StatementDefaultContext):
        pass

    # Exit a parse tree produced by TrinoParser#statementDefault.
    def exitStatementDefault(self, ctx:TrinoParser.StatementDefaultContext):
        pass


    # Enter a parse tree produced by TrinoParser#use.
    def enterUse(self, ctx:TrinoParser.UseContext):
        pass

    # Exit a parse tree produced by TrinoParser#use.
    def exitUse(self, ctx:TrinoParser.UseContext):
        pass


    # Enter a parse tree produced by TrinoParser#createCatalog.
    def enterCreateCatalog(self, ctx:TrinoParser.CreateCatalogContext):
        pass

    # Exit a parse tree produced by TrinoParser#createCatalog.
    def exitCreateCatalog(self, ctx:TrinoParser.CreateCatalogContext):
        pass


    # Enter a parse tree produced by TrinoParser#dropCatalog.
    def enterDropCatalog(self, ctx:TrinoParser.DropCatalogContext):
        pass

    # Exit a parse tree produced by TrinoParser#dropCatalog.
    def exitDropCatalog(self, ctx:TrinoParser.DropCatalogContext):
        pass


    # Enter a parse tree produced by TrinoParser#createSchema.
    def enterCreateSchema(self, ctx:TrinoParser.CreateSchemaContext):
        pass

    # Exit a parse tree produced by TrinoParser#createSchema.
    def exitCreateSchema(self, ctx:TrinoParser.CreateSchemaContext):
        pass


    # Enter a parse tree produced by TrinoParser#dropSchema.
    def enterDropSchema(self, ctx:TrinoParser.DropSchemaContext):
        pass

    # Exit a parse tree produced by TrinoParser#dropSchema.
    def exitDropSchema(self, ctx:TrinoParser.DropSchemaContext):
        pass


    # Enter a parse tree produced by TrinoParser#renameSchema.
    def enterRenameSchema(self, ctx:TrinoParser.RenameSchemaContext):
        pass

    # Exit a parse tree produced by TrinoParser#renameSchema.
    def exitRenameSchema(self, ctx:TrinoParser.RenameSchemaContext):
        pass


    # Enter a parse tree produced by TrinoParser#setSchemaAuthorization.
    def enterSetSchemaAuthorization(self, ctx:TrinoParser.SetSchemaAuthorizationContext):
        pass

    # Exit a parse tree produced by TrinoParser#setSchemaAuthorization.
    def exitSetSchemaAuthorization(self, ctx:TrinoParser.SetSchemaAuthorizationContext):
        pass


    # Enter a parse tree produced by TrinoParser#createTableAsSelect.
    def enterCreateTableAsSelect(self, ctx:TrinoParser.CreateTableAsSelectContext):
        pass

    # Exit a parse tree produced by TrinoParser#createTableAsSelect.
    def exitCreateTableAsSelect(self, ctx:TrinoParser.CreateTableAsSelectContext):
        pass


    # Enter a parse tree produced by TrinoParser#createTable.
    def enterCreateTable(self, ctx:TrinoParser.CreateTableContext):
        pass

    # Exit a parse tree produced by TrinoParser#createTable.
    def exitCreateTable(self, ctx:TrinoParser.CreateTableContext):
        pass


    # Enter a parse tree produced by TrinoParser#dropTable.
    def enterDropTable(self, ctx:TrinoParser.DropTableContext):
        pass

    # Exit a parse tree produced by TrinoParser#dropTable.
    def exitDropTable(self, ctx:TrinoParser.DropTableContext):
        pass


    # Enter a parse tree produced by TrinoParser#insertInto.
    def enterInsertInto(self, ctx:TrinoParser.InsertIntoContext):
        pass

    # Exit a parse tree produced by TrinoParser#insertInto.
    def exitInsertInto(self, ctx:TrinoParser.InsertIntoContext):
        pass


    # Enter a parse tree produced by TrinoParser#delete.
    def enterDelete(self, ctx:TrinoParser.DeleteContext):
        pass

    # Exit a parse tree produced by TrinoParser#delete.
    def exitDelete(self, ctx:TrinoParser.DeleteContext):
        pass


    # Enter a parse tree produced by TrinoParser#truncateTable.
    def enterTruncateTable(self, ctx:TrinoParser.TruncateTableContext):
        pass

    # Exit a parse tree produced by TrinoParser#truncateTable.
    def exitTruncateTable(self, ctx:TrinoParser.TruncateTableContext):
        pass


    # Enter a parse tree produced by TrinoParser#commentTable.
    def enterCommentTable(self, ctx:TrinoParser.CommentTableContext):
        pass

    # Exit a parse tree produced by TrinoParser#commentTable.
    def exitCommentTable(self, ctx:TrinoParser.CommentTableContext):
        pass


    # Enter a parse tree produced by TrinoParser#commentView.
    def enterCommentView(self, ctx:TrinoParser.CommentViewContext):
        pass

    # Exit a parse tree produced by TrinoParser#commentView.
    def exitCommentView(self, ctx:TrinoParser.CommentViewContext):
        pass


    # Enter a parse tree produced by TrinoParser#commentColumn.
    def enterCommentColumn(self, ctx:TrinoParser.CommentColumnContext):
        pass

    # Exit a parse tree produced by TrinoParser#commentColumn.
    def exitCommentColumn(self, ctx:TrinoParser.CommentColumnContext):
        pass


    # Enter a parse tree produced by TrinoParser#renameTable.
    def enterRenameTable(self, ctx:TrinoParser.RenameTableContext):
        pass

    # Exit a parse tree produced by TrinoParser#renameTable.
    def exitRenameTable(self, ctx:TrinoParser.RenameTableContext):
        pass


    # Enter a parse tree produced by TrinoParser#addColumn.
    def enterAddColumn(self, ctx:TrinoParser.AddColumnContext):
        pass

    # Exit a parse tree produced by TrinoParser#addColumn.
    def exitAddColumn(self, ctx:TrinoParser.AddColumnContext):
        pass


    # Enter a parse tree produced by TrinoParser#renameColumn.
    def enterRenameColumn(self, ctx:TrinoParser.RenameColumnContext):
        pass

    # Exit a parse tree produced by TrinoParser#renameColumn.
    def exitRenameColumn(self, ctx:TrinoParser.RenameColumnContext):
        pass


    # Enter a parse tree produced by TrinoParser#dropColumn.
    def enterDropColumn(self, ctx:TrinoParser.DropColumnContext):
        pass

    # Exit a parse tree produced by TrinoParser#dropColumn.
    def exitDropColumn(self, ctx:TrinoParser.DropColumnContext):
        pass


    # Enter a parse tree produced by TrinoParser#setColumnType.
    def enterSetColumnType(self, ctx:TrinoParser.SetColumnTypeContext):
        pass

    # Exit a parse tree produced by TrinoParser#setColumnType.
    def exitSetColumnType(self, ctx:TrinoParser.SetColumnTypeContext):
        pass


    # Enter a parse tree produced by TrinoParser#setTableAuthorization.
    def enterSetTableAuthorization(self, ctx:TrinoParser.SetTableAuthorizationContext):
        pass

    # Exit a parse tree produced by TrinoParser#setTableAuthorization.
    def exitSetTableAuthorization(self, ctx:TrinoParser.SetTableAuthorizationContext):
        pass


    # Enter a parse tree produced by TrinoParser#setTableProperties.
    def enterSetTableProperties(self, ctx:TrinoParser.SetTablePropertiesContext):
        pass

    # Exit a parse tree produced by TrinoParser#setTableProperties.
    def exitSetTableProperties(self, ctx:TrinoParser.SetTablePropertiesContext):
        pass


    # Enter a parse tree produced by TrinoParser#tableExecute.
    def enterTableExecute(self, ctx:TrinoParser.TableExecuteContext):
        pass

    # Exit a parse tree produced by TrinoParser#tableExecute.
    def exitTableExecute(self, ctx:TrinoParser.TableExecuteContext):
        pass


    # Enter a parse tree produced by TrinoParser#analyze.
    def enterAnalyze(self, ctx:TrinoParser.AnalyzeContext):
        pass

    # Exit a parse tree produced by TrinoParser#analyze.
    def exitAnalyze(self, ctx:TrinoParser.AnalyzeContext):
        pass


    # Enter a parse tree produced by TrinoParser#createMaterializedView.
    def enterCreateMaterializedView(self, ctx:TrinoParser.CreateMaterializedViewContext):
        pass

    # Exit a parse tree produced by TrinoParser#createMaterializedView.
    def exitCreateMaterializedView(self, ctx:TrinoParser.CreateMaterializedViewContext):
        pass


    # Enter a parse tree produced by TrinoParser#createView.
    def enterCreateView(self, ctx:TrinoParser.CreateViewContext):
        pass

    # Exit a parse tree produced by TrinoParser#createView.
    def exitCreateView(self, ctx:TrinoParser.CreateViewContext):
        pass


    # Enter a parse tree produced by TrinoParser#refreshMaterializedView.
    def enterRefreshMaterializedView(self, ctx:TrinoParser.RefreshMaterializedViewContext):
        pass

    # Exit a parse tree produced by TrinoParser#refreshMaterializedView.
    def exitRefreshMaterializedView(self, ctx:TrinoParser.RefreshMaterializedViewContext):
        pass


    # Enter a parse tree produced by TrinoParser#dropMaterializedView.
    def enterDropMaterializedView(self, ctx:TrinoParser.DropMaterializedViewContext):
        pass

    # Exit a parse tree produced by TrinoParser#dropMaterializedView.
    def exitDropMaterializedView(self, ctx:TrinoParser.DropMaterializedViewContext):
        pass


    # Enter a parse tree produced by TrinoParser#renameMaterializedView.
    def enterRenameMaterializedView(self, ctx:TrinoParser.RenameMaterializedViewContext):
        pass

    # Exit a parse tree produced by TrinoParser#renameMaterializedView.
    def exitRenameMaterializedView(self, ctx:TrinoParser.RenameMaterializedViewContext):
        pass


    # Enter a parse tree produced by TrinoParser#setMaterializedViewProperties.
    def enterSetMaterializedViewProperties(self, ctx:TrinoParser.SetMaterializedViewPropertiesContext):
        pass

    # Exit a parse tree produced by TrinoParser#setMaterializedViewProperties.
    def exitSetMaterializedViewProperties(self, ctx:TrinoParser.SetMaterializedViewPropertiesContext):
        pass


    # Enter a parse tree produced by TrinoParser#dropView.
    def enterDropView(self, ctx:TrinoParser.DropViewContext):
        pass

    # Exit a parse tree produced by TrinoParser#dropView.
    def exitDropView(self, ctx:TrinoParser.DropViewContext):
        pass


    # Enter a parse tree produced by TrinoParser#renameView.
    def enterRenameView(self, ctx:TrinoParser.RenameViewContext):
        pass

    # Exit a parse tree produced by TrinoParser#renameView.
    def exitRenameView(self, ctx:TrinoParser.RenameViewContext):
        pass


    # Enter a parse tree produced by TrinoParser#setViewAuthorization.
    def enterSetViewAuthorization(self, ctx:TrinoParser.SetViewAuthorizationContext):
        pass

    # Exit a parse tree produced by TrinoParser#setViewAuthorization.
    def exitSetViewAuthorization(self, ctx:TrinoParser.SetViewAuthorizationContext):
        pass


    # Enter a parse tree produced by TrinoParser#call.
    def enterCall(self, ctx:TrinoParser.CallContext):
        pass

    # Exit a parse tree produced by TrinoParser#call.
    def exitCall(self, ctx:TrinoParser.CallContext):
        pass


    # Enter a parse tree produced by TrinoParser#createFunction.
    def enterCreateFunction(self, ctx:TrinoParser.CreateFunctionContext):
        pass

    # Exit a parse tree produced by TrinoParser#createFunction.
    def exitCreateFunction(self, ctx:TrinoParser.CreateFunctionContext):
        pass


    # Enter a parse tree produced by TrinoParser#dropFunction.
    def enterDropFunction(self, ctx:TrinoParser.DropFunctionContext):
        pass

    # Exit a parse tree produced by TrinoParser#dropFunction.
    def exitDropFunction(self, ctx:TrinoParser.DropFunctionContext):
        pass


    # Enter a parse tree produced by TrinoParser#createRole.
    def enterCreateRole(self, ctx:TrinoParser.CreateRoleContext):
        pass

    # Exit a parse tree produced by TrinoParser#createRole.
    def exitCreateRole(self, ctx:TrinoParser.CreateRoleContext):
        pass


    # Enter a parse tree produced by TrinoParser#dropRole.
    def enterDropRole(self, ctx:TrinoParser.DropRoleContext):
        pass

    # Exit a parse tree produced by TrinoParser#dropRole.
    def exitDropRole(self, ctx:TrinoParser.DropRoleContext):
        pass


    # Enter a parse tree produced by TrinoParser#grantRoles.
    def enterGrantRoles(self, ctx:TrinoParser.GrantRolesContext):
        pass

    # Exit a parse tree produced by TrinoParser#grantRoles.
    def exitGrantRoles(self, ctx:TrinoParser.GrantRolesContext):
        pass


    # Enter a parse tree produced by TrinoParser#revokeRoles.
    def enterRevokeRoles(self, ctx:TrinoParser.RevokeRolesContext):
        pass

    # Exit a parse tree produced by TrinoParser#revokeRoles.
    def exitRevokeRoles(self, ctx:TrinoParser.RevokeRolesContext):
        pass


    # Enter a parse tree produced by TrinoParser#setRole.
    def enterSetRole(self, ctx:TrinoParser.SetRoleContext):
        pass

    # Exit a parse tree produced by TrinoParser#setRole.
    def exitSetRole(self, ctx:TrinoParser.SetRoleContext):
        pass


    # Enter a parse tree produced by TrinoParser#grant.
    def enterGrant(self, ctx:TrinoParser.GrantContext):
        pass

    # Exit a parse tree produced by TrinoParser#grant.
    def exitGrant(self, ctx:TrinoParser.GrantContext):
        pass


    # Enter a parse tree produced by TrinoParser#deny.
    def enterDeny(self, ctx:TrinoParser.DenyContext):
        pass

    # Exit a parse tree produced by TrinoParser#deny.
    def exitDeny(self, ctx:TrinoParser.DenyContext):
        pass


    # Enter a parse tree produced by TrinoParser#revoke.
    def enterRevoke(self, ctx:TrinoParser.RevokeContext):
        pass

    # Exit a parse tree produced by TrinoParser#revoke.
    def exitRevoke(self, ctx:TrinoParser.RevokeContext):
        pass


    # Enter a parse tree produced by TrinoParser#showGrants.
    def enterShowGrants(self, ctx:TrinoParser.ShowGrantsContext):
        pass

    # Exit a parse tree produced by TrinoParser#showGrants.
    def exitShowGrants(self, ctx:TrinoParser.ShowGrantsContext):
        pass


    # Enter a parse tree produced by TrinoParser#explain.
    def enterExplain(self, ctx:TrinoParser.ExplainContext):
        pass

    # Exit a parse tree produced by TrinoParser#explain.
    def exitExplain(self, ctx:TrinoParser.ExplainContext):
        pass


    # Enter a parse tree produced by TrinoParser#explainAnalyze.
    def enterExplainAnalyze(self, ctx:TrinoParser.ExplainAnalyzeContext):
        pass

    # Exit a parse tree produced by TrinoParser#explainAnalyze.
    def exitExplainAnalyze(self, ctx:TrinoParser.ExplainAnalyzeContext):
        pass


    # Enter a parse tree produced by TrinoParser#showCreateTable.
    def enterShowCreateTable(self, ctx:TrinoParser.ShowCreateTableContext):
        pass

    # Exit a parse tree produced by TrinoParser#showCreateTable.
    def exitShowCreateTable(self, ctx:TrinoParser.ShowCreateTableContext):
        pass


    # Enter a parse tree produced by TrinoParser#showCreateSchema.
    def enterShowCreateSchema(self, ctx:TrinoParser.ShowCreateSchemaContext):
        pass

    # Exit a parse tree produced by TrinoParser#showCreateSchema.
    def exitShowCreateSchema(self, ctx:TrinoParser.ShowCreateSchemaContext):
        pass


    # Enter a parse tree produced by TrinoParser#showCreateView.
    def enterShowCreateView(self, ctx:TrinoParser.ShowCreateViewContext):
        pass

    # Exit a parse tree produced by TrinoParser#showCreateView.
    def exitShowCreateView(self, ctx:TrinoParser.ShowCreateViewContext):
        pass


    # Enter a parse tree produced by TrinoParser#showCreateMaterializedView.
    def enterShowCreateMaterializedView(self, ctx:TrinoParser.ShowCreateMaterializedViewContext):
        pass

    # Exit a parse tree produced by TrinoParser#showCreateMaterializedView.
    def exitShowCreateMaterializedView(self, ctx:TrinoParser.ShowCreateMaterializedViewContext):
        pass


    # Enter a parse tree produced by TrinoParser#showTables.
    def enterShowTables(self, ctx:TrinoParser.ShowTablesContext):
        pass

    # Exit a parse tree produced by TrinoParser#showTables.
    def exitShowTables(self, ctx:TrinoParser.ShowTablesContext):
        pass


    # Enter a parse tree produced by TrinoParser#showSchemas.
    def enterShowSchemas(self, ctx:TrinoParser.ShowSchemasContext):
        pass

    # Exit a parse tree produced by TrinoParser#showSchemas.
    def exitShowSchemas(self, ctx:TrinoParser.ShowSchemasContext):
        pass


    # Enter a parse tree produced by TrinoParser#showCatalogs.
    def enterShowCatalogs(self, ctx:TrinoParser.ShowCatalogsContext):
        pass

    # Exit a parse tree produced by TrinoParser#showCatalogs.
    def exitShowCatalogs(self, ctx:TrinoParser.ShowCatalogsContext):
        pass


    # Enter a parse tree produced by TrinoParser#showColumns.
    def enterShowColumns(self, ctx:TrinoParser.ShowColumnsContext):
        pass

    # Exit a parse tree produced by TrinoParser#showColumns.
    def exitShowColumns(self, ctx:TrinoParser.ShowColumnsContext):
        pass


    # Enter a parse tree produced by TrinoParser#showStats.
    def enterShowStats(self, ctx:TrinoParser.ShowStatsContext):
        pass

    # Exit a parse tree produced by TrinoParser#showStats.
    def exitShowStats(self, ctx:TrinoParser.ShowStatsContext):
        pass


    # Enter a parse tree produced by TrinoParser#showStatsForQuery.
    def enterShowStatsForQuery(self, ctx:TrinoParser.ShowStatsForQueryContext):
        pass

    # Exit a parse tree produced by TrinoParser#showStatsForQuery.
    def exitShowStatsForQuery(self, ctx:TrinoParser.ShowStatsForQueryContext):
        pass


    # Enter a parse tree produced by TrinoParser#showRoles.
    def enterShowRoles(self, ctx:TrinoParser.ShowRolesContext):
        pass

    # Exit a parse tree produced by TrinoParser#showRoles.
    def exitShowRoles(self, ctx:TrinoParser.ShowRolesContext):
        pass


    # Enter a parse tree produced by TrinoParser#showRoleGrants.
    def enterShowRoleGrants(self, ctx:TrinoParser.ShowRoleGrantsContext):
        pass

    # Exit a parse tree produced by TrinoParser#showRoleGrants.
    def exitShowRoleGrants(self, ctx:TrinoParser.ShowRoleGrantsContext):
        pass


    # Enter a parse tree produced by TrinoParser#showFunctions.
    def enterShowFunctions(self, ctx:TrinoParser.ShowFunctionsContext):
        pass

    # Exit a parse tree produced by TrinoParser#showFunctions.
    def exitShowFunctions(self, ctx:TrinoParser.ShowFunctionsContext):
        pass


    # Enter a parse tree produced by TrinoParser#showSession.
    def enterShowSession(self, ctx:TrinoParser.ShowSessionContext):
        pass

    # Exit a parse tree produced by TrinoParser#showSession.
    def exitShowSession(self, ctx:TrinoParser.ShowSessionContext):
        pass


    # Enter a parse tree produced by TrinoParser#setSessionAuthorization.
    def enterSetSessionAuthorization(self, ctx:TrinoParser.SetSessionAuthorizationContext):
        pass

    # Exit a parse tree produced by TrinoParser#setSessionAuthorization.
    def exitSetSessionAuthorization(self, ctx:TrinoParser.SetSessionAuthorizationContext):
        pass


    # Enter a parse tree produced by TrinoParser#resetSessionAuthorization.
    def enterResetSessionAuthorization(self, ctx:TrinoParser.ResetSessionAuthorizationContext):
        pass

    # Exit a parse tree produced by TrinoParser#resetSessionAuthorization.
    def exitResetSessionAuthorization(self, ctx:TrinoParser.ResetSessionAuthorizationContext):
        pass


    # Enter a parse tree produced by TrinoParser#setSession.
    def enterSetSession(self, ctx:TrinoParser.SetSessionContext):
        pass

    # Exit a parse tree produced by TrinoParser#setSession.
    def exitSetSession(self, ctx:TrinoParser.SetSessionContext):
        pass


    # Enter a parse tree produced by TrinoParser#resetSession.
    def enterResetSession(self, ctx:TrinoParser.ResetSessionContext):
        pass

    # Exit a parse tree produced by TrinoParser#resetSession.
    def exitResetSession(self, ctx:TrinoParser.ResetSessionContext):
        pass


    # Enter a parse tree produced by TrinoParser#startTransaction.
    def enterStartTransaction(self, ctx:TrinoParser.StartTransactionContext):
        pass

    # Exit a parse tree produced by TrinoParser#startTransaction.
    def exitStartTransaction(self, ctx:TrinoParser.StartTransactionContext):
        pass


    # Enter a parse tree produced by TrinoParser#commit.
    def enterCommit(self, ctx:TrinoParser.CommitContext):
        pass

    # Exit a parse tree produced by TrinoParser#commit.
    def exitCommit(self, ctx:TrinoParser.CommitContext):
        pass


    # Enter a parse tree produced by TrinoParser#rollback.
    def enterRollback(self, ctx:TrinoParser.RollbackContext):
        pass

    # Exit a parse tree produced by TrinoParser#rollback.
    def exitRollback(self, ctx:TrinoParser.RollbackContext):
        pass


    # Enter a parse tree produced by TrinoParser#prepare.
    def enterPrepare(self, ctx:TrinoParser.PrepareContext):
        pass

    # Exit a parse tree produced by TrinoParser#prepare.
    def exitPrepare(self, ctx:TrinoParser.PrepareContext):
        pass


    # Enter a parse tree produced by TrinoParser#deallocate.
    def enterDeallocate(self, ctx:TrinoParser.DeallocateContext):
        pass

    # Exit a parse tree produced by TrinoParser#deallocate.
    def exitDeallocate(self, ctx:TrinoParser.DeallocateContext):
        pass


    # Enter a parse tree produced by TrinoParser#execute.
    def enterExecute(self, ctx:TrinoParser.ExecuteContext):
        pass

    # Exit a parse tree produced by TrinoParser#execute.
    def exitExecute(self, ctx:TrinoParser.ExecuteContext):
        pass


    # Enter a parse tree produced by TrinoParser#executeImmediate.
    def enterExecuteImmediate(self, ctx:TrinoParser.ExecuteImmediateContext):
        pass

    # Exit a parse tree produced by TrinoParser#executeImmediate.
    def exitExecuteImmediate(self, ctx:TrinoParser.ExecuteImmediateContext):
        pass


    # Enter a parse tree produced by TrinoParser#describeInput.
    def enterDescribeInput(self, ctx:TrinoParser.DescribeInputContext):
        pass

    # Exit a parse tree produced by TrinoParser#describeInput.
    def exitDescribeInput(self, ctx:TrinoParser.DescribeInputContext):
        pass


    # Enter a parse tree produced by TrinoParser#describeOutput.
    def enterDescribeOutput(self, ctx:TrinoParser.DescribeOutputContext):
        pass

    # Exit a parse tree produced by TrinoParser#describeOutput.
    def exitDescribeOutput(self, ctx:TrinoParser.DescribeOutputContext):
        pass


    # Enter a parse tree produced by TrinoParser#setPath.
    def enterSetPath(self, ctx:TrinoParser.SetPathContext):
        pass

    # Exit a parse tree produced by TrinoParser#setPath.
    def exitSetPath(self, ctx:TrinoParser.SetPathContext):
        pass


    # Enter a parse tree produced by TrinoParser#setTimeZone.
    def enterSetTimeZone(self, ctx:TrinoParser.SetTimeZoneContext):
        pass

    # Exit a parse tree produced by TrinoParser#setTimeZone.
    def exitSetTimeZone(self, ctx:TrinoParser.SetTimeZoneContext):
        pass


    # Enter a parse tree produced by TrinoParser#update.
    def enterUpdate(self, ctx:TrinoParser.UpdateContext):
        pass

    # Exit a parse tree produced by TrinoParser#update.
    def exitUpdate(self, ctx:TrinoParser.UpdateContext):
        pass


    # Enter a parse tree produced by TrinoParser#merge.
    def enterMerge(self, ctx:TrinoParser.MergeContext):
        pass

    # Exit a parse tree produced by TrinoParser#merge.
    def exitMerge(self, ctx:TrinoParser.MergeContext):
        pass


    # Enter a parse tree produced by TrinoParser#rootQuery.
    def enterRootQuery(self, ctx:TrinoParser.RootQueryContext):
        pass

    # Exit a parse tree produced by TrinoParser#rootQuery.
    def exitRootQuery(self, ctx:TrinoParser.RootQueryContext):
        pass


    # Enter a parse tree produced by TrinoParser#withFunction.
    def enterWithFunction(self, ctx:TrinoParser.WithFunctionContext):
        pass

    # Exit a parse tree produced by TrinoParser#withFunction.
    def exitWithFunction(self, ctx:TrinoParser.WithFunctionContext):
        pass


    # Enter a parse tree produced by TrinoParser#query.
    def enterQuery(self, ctx:TrinoParser.QueryContext):
        pass

    # Exit a parse tree produced by TrinoParser#query.
    def exitQuery(self, ctx:TrinoParser.QueryContext):
        pass


    # Enter a parse tree produced by TrinoParser#with.
    def enterWith(self, ctx:TrinoParser.WithContext):
        pass

    # Exit a parse tree produced by TrinoParser#with.
    def exitWith(self, ctx:TrinoParser.WithContext):
        pass


    # Enter a parse tree produced by TrinoParser#tableElement.
    def enterTableElement(self, ctx:TrinoParser.TableElementContext):
        pass

    # Exit a parse tree produced by TrinoParser#tableElement.
    def exitTableElement(self, ctx:TrinoParser.TableElementContext):
        pass


    # Enter a parse tree produced by TrinoParser#columnDefinition.
    def enterColumnDefinition(self, ctx:TrinoParser.ColumnDefinitionContext):
        pass

    # Exit a parse tree produced by TrinoParser#columnDefinition.
    def exitColumnDefinition(self, ctx:TrinoParser.ColumnDefinitionContext):
        pass


    # Enter a parse tree produced by TrinoParser#likeClause.
    def enterLikeClause(self, ctx:TrinoParser.LikeClauseContext):
        pass

    # Exit a parse tree produced by TrinoParser#likeClause.
    def exitLikeClause(self, ctx:TrinoParser.LikeClauseContext):
        pass


    # Enter a parse tree produced by TrinoParser#properties.
    def enterProperties(self, ctx:TrinoParser.PropertiesContext):
        pass

    # Exit a parse tree produced by TrinoParser#properties.
    def exitProperties(self, ctx:TrinoParser.PropertiesContext):
        pass


    # Enter a parse tree produced by TrinoParser#propertyAssignments.
    def enterPropertyAssignments(self, ctx:TrinoParser.PropertyAssignmentsContext):
        pass

    # Exit a parse tree produced by TrinoParser#propertyAssignments.
    def exitPropertyAssignments(self, ctx:TrinoParser.PropertyAssignmentsContext):
        pass


    # Enter a parse tree produced by TrinoParser#property.
    def enterProperty(self, ctx:TrinoParser.PropertyContext):
        pass

    # Exit a parse tree produced by TrinoParser#property.
    def exitProperty(self, ctx:TrinoParser.PropertyContext):
        pass


    # Enter a parse tree produced by TrinoParser#defaultPropertyValue.
    def enterDefaultPropertyValue(self, ctx:TrinoParser.DefaultPropertyValueContext):
        pass

    # Exit a parse tree produced by TrinoParser#defaultPropertyValue.
    def exitDefaultPropertyValue(self, ctx:TrinoParser.DefaultPropertyValueContext):
        pass


    # Enter a parse tree produced by TrinoParser#nonDefaultPropertyValue.
    def enterNonDefaultPropertyValue(self, ctx:TrinoParser.NonDefaultPropertyValueContext):
        pass

    # Exit a parse tree produced by TrinoParser#nonDefaultPropertyValue.
    def exitNonDefaultPropertyValue(self, ctx:TrinoParser.NonDefaultPropertyValueContext):
        pass


    # Enter a parse tree produced by TrinoParser#queryNoWith.
    def enterQueryNoWith(self, ctx:TrinoParser.QueryNoWithContext):
        pass

    # Exit a parse tree produced by TrinoParser#queryNoWith.
    def exitQueryNoWith(self, ctx:TrinoParser.QueryNoWithContext):
        pass


    # Enter a parse tree produced by TrinoParser#limitRowCount.
    def enterLimitRowCount(self, ctx:TrinoParser.LimitRowCountContext):
        pass

    # Exit a parse tree produced by TrinoParser#limitRowCount.
    def exitLimitRowCount(self, ctx:TrinoParser.LimitRowCountContext):
        pass


    # Enter a parse tree produced by TrinoParser#rowCount.
    def enterRowCount(self, ctx:TrinoParser.RowCountContext):
        pass

    # Exit a parse tree produced by TrinoParser#rowCount.
    def exitRowCount(self, ctx:TrinoParser.RowCountContext):
        pass


    # Enter a parse tree produced by TrinoParser#queryTermDefault.
    def enterQueryTermDefault(self, ctx:TrinoParser.QueryTermDefaultContext):
        pass

    # Exit a parse tree produced by TrinoParser#queryTermDefault.
    def exitQueryTermDefault(self, ctx:TrinoParser.QueryTermDefaultContext):
        pass


    # Enter a parse tree produced by TrinoParser#setOperation.
    def enterSetOperation(self, ctx:TrinoParser.SetOperationContext):
        pass

    # Exit a parse tree produced by TrinoParser#setOperation.
    def exitSetOperation(self, ctx:TrinoParser.SetOperationContext):
        pass


    # Enter a parse tree produced by TrinoParser#queryPrimaryDefault.
    def enterQueryPrimaryDefault(self, ctx:TrinoParser.QueryPrimaryDefaultContext):
        pass

    # Exit a parse tree produced by TrinoParser#queryPrimaryDefault.
    def exitQueryPrimaryDefault(self, ctx:TrinoParser.QueryPrimaryDefaultContext):
        pass


    # Enter a parse tree produced by TrinoParser#table.
    def enterTable(self, ctx:TrinoParser.TableContext):
        pass

    # Exit a parse tree produced by TrinoParser#table.
    def exitTable(self, ctx:TrinoParser.TableContext):
        pass


    # Enter a parse tree produced by TrinoParser#inlineTable.
    def enterInlineTable(self, ctx:TrinoParser.InlineTableContext):
        pass

    # Exit a parse tree produced by TrinoParser#inlineTable.
    def exitInlineTable(self, ctx:TrinoParser.InlineTableContext):
        pass


    # Enter a parse tree produced by TrinoParser#subquery.
    def enterSubquery(self, ctx:TrinoParser.SubqueryContext):
        pass

    # Exit a parse tree produced by TrinoParser#subquery.
    def exitSubquery(self, ctx:TrinoParser.SubqueryContext):
        pass


    # Enter a parse tree produced by TrinoParser#sortItem.
    def enterSortItem(self, ctx:TrinoParser.SortItemContext):
        pass

    # Exit a parse tree produced by TrinoParser#sortItem.
    def exitSortItem(self, ctx:TrinoParser.SortItemContext):
        pass


    # Enter a parse tree produced by TrinoParser#querySpecification.
    def enterQuerySpecification(self, ctx:TrinoParser.QuerySpecificationContext):
        pass

    # Exit a parse tree produced by TrinoParser#querySpecification.
    def exitQuerySpecification(self, ctx:TrinoParser.QuerySpecificationContext):
        pass


    # Enter a parse tree produced by TrinoParser#groupBy.
    def enterGroupBy(self, ctx:TrinoParser.GroupByContext):
        pass

    # Exit a parse tree produced by TrinoParser#groupBy.
    def exitGroupBy(self, ctx:TrinoParser.GroupByContext):
        pass


    # Enter a parse tree produced by TrinoParser#singleGroupingSet.
    def enterSingleGroupingSet(self, ctx:TrinoParser.SingleGroupingSetContext):
        pass

    # Exit a parse tree produced by TrinoParser#singleGroupingSet.
    def exitSingleGroupingSet(self, ctx:TrinoParser.SingleGroupingSetContext):
        pass


    # Enter a parse tree produced by TrinoParser#rollup.
    def enterRollup(self, ctx:TrinoParser.RollupContext):
        pass

    # Exit a parse tree produced by TrinoParser#rollup.
    def exitRollup(self, ctx:TrinoParser.RollupContext):
        pass


    # Enter a parse tree produced by TrinoParser#cube.
    def enterCube(self, ctx:TrinoParser.CubeContext):
        pass

    # Exit a parse tree produced by TrinoParser#cube.
    def exitCube(self, ctx:TrinoParser.CubeContext):
        pass


    # Enter a parse tree produced by TrinoParser#multipleGroupingSets.
    def enterMultipleGroupingSets(self, ctx:TrinoParser.MultipleGroupingSetsContext):
        pass

    # Exit a parse tree produced by TrinoParser#multipleGroupingSets.
    def exitMultipleGroupingSets(self, ctx:TrinoParser.MultipleGroupingSetsContext):
        pass


    # Enter a parse tree produced by TrinoParser#groupingSet.
    def enterGroupingSet(self, ctx:TrinoParser.GroupingSetContext):
        pass

    # Exit a parse tree produced by TrinoParser#groupingSet.
    def exitGroupingSet(self, ctx:TrinoParser.GroupingSetContext):
        pass


    # Enter a parse tree produced by TrinoParser#windowDefinition.
    def enterWindowDefinition(self, ctx:TrinoParser.WindowDefinitionContext):
        pass

    # Exit a parse tree produced by TrinoParser#windowDefinition.
    def exitWindowDefinition(self, ctx:TrinoParser.WindowDefinitionContext):
        pass


    # Enter a parse tree produced by TrinoParser#windowSpecification.
    def enterWindowSpecification(self, ctx:TrinoParser.WindowSpecificationContext):
        pass

    # Exit a parse tree produced by TrinoParser#windowSpecification.
    def exitWindowSpecification(self, ctx:TrinoParser.WindowSpecificationContext):
        pass


    # Enter a parse tree produced by TrinoParser#namedQuery.
    def enterNamedQuery(self, ctx:TrinoParser.NamedQueryContext):
        pass

    # Exit a parse tree produced by TrinoParser#namedQuery.
    def exitNamedQuery(self, ctx:TrinoParser.NamedQueryContext):
        pass


    # Enter a parse tree produced by TrinoParser#setQuantifier.
    def enterSetQuantifier(self, ctx:TrinoParser.SetQuantifierContext):
        pass

    # Exit a parse tree produced by TrinoParser#setQuantifier.
    def exitSetQuantifier(self, ctx:TrinoParser.SetQuantifierContext):
        pass


    # Enter a parse tree produced by TrinoParser#selectSingle.
    def enterSelectSingle(self, ctx:TrinoParser.SelectSingleContext):
        pass

    # Exit a parse tree produced by TrinoParser#selectSingle.
    def exitSelectSingle(self, ctx:TrinoParser.SelectSingleContext):
        pass


    # Enter a parse tree produced by TrinoParser#selectAll.
    def enterSelectAll(self, ctx:TrinoParser.SelectAllContext):
        pass

    # Exit a parse tree produced by TrinoParser#selectAll.
    def exitSelectAll(self, ctx:TrinoParser.SelectAllContext):
        pass


    # Enter a parse tree produced by TrinoParser#relationDefault.
    def enterRelationDefault(self, ctx:TrinoParser.RelationDefaultContext):
        pass

    # Exit a parse tree produced by TrinoParser#relationDefault.
    def exitRelationDefault(self, ctx:TrinoParser.RelationDefaultContext):
        pass


    # Enter a parse tree produced by TrinoParser#joinRelation.
    def enterJoinRelation(self, ctx:TrinoParser.JoinRelationContext):
        pass

    # Exit a parse tree produced by TrinoParser#joinRelation.
    def exitJoinRelation(self, ctx:TrinoParser.JoinRelationContext):
        pass


    # Enter a parse tree produced by TrinoParser#joinType.
    def enterJoinType(self, ctx:TrinoParser.JoinTypeContext):
        pass

    # Exit a parse tree produced by TrinoParser#joinType.
    def exitJoinType(self, ctx:TrinoParser.JoinTypeContext):
        pass


    # Enter a parse tree produced by TrinoParser#joinCriteria.
    def enterJoinCriteria(self, ctx:TrinoParser.JoinCriteriaContext):
        pass

    # Exit a parse tree produced by TrinoParser#joinCriteria.
    def exitJoinCriteria(self, ctx:TrinoParser.JoinCriteriaContext):
        pass


    # Enter a parse tree produced by TrinoParser#sampledRelation.
    def enterSampledRelation(self, ctx:TrinoParser.SampledRelationContext):
        pass

    # Exit a parse tree produced by TrinoParser#sampledRelation.
    def exitSampledRelation(self, ctx:TrinoParser.SampledRelationContext):
        pass


    # Enter a parse tree produced by TrinoParser#sampleType.
    def enterSampleType(self, ctx:TrinoParser.SampleTypeContext):
        pass

    # Exit a parse tree produced by TrinoParser#sampleType.
    def exitSampleType(self, ctx:TrinoParser.SampleTypeContext):
        pass


    # Enter a parse tree produced by TrinoParser#trimsSpecification.
    def enterTrimsSpecification(self, ctx:TrinoParser.TrimsSpecificationContext):
        pass

    # Exit a parse tree produced by TrinoParser#trimsSpecification.
    def exitTrimsSpecification(self, ctx:TrinoParser.TrimsSpecificationContext):
        pass


    # Enter a parse tree produced by TrinoParser#listAggOverflowBehavior.
    def enterListAggOverflowBehavior(self, ctx:TrinoParser.ListAggOverflowBehaviorContext):
        pass

    # Exit a parse tree produced by TrinoParser#listAggOverflowBehavior.
    def exitListAggOverflowBehavior(self, ctx:TrinoParser.ListAggOverflowBehaviorContext):
        pass


    # Enter a parse tree produced by TrinoParser#listaggCountIndication.
    def enterListaggCountIndication(self, ctx:TrinoParser.ListaggCountIndicationContext):
        pass

    # Exit a parse tree produced by TrinoParser#listaggCountIndication.
    def exitListaggCountIndication(self, ctx:TrinoParser.ListaggCountIndicationContext):
        pass


    # Enter a parse tree produced by TrinoParser#patternRecognition.
    def enterPatternRecognition(self, ctx:TrinoParser.PatternRecognitionContext):
        pass

    # Exit a parse tree produced by TrinoParser#patternRecognition.
    def exitPatternRecognition(self, ctx:TrinoParser.PatternRecognitionContext):
        pass


    # Enter a parse tree produced by TrinoParser#measureDefinition.
    def enterMeasureDefinition(self, ctx:TrinoParser.MeasureDefinitionContext):
        pass

    # Exit a parse tree produced by TrinoParser#measureDefinition.
    def exitMeasureDefinition(self, ctx:TrinoParser.MeasureDefinitionContext):
        pass


    # Enter a parse tree produced by TrinoParser#rowsPerMatch.
    def enterRowsPerMatch(self, ctx:TrinoParser.RowsPerMatchContext):
        pass

    # Exit a parse tree produced by TrinoParser#rowsPerMatch.
    def exitRowsPerMatch(self, ctx:TrinoParser.RowsPerMatchContext):
        pass


    # Enter a parse tree produced by TrinoParser#emptyMatchHandling.
    def enterEmptyMatchHandling(self, ctx:TrinoParser.EmptyMatchHandlingContext):
        pass

    # Exit a parse tree produced by TrinoParser#emptyMatchHandling.
    def exitEmptyMatchHandling(self, ctx:TrinoParser.EmptyMatchHandlingContext):
        pass


    # Enter a parse tree produced by TrinoParser#skipTo.
    def enterSkipTo(self, ctx:TrinoParser.SkipToContext):
        pass

    # Exit a parse tree produced by TrinoParser#skipTo.
    def exitSkipTo(self, ctx:TrinoParser.SkipToContext):
        pass


    # Enter a parse tree produced by TrinoParser#subsetDefinition.
    def enterSubsetDefinition(self, ctx:TrinoParser.SubsetDefinitionContext):
        pass

    # Exit a parse tree produced by TrinoParser#subsetDefinition.
    def exitSubsetDefinition(self, ctx:TrinoParser.SubsetDefinitionContext):
        pass


    # Enter a parse tree produced by TrinoParser#variableDefinition.
    def enterVariableDefinition(self, ctx:TrinoParser.VariableDefinitionContext):
        pass

    # Exit a parse tree produced by TrinoParser#variableDefinition.
    def exitVariableDefinition(self, ctx:TrinoParser.VariableDefinitionContext):
        pass


    # Enter a parse tree produced by TrinoParser#aliasedRelation.
    def enterAliasedRelation(self, ctx:TrinoParser.AliasedRelationContext):
        pass

    # Exit a parse tree produced by TrinoParser#aliasedRelation.
    def exitAliasedRelation(self, ctx:TrinoParser.AliasedRelationContext):
        pass


    # Enter a parse tree produced by TrinoParser#columnAliases.
    def enterColumnAliases(self, ctx:TrinoParser.ColumnAliasesContext):
        pass

    # Exit a parse tree produced by TrinoParser#columnAliases.
    def exitColumnAliases(self, ctx:TrinoParser.ColumnAliasesContext):
        pass


    # Enter a parse tree produced by TrinoParser#tableName.
    def enterTableName(self, ctx:TrinoParser.TableNameContext):
        pass

    # Exit a parse tree produced by TrinoParser#tableName.
    def exitTableName(self, ctx:TrinoParser.TableNameContext):
        pass


    # Enter a parse tree produced by TrinoParser#subqueryRelation.
    def enterSubqueryRelation(self, ctx:TrinoParser.SubqueryRelationContext):
        pass

    # Exit a parse tree produced by TrinoParser#subqueryRelation.
    def exitSubqueryRelation(self, ctx:TrinoParser.SubqueryRelationContext):
        pass


    # Enter a parse tree produced by TrinoParser#unnest.
    def enterUnnest(self, ctx:TrinoParser.UnnestContext):
        pass

    # Exit a parse tree produced by TrinoParser#unnest.
    def exitUnnest(self, ctx:TrinoParser.UnnestContext):
        pass


    # Enter a parse tree produced by TrinoParser#lateral.
    def enterLateral(self, ctx:TrinoParser.LateralContext):
        pass

    # Exit a parse tree produced by TrinoParser#lateral.
    def exitLateral(self, ctx:TrinoParser.LateralContext):
        pass


    # Enter a parse tree produced by TrinoParser#tableFunctionInvocation.
    def enterTableFunctionInvocation(self, ctx:TrinoParser.TableFunctionInvocationContext):
        pass

    # Exit a parse tree produced by TrinoParser#tableFunctionInvocation.
    def exitTableFunctionInvocation(self, ctx:TrinoParser.TableFunctionInvocationContext):
        pass


    # Enter a parse tree produced by TrinoParser#parenthesizedRelation.
    def enterParenthesizedRelation(self, ctx:TrinoParser.ParenthesizedRelationContext):
        pass

    # Exit a parse tree produced by TrinoParser#parenthesizedRelation.
    def exitParenthesizedRelation(self, ctx:TrinoParser.ParenthesizedRelationContext):
        pass


    # Enter a parse tree produced by TrinoParser#tableFunctionCall.
    def enterTableFunctionCall(self, ctx:TrinoParser.TableFunctionCallContext):
        pass

    # Exit a parse tree produced by TrinoParser#tableFunctionCall.
    def exitTableFunctionCall(self, ctx:TrinoParser.TableFunctionCallContext):
        pass


    # Enter a parse tree produced by TrinoParser#tableFunctionArgument.
    def enterTableFunctionArgument(self, ctx:TrinoParser.TableFunctionArgumentContext):
        pass

    # Exit a parse tree produced by TrinoParser#tableFunctionArgument.
    def exitTableFunctionArgument(self, ctx:TrinoParser.TableFunctionArgumentContext):
        pass


    # Enter a parse tree produced by TrinoParser#tableArgument.
    def enterTableArgument(self, ctx:TrinoParser.TableArgumentContext):
        pass

    # Exit a parse tree produced by TrinoParser#tableArgument.
    def exitTableArgument(self, ctx:TrinoParser.TableArgumentContext):
        pass


    # Enter a parse tree produced by TrinoParser#tableArgumentTable.
    def enterTableArgumentTable(self, ctx:TrinoParser.TableArgumentTableContext):
        pass

    # Exit a parse tree produced by TrinoParser#tableArgumentTable.
    def exitTableArgumentTable(self, ctx:TrinoParser.TableArgumentTableContext):
        pass


    # Enter a parse tree produced by TrinoParser#tableArgumentQuery.
    def enterTableArgumentQuery(self, ctx:TrinoParser.TableArgumentQueryContext):
        pass

    # Exit a parse tree produced by TrinoParser#tableArgumentQuery.
    def exitTableArgumentQuery(self, ctx:TrinoParser.TableArgumentQueryContext):
        pass


    # Enter a parse tree produced by TrinoParser#descriptorArgument.
    def enterDescriptorArgument(self, ctx:TrinoParser.DescriptorArgumentContext):
        pass

    # Exit a parse tree produced by TrinoParser#descriptorArgument.
    def exitDescriptorArgument(self, ctx:TrinoParser.DescriptorArgumentContext):
        pass


    # Enter a parse tree produced by TrinoParser#descriptorField.
    def enterDescriptorField(self, ctx:TrinoParser.DescriptorFieldContext):
        pass

    # Exit a parse tree produced by TrinoParser#descriptorField.
    def exitDescriptorField(self, ctx:TrinoParser.DescriptorFieldContext):
        pass


    # Enter a parse tree produced by TrinoParser#copartitionTables.
    def enterCopartitionTables(self, ctx:TrinoParser.CopartitionTablesContext):
        pass

    # Exit a parse tree produced by TrinoParser#copartitionTables.
    def exitCopartitionTables(self, ctx:TrinoParser.CopartitionTablesContext):
        pass


    # Enter a parse tree produced by TrinoParser#expression.
    def enterExpression(self, ctx:TrinoParser.ExpressionContext):
        pass

    # Exit a parse tree produced by TrinoParser#expression.
    def exitExpression(self, ctx:TrinoParser.ExpressionContext):
        pass


    # Enter a parse tree produced by TrinoParser#logicalNot.
    def enterLogicalNot(self, ctx:TrinoParser.LogicalNotContext):
        pass

    # Exit a parse tree produced by TrinoParser#logicalNot.
    def exitLogicalNot(self, ctx:TrinoParser.LogicalNotContext):
        pass


    # Enter a parse tree produced by TrinoParser#predicated.
    def enterPredicated(self, ctx:TrinoParser.PredicatedContext):
        pass

    # Exit a parse tree produced by TrinoParser#predicated.
    def exitPredicated(self, ctx:TrinoParser.PredicatedContext):
        pass


    # Enter a parse tree produced by TrinoParser#or.
    def enterOr(self, ctx:TrinoParser.OrContext):
        pass

    # Exit a parse tree produced by TrinoParser#or.
    def exitOr(self, ctx:TrinoParser.OrContext):
        pass


    # Enter a parse tree produced by TrinoParser#and.
    def enterAnd(self, ctx:TrinoParser.AndContext):
        pass

    # Exit a parse tree produced by TrinoParser#and.
    def exitAnd(self, ctx:TrinoParser.AndContext):
        pass


    # Enter a parse tree produced by TrinoParser#comparison.
    def enterComparison(self, ctx:TrinoParser.ComparisonContext):
        pass

    # Exit a parse tree produced by TrinoParser#comparison.
    def exitComparison(self, ctx:TrinoParser.ComparisonContext):
        pass


    # Enter a parse tree produced by TrinoParser#quantifiedComparison.
    def enterQuantifiedComparison(self, ctx:TrinoParser.QuantifiedComparisonContext):
        pass

    # Exit a parse tree produced by TrinoParser#quantifiedComparison.
    def exitQuantifiedComparison(self, ctx:TrinoParser.QuantifiedComparisonContext):
        pass


    # Enter a parse tree produced by TrinoParser#between.
    def enterBetween(self, ctx:TrinoParser.BetweenContext):
        pass

    # Exit a parse tree produced by TrinoParser#between.
    def exitBetween(self, ctx:TrinoParser.BetweenContext):
        pass


    # Enter a parse tree produced by TrinoParser#inList.
    def enterInList(self, ctx:TrinoParser.InListContext):
        pass

    # Exit a parse tree produced by TrinoParser#inList.
    def exitInList(self, ctx:TrinoParser.InListContext):
        pass


    # Enter a parse tree produced by TrinoParser#inSubquery.
    def enterInSubquery(self, ctx:TrinoParser.InSubqueryContext):
        pass

    # Exit a parse tree produced by TrinoParser#inSubquery.
    def exitInSubquery(self, ctx:TrinoParser.InSubqueryContext):
        pass


    # Enter a parse tree produced by TrinoParser#like.
    def enterLike(self, ctx:TrinoParser.LikeContext):
        pass

    # Exit a parse tree produced by TrinoParser#like.
    def exitLike(self, ctx:TrinoParser.LikeContext):
        pass


    # Enter a parse tree produced by TrinoParser#nullPredicate.
    def enterNullPredicate(self, ctx:TrinoParser.NullPredicateContext):
        pass

    # Exit a parse tree produced by TrinoParser#nullPredicate.
    def exitNullPredicate(self, ctx:TrinoParser.NullPredicateContext):
        pass


    # Enter a parse tree produced by TrinoParser#distinctFrom.
    def enterDistinctFrom(self, ctx:TrinoParser.DistinctFromContext):
        pass

    # Exit a parse tree produced by TrinoParser#distinctFrom.
    def exitDistinctFrom(self, ctx:TrinoParser.DistinctFromContext):
        pass


    # Enter a parse tree produced by TrinoParser#valueExpressionDefault.
    def enterValueExpressionDefault(self, ctx:TrinoParser.ValueExpressionDefaultContext):
        pass

    # Exit a parse tree produced by TrinoParser#valueExpressionDefault.
    def exitValueExpressionDefault(self, ctx:TrinoParser.ValueExpressionDefaultContext):
        pass


    # Enter a parse tree produced by TrinoParser#concatenation.
    def enterConcatenation(self, ctx:TrinoParser.ConcatenationContext):
        pass

    # Exit a parse tree produced by TrinoParser#concatenation.
    def exitConcatenation(self, ctx:TrinoParser.ConcatenationContext):
        pass


    # Enter a parse tree produced by TrinoParser#arithmeticBinary.
    def enterArithmeticBinary(self, ctx:TrinoParser.ArithmeticBinaryContext):
        pass

    # Exit a parse tree produced by TrinoParser#arithmeticBinary.
    def exitArithmeticBinary(self, ctx:TrinoParser.ArithmeticBinaryContext):
        pass


    # Enter a parse tree produced by TrinoParser#arithmeticUnary.
    def enterArithmeticUnary(self, ctx:TrinoParser.ArithmeticUnaryContext):
        pass

    # Exit a parse tree produced by TrinoParser#arithmeticUnary.
    def exitArithmeticUnary(self, ctx:TrinoParser.ArithmeticUnaryContext):
        pass


    # Enter a parse tree produced by TrinoParser#atTimeZone.
    def enterAtTimeZone(self, ctx:TrinoParser.AtTimeZoneContext):
        pass

    # Exit a parse tree produced by TrinoParser#atTimeZone.
    def exitAtTimeZone(self, ctx:TrinoParser.AtTimeZoneContext):
        pass


    # Enter a parse tree produced by TrinoParser#dereference.
    def enterDereference(self, ctx:TrinoParser.DereferenceContext):
        pass

    # Exit a parse tree produced by TrinoParser#dereference.
    def exitDereference(self, ctx:TrinoParser.DereferenceContext):
        pass


    # Enter a parse tree produced by TrinoParser#typeConstructor.
    def enterTypeConstructor(self, ctx:TrinoParser.TypeConstructorContext):
        pass

    # Exit a parse tree produced by TrinoParser#typeConstructor.
    def exitTypeConstructor(self, ctx:TrinoParser.TypeConstructorContext):
        pass


    # Enter a parse tree produced by TrinoParser#jsonValue.
    def enterJsonValue(self, ctx:TrinoParser.JsonValueContext):
        pass

    # Exit a parse tree produced by TrinoParser#jsonValue.
    def exitJsonValue(self, ctx:TrinoParser.JsonValueContext):
        pass


    # Enter a parse tree produced by TrinoParser#specialDateTimeFunction.
    def enterSpecialDateTimeFunction(self, ctx:TrinoParser.SpecialDateTimeFunctionContext):
        pass

    # Exit a parse tree produced by TrinoParser#specialDateTimeFunction.
    def exitSpecialDateTimeFunction(self, ctx:TrinoParser.SpecialDateTimeFunctionContext):
        pass


    # Enter a parse tree produced by TrinoParser#substring.
    def enterSubstring(self, ctx:TrinoParser.SubstringContext):
        pass

    # Exit a parse tree produced by TrinoParser#substring.
    def exitSubstring(self, ctx:TrinoParser.SubstringContext):
        pass


    # Enter a parse tree produced by TrinoParser#cast.
    def enterCast(self, ctx:TrinoParser.CastContext):
        pass

    # Exit a parse tree produced by TrinoParser#cast.
    def exitCast(self, ctx:TrinoParser.CastContext):
        pass


    # Enter a parse tree produced by TrinoParser#lambda.
    def enterLambda(self, ctx:TrinoParser.LambdaContext):
        pass

    # Exit a parse tree produced by TrinoParser#lambda.
    def exitLambda(self, ctx:TrinoParser.LambdaContext):
        pass


    # Enter a parse tree produced by TrinoParser#parenthesizedExpression.
    def enterParenthesizedExpression(self, ctx:TrinoParser.ParenthesizedExpressionContext):
        pass

    # Exit a parse tree produced by TrinoParser#parenthesizedExpression.
    def exitParenthesizedExpression(self, ctx:TrinoParser.ParenthesizedExpressionContext):
        pass


    # Enter a parse tree produced by TrinoParser#trim.
    def enterTrim(self, ctx:TrinoParser.TrimContext):
        pass

    # Exit a parse tree produced by TrinoParser#trim.
    def exitTrim(self, ctx:TrinoParser.TrimContext):
        pass


    # Enter a parse tree produced by TrinoParser#parameter.
    def enterParameter(self, ctx:TrinoParser.ParameterContext):
        pass

    # Exit a parse tree produced by TrinoParser#parameter.
    def exitParameter(self, ctx:TrinoParser.ParameterContext):
        pass


    # Enter a parse tree produced by TrinoParser#normalize.
    def enterNormalize(self, ctx:TrinoParser.NormalizeContext):
        pass

    # Exit a parse tree produced by TrinoParser#normalize.
    def exitNormalize(self, ctx:TrinoParser.NormalizeContext):
        pass


    # Enter a parse tree produced by TrinoParser#jsonObject.
    def enterJsonObject(self, ctx:TrinoParser.JsonObjectContext):
        pass

    # Exit a parse tree produced by TrinoParser#jsonObject.
    def exitJsonObject(self, ctx:TrinoParser.JsonObjectContext):
        pass


    # Enter a parse tree produced by TrinoParser#intervalLiteral.
    def enterIntervalLiteral(self, ctx:TrinoParser.IntervalLiteralContext):
        pass

    # Exit a parse tree produced by TrinoParser#intervalLiteral.
    def exitIntervalLiteral(self, ctx:TrinoParser.IntervalLiteralContext):
        pass


    # Enter a parse tree produced by TrinoParser#numericLiteral.
    def enterNumericLiteral(self, ctx:TrinoParser.NumericLiteralContext):
        pass

    # Exit a parse tree produced by TrinoParser#numericLiteral.
    def exitNumericLiteral(self, ctx:TrinoParser.NumericLiteralContext):
        pass


    # Enter a parse tree produced by TrinoParser#booleanLiteral.
    def enterBooleanLiteral(self, ctx:TrinoParser.BooleanLiteralContext):
        pass

    # Exit a parse tree produced by TrinoParser#booleanLiteral.
    def exitBooleanLiteral(self, ctx:TrinoParser.BooleanLiteralContext):
        pass


    # Enter a parse tree produced by TrinoParser#jsonArray.
    def enterJsonArray(self, ctx:TrinoParser.JsonArrayContext):
        pass

    # Exit a parse tree produced by TrinoParser#jsonArray.
    def exitJsonArray(self, ctx:TrinoParser.JsonArrayContext):
        pass


    # Enter a parse tree produced by TrinoParser#simpleCase.
    def enterSimpleCase(self, ctx:TrinoParser.SimpleCaseContext):
        pass

    # Exit a parse tree produced by TrinoParser#simpleCase.
    def exitSimpleCase(self, ctx:TrinoParser.SimpleCaseContext):
        pass


    # Enter a parse tree produced by TrinoParser#columnReference.
    def enterColumnReference(self, ctx:TrinoParser.ColumnReferenceContext):
        pass

    # Exit a parse tree produced by TrinoParser#columnReference.
    def exitColumnReference(self, ctx:TrinoParser.ColumnReferenceContext):
        pass


    # Enter a parse tree produced by TrinoParser#nullLiteral.
    def enterNullLiteral(self, ctx:TrinoParser.NullLiteralContext):
        pass

    # Exit a parse tree produced by TrinoParser#nullLiteral.
    def exitNullLiteral(self, ctx:TrinoParser.NullLiteralContext):
        pass


    # Enter a parse tree produced by TrinoParser#rowConstructor.
    def enterRowConstructor(self, ctx:TrinoParser.RowConstructorContext):
        pass

    # Exit a parse tree produced by TrinoParser#rowConstructor.
    def exitRowConstructor(self, ctx:TrinoParser.RowConstructorContext):
        pass


    # Enter a parse tree produced by TrinoParser#subscript.
    def enterSubscript(self, ctx:TrinoParser.SubscriptContext):
        pass

    # Exit a parse tree produced by TrinoParser#subscript.
    def exitSubscript(self, ctx:TrinoParser.SubscriptContext):
        pass


    # Enter a parse tree produced by TrinoParser#jsonExists.
    def enterJsonExists(self, ctx:TrinoParser.JsonExistsContext):
        pass

    # Exit a parse tree produced by TrinoParser#jsonExists.
    def exitJsonExists(self, ctx:TrinoParser.JsonExistsContext):
        pass


    # Enter a parse tree produced by TrinoParser#currentPath.
    def enterCurrentPath(self, ctx:TrinoParser.CurrentPathContext):
        pass

    # Exit a parse tree produced by TrinoParser#currentPath.
    def exitCurrentPath(self, ctx:TrinoParser.CurrentPathContext):
        pass


    # Enter a parse tree produced by TrinoParser#subqueryExpression.
    def enterSubqueryExpression(self, ctx:TrinoParser.SubqueryExpressionContext):
        pass

    # Exit a parse tree produced by TrinoParser#subqueryExpression.
    def exitSubqueryExpression(self, ctx:TrinoParser.SubqueryExpressionContext):
        pass


    # Enter a parse tree produced by TrinoParser#binaryLiteral.
    def enterBinaryLiteral(self, ctx:TrinoParser.BinaryLiteralContext):
        pass

    # Exit a parse tree produced by TrinoParser#binaryLiteral.
    def exitBinaryLiteral(self, ctx:TrinoParser.BinaryLiteralContext):
        pass


    # Enter a parse tree produced by TrinoParser#currentUser.
    def enterCurrentUser(self, ctx:TrinoParser.CurrentUserContext):
        pass

    # Exit a parse tree produced by TrinoParser#currentUser.
    def exitCurrentUser(self, ctx:TrinoParser.CurrentUserContext):
        pass


    # Enter a parse tree produced by TrinoParser#jsonQuery.
    def enterJsonQuery(self, ctx:TrinoParser.JsonQueryContext):
        pass

    # Exit a parse tree produced by TrinoParser#jsonQuery.
    def exitJsonQuery(self, ctx:TrinoParser.JsonQueryContext):
        pass


    # Enter a parse tree produced by TrinoParser#measure.
    def enterMeasure(self, ctx:TrinoParser.MeasureContext):
        pass

    # Exit a parse tree produced by TrinoParser#measure.
    def exitMeasure(self, ctx:TrinoParser.MeasureContext):
        pass


    # Enter a parse tree produced by TrinoParser#extract.
    def enterExtract(self, ctx:TrinoParser.ExtractContext):
        pass

    # Exit a parse tree produced by TrinoParser#extract.
    def exitExtract(self, ctx:TrinoParser.ExtractContext):
        pass


    # Enter a parse tree produced by TrinoParser#stringLiteral.
    def enterStringLiteral(self, ctx:TrinoParser.StringLiteralContext):
        pass

    # Exit a parse tree produced by TrinoParser#stringLiteral.
    def exitStringLiteral(self, ctx:TrinoParser.StringLiteralContext):
        pass


    # Enter a parse tree produced by TrinoParser#arrayConstructor.
    def enterArrayConstructor(self, ctx:TrinoParser.ArrayConstructorContext):
        pass

    # Exit a parse tree produced by TrinoParser#arrayConstructor.
    def exitArrayConstructor(self, ctx:TrinoParser.ArrayConstructorContext):
        pass


    # Enter a parse tree produced by TrinoParser#functionCall.
    def enterFunctionCall(self, ctx:TrinoParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by TrinoParser#functionCall.
    def exitFunctionCall(self, ctx:TrinoParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by TrinoParser#currentSchema.
    def enterCurrentSchema(self, ctx:TrinoParser.CurrentSchemaContext):
        pass

    # Exit a parse tree produced by TrinoParser#currentSchema.
    def exitCurrentSchema(self, ctx:TrinoParser.CurrentSchemaContext):
        pass


    # Enter a parse tree produced by TrinoParser#exists.
    def enterExists(self, ctx:TrinoParser.ExistsContext):
        pass

    # Exit a parse tree produced by TrinoParser#exists.
    def exitExists(self, ctx:TrinoParser.ExistsContext):
        pass


    # Enter a parse tree produced by TrinoParser#position.
    def enterPosition(self, ctx:TrinoParser.PositionContext):
        pass

    # Exit a parse tree produced by TrinoParser#position.
    def exitPosition(self, ctx:TrinoParser.PositionContext):
        pass


    # Enter a parse tree produced by TrinoParser#listagg.
    def enterListagg(self, ctx:TrinoParser.ListaggContext):
        pass

    # Exit a parse tree produced by TrinoParser#listagg.
    def exitListagg(self, ctx:TrinoParser.ListaggContext):
        pass


    # Enter a parse tree produced by TrinoParser#searchedCase.
    def enterSearchedCase(self, ctx:TrinoParser.SearchedCaseContext):
        pass

    # Exit a parse tree produced by TrinoParser#searchedCase.
    def exitSearchedCase(self, ctx:TrinoParser.SearchedCaseContext):
        pass


    # Enter a parse tree produced by TrinoParser#currentCatalog.
    def enterCurrentCatalog(self, ctx:TrinoParser.CurrentCatalogContext):
        pass

    # Exit a parse tree produced by TrinoParser#currentCatalog.
    def exitCurrentCatalog(self, ctx:TrinoParser.CurrentCatalogContext):
        pass


    # Enter a parse tree produced by TrinoParser#groupingOperation.
    def enterGroupingOperation(self, ctx:TrinoParser.GroupingOperationContext):
        pass

    # Exit a parse tree produced by TrinoParser#groupingOperation.
    def exitGroupingOperation(self, ctx:TrinoParser.GroupingOperationContext):
        pass


    # Enter a parse tree produced by TrinoParser#jsonPathInvocation.
    def enterJsonPathInvocation(self, ctx:TrinoParser.JsonPathInvocationContext):
        pass

    # Exit a parse tree produced by TrinoParser#jsonPathInvocation.
    def exitJsonPathInvocation(self, ctx:TrinoParser.JsonPathInvocationContext):
        pass


    # Enter a parse tree produced by TrinoParser#jsonValueExpression.
    def enterJsonValueExpression(self, ctx:TrinoParser.JsonValueExpressionContext):
        pass

    # Exit a parse tree produced by TrinoParser#jsonValueExpression.
    def exitJsonValueExpression(self, ctx:TrinoParser.JsonValueExpressionContext):
        pass


    # Enter a parse tree produced by TrinoParser#jsonRepresentation.
    def enterJsonRepresentation(self, ctx:TrinoParser.JsonRepresentationContext):
        pass

    # Exit a parse tree produced by TrinoParser#jsonRepresentation.
    def exitJsonRepresentation(self, ctx:TrinoParser.JsonRepresentationContext):
        pass


    # Enter a parse tree produced by TrinoParser#jsonArgument.
    def enterJsonArgument(self, ctx:TrinoParser.JsonArgumentContext):
        pass

    # Exit a parse tree produced by TrinoParser#jsonArgument.
    def exitJsonArgument(self, ctx:TrinoParser.JsonArgumentContext):
        pass


    # Enter a parse tree produced by TrinoParser#jsonExistsErrorBehavior.
    def enterJsonExistsErrorBehavior(self, ctx:TrinoParser.JsonExistsErrorBehaviorContext):
        pass

    # Exit a parse tree produced by TrinoParser#jsonExistsErrorBehavior.
    def exitJsonExistsErrorBehavior(self, ctx:TrinoParser.JsonExistsErrorBehaviorContext):
        pass


    # Enter a parse tree produced by TrinoParser#jsonValueBehavior.
    def enterJsonValueBehavior(self, ctx:TrinoParser.JsonValueBehaviorContext):
        pass

    # Exit a parse tree produced by TrinoParser#jsonValueBehavior.
    def exitJsonValueBehavior(self, ctx:TrinoParser.JsonValueBehaviorContext):
        pass


    # Enter a parse tree produced by TrinoParser#jsonQueryWrapperBehavior.
    def enterJsonQueryWrapperBehavior(self, ctx:TrinoParser.JsonQueryWrapperBehaviorContext):
        pass

    # Exit a parse tree produced by TrinoParser#jsonQueryWrapperBehavior.
    def exitJsonQueryWrapperBehavior(self, ctx:TrinoParser.JsonQueryWrapperBehaviorContext):
        pass


    # Enter a parse tree produced by TrinoParser#jsonQueryBehavior.
    def enterJsonQueryBehavior(self, ctx:TrinoParser.JsonQueryBehaviorContext):
        pass

    # Exit a parse tree produced by TrinoParser#jsonQueryBehavior.
    def exitJsonQueryBehavior(self, ctx:TrinoParser.JsonQueryBehaviorContext):
        pass


    # Enter a parse tree produced by TrinoParser#jsonObjectMember.
    def enterJsonObjectMember(self, ctx:TrinoParser.JsonObjectMemberContext):
        pass

    # Exit a parse tree produced by TrinoParser#jsonObjectMember.
    def exitJsonObjectMember(self, ctx:TrinoParser.JsonObjectMemberContext):
        pass


    # Enter a parse tree produced by TrinoParser#processingMode.
    def enterProcessingMode(self, ctx:TrinoParser.ProcessingModeContext):
        pass

    # Exit a parse tree produced by TrinoParser#processingMode.
    def exitProcessingMode(self, ctx:TrinoParser.ProcessingModeContext):
        pass


    # Enter a parse tree produced by TrinoParser#nullTreatment.
    def enterNullTreatment(self, ctx:TrinoParser.NullTreatmentContext):
        pass

    # Exit a parse tree produced by TrinoParser#nullTreatment.
    def exitNullTreatment(self, ctx:TrinoParser.NullTreatmentContext):
        pass


    # Enter a parse tree produced by TrinoParser#basicStringLiteral.
    def enterBasicStringLiteral(self, ctx:TrinoParser.BasicStringLiteralContext):
        pass

    # Exit a parse tree produced by TrinoParser#basicStringLiteral.
    def exitBasicStringLiteral(self, ctx:TrinoParser.BasicStringLiteralContext):
        pass


    # Enter a parse tree produced by TrinoParser#unicodeStringLiteral.
    def enterUnicodeStringLiteral(self, ctx:TrinoParser.UnicodeStringLiteralContext):
        pass

    # Exit a parse tree produced by TrinoParser#unicodeStringLiteral.
    def exitUnicodeStringLiteral(self, ctx:TrinoParser.UnicodeStringLiteralContext):
        pass


    # Enter a parse tree produced by TrinoParser#timeZoneInterval.
    def enterTimeZoneInterval(self, ctx:TrinoParser.TimeZoneIntervalContext):
        pass

    # Exit a parse tree produced by TrinoParser#timeZoneInterval.
    def exitTimeZoneInterval(self, ctx:TrinoParser.TimeZoneIntervalContext):
        pass


    # Enter a parse tree produced by TrinoParser#timeZoneString.
    def enterTimeZoneString(self, ctx:TrinoParser.TimeZoneStringContext):
        pass

    # Exit a parse tree produced by TrinoParser#timeZoneString.
    def exitTimeZoneString(self, ctx:TrinoParser.TimeZoneStringContext):
        pass


    # Enter a parse tree produced by TrinoParser#comparisonOperator.
    def enterComparisonOperator(self, ctx:TrinoParser.ComparisonOperatorContext):
        pass

    # Exit a parse tree produced by TrinoParser#comparisonOperator.
    def exitComparisonOperator(self, ctx:TrinoParser.ComparisonOperatorContext):
        pass


    # Enter a parse tree produced by TrinoParser#comparisonQuantifier.
    def enterComparisonQuantifier(self, ctx:TrinoParser.ComparisonQuantifierContext):
        pass

    # Exit a parse tree produced by TrinoParser#comparisonQuantifier.
    def exitComparisonQuantifier(self, ctx:TrinoParser.ComparisonQuantifierContext):
        pass


    # Enter a parse tree produced by TrinoParser#booleanValue.
    def enterBooleanValue(self, ctx:TrinoParser.BooleanValueContext):
        pass

    # Exit a parse tree produced by TrinoParser#booleanValue.
    def exitBooleanValue(self, ctx:TrinoParser.BooleanValueContext):
        pass


    # Enter a parse tree produced by TrinoParser#interval.
    def enterInterval(self, ctx:TrinoParser.IntervalContext):
        pass

    # Exit a parse tree produced by TrinoParser#interval.
    def exitInterval(self, ctx:TrinoParser.IntervalContext):
        pass


    # Enter a parse tree produced by TrinoParser#intervalField.
    def enterIntervalField(self, ctx:TrinoParser.IntervalFieldContext):
        pass

    # Exit a parse tree produced by TrinoParser#intervalField.
    def exitIntervalField(self, ctx:TrinoParser.IntervalFieldContext):
        pass


    # Enter a parse tree produced by TrinoParser#normalForm.
    def enterNormalForm(self, ctx:TrinoParser.NormalFormContext):
        pass

    # Exit a parse tree produced by TrinoParser#normalForm.
    def exitNormalForm(self, ctx:TrinoParser.NormalFormContext):
        pass


    # Enter a parse tree produced by TrinoParser#rowType.
    def enterRowType(self, ctx:TrinoParser.RowTypeContext):
        pass

    # Exit a parse tree produced by TrinoParser#rowType.
    def exitRowType(self, ctx:TrinoParser.RowTypeContext):
        pass


    # Enter a parse tree produced by TrinoParser#intervalType.
    def enterIntervalType(self, ctx:TrinoParser.IntervalTypeContext):
        pass

    # Exit a parse tree produced by TrinoParser#intervalType.
    def exitIntervalType(self, ctx:TrinoParser.IntervalTypeContext):
        pass


    # Enter a parse tree produced by TrinoParser#arrayType.
    def enterArrayType(self, ctx:TrinoParser.ArrayTypeContext):
        pass

    # Exit a parse tree produced by TrinoParser#arrayType.
    def exitArrayType(self, ctx:TrinoParser.ArrayTypeContext):
        pass


    # Enter a parse tree produced by TrinoParser#doublePrecisionType.
    def enterDoublePrecisionType(self, ctx:TrinoParser.DoublePrecisionTypeContext):
        pass

    # Exit a parse tree produced by TrinoParser#doublePrecisionType.
    def exitDoublePrecisionType(self, ctx:TrinoParser.DoublePrecisionTypeContext):
        pass


    # Enter a parse tree produced by TrinoParser#legacyArrayType.
    def enterLegacyArrayType(self, ctx:TrinoParser.LegacyArrayTypeContext):
        pass

    # Exit a parse tree produced by TrinoParser#legacyArrayType.
    def exitLegacyArrayType(self, ctx:TrinoParser.LegacyArrayTypeContext):
        pass


    # Enter a parse tree produced by TrinoParser#genericType.
    def enterGenericType(self, ctx:TrinoParser.GenericTypeContext):
        pass

    # Exit a parse tree produced by TrinoParser#genericType.
    def exitGenericType(self, ctx:TrinoParser.GenericTypeContext):
        pass


    # Enter a parse tree produced by TrinoParser#dateTimeType.
    def enterDateTimeType(self, ctx:TrinoParser.DateTimeTypeContext):
        pass

    # Exit a parse tree produced by TrinoParser#dateTimeType.
    def exitDateTimeType(self, ctx:TrinoParser.DateTimeTypeContext):
        pass


    # Enter a parse tree produced by TrinoParser#legacyMapType.
    def enterLegacyMapType(self, ctx:TrinoParser.LegacyMapTypeContext):
        pass

    # Exit a parse tree produced by TrinoParser#legacyMapType.
    def exitLegacyMapType(self, ctx:TrinoParser.LegacyMapTypeContext):
        pass


    # Enter a parse tree produced by TrinoParser#rowField.
    def enterRowField(self, ctx:TrinoParser.RowFieldContext):
        pass

    # Exit a parse tree produced by TrinoParser#rowField.
    def exitRowField(self, ctx:TrinoParser.RowFieldContext):
        pass


    # Enter a parse tree produced by TrinoParser#typeParameter.
    def enterTypeParameter(self, ctx:TrinoParser.TypeParameterContext):
        pass

    # Exit a parse tree produced by TrinoParser#typeParameter.
    def exitTypeParameter(self, ctx:TrinoParser.TypeParameterContext):
        pass


    # Enter a parse tree produced by TrinoParser#whenClause.
    def enterWhenClause(self, ctx:TrinoParser.WhenClauseContext):
        pass

    # Exit a parse tree produced by TrinoParser#whenClause.
    def exitWhenClause(self, ctx:TrinoParser.WhenClauseContext):
        pass


    # Enter a parse tree produced by TrinoParser#filter.
    def enterFilter(self, ctx:TrinoParser.FilterContext):
        pass

    # Exit a parse tree produced by TrinoParser#filter.
    def exitFilter(self, ctx:TrinoParser.FilterContext):
        pass


    # Enter a parse tree produced by TrinoParser#mergeUpdate.
    def enterMergeUpdate(self, ctx:TrinoParser.MergeUpdateContext):
        pass

    # Exit a parse tree produced by TrinoParser#mergeUpdate.
    def exitMergeUpdate(self, ctx:TrinoParser.MergeUpdateContext):
        pass


    # Enter a parse tree produced by TrinoParser#mergeDelete.
    def enterMergeDelete(self, ctx:TrinoParser.MergeDeleteContext):
        pass

    # Exit a parse tree produced by TrinoParser#mergeDelete.
    def exitMergeDelete(self, ctx:TrinoParser.MergeDeleteContext):
        pass


    # Enter a parse tree produced by TrinoParser#mergeInsert.
    def enterMergeInsert(self, ctx:TrinoParser.MergeInsertContext):
        pass

    # Exit a parse tree produced by TrinoParser#mergeInsert.
    def exitMergeInsert(self, ctx:TrinoParser.MergeInsertContext):
        pass


    # Enter a parse tree produced by TrinoParser#over.
    def enterOver(self, ctx:TrinoParser.OverContext):
        pass

    # Exit a parse tree produced by TrinoParser#over.
    def exitOver(self, ctx:TrinoParser.OverContext):
        pass


    # Enter a parse tree produced by TrinoParser#windowFrame.
    def enterWindowFrame(self, ctx:TrinoParser.WindowFrameContext):
        pass

    # Exit a parse tree produced by TrinoParser#windowFrame.
    def exitWindowFrame(self, ctx:TrinoParser.WindowFrameContext):
        pass


    # Enter a parse tree produced by TrinoParser#frameExtent.
    def enterFrameExtent(self, ctx:TrinoParser.FrameExtentContext):
        pass

    # Exit a parse tree produced by TrinoParser#frameExtent.
    def exitFrameExtent(self, ctx:TrinoParser.FrameExtentContext):
        pass


    # Enter a parse tree produced by TrinoParser#unboundedFrame.
    def enterUnboundedFrame(self, ctx:TrinoParser.UnboundedFrameContext):
        pass

    # Exit a parse tree produced by TrinoParser#unboundedFrame.
    def exitUnboundedFrame(self, ctx:TrinoParser.UnboundedFrameContext):
        pass


    # Enter a parse tree produced by TrinoParser#currentRowBound.
    def enterCurrentRowBound(self, ctx:TrinoParser.CurrentRowBoundContext):
        pass

    # Exit a parse tree produced by TrinoParser#currentRowBound.
    def exitCurrentRowBound(self, ctx:TrinoParser.CurrentRowBoundContext):
        pass


    # Enter a parse tree produced by TrinoParser#boundedFrame.
    def enterBoundedFrame(self, ctx:TrinoParser.BoundedFrameContext):
        pass

    # Exit a parse tree produced by TrinoParser#boundedFrame.
    def exitBoundedFrame(self, ctx:TrinoParser.BoundedFrameContext):
        pass


    # Enter a parse tree produced by TrinoParser#quantifiedPrimary.
    def enterQuantifiedPrimary(self, ctx:TrinoParser.QuantifiedPrimaryContext):
        pass

    # Exit a parse tree produced by TrinoParser#quantifiedPrimary.
    def exitQuantifiedPrimary(self, ctx:TrinoParser.QuantifiedPrimaryContext):
        pass


    # Enter a parse tree produced by TrinoParser#patternConcatenation.
    def enterPatternConcatenation(self, ctx:TrinoParser.PatternConcatenationContext):
        pass

    # Exit a parse tree produced by TrinoParser#patternConcatenation.
    def exitPatternConcatenation(self, ctx:TrinoParser.PatternConcatenationContext):
        pass


    # Enter a parse tree produced by TrinoParser#patternAlternation.
    def enterPatternAlternation(self, ctx:TrinoParser.PatternAlternationContext):
        pass

    # Exit a parse tree produced by TrinoParser#patternAlternation.
    def exitPatternAlternation(self, ctx:TrinoParser.PatternAlternationContext):
        pass


    # Enter a parse tree produced by TrinoParser#patternVariable.
    def enterPatternVariable(self, ctx:TrinoParser.PatternVariableContext):
        pass

    # Exit a parse tree produced by TrinoParser#patternVariable.
    def exitPatternVariable(self, ctx:TrinoParser.PatternVariableContext):
        pass


    # Enter a parse tree produced by TrinoParser#emptyPattern.
    def enterEmptyPattern(self, ctx:TrinoParser.EmptyPatternContext):
        pass

    # Exit a parse tree produced by TrinoParser#emptyPattern.
    def exitEmptyPattern(self, ctx:TrinoParser.EmptyPatternContext):
        pass


    # Enter a parse tree produced by TrinoParser#patternPermutation.
    def enterPatternPermutation(self, ctx:TrinoParser.PatternPermutationContext):
        pass

    # Exit a parse tree produced by TrinoParser#patternPermutation.
    def exitPatternPermutation(self, ctx:TrinoParser.PatternPermutationContext):
        pass


    # Enter a parse tree produced by TrinoParser#groupedPattern.
    def enterGroupedPattern(self, ctx:TrinoParser.GroupedPatternContext):
        pass

    # Exit a parse tree produced by TrinoParser#groupedPattern.
    def exitGroupedPattern(self, ctx:TrinoParser.GroupedPatternContext):
        pass


    # Enter a parse tree produced by TrinoParser#partitionStartAnchor.
    def enterPartitionStartAnchor(self, ctx:TrinoParser.PartitionStartAnchorContext):
        pass

    # Exit a parse tree produced by TrinoParser#partitionStartAnchor.
    def exitPartitionStartAnchor(self, ctx:TrinoParser.PartitionStartAnchorContext):
        pass


    # Enter a parse tree produced by TrinoParser#partitionEndAnchor.
    def enterPartitionEndAnchor(self, ctx:TrinoParser.PartitionEndAnchorContext):
        pass

    # Exit a parse tree produced by TrinoParser#partitionEndAnchor.
    def exitPartitionEndAnchor(self, ctx:TrinoParser.PartitionEndAnchorContext):
        pass


    # Enter a parse tree produced by TrinoParser#excludedPattern.
    def enterExcludedPattern(self, ctx:TrinoParser.ExcludedPatternContext):
        pass

    # Exit a parse tree produced by TrinoParser#excludedPattern.
    def exitExcludedPattern(self, ctx:TrinoParser.ExcludedPatternContext):
        pass


    # Enter a parse tree produced by TrinoParser#zeroOrMoreQuantifier.
    def enterZeroOrMoreQuantifier(self, ctx:TrinoParser.ZeroOrMoreQuantifierContext):
        pass

    # Exit a parse tree produced by TrinoParser#zeroOrMoreQuantifier.
    def exitZeroOrMoreQuantifier(self, ctx:TrinoParser.ZeroOrMoreQuantifierContext):
        pass


    # Enter a parse tree produced by TrinoParser#oneOrMoreQuantifier.
    def enterOneOrMoreQuantifier(self, ctx:TrinoParser.OneOrMoreQuantifierContext):
        pass

    # Exit a parse tree produced by TrinoParser#oneOrMoreQuantifier.
    def exitOneOrMoreQuantifier(self, ctx:TrinoParser.OneOrMoreQuantifierContext):
        pass


    # Enter a parse tree produced by TrinoParser#zeroOrOneQuantifier.
    def enterZeroOrOneQuantifier(self, ctx:TrinoParser.ZeroOrOneQuantifierContext):
        pass

    # Exit a parse tree produced by TrinoParser#zeroOrOneQuantifier.
    def exitZeroOrOneQuantifier(self, ctx:TrinoParser.ZeroOrOneQuantifierContext):
        pass


    # Enter a parse tree produced by TrinoParser#rangeQuantifier.
    def enterRangeQuantifier(self, ctx:TrinoParser.RangeQuantifierContext):
        pass

    # Exit a parse tree produced by TrinoParser#rangeQuantifier.
    def exitRangeQuantifier(self, ctx:TrinoParser.RangeQuantifierContext):
        pass


    # Enter a parse tree produced by TrinoParser#updateAssignment.
    def enterUpdateAssignment(self, ctx:TrinoParser.UpdateAssignmentContext):
        pass

    # Exit a parse tree produced by TrinoParser#updateAssignment.
    def exitUpdateAssignment(self, ctx:TrinoParser.UpdateAssignmentContext):
        pass


    # Enter a parse tree produced by TrinoParser#explainFormat.
    def enterExplainFormat(self, ctx:TrinoParser.ExplainFormatContext):
        pass

    # Exit a parse tree produced by TrinoParser#explainFormat.
    def exitExplainFormat(self, ctx:TrinoParser.ExplainFormatContext):
        pass


    # Enter a parse tree produced by TrinoParser#explainType.
    def enterExplainType(self, ctx:TrinoParser.ExplainTypeContext):
        pass

    # Exit a parse tree produced by TrinoParser#explainType.
    def exitExplainType(self, ctx:TrinoParser.ExplainTypeContext):
        pass


    # Enter a parse tree produced by TrinoParser#isolationLevel.
    def enterIsolationLevel(self, ctx:TrinoParser.IsolationLevelContext):
        pass

    # Exit a parse tree produced by TrinoParser#isolationLevel.
    def exitIsolationLevel(self, ctx:TrinoParser.IsolationLevelContext):
        pass


    # Enter a parse tree produced by TrinoParser#transactionAccessMode.
    def enterTransactionAccessMode(self, ctx:TrinoParser.TransactionAccessModeContext):
        pass

    # Exit a parse tree produced by TrinoParser#transactionAccessMode.
    def exitTransactionAccessMode(self, ctx:TrinoParser.TransactionAccessModeContext):
        pass


    # Enter a parse tree produced by TrinoParser#readUncommitted.
    def enterReadUncommitted(self, ctx:TrinoParser.ReadUncommittedContext):
        pass

    # Exit a parse tree produced by TrinoParser#readUncommitted.
    def exitReadUncommitted(self, ctx:TrinoParser.ReadUncommittedContext):
        pass


    # Enter a parse tree produced by TrinoParser#readCommitted.
    def enterReadCommitted(self, ctx:TrinoParser.ReadCommittedContext):
        pass

    # Exit a parse tree produced by TrinoParser#readCommitted.
    def exitReadCommitted(self, ctx:TrinoParser.ReadCommittedContext):
        pass


    # Enter a parse tree produced by TrinoParser#repeatableRead.
    def enterRepeatableRead(self, ctx:TrinoParser.RepeatableReadContext):
        pass

    # Exit a parse tree produced by TrinoParser#repeatableRead.
    def exitRepeatableRead(self, ctx:TrinoParser.RepeatableReadContext):
        pass


    # Enter a parse tree produced by TrinoParser#serializable.
    def enterSerializable(self, ctx:TrinoParser.SerializableContext):
        pass

    # Exit a parse tree produced by TrinoParser#serializable.
    def exitSerializable(self, ctx:TrinoParser.SerializableContext):
        pass


    # Enter a parse tree produced by TrinoParser#positionalArgument.
    def enterPositionalArgument(self, ctx:TrinoParser.PositionalArgumentContext):
        pass

    # Exit a parse tree produced by TrinoParser#positionalArgument.
    def exitPositionalArgument(self, ctx:TrinoParser.PositionalArgumentContext):
        pass


    # Enter a parse tree produced by TrinoParser#namedArgument.
    def enterNamedArgument(self, ctx:TrinoParser.NamedArgumentContext):
        pass

    # Exit a parse tree produced by TrinoParser#namedArgument.
    def exitNamedArgument(self, ctx:TrinoParser.NamedArgumentContext):
        pass


    # Enter a parse tree produced by TrinoParser#qualifiedArgument.
    def enterQualifiedArgument(self, ctx:TrinoParser.QualifiedArgumentContext):
        pass

    # Exit a parse tree produced by TrinoParser#qualifiedArgument.
    def exitQualifiedArgument(self, ctx:TrinoParser.QualifiedArgumentContext):
        pass


    # Enter a parse tree produced by TrinoParser#unqualifiedArgument.
    def enterUnqualifiedArgument(self, ctx:TrinoParser.UnqualifiedArgumentContext):
        pass

    # Exit a parse tree produced by TrinoParser#unqualifiedArgument.
    def exitUnqualifiedArgument(self, ctx:TrinoParser.UnqualifiedArgumentContext):
        pass


    # Enter a parse tree produced by TrinoParser#pathSpecification.
    def enterPathSpecification(self, ctx:TrinoParser.PathSpecificationContext):
        pass

    # Exit a parse tree produced by TrinoParser#pathSpecification.
    def exitPathSpecification(self, ctx:TrinoParser.PathSpecificationContext):
        pass


    # Enter a parse tree produced by TrinoParser#functionSpecification.
    def enterFunctionSpecification(self, ctx:TrinoParser.FunctionSpecificationContext):
        pass

    # Exit a parse tree produced by TrinoParser#functionSpecification.
    def exitFunctionSpecification(self, ctx:TrinoParser.FunctionSpecificationContext):
        pass


    # Enter a parse tree produced by TrinoParser#functionDeclaration.
    def enterFunctionDeclaration(self, ctx:TrinoParser.FunctionDeclarationContext):
        pass

    # Exit a parse tree produced by TrinoParser#functionDeclaration.
    def exitFunctionDeclaration(self, ctx:TrinoParser.FunctionDeclarationContext):
        pass


    # Enter a parse tree produced by TrinoParser#parameterDeclaration.
    def enterParameterDeclaration(self, ctx:TrinoParser.ParameterDeclarationContext):
        pass

    # Exit a parse tree produced by TrinoParser#parameterDeclaration.
    def exitParameterDeclaration(self, ctx:TrinoParser.ParameterDeclarationContext):
        pass


    # Enter a parse tree produced by TrinoParser#returnsClause.
    def enterReturnsClause(self, ctx:TrinoParser.ReturnsClauseContext):
        pass

    # Exit a parse tree produced by TrinoParser#returnsClause.
    def exitReturnsClause(self, ctx:TrinoParser.ReturnsClauseContext):
        pass


    # Enter a parse tree produced by TrinoParser#languageCharacteristic.
    def enterLanguageCharacteristic(self, ctx:TrinoParser.LanguageCharacteristicContext):
        pass

    # Exit a parse tree produced by TrinoParser#languageCharacteristic.
    def exitLanguageCharacteristic(self, ctx:TrinoParser.LanguageCharacteristicContext):
        pass


    # Enter a parse tree produced by TrinoParser#deterministicCharacteristic.
    def enterDeterministicCharacteristic(self, ctx:TrinoParser.DeterministicCharacteristicContext):
        pass

    # Exit a parse tree produced by TrinoParser#deterministicCharacteristic.
    def exitDeterministicCharacteristic(self, ctx:TrinoParser.DeterministicCharacteristicContext):
        pass


    # Enter a parse tree produced by TrinoParser#returnsNullOnNullInputCharacteristic.
    def enterReturnsNullOnNullInputCharacteristic(self, ctx:TrinoParser.ReturnsNullOnNullInputCharacteristicContext):
        pass

    # Exit a parse tree produced by TrinoParser#returnsNullOnNullInputCharacteristic.
    def exitReturnsNullOnNullInputCharacteristic(self, ctx:TrinoParser.ReturnsNullOnNullInputCharacteristicContext):
        pass


    # Enter a parse tree produced by TrinoParser#calledOnNullInputCharacteristic.
    def enterCalledOnNullInputCharacteristic(self, ctx:TrinoParser.CalledOnNullInputCharacteristicContext):
        pass

    # Exit a parse tree produced by TrinoParser#calledOnNullInputCharacteristic.
    def exitCalledOnNullInputCharacteristic(self, ctx:TrinoParser.CalledOnNullInputCharacteristicContext):
        pass


    # Enter a parse tree produced by TrinoParser#securityCharacteristic.
    def enterSecurityCharacteristic(self, ctx:TrinoParser.SecurityCharacteristicContext):
        pass

    # Exit a parse tree produced by TrinoParser#securityCharacteristic.
    def exitSecurityCharacteristic(self, ctx:TrinoParser.SecurityCharacteristicContext):
        pass


    # Enter a parse tree produced by TrinoParser#commentCharacteristic.
    def enterCommentCharacteristic(self, ctx:TrinoParser.CommentCharacteristicContext):
        pass

    # Exit a parse tree produced by TrinoParser#commentCharacteristic.
    def exitCommentCharacteristic(self, ctx:TrinoParser.CommentCharacteristicContext):
        pass


    # Enter a parse tree produced by TrinoParser#returnStatement.
    def enterReturnStatement(self, ctx:TrinoParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by TrinoParser#returnStatement.
    def exitReturnStatement(self, ctx:TrinoParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by TrinoParser#assignmentStatement.
    def enterAssignmentStatement(self, ctx:TrinoParser.AssignmentStatementContext):
        pass

    # Exit a parse tree produced by TrinoParser#assignmentStatement.
    def exitAssignmentStatement(self, ctx:TrinoParser.AssignmentStatementContext):
        pass


    # Enter a parse tree produced by TrinoParser#simpleCaseStatement.
    def enterSimpleCaseStatement(self, ctx:TrinoParser.SimpleCaseStatementContext):
        pass

    # Exit a parse tree produced by TrinoParser#simpleCaseStatement.
    def exitSimpleCaseStatement(self, ctx:TrinoParser.SimpleCaseStatementContext):
        pass


    # Enter a parse tree produced by TrinoParser#searchedCaseStatement.
    def enterSearchedCaseStatement(self, ctx:TrinoParser.SearchedCaseStatementContext):
        pass

    # Exit a parse tree produced by TrinoParser#searchedCaseStatement.
    def exitSearchedCaseStatement(self, ctx:TrinoParser.SearchedCaseStatementContext):
        pass


    # Enter a parse tree produced by TrinoParser#ifStatement.
    def enterIfStatement(self, ctx:TrinoParser.IfStatementContext):
        pass

    # Exit a parse tree produced by TrinoParser#ifStatement.
    def exitIfStatement(self, ctx:TrinoParser.IfStatementContext):
        pass


    # Enter a parse tree produced by TrinoParser#iterateStatement.
    def enterIterateStatement(self, ctx:TrinoParser.IterateStatementContext):
        pass

    # Exit a parse tree produced by TrinoParser#iterateStatement.
    def exitIterateStatement(self, ctx:TrinoParser.IterateStatementContext):
        pass


    # Enter a parse tree produced by TrinoParser#leaveStatement.
    def enterLeaveStatement(self, ctx:TrinoParser.LeaveStatementContext):
        pass

    # Exit a parse tree produced by TrinoParser#leaveStatement.
    def exitLeaveStatement(self, ctx:TrinoParser.LeaveStatementContext):
        pass


    # Enter a parse tree produced by TrinoParser#compoundStatement.
    def enterCompoundStatement(self, ctx:TrinoParser.CompoundStatementContext):
        pass

    # Exit a parse tree produced by TrinoParser#compoundStatement.
    def exitCompoundStatement(self, ctx:TrinoParser.CompoundStatementContext):
        pass


    # Enter a parse tree produced by TrinoParser#loopStatement.
    def enterLoopStatement(self, ctx:TrinoParser.LoopStatementContext):
        pass

    # Exit a parse tree produced by TrinoParser#loopStatement.
    def exitLoopStatement(self, ctx:TrinoParser.LoopStatementContext):
        pass


    # Enter a parse tree produced by TrinoParser#whileStatement.
    def enterWhileStatement(self, ctx:TrinoParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by TrinoParser#whileStatement.
    def exitWhileStatement(self, ctx:TrinoParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by TrinoParser#repeatStatement.
    def enterRepeatStatement(self, ctx:TrinoParser.RepeatStatementContext):
        pass

    # Exit a parse tree produced by TrinoParser#repeatStatement.
    def exitRepeatStatement(self, ctx:TrinoParser.RepeatStatementContext):
        pass


    # Enter a parse tree produced by TrinoParser#caseStatementWhenClause.
    def enterCaseStatementWhenClause(self, ctx:TrinoParser.CaseStatementWhenClauseContext):
        pass

    # Exit a parse tree produced by TrinoParser#caseStatementWhenClause.
    def exitCaseStatementWhenClause(self, ctx:TrinoParser.CaseStatementWhenClauseContext):
        pass


    # Enter a parse tree produced by TrinoParser#elseIfClause.
    def enterElseIfClause(self, ctx:TrinoParser.ElseIfClauseContext):
        pass

    # Exit a parse tree produced by TrinoParser#elseIfClause.
    def exitElseIfClause(self, ctx:TrinoParser.ElseIfClauseContext):
        pass


    # Enter a parse tree produced by TrinoParser#elseClause.
    def enterElseClause(self, ctx:TrinoParser.ElseClauseContext):
        pass

    # Exit a parse tree produced by TrinoParser#elseClause.
    def exitElseClause(self, ctx:TrinoParser.ElseClauseContext):
        pass


    # Enter a parse tree produced by TrinoParser#variableDeclaration.
    def enterVariableDeclaration(self, ctx:TrinoParser.VariableDeclarationContext):
        pass

    # Exit a parse tree produced by TrinoParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx:TrinoParser.VariableDeclarationContext):
        pass


    # Enter a parse tree produced by TrinoParser#sqlStatementList.
    def enterSqlStatementList(self, ctx:TrinoParser.SqlStatementListContext):
        pass

    # Exit a parse tree produced by TrinoParser#sqlStatementList.
    def exitSqlStatementList(self, ctx:TrinoParser.SqlStatementListContext):
        pass


    # Enter a parse tree produced by TrinoParser#privilege.
    def enterPrivilege(self, ctx:TrinoParser.PrivilegeContext):
        pass

    # Exit a parse tree produced by TrinoParser#privilege.
    def exitPrivilege(self, ctx:TrinoParser.PrivilegeContext):
        pass


    # Enter a parse tree produced by TrinoParser#qualifiedName.
    def enterQualifiedName(self, ctx:TrinoParser.QualifiedNameContext):
        pass

    # Exit a parse tree produced by TrinoParser#qualifiedName.
    def exitQualifiedName(self, ctx:TrinoParser.QualifiedNameContext):
        pass


    # Enter a parse tree produced by TrinoParser#queryPeriod.
    def enterQueryPeriod(self, ctx:TrinoParser.QueryPeriodContext):
        pass

    # Exit a parse tree produced by TrinoParser#queryPeriod.
    def exitQueryPeriod(self, ctx:TrinoParser.QueryPeriodContext):
        pass


    # Enter a parse tree produced by TrinoParser#rangeType.
    def enterRangeType(self, ctx:TrinoParser.RangeTypeContext):
        pass

    # Exit a parse tree produced by TrinoParser#rangeType.
    def exitRangeType(self, ctx:TrinoParser.RangeTypeContext):
        pass


    # Enter a parse tree produced by TrinoParser#specifiedPrincipal.
    def enterSpecifiedPrincipal(self, ctx:TrinoParser.SpecifiedPrincipalContext):
        pass

    # Exit a parse tree produced by TrinoParser#specifiedPrincipal.
    def exitSpecifiedPrincipal(self, ctx:TrinoParser.SpecifiedPrincipalContext):
        pass


    # Enter a parse tree produced by TrinoParser#currentUserGrantor.
    def enterCurrentUserGrantor(self, ctx:TrinoParser.CurrentUserGrantorContext):
        pass

    # Exit a parse tree produced by TrinoParser#currentUserGrantor.
    def exitCurrentUserGrantor(self, ctx:TrinoParser.CurrentUserGrantorContext):
        pass


    # Enter a parse tree produced by TrinoParser#currentRoleGrantor.
    def enterCurrentRoleGrantor(self, ctx:TrinoParser.CurrentRoleGrantorContext):
        pass

    # Exit a parse tree produced by TrinoParser#currentRoleGrantor.
    def exitCurrentRoleGrantor(self, ctx:TrinoParser.CurrentRoleGrantorContext):
        pass


    # Enter a parse tree produced by TrinoParser#unspecifiedPrincipal.
    def enterUnspecifiedPrincipal(self, ctx:TrinoParser.UnspecifiedPrincipalContext):
        pass

    # Exit a parse tree produced by TrinoParser#unspecifiedPrincipal.
    def exitUnspecifiedPrincipal(self, ctx:TrinoParser.UnspecifiedPrincipalContext):
        pass


    # Enter a parse tree produced by TrinoParser#userPrincipal.
    def enterUserPrincipal(self, ctx:TrinoParser.UserPrincipalContext):
        pass

    # Exit a parse tree produced by TrinoParser#userPrincipal.
    def exitUserPrincipal(self, ctx:TrinoParser.UserPrincipalContext):
        pass


    # Enter a parse tree produced by TrinoParser#rolePrincipal.
    def enterRolePrincipal(self, ctx:TrinoParser.RolePrincipalContext):
        pass

    # Exit a parse tree produced by TrinoParser#rolePrincipal.
    def exitRolePrincipal(self, ctx:TrinoParser.RolePrincipalContext):
        pass


    # Enter a parse tree produced by TrinoParser#roles.
    def enterRoles(self, ctx:TrinoParser.RolesContext):
        pass

    # Exit a parse tree produced by TrinoParser#roles.
    def exitRoles(self, ctx:TrinoParser.RolesContext):
        pass


    # Enter a parse tree produced by TrinoParser#unquotedIdentifier.
    def enterUnquotedIdentifier(self, ctx:TrinoParser.UnquotedIdentifierContext):
        pass

    # Exit a parse tree produced by TrinoParser#unquotedIdentifier.
    def exitUnquotedIdentifier(self, ctx:TrinoParser.UnquotedIdentifierContext):
        pass


    # Enter a parse tree produced by TrinoParser#quotedIdentifier.
    def enterQuotedIdentifier(self, ctx:TrinoParser.QuotedIdentifierContext):
        pass

    # Exit a parse tree produced by TrinoParser#quotedIdentifier.
    def exitQuotedIdentifier(self, ctx:TrinoParser.QuotedIdentifierContext):
        pass


    # Enter a parse tree produced by TrinoParser#backQuotedIdentifier.
    def enterBackQuotedIdentifier(self, ctx:TrinoParser.BackQuotedIdentifierContext):
        pass

    # Exit a parse tree produced by TrinoParser#backQuotedIdentifier.
    def exitBackQuotedIdentifier(self, ctx:TrinoParser.BackQuotedIdentifierContext):
        pass


    # Enter a parse tree produced by TrinoParser#digitIdentifier.
    def enterDigitIdentifier(self, ctx:TrinoParser.DigitIdentifierContext):
        pass

    # Exit a parse tree produced by TrinoParser#digitIdentifier.
    def exitDigitIdentifier(self, ctx:TrinoParser.DigitIdentifierContext):
        pass


    # Enter a parse tree produced by TrinoParser#decimalLiteral.
    def enterDecimalLiteral(self, ctx:TrinoParser.DecimalLiteralContext):
        pass

    # Exit a parse tree produced by TrinoParser#decimalLiteral.
    def exitDecimalLiteral(self, ctx:TrinoParser.DecimalLiteralContext):
        pass


    # Enter a parse tree produced by TrinoParser#doubleLiteral.
    def enterDoubleLiteral(self, ctx:TrinoParser.DoubleLiteralContext):
        pass

    # Exit a parse tree produced by TrinoParser#doubleLiteral.
    def exitDoubleLiteral(self, ctx:TrinoParser.DoubleLiteralContext):
        pass


    # Enter a parse tree produced by TrinoParser#integerLiteral.
    def enterIntegerLiteral(self, ctx:TrinoParser.IntegerLiteralContext):
        pass

    # Exit a parse tree produced by TrinoParser#integerLiteral.
    def exitIntegerLiteral(self, ctx:TrinoParser.IntegerLiteralContext):
        pass


    # Enter a parse tree produced by TrinoParser#identifierUser.
    def enterIdentifierUser(self, ctx:TrinoParser.IdentifierUserContext):
        pass

    # Exit a parse tree produced by TrinoParser#identifierUser.
    def exitIdentifierUser(self, ctx:TrinoParser.IdentifierUserContext):
        pass


    # Enter a parse tree produced by TrinoParser#stringUser.
    def enterStringUser(self, ctx:TrinoParser.StringUserContext):
        pass

    # Exit a parse tree produced by TrinoParser#stringUser.
    def exitStringUser(self, ctx:TrinoParser.StringUserContext):
        pass


    # Enter a parse tree produced by TrinoParser#nonReserved.
    def enterNonReserved(self, ctx:TrinoParser.NonReservedContext):
        pass

    # Exit a parse tree produced by TrinoParser#nonReserved.
    def exitNonReserved(self, ctx:TrinoParser.NonReservedContext):
        pass



del TrinoParser