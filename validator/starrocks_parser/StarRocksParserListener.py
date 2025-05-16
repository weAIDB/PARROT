# Generated from sql/starrocks/StarRocksParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .StarRocksParser import StarRocksParser
else:
    from StarRocksParser import StarRocksParser

# This class defines a complete listener for a parse tree produced by StarRocksParser.
class StarRocksParserListener(ParseTreeListener):

    # Enter a parse tree produced by StarRocksParser#sqlStatements.
    def enterSqlStatements(self, ctx:StarRocksParser.SqlStatementsContext):
        pass

    # Exit a parse tree produced by StarRocksParser#sqlStatements.
    def exitSqlStatements(self, ctx:StarRocksParser.SqlStatementsContext):
        pass


    # Enter a parse tree produced by StarRocksParser#singleStatement.
    def enterSingleStatement(self, ctx:StarRocksParser.SingleStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#singleStatement.
    def exitSingleStatement(self, ctx:StarRocksParser.SingleStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#emptyStatement.
    def enterEmptyStatement(self, ctx:StarRocksParser.EmptyStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#emptyStatement.
    def exitEmptyStatement(self, ctx:StarRocksParser.EmptyStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#statement.
    def enterStatement(self, ctx:StarRocksParser.StatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#statement.
    def exitStatement(self, ctx:StarRocksParser.StatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#useDatabaseStatement.
    def enterUseDatabaseStatement(self, ctx:StarRocksParser.UseDatabaseStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#useDatabaseStatement.
    def exitUseDatabaseStatement(self, ctx:StarRocksParser.UseDatabaseStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#useCatalogStatement.
    def enterUseCatalogStatement(self, ctx:StarRocksParser.UseCatalogStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#useCatalogStatement.
    def exitUseCatalogStatement(self, ctx:StarRocksParser.UseCatalogStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#setCatalogStatement.
    def enterSetCatalogStatement(self, ctx:StarRocksParser.SetCatalogStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#setCatalogStatement.
    def exitSetCatalogStatement(self, ctx:StarRocksParser.SetCatalogStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#showDatabasesStatement.
    def enterShowDatabasesStatement(self, ctx:StarRocksParser.ShowDatabasesStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#showDatabasesStatement.
    def exitShowDatabasesStatement(self, ctx:StarRocksParser.ShowDatabasesStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#alterDbQuotaStatement.
    def enterAlterDbQuotaStatement(self, ctx:StarRocksParser.AlterDbQuotaStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#alterDbQuotaStatement.
    def exitAlterDbQuotaStatement(self, ctx:StarRocksParser.AlterDbQuotaStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#createDbStatement.
    def enterCreateDbStatement(self, ctx:StarRocksParser.CreateDbStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#createDbStatement.
    def exitCreateDbStatement(self, ctx:StarRocksParser.CreateDbStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#dropDbStatement.
    def enterDropDbStatement(self, ctx:StarRocksParser.DropDbStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#dropDbStatement.
    def exitDropDbStatement(self, ctx:StarRocksParser.DropDbStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#showCreateDbStatement.
    def enterShowCreateDbStatement(self, ctx:StarRocksParser.ShowCreateDbStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#showCreateDbStatement.
    def exitShowCreateDbStatement(self, ctx:StarRocksParser.ShowCreateDbStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#alterDatabaseRenameStatement.
    def enterAlterDatabaseRenameStatement(self, ctx:StarRocksParser.AlterDatabaseRenameStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#alterDatabaseRenameStatement.
    def exitAlterDatabaseRenameStatement(self, ctx:StarRocksParser.AlterDatabaseRenameStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#recoverDbStmt.
    def enterRecoverDbStmt(self, ctx:StarRocksParser.RecoverDbStmtContext):
        pass

    # Exit a parse tree produced by StarRocksParser#recoverDbStmt.
    def exitRecoverDbStmt(self, ctx:StarRocksParser.RecoverDbStmtContext):
        pass


    # Enter a parse tree produced by StarRocksParser#showDataStmt.
    def enterShowDataStmt(self, ctx:StarRocksParser.ShowDataStmtContext):
        pass

    # Exit a parse tree produced by StarRocksParser#showDataStmt.
    def exitShowDataStmt(self, ctx:StarRocksParser.ShowDataStmtContext):
        pass


    # Enter a parse tree produced by StarRocksParser#createTableStatement.
    def enterCreateTableStatement(self, ctx:StarRocksParser.CreateTableStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#createTableStatement.
    def exitCreateTableStatement(self, ctx:StarRocksParser.CreateTableStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#columnDesc.
    def enterColumnDesc(self, ctx:StarRocksParser.ColumnDescContext):
        pass

    # Exit a parse tree produced by StarRocksParser#columnDesc.
    def exitColumnDesc(self, ctx:StarRocksParser.ColumnDescContext):
        pass


    # Enter a parse tree produced by StarRocksParser#charsetName.
    def enterCharsetName(self, ctx:StarRocksParser.CharsetNameContext):
        pass

    # Exit a parse tree produced by StarRocksParser#charsetName.
    def exitCharsetName(self, ctx:StarRocksParser.CharsetNameContext):
        pass


    # Enter a parse tree produced by StarRocksParser#defaultDesc.
    def enterDefaultDesc(self, ctx:StarRocksParser.DefaultDescContext):
        pass

    # Exit a parse tree produced by StarRocksParser#defaultDesc.
    def exitDefaultDesc(self, ctx:StarRocksParser.DefaultDescContext):
        pass


    # Enter a parse tree produced by StarRocksParser#generatedColumnDesc.
    def enterGeneratedColumnDesc(self, ctx:StarRocksParser.GeneratedColumnDescContext):
        pass

    # Exit a parse tree produced by StarRocksParser#generatedColumnDesc.
    def exitGeneratedColumnDesc(self, ctx:StarRocksParser.GeneratedColumnDescContext):
        pass


    # Enter a parse tree produced by StarRocksParser#indexDesc.
    def enterIndexDesc(self, ctx:StarRocksParser.IndexDescContext):
        pass

    # Exit a parse tree produced by StarRocksParser#indexDesc.
    def exitIndexDesc(self, ctx:StarRocksParser.IndexDescContext):
        pass


    # Enter a parse tree produced by StarRocksParser#engineDesc.
    def enterEngineDesc(self, ctx:StarRocksParser.EngineDescContext):
        pass

    # Exit a parse tree produced by StarRocksParser#engineDesc.
    def exitEngineDesc(self, ctx:StarRocksParser.EngineDescContext):
        pass


    # Enter a parse tree produced by StarRocksParser#charsetDesc.
    def enterCharsetDesc(self, ctx:StarRocksParser.CharsetDescContext):
        pass

    # Exit a parse tree produced by StarRocksParser#charsetDesc.
    def exitCharsetDesc(self, ctx:StarRocksParser.CharsetDescContext):
        pass


    # Enter a parse tree produced by StarRocksParser#collateDesc.
    def enterCollateDesc(self, ctx:StarRocksParser.CollateDescContext):
        pass

    # Exit a parse tree produced by StarRocksParser#collateDesc.
    def exitCollateDesc(self, ctx:StarRocksParser.CollateDescContext):
        pass


    # Enter a parse tree produced by StarRocksParser#keyDesc.
    def enterKeyDesc(self, ctx:StarRocksParser.KeyDescContext):
        pass

    # Exit a parse tree produced by StarRocksParser#keyDesc.
    def exitKeyDesc(self, ctx:StarRocksParser.KeyDescContext):
        pass


    # Enter a parse tree produced by StarRocksParser#orderByDesc.
    def enterOrderByDesc(self, ctx:StarRocksParser.OrderByDescContext):
        pass

    # Exit a parse tree produced by StarRocksParser#orderByDesc.
    def exitOrderByDesc(self, ctx:StarRocksParser.OrderByDescContext):
        pass


    # Enter a parse tree produced by StarRocksParser#aggDesc.
    def enterAggDesc(self, ctx:StarRocksParser.AggDescContext):
        pass

    # Exit a parse tree produced by StarRocksParser#aggDesc.
    def exitAggDesc(self, ctx:StarRocksParser.AggDescContext):
        pass


    # Enter a parse tree produced by StarRocksParser#rollupDesc.
    def enterRollupDesc(self, ctx:StarRocksParser.RollupDescContext):
        pass

    # Exit a parse tree produced by StarRocksParser#rollupDesc.
    def exitRollupDesc(self, ctx:StarRocksParser.RollupDescContext):
        pass


    # Enter a parse tree produced by StarRocksParser#rollupItem.
    def enterRollupItem(self, ctx:StarRocksParser.RollupItemContext):
        pass

    # Exit a parse tree produced by StarRocksParser#rollupItem.
    def exitRollupItem(self, ctx:StarRocksParser.RollupItemContext):
        pass


    # Enter a parse tree produced by StarRocksParser#dupKeys.
    def enterDupKeys(self, ctx:StarRocksParser.DupKeysContext):
        pass

    # Exit a parse tree produced by StarRocksParser#dupKeys.
    def exitDupKeys(self, ctx:StarRocksParser.DupKeysContext):
        pass


    # Enter a parse tree produced by StarRocksParser#fromRollup.
    def enterFromRollup(self, ctx:StarRocksParser.FromRollupContext):
        pass

    # Exit a parse tree produced by StarRocksParser#fromRollup.
    def exitFromRollup(self, ctx:StarRocksParser.FromRollupContext):
        pass


    # Enter a parse tree produced by StarRocksParser#orReplace.
    def enterOrReplace(self, ctx:StarRocksParser.OrReplaceContext):
        pass

    # Exit a parse tree produced by StarRocksParser#orReplace.
    def exitOrReplace(self, ctx:StarRocksParser.OrReplaceContext):
        pass


    # Enter a parse tree produced by StarRocksParser#ifNotExists.
    def enterIfNotExists(self, ctx:StarRocksParser.IfNotExistsContext):
        pass

    # Exit a parse tree produced by StarRocksParser#ifNotExists.
    def exitIfNotExists(self, ctx:StarRocksParser.IfNotExistsContext):
        pass


    # Enter a parse tree produced by StarRocksParser#createTableAsSelectStatement.
    def enterCreateTableAsSelectStatement(self, ctx:StarRocksParser.CreateTableAsSelectStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#createTableAsSelectStatement.
    def exitCreateTableAsSelectStatement(self, ctx:StarRocksParser.CreateTableAsSelectStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#dropTableStatement.
    def enterDropTableStatement(self, ctx:StarRocksParser.DropTableStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#dropTableStatement.
    def exitDropTableStatement(self, ctx:StarRocksParser.DropTableStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#cleanTemporaryTableStatement.
    def enterCleanTemporaryTableStatement(self, ctx:StarRocksParser.CleanTemporaryTableStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#cleanTemporaryTableStatement.
    def exitCleanTemporaryTableStatement(self, ctx:StarRocksParser.CleanTemporaryTableStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#alterTableStatement.
    def enterAlterTableStatement(self, ctx:StarRocksParser.AlterTableStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#alterTableStatement.
    def exitAlterTableStatement(self, ctx:StarRocksParser.AlterTableStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#createIndexStatement.
    def enterCreateIndexStatement(self, ctx:StarRocksParser.CreateIndexStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#createIndexStatement.
    def exitCreateIndexStatement(self, ctx:StarRocksParser.CreateIndexStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#dropIndexStatement.
    def enterDropIndexStatement(self, ctx:StarRocksParser.DropIndexStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#dropIndexStatement.
    def exitDropIndexStatement(self, ctx:StarRocksParser.DropIndexStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#indexType.
    def enterIndexType(self, ctx:StarRocksParser.IndexTypeContext):
        pass

    # Exit a parse tree produced by StarRocksParser#indexType.
    def exitIndexType(self, ctx:StarRocksParser.IndexTypeContext):
        pass


    # Enter a parse tree produced by StarRocksParser#showTableStatement.
    def enterShowTableStatement(self, ctx:StarRocksParser.ShowTableStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#showTableStatement.
    def exitShowTableStatement(self, ctx:StarRocksParser.ShowTableStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#showTemporaryTablesStatement.
    def enterShowTemporaryTablesStatement(self, ctx:StarRocksParser.ShowTemporaryTablesStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#showTemporaryTablesStatement.
    def exitShowTemporaryTablesStatement(self, ctx:StarRocksParser.ShowTemporaryTablesStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#showCreateTableStatement.
    def enterShowCreateTableStatement(self, ctx:StarRocksParser.ShowCreateTableStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#showCreateTableStatement.
    def exitShowCreateTableStatement(self, ctx:StarRocksParser.ShowCreateTableStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#showColumnStatement.
    def enterShowColumnStatement(self, ctx:StarRocksParser.ShowColumnStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#showColumnStatement.
    def exitShowColumnStatement(self, ctx:StarRocksParser.ShowColumnStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#showTableStatusStatement.
    def enterShowTableStatusStatement(self, ctx:StarRocksParser.ShowTableStatusStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#showTableStatusStatement.
    def exitShowTableStatusStatement(self, ctx:StarRocksParser.ShowTableStatusStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#refreshTableStatement.
    def enterRefreshTableStatement(self, ctx:StarRocksParser.RefreshTableStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#refreshTableStatement.
    def exitRefreshTableStatement(self, ctx:StarRocksParser.RefreshTableStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#showAlterStatement.
    def enterShowAlterStatement(self, ctx:StarRocksParser.ShowAlterStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#showAlterStatement.
    def exitShowAlterStatement(self, ctx:StarRocksParser.ShowAlterStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#descTableStatement.
    def enterDescTableStatement(self, ctx:StarRocksParser.DescTableStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#descTableStatement.
    def exitDescTableStatement(self, ctx:StarRocksParser.DescTableStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#createTableLikeStatement.
    def enterCreateTableLikeStatement(self, ctx:StarRocksParser.CreateTableLikeStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#createTableLikeStatement.
    def exitCreateTableLikeStatement(self, ctx:StarRocksParser.CreateTableLikeStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#showIndexStatement.
    def enterShowIndexStatement(self, ctx:StarRocksParser.ShowIndexStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#showIndexStatement.
    def exitShowIndexStatement(self, ctx:StarRocksParser.ShowIndexStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#recoverTableStatement.
    def enterRecoverTableStatement(self, ctx:StarRocksParser.RecoverTableStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#recoverTableStatement.
    def exitRecoverTableStatement(self, ctx:StarRocksParser.RecoverTableStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#truncateTableStatement.
    def enterTruncateTableStatement(self, ctx:StarRocksParser.TruncateTableStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#truncateTableStatement.
    def exitTruncateTableStatement(self, ctx:StarRocksParser.TruncateTableStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#cancelAlterTableStatement.
    def enterCancelAlterTableStatement(self, ctx:StarRocksParser.CancelAlterTableStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#cancelAlterTableStatement.
    def exitCancelAlterTableStatement(self, ctx:StarRocksParser.CancelAlterTableStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#showPartitionsStatement.
    def enterShowPartitionsStatement(self, ctx:StarRocksParser.ShowPartitionsStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#showPartitionsStatement.
    def exitShowPartitionsStatement(self, ctx:StarRocksParser.ShowPartitionsStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#recoverPartitionStatement.
    def enterRecoverPartitionStatement(self, ctx:StarRocksParser.RecoverPartitionStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#recoverPartitionStatement.
    def exitRecoverPartitionStatement(self, ctx:StarRocksParser.RecoverPartitionStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#createViewStatement.
    def enterCreateViewStatement(self, ctx:StarRocksParser.CreateViewStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#createViewStatement.
    def exitCreateViewStatement(self, ctx:StarRocksParser.CreateViewStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#alterViewStatement.
    def enterAlterViewStatement(self, ctx:StarRocksParser.AlterViewStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#alterViewStatement.
    def exitAlterViewStatement(self, ctx:StarRocksParser.AlterViewStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#dropViewStatement.
    def enterDropViewStatement(self, ctx:StarRocksParser.DropViewStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#dropViewStatement.
    def exitDropViewStatement(self, ctx:StarRocksParser.DropViewStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#columnNameWithComment.
    def enterColumnNameWithComment(self, ctx:StarRocksParser.ColumnNameWithCommentContext):
        pass

    # Exit a parse tree produced by StarRocksParser#columnNameWithComment.
    def exitColumnNameWithComment(self, ctx:StarRocksParser.ColumnNameWithCommentContext):
        pass


    # Enter a parse tree produced by StarRocksParser#submitTaskStatement.
    def enterSubmitTaskStatement(self, ctx:StarRocksParser.SubmitTaskStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#submitTaskStatement.
    def exitSubmitTaskStatement(self, ctx:StarRocksParser.SubmitTaskStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#taskClause.
    def enterTaskClause(self, ctx:StarRocksParser.TaskClauseContext):
        pass

    # Exit a parse tree produced by StarRocksParser#taskClause.
    def exitTaskClause(self, ctx:StarRocksParser.TaskClauseContext):
        pass


    # Enter a parse tree produced by StarRocksParser#dropTaskStatement.
    def enterDropTaskStatement(self, ctx:StarRocksParser.DropTaskStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#dropTaskStatement.
    def exitDropTaskStatement(self, ctx:StarRocksParser.DropTaskStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#taskScheduleDesc.
    def enterTaskScheduleDesc(self, ctx:StarRocksParser.TaskScheduleDescContext):
        pass

    # Exit a parse tree produced by StarRocksParser#taskScheduleDesc.
    def exitTaskScheduleDesc(self, ctx:StarRocksParser.TaskScheduleDescContext):
        pass


    # Enter a parse tree produced by StarRocksParser#createMaterializedViewStatement.
    def enterCreateMaterializedViewStatement(self, ctx:StarRocksParser.CreateMaterializedViewStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#createMaterializedViewStatement.
    def exitCreateMaterializedViewStatement(self, ctx:StarRocksParser.CreateMaterializedViewStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#materializedViewDesc.
    def enterMaterializedViewDesc(self, ctx:StarRocksParser.MaterializedViewDescContext):
        pass

    # Exit a parse tree produced by StarRocksParser#materializedViewDesc.
    def exitMaterializedViewDesc(self, ctx:StarRocksParser.MaterializedViewDescContext):
        pass


    # Enter a parse tree produced by StarRocksParser#showMaterializedViewsStatement.
    def enterShowMaterializedViewsStatement(self, ctx:StarRocksParser.ShowMaterializedViewsStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#showMaterializedViewsStatement.
    def exitShowMaterializedViewsStatement(self, ctx:StarRocksParser.ShowMaterializedViewsStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#dropMaterializedViewStatement.
    def enterDropMaterializedViewStatement(self, ctx:StarRocksParser.DropMaterializedViewStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#dropMaterializedViewStatement.
    def exitDropMaterializedViewStatement(self, ctx:StarRocksParser.DropMaterializedViewStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#alterMaterializedViewStatement.
    def enterAlterMaterializedViewStatement(self, ctx:StarRocksParser.AlterMaterializedViewStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#alterMaterializedViewStatement.
    def exitAlterMaterializedViewStatement(self, ctx:StarRocksParser.AlterMaterializedViewStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#refreshMaterializedViewStatement.
    def enterRefreshMaterializedViewStatement(self, ctx:StarRocksParser.RefreshMaterializedViewStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#refreshMaterializedViewStatement.
    def exitRefreshMaterializedViewStatement(self, ctx:StarRocksParser.RefreshMaterializedViewStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#cancelRefreshMaterializedViewStatement.
    def enterCancelRefreshMaterializedViewStatement(self, ctx:StarRocksParser.CancelRefreshMaterializedViewStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#cancelRefreshMaterializedViewStatement.
    def exitCancelRefreshMaterializedViewStatement(self, ctx:StarRocksParser.CancelRefreshMaterializedViewStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#adminSetConfigStatement.
    def enterAdminSetConfigStatement(self, ctx:StarRocksParser.AdminSetConfigStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#adminSetConfigStatement.
    def exitAdminSetConfigStatement(self, ctx:StarRocksParser.AdminSetConfigStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#adminSetReplicaStatusStatement.
    def enterAdminSetReplicaStatusStatement(self, ctx:StarRocksParser.AdminSetReplicaStatusStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#adminSetReplicaStatusStatement.
    def exitAdminSetReplicaStatusStatement(self, ctx:StarRocksParser.AdminSetReplicaStatusStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#adminShowConfigStatement.
    def enterAdminShowConfigStatement(self, ctx:StarRocksParser.AdminShowConfigStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#adminShowConfigStatement.
    def exitAdminShowConfigStatement(self, ctx:StarRocksParser.AdminShowConfigStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#adminShowReplicaDistributionStatement.
    def enterAdminShowReplicaDistributionStatement(self, ctx:StarRocksParser.AdminShowReplicaDistributionStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#adminShowReplicaDistributionStatement.
    def exitAdminShowReplicaDistributionStatement(self, ctx:StarRocksParser.AdminShowReplicaDistributionStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#adminShowReplicaStatusStatement.
    def enterAdminShowReplicaStatusStatement(self, ctx:StarRocksParser.AdminShowReplicaStatusStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#adminShowReplicaStatusStatement.
    def exitAdminShowReplicaStatusStatement(self, ctx:StarRocksParser.AdminShowReplicaStatusStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#adminRepairTableStatement.
    def enterAdminRepairTableStatement(self, ctx:StarRocksParser.AdminRepairTableStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#adminRepairTableStatement.
    def exitAdminRepairTableStatement(self, ctx:StarRocksParser.AdminRepairTableStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#adminCancelRepairTableStatement.
    def enterAdminCancelRepairTableStatement(self, ctx:StarRocksParser.AdminCancelRepairTableStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#adminCancelRepairTableStatement.
    def exitAdminCancelRepairTableStatement(self, ctx:StarRocksParser.AdminCancelRepairTableStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#adminCheckTabletsStatement.
    def enterAdminCheckTabletsStatement(self, ctx:StarRocksParser.AdminCheckTabletsStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#adminCheckTabletsStatement.
    def exitAdminCheckTabletsStatement(self, ctx:StarRocksParser.AdminCheckTabletsStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#adminSetPartitionVersion.
    def enterAdminSetPartitionVersion(self, ctx:StarRocksParser.AdminSetPartitionVersionContext):
        pass

    # Exit a parse tree produced by StarRocksParser#adminSetPartitionVersion.
    def exitAdminSetPartitionVersion(self, ctx:StarRocksParser.AdminSetPartitionVersionContext):
        pass


    # Enter a parse tree produced by StarRocksParser#killStatement.
    def enterKillStatement(self, ctx:StarRocksParser.KillStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#killStatement.
    def exitKillStatement(self, ctx:StarRocksParser.KillStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#syncStatement.
    def enterSyncStatement(self, ctx:StarRocksParser.SyncStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#syncStatement.
    def exitSyncStatement(self, ctx:StarRocksParser.SyncStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#alterSystemStatement.
    def enterAlterSystemStatement(self, ctx:StarRocksParser.AlterSystemStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#alterSystemStatement.
    def exitAlterSystemStatement(self, ctx:StarRocksParser.AlterSystemStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#cancelAlterSystemStatement.
    def enterCancelAlterSystemStatement(self, ctx:StarRocksParser.CancelAlterSystemStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#cancelAlterSystemStatement.
    def exitCancelAlterSystemStatement(self, ctx:StarRocksParser.CancelAlterSystemStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#showComputeNodesStatement.
    def enterShowComputeNodesStatement(self, ctx:StarRocksParser.ShowComputeNodesStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#showComputeNodesStatement.
    def exitShowComputeNodesStatement(self, ctx:StarRocksParser.ShowComputeNodesStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#createExternalCatalogStatement.
    def enterCreateExternalCatalogStatement(self, ctx:StarRocksParser.CreateExternalCatalogStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#createExternalCatalogStatement.
    def exitCreateExternalCatalogStatement(self, ctx:StarRocksParser.CreateExternalCatalogStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#showCreateExternalCatalogStatement.
    def enterShowCreateExternalCatalogStatement(self, ctx:StarRocksParser.ShowCreateExternalCatalogStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#showCreateExternalCatalogStatement.
    def exitShowCreateExternalCatalogStatement(self, ctx:StarRocksParser.ShowCreateExternalCatalogStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#dropExternalCatalogStatement.
    def enterDropExternalCatalogStatement(self, ctx:StarRocksParser.DropExternalCatalogStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#dropExternalCatalogStatement.
    def exitDropExternalCatalogStatement(self, ctx:StarRocksParser.DropExternalCatalogStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#showCatalogsStatement.
    def enterShowCatalogsStatement(self, ctx:StarRocksParser.ShowCatalogsStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#showCatalogsStatement.
    def exitShowCatalogsStatement(self, ctx:StarRocksParser.ShowCatalogsStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#alterCatalogStatement.
    def enterAlterCatalogStatement(self, ctx:StarRocksParser.AlterCatalogStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#alterCatalogStatement.
    def exitAlterCatalogStatement(self, ctx:StarRocksParser.AlterCatalogStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#createStorageVolumeStatement.
    def enterCreateStorageVolumeStatement(self, ctx:StarRocksParser.CreateStorageVolumeStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#createStorageVolumeStatement.
    def exitCreateStorageVolumeStatement(self, ctx:StarRocksParser.CreateStorageVolumeStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#typeDesc.
    def enterTypeDesc(self, ctx:StarRocksParser.TypeDescContext):
        pass

    # Exit a parse tree produced by StarRocksParser#typeDesc.
    def exitTypeDesc(self, ctx:StarRocksParser.TypeDescContext):
        pass


    # Enter a parse tree produced by StarRocksParser#locationsDesc.
    def enterLocationsDesc(self, ctx:StarRocksParser.LocationsDescContext):
        pass

    # Exit a parse tree produced by StarRocksParser#locationsDesc.
    def exitLocationsDesc(self, ctx:StarRocksParser.LocationsDescContext):
        pass


    # Enter a parse tree produced by StarRocksParser#showStorageVolumesStatement.
    def enterShowStorageVolumesStatement(self, ctx:StarRocksParser.ShowStorageVolumesStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#showStorageVolumesStatement.
    def exitShowStorageVolumesStatement(self, ctx:StarRocksParser.ShowStorageVolumesStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#dropStorageVolumeStatement.
    def enterDropStorageVolumeStatement(self, ctx:StarRocksParser.DropStorageVolumeStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#dropStorageVolumeStatement.
    def exitDropStorageVolumeStatement(self, ctx:StarRocksParser.DropStorageVolumeStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#alterStorageVolumeStatement.
    def enterAlterStorageVolumeStatement(self, ctx:StarRocksParser.AlterStorageVolumeStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#alterStorageVolumeStatement.
    def exitAlterStorageVolumeStatement(self, ctx:StarRocksParser.AlterStorageVolumeStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#alterStorageVolumeClause.
    def enterAlterStorageVolumeClause(self, ctx:StarRocksParser.AlterStorageVolumeClauseContext):
        pass

    # Exit a parse tree produced by StarRocksParser#alterStorageVolumeClause.
    def exitAlterStorageVolumeClause(self, ctx:StarRocksParser.AlterStorageVolumeClauseContext):
        pass


    # Enter a parse tree produced by StarRocksParser#modifyStorageVolumePropertiesClause.
    def enterModifyStorageVolumePropertiesClause(self, ctx:StarRocksParser.ModifyStorageVolumePropertiesClauseContext):
        pass

    # Exit a parse tree produced by StarRocksParser#modifyStorageVolumePropertiesClause.
    def exitModifyStorageVolumePropertiesClause(self, ctx:StarRocksParser.ModifyStorageVolumePropertiesClauseContext):
        pass


    # Enter a parse tree produced by StarRocksParser#modifyStorageVolumeCommentClause.
    def enterModifyStorageVolumeCommentClause(self, ctx:StarRocksParser.ModifyStorageVolumeCommentClauseContext):
        pass

    # Exit a parse tree produced by StarRocksParser#modifyStorageVolumeCommentClause.
    def exitModifyStorageVolumeCommentClause(self, ctx:StarRocksParser.ModifyStorageVolumeCommentClauseContext):
        pass


    # Enter a parse tree produced by StarRocksParser#descStorageVolumeStatement.
    def enterDescStorageVolumeStatement(self, ctx:StarRocksParser.DescStorageVolumeStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#descStorageVolumeStatement.
    def exitDescStorageVolumeStatement(self, ctx:StarRocksParser.DescStorageVolumeStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#setDefaultStorageVolumeStatement.
    def enterSetDefaultStorageVolumeStatement(self, ctx:StarRocksParser.SetDefaultStorageVolumeStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#setDefaultStorageVolumeStatement.
    def exitSetDefaultStorageVolumeStatement(self, ctx:StarRocksParser.SetDefaultStorageVolumeStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#updateFailPointStatusStatement.
    def enterUpdateFailPointStatusStatement(self, ctx:StarRocksParser.UpdateFailPointStatusStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#updateFailPointStatusStatement.
    def exitUpdateFailPointStatusStatement(self, ctx:StarRocksParser.UpdateFailPointStatusStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#showFailPointStatement.
    def enterShowFailPointStatement(self, ctx:StarRocksParser.ShowFailPointStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#showFailPointStatement.
    def exitShowFailPointStatement(self, ctx:StarRocksParser.ShowFailPointStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#createDictionaryStatement.
    def enterCreateDictionaryStatement(self, ctx:StarRocksParser.CreateDictionaryStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#createDictionaryStatement.
    def exitCreateDictionaryStatement(self, ctx:StarRocksParser.CreateDictionaryStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#dropDictionaryStatement.
    def enterDropDictionaryStatement(self, ctx:StarRocksParser.DropDictionaryStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#dropDictionaryStatement.
    def exitDropDictionaryStatement(self, ctx:StarRocksParser.DropDictionaryStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#refreshDictionaryStatement.
    def enterRefreshDictionaryStatement(self, ctx:StarRocksParser.RefreshDictionaryStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#refreshDictionaryStatement.
    def exitRefreshDictionaryStatement(self, ctx:StarRocksParser.RefreshDictionaryStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#showDictionaryStatement.
    def enterShowDictionaryStatement(self, ctx:StarRocksParser.ShowDictionaryStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#showDictionaryStatement.
    def exitShowDictionaryStatement(self, ctx:StarRocksParser.ShowDictionaryStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#cancelRefreshDictionaryStatement.
    def enterCancelRefreshDictionaryStatement(self, ctx:StarRocksParser.CancelRefreshDictionaryStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#cancelRefreshDictionaryStatement.
    def exitCancelRefreshDictionaryStatement(self, ctx:StarRocksParser.CancelRefreshDictionaryStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#dictionaryColumnDesc.
    def enterDictionaryColumnDesc(self, ctx:StarRocksParser.DictionaryColumnDescContext):
        pass

    # Exit a parse tree produced by StarRocksParser#dictionaryColumnDesc.
    def exitDictionaryColumnDesc(self, ctx:StarRocksParser.DictionaryColumnDescContext):
        pass


    # Enter a parse tree produced by StarRocksParser#dictionaryName.
    def enterDictionaryName(self, ctx:StarRocksParser.DictionaryNameContext):
        pass

    # Exit a parse tree produced by StarRocksParser#dictionaryName.
    def exitDictionaryName(self, ctx:StarRocksParser.DictionaryNameContext):
        pass


    # Enter a parse tree produced by StarRocksParser#alterClause.
    def enterAlterClause(self, ctx:StarRocksParser.AlterClauseContext):
        pass

    # Exit a parse tree produced by StarRocksParser#alterClause.
    def exitAlterClause(self, ctx:StarRocksParser.AlterClauseContext):
        pass


    # Enter a parse tree produced by StarRocksParser#addFrontendClause.
    def enterAddFrontendClause(self, ctx:StarRocksParser.AddFrontendClauseContext):
        pass

    # Exit a parse tree produced by StarRocksParser#addFrontendClause.
    def exitAddFrontendClause(self, ctx:StarRocksParser.AddFrontendClauseContext):
        pass


    # Enter a parse tree produced by StarRocksParser#dropFrontendClause.
    def enterDropFrontendClause(self, ctx:StarRocksParser.DropFrontendClauseContext):
        pass

    # Exit a parse tree produced by StarRocksParser#dropFrontendClause.
    def exitDropFrontendClause(self, ctx:StarRocksParser.DropFrontendClauseContext):
        pass


    # Enter a parse tree produced by StarRocksParser#modifyFrontendHostClause.
    def enterModifyFrontendHostClause(self, ctx:StarRocksParser.ModifyFrontendHostClauseContext):
        pass

    # Exit a parse tree produced by StarRocksParser#modifyFrontendHostClause.
    def exitModifyFrontendHostClause(self, ctx:StarRocksParser.ModifyFrontendHostClauseContext):
        pass


    # Enter a parse tree produced by StarRocksParser#addBackendClause.
    def enterAddBackendClause(self, ctx:StarRocksParser.AddBackendClauseContext):
        pass

    # Exit a parse tree produced by StarRocksParser#addBackendClause.
    def exitAddBackendClause(self, ctx:StarRocksParser.AddBackendClauseContext):
        pass


    # Enter a parse tree produced by StarRocksParser#dropBackendClause.
    def enterDropBackendClause(self, ctx:StarRocksParser.DropBackendClauseContext):
        pass

    # Exit a parse tree produced by StarRocksParser#dropBackendClause.
    def exitDropBackendClause(self, ctx:StarRocksParser.DropBackendClauseContext):
        pass


    # Enter a parse tree produced by StarRocksParser#decommissionBackendClause.
    def enterDecommissionBackendClause(self, ctx:StarRocksParser.DecommissionBackendClauseContext):
        pass

    # Exit a parse tree produced by StarRocksParser#decommissionBackendClause.
    def exitDecommissionBackendClause(self, ctx:StarRocksParser.DecommissionBackendClauseContext):
        pass


    # Enter a parse tree produced by StarRocksParser#modifyBackendClause.
    def enterModifyBackendClause(self, ctx:StarRocksParser.ModifyBackendClauseContext):
        pass

    # Exit a parse tree produced by StarRocksParser#modifyBackendClause.
    def exitModifyBackendClause(self, ctx:StarRocksParser.ModifyBackendClauseContext):
        pass


    # Enter a parse tree produced by StarRocksParser#addComputeNodeClause.
    def enterAddComputeNodeClause(self, ctx:StarRocksParser.AddComputeNodeClauseContext):
        pass

    # Exit a parse tree produced by StarRocksParser#addComputeNodeClause.
    def exitAddComputeNodeClause(self, ctx:StarRocksParser.AddComputeNodeClauseContext):
        pass


    # Enter a parse tree produced by StarRocksParser#dropComputeNodeClause.
    def enterDropComputeNodeClause(self, ctx:StarRocksParser.DropComputeNodeClauseContext):
        pass

    # Exit a parse tree produced by StarRocksParser#dropComputeNodeClause.
    def exitDropComputeNodeClause(self, ctx:StarRocksParser.DropComputeNodeClauseContext):
        pass


    # Enter a parse tree produced by StarRocksParser#modifyBrokerClause.
    def enterModifyBrokerClause(self, ctx:StarRocksParser.ModifyBrokerClauseContext):
        pass

    # Exit a parse tree produced by StarRocksParser#modifyBrokerClause.
    def exitModifyBrokerClause(self, ctx:StarRocksParser.ModifyBrokerClauseContext):
        pass


    # Enter a parse tree produced by StarRocksParser#alterLoadErrorUrlClause.
    def enterAlterLoadErrorUrlClause(self, ctx:StarRocksParser.AlterLoadErrorUrlClauseContext):
        pass

    # Exit a parse tree produced by StarRocksParser#alterLoadErrorUrlClause.
    def exitAlterLoadErrorUrlClause(self, ctx:StarRocksParser.AlterLoadErrorUrlClauseContext):
        pass


    # Enter a parse tree produced by StarRocksParser#createImageClause.
    def enterCreateImageClause(self, ctx:StarRocksParser.CreateImageClauseContext):
        pass

    # Exit a parse tree produced by StarRocksParser#createImageClause.
    def exitCreateImageClause(self, ctx:StarRocksParser.CreateImageClauseContext):
        pass


    # Enter a parse tree produced by StarRocksParser#cleanTabletSchedQClause.
    def enterCleanTabletSchedQClause(self, ctx:StarRocksParser.CleanTabletSchedQClauseContext):
        pass

    # Exit a parse tree produced by StarRocksParser#cleanTabletSchedQClause.
    def exitCleanTabletSchedQClause(self, ctx:StarRocksParser.CleanTabletSchedQClauseContext):
        pass


    # Enter a parse tree produced by StarRocksParser#decommissionDiskClause.
    def enterDecommissionDiskClause(self, ctx:StarRocksParser.DecommissionDiskClauseContext):
        pass

    # Exit a parse tree produced by StarRocksParser#decommissionDiskClause.
    def exitDecommissionDiskClause(self, ctx:StarRocksParser.DecommissionDiskClauseContext):
        pass


    # Enter a parse tree produced by StarRocksParser#cancelDecommissionDiskClause.
    def enterCancelDecommissionDiskClause(self, ctx:StarRocksParser.CancelDecommissionDiskClauseContext):
        pass

    # Exit a parse tree produced by StarRocksParser#cancelDecommissionDiskClause.
    def exitCancelDecommissionDiskClause(self, ctx:StarRocksParser.CancelDecommissionDiskClauseContext):
        pass


    # Enter a parse tree produced by StarRocksParser#disableDiskClause.
    def enterDisableDiskClause(self, ctx:StarRocksParser.DisableDiskClauseContext):
        pass

    # Exit a parse tree produced by StarRocksParser#disableDiskClause.
    def exitDisableDiskClause(self, ctx:StarRocksParser.DisableDiskClauseContext):
        pass


    # Enter a parse tree produced by StarRocksParser#cancelDisableDiskClause.
    def enterCancelDisableDiskClause(self, ctx:StarRocksParser.CancelDisableDiskClauseContext):
        pass

    # Exit a parse tree produced by StarRocksParser#cancelDisableDiskClause.
    def exitCancelDisableDiskClause(self, ctx:StarRocksParser.CancelDisableDiskClauseContext):
        pass


    # Enter a parse tree produced by StarRocksParser#createIndexClause.
    def enterCreateIndexClause(self, ctx:StarRocksParser.CreateIndexClauseContext):
        pass

    # Exit a parse tree produced by StarRocksParser#createIndexClause.
    def exitCreateIndexClause(self, ctx:StarRocksParser.CreateIndexClauseContext):
        pass


    # Enter a parse tree produced by StarRocksParser#dropIndexClause.
    def enterDropIndexClause(self, ctx:StarRocksParser.DropIndexClauseContext):
        pass

    # Exit a parse tree produced by StarRocksParser#dropIndexClause.
    def exitDropIndexClause(self, ctx:StarRocksParser.DropIndexClauseContext):
        pass


    # Enter a parse tree produced by StarRocksParser#tableRenameClause.
    def enterTableRenameClause(self, ctx:StarRocksParser.TableRenameClauseContext):
        pass

    # Exit a parse tree produced by StarRocksParser#tableRenameClause.
    def exitTableRenameClause(self, ctx:StarRocksParser.TableRenameClauseContext):
        pass


    # Enter a parse tree produced by StarRocksParser#swapTableClause.
    def enterSwapTableClause(self, ctx:StarRocksParser.SwapTableClauseContext):
        pass

    # Exit a parse tree produced by StarRocksParser#swapTableClause.
    def exitSwapTableClause(self, ctx:StarRocksParser.SwapTableClauseContext):
        pass


    # Enter a parse tree produced by StarRocksParser#modifyPropertiesClause.
    def enterModifyPropertiesClause(self, ctx:StarRocksParser.ModifyPropertiesClauseContext):
        pass

    # Exit a parse tree produced by StarRocksParser#modifyPropertiesClause.
    def exitModifyPropertiesClause(self, ctx:StarRocksParser.ModifyPropertiesClauseContext):
        pass


    # Enter a parse tree produced by StarRocksParser#modifyCommentClause.
    def enterModifyCommentClause(self, ctx:StarRocksParser.ModifyCommentClauseContext):
        pass

    # Exit a parse tree produced by StarRocksParser#modifyCommentClause.
    def exitModifyCommentClause(self, ctx:StarRocksParser.ModifyCommentClauseContext):
        pass


    # Enter a parse tree produced by StarRocksParser#optimizeClause.
    def enterOptimizeClause(self, ctx:StarRocksParser.OptimizeClauseContext):
        pass

    # Exit a parse tree produced by StarRocksParser#optimizeClause.
    def exitOptimizeClause(self, ctx:StarRocksParser.OptimizeClauseContext):
        pass


    # Enter a parse tree produced by StarRocksParser#addColumnClause.
    def enterAddColumnClause(self, ctx:StarRocksParser.AddColumnClauseContext):
        pass

    # Exit a parse tree produced by StarRocksParser#addColumnClause.
    def exitAddColumnClause(self, ctx:StarRocksParser.AddColumnClauseContext):
        pass


    # Enter a parse tree produced by StarRocksParser#addColumnsClause.
    def enterAddColumnsClause(self, ctx:StarRocksParser.AddColumnsClauseContext):
        pass

    # Exit a parse tree produced by StarRocksParser#addColumnsClause.
    def exitAddColumnsClause(self, ctx:StarRocksParser.AddColumnsClauseContext):
        pass


    # Enter a parse tree produced by StarRocksParser#dropColumnClause.
    def enterDropColumnClause(self, ctx:StarRocksParser.DropColumnClauseContext):
        pass

    # Exit a parse tree produced by StarRocksParser#dropColumnClause.
    def exitDropColumnClause(self, ctx:StarRocksParser.DropColumnClauseContext):
        pass


    # Enter a parse tree produced by StarRocksParser#modifyColumnClause.
    def enterModifyColumnClause(self, ctx:StarRocksParser.ModifyColumnClauseContext):
        pass

    # Exit a parse tree produced by StarRocksParser#modifyColumnClause.
    def exitModifyColumnClause(self, ctx:StarRocksParser.ModifyColumnClauseContext):
        pass


    # Enter a parse tree produced by StarRocksParser#columnRenameClause.
    def enterColumnRenameClause(self, ctx:StarRocksParser.ColumnRenameClauseContext):
        pass

    # Exit a parse tree produced by StarRocksParser#columnRenameClause.
    def exitColumnRenameClause(self, ctx:StarRocksParser.ColumnRenameClauseContext):
        pass


    # Enter a parse tree produced by StarRocksParser#reorderColumnsClause.
    def enterReorderColumnsClause(self, ctx:StarRocksParser.ReorderColumnsClauseContext):
        pass

    # Exit a parse tree produced by StarRocksParser#reorderColumnsClause.
    def exitReorderColumnsClause(self, ctx:StarRocksParser.ReorderColumnsClauseContext):
        pass


    # Enter a parse tree produced by StarRocksParser#rollupRenameClause.
    def enterRollupRenameClause(self, ctx:StarRocksParser.RollupRenameClauseContext):
        pass

    # Exit a parse tree produced by StarRocksParser#rollupRenameClause.
    def exitRollupRenameClause(self, ctx:StarRocksParser.RollupRenameClauseContext):
        pass


    # Enter a parse tree produced by StarRocksParser#compactionClause.
    def enterCompactionClause(self, ctx:StarRocksParser.CompactionClauseContext):
        pass

    # Exit a parse tree produced by StarRocksParser#compactionClause.
    def exitCompactionClause(self, ctx:StarRocksParser.CompactionClauseContext):
        pass


    # Enter a parse tree produced by StarRocksParser#subfieldName.
    def enterSubfieldName(self, ctx:StarRocksParser.SubfieldNameContext):
        pass

    # Exit a parse tree produced by StarRocksParser#subfieldName.
    def exitSubfieldName(self, ctx:StarRocksParser.SubfieldNameContext):
        pass


    # Enter a parse tree produced by StarRocksParser#nestedFieldName.
    def enterNestedFieldName(self, ctx:StarRocksParser.NestedFieldNameContext):
        pass

    # Exit a parse tree produced by StarRocksParser#nestedFieldName.
    def exitNestedFieldName(self, ctx:StarRocksParser.NestedFieldNameContext):
        pass


    # Enter a parse tree produced by StarRocksParser#addFieldClause.
    def enterAddFieldClause(self, ctx:StarRocksParser.AddFieldClauseContext):
        pass

    # Exit a parse tree produced by StarRocksParser#addFieldClause.
    def exitAddFieldClause(self, ctx:StarRocksParser.AddFieldClauseContext):
        pass


    # Enter a parse tree produced by StarRocksParser#dropFieldClause.
    def enterDropFieldClause(self, ctx:StarRocksParser.DropFieldClauseContext):
        pass

    # Exit a parse tree produced by StarRocksParser#dropFieldClause.
    def exitDropFieldClause(self, ctx:StarRocksParser.DropFieldClauseContext):
        pass


    # Enter a parse tree produced by StarRocksParser#addPartitionClause.
    def enterAddPartitionClause(self, ctx:StarRocksParser.AddPartitionClauseContext):
        pass

    # Exit a parse tree produced by StarRocksParser#addPartitionClause.
    def exitAddPartitionClause(self, ctx:StarRocksParser.AddPartitionClauseContext):
        pass


    # Enter a parse tree produced by StarRocksParser#dropPartitionClause.
    def enterDropPartitionClause(self, ctx:StarRocksParser.DropPartitionClauseContext):
        pass

    # Exit a parse tree produced by StarRocksParser#dropPartitionClause.
    def exitDropPartitionClause(self, ctx:StarRocksParser.DropPartitionClauseContext):
        pass


    # Enter a parse tree produced by StarRocksParser#truncatePartitionClause.
    def enterTruncatePartitionClause(self, ctx:StarRocksParser.TruncatePartitionClauseContext):
        pass

    # Exit a parse tree produced by StarRocksParser#truncatePartitionClause.
    def exitTruncatePartitionClause(self, ctx:StarRocksParser.TruncatePartitionClauseContext):
        pass


    # Enter a parse tree produced by StarRocksParser#modifyPartitionClause.
    def enterModifyPartitionClause(self, ctx:StarRocksParser.ModifyPartitionClauseContext):
        pass

    # Exit a parse tree produced by StarRocksParser#modifyPartitionClause.
    def exitModifyPartitionClause(self, ctx:StarRocksParser.ModifyPartitionClauseContext):
        pass


    # Enter a parse tree produced by StarRocksParser#replacePartitionClause.
    def enterReplacePartitionClause(self, ctx:StarRocksParser.ReplacePartitionClauseContext):
        pass

    # Exit a parse tree produced by StarRocksParser#replacePartitionClause.
    def exitReplacePartitionClause(self, ctx:StarRocksParser.ReplacePartitionClauseContext):
        pass


    # Enter a parse tree produced by StarRocksParser#partitionRenameClause.
    def enterPartitionRenameClause(self, ctx:StarRocksParser.PartitionRenameClauseContext):
        pass

    # Exit a parse tree produced by StarRocksParser#partitionRenameClause.
    def exitPartitionRenameClause(self, ctx:StarRocksParser.PartitionRenameClauseContext):
        pass


    # Enter a parse tree produced by StarRocksParser#insertStatement.
    def enterInsertStatement(self, ctx:StarRocksParser.InsertStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#insertStatement.
    def exitInsertStatement(self, ctx:StarRocksParser.InsertStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#updateStatement.
    def enterUpdateStatement(self, ctx:StarRocksParser.UpdateStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#updateStatement.
    def exitUpdateStatement(self, ctx:StarRocksParser.UpdateStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#deleteStatement.
    def enterDeleteStatement(self, ctx:StarRocksParser.DeleteStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#deleteStatement.
    def exitDeleteStatement(self, ctx:StarRocksParser.DeleteStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#createRoutineLoadStatement.
    def enterCreateRoutineLoadStatement(self, ctx:StarRocksParser.CreateRoutineLoadStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#createRoutineLoadStatement.
    def exitCreateRoutineLoadStatement(self, ctx:StarRocksParser.CreateRoutineLoadStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#alterRoutineLoadStatement.
    def enterAlterRoutineLoadStatement(self, ctx:StarRocksParser.AlterRoutineLoadStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#alterRoutineLoadStatement.
    def exitAlterRoutineLoadStatement(self, ctx:StarRocksParser.AlterRoutineLoadStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#dataSource.
    def enterDataSource(self, ctx:StarRocksParser.DataSourceContext):
        pass

    # Exit a parse tree produced by StarRocksParser#dataSource.
    def exitDataSource(self, ctx:StarRocksParser.DataSourceContext):
        pass


    # Enter a parse tree produced by StarRocksParser#loadProperties.
    def enterLoadProperties(self, ctx:StarRocksParser.LoadPropertiesContext):
        pass

    # Exit a parse tree produced by StarRocksParser#loadProperties.
    def exitLoadProperties(self, ctx:StarRocksParser.LoadPropertiesContext):
        pass


    # Enter a parse tree produced by StarRocksParser#colSeparatorProperty.
    def enterColSeparatorProperty(self, ctx:StarRocksParser.ColSeparatorPropertyContext):
        pass

    # Exit a parse tree produced by StarRocksParser#colSeparatorProperty.
    def exitColSeparatorProperty(self, ctx:StarRocksParser.ColSeparatorPropertyContext):
        pass


    # Enter a parse tree produced by StarRocksParser#rowDelimiterProperty.
    def enterRowDelimiterProperty(self, ctx:StarRocksParser.RowDelimiterPropertyContext):
        pass

    # Exit a parse tree produced by StarRocksParser#rowDelimiterProperty.
    def exitRowDelimiterProperty(self, ctx:StarRocksParser.RowDelimiterPropertyContext):
        pass


    # Enter a parse tree produced by StarRocksParser#importColumns.
    def enterImportColumns(self, ctx:StarRocksParser.ImportColumnsContext):
        pass

    # Exit a parse tree produced by StarRocksParser#importColumns.
    def exitImportColumns(self, ctx:StarRocksParser.ImportColumnsContext):
        pass


    # Enter a parse tree produced by StarRocksParser#columnProperties.
    def enterColumnProperties(self, ctx:StarRocksParser.ColumnPropertiesContext):
        pass

    # Exit a parse tree produced by StarRocksParser#columnProperties.
    def exitColumnProperties(self, ctx:StarRocksParser.ColumnPropertiesContext):
        pass


    # Enter a parse tree produced by StarRocksParser#jobProperties.
    def enterJobProperties(self, ctx:StarRocksParser.JobPropertiesContext):
        pass

    # Exit a parse tree produced by StarRocksParser#jobProperties.
    def exitJobProperties(self, ctx:StarRocksParser.JobPropertiesContext):
        pass


    # Enter a parse tree produced by StarRocksParser#dataSourceProperties.
    def enterDataSourceProperties(self, ctx:StarRocksParser.DataSourcePropertiesContext):
        pass

    # Exit a parse tree produced by StarRocksParser#dataSourceProperties.
    def exitDataSourceProperties(self, ctx:StarRocksParser.DataSourcePropertiesContext):
        pass


    # Enter a parse tree produced by StarRocksParser#stopRoutineLoadStatement.
    def enterStopRoutineLoadStatement(self, ctx:StarRocksParser.StopRoutineLoadStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#stopRoutineLoadStatement.
    def exitStopRoutineLoadStatement(self, ctx:StarRocksParser.StopRoutineLoadStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#resumeRoutineLoadStatement.
    def enterResumeRoutineLoadStatement(self, ctx:StarRocksParser.ResumeRoutineLoadStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#resumeRoutineLoadStatement.
    def exitResumeRoutineLoadStatement(self, ctx:StarRocksParser.ResumeRoutineLoadStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#pauseRoutineLoadStatement.
    def enterPauseRoutineLoadStatement(self, ctx:StarRocksParser.PauseRoutineLoadStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#pauseRoutineLoadStatement.
    def exitPauseRoutineLoadStatement(self, ctx:StarRocksParser.PauseRoutineLoadStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#showRoutineLoadStatement.
    def enterShowRoutineLoadStatement(self, ctx:StarRocksParser.ShowRoutineLoadStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#showRoutineLoadStatement.
    def exitShowRoutineLoadStatement(self, ctx:StarRocksParser.ShowRoutineLoadStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#showRoutineLoadTaskStatement.
    def enterShowRoutineLoadTaskStatement(self, ctx:StarRocksParser.ShowRoutineLoadTaskStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#showRoutineLoadTaskStatement.
    def exitShowRoutineLoadTaskStatement(self, ctx:StarRocksParser.ShowRoutineLoadTaskStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#showCreateRoutineLoadStatement.
    def enterShowCreateRoutineLoadStatement(self, ctx:StarRocksParser.ShowCreateRoutineLoadStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#showCreateRoutineLoadStatement.
    def exitShowCreateRoutineLoadStatement(self, ctx:StarRocksParser.ShowCreateRoutineLoadStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#showStreamLoadStatement.
    def enterShowStreamLoadStatement(self, ctx:StarRocksParser.ShowStreamLoadStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#showStreamLoadStatement.
    def exitShowStreamLoadStatement(self, ctx:StarRocksParser.ShowStreamLoadStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#analyzeStatement.
    def enterAnalyzeStatement(self, ctx:StarRocksParser.AnalyzeStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#analyzeStatement.
    def exitAnalyzeStatement(self, ctx:StarRocksParser.AnalyzeStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#dropStatsStatement.
    def enterDropStatsStatement(self, ctx:StarRocksParser.DropStatsStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#dropStatsStatement.
    def exitDropStatsStatement(self, ctx:StarRocksParser.DropStatsStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#analyzeHistogramStatement.
    def enterAnalyzeHistogramStatement(self, ctx:StarRocksParser.AnalyzeHistogramStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#analyzeHistogramStatement.
    def exitAnalyzeHistogramStatement(self, ctx:StarRocksParser.AnalyzeHistogramStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#dropHistogramStatement.
    def enterDropHistogramStatement(self, ctx:StarRocksParser.DropHistogramStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#dropHistogramStatement.
    def exitDropHistogramStatement(self, ctx:StarRocksParser.DropHistogramStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#createAnalyzeStatement.
    def enterCreateAnalyzeStatement(self, ctx:StarRocksParser.CreateAnalyzeStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#createAnalyzeStatement.
    def exitCreateAnalyzeStatement(self, ctx:StarRocksParser.CreateAnalyzeStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#dropAnalyzeJobStatement.
    def enterDropAnalyzeJobStatement(self, ctx:StarRocksParser.DropAnalyzeJobStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#dropAnalyzeJobStatement.
    def exitDropAnalyzeJobStatement(self, ctx:StarRocksParser.DropAnalyzeJobStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#showAnalyzeStatement.
    def enterShowAnalyzeStatement(self, ctx:StarRocksParser.ShowAnalyzeStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#showAnalyzeStatement.
    def exitShowAnalyzeStatement(self, ctx:StarRocksParser.ShowAnalyzeStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#showStatsMetaStatement.
    def enterShowStatsMetaStatement(self, ctx:StarRocksParser.ShowStatsMetaStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#showStatsMetaStatement.
    def exitShowStatsMetaStatement(self, ctx:StarRocksParser.ShowStatsMetaStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#showHistogramMetaStatement.
    def enterShowHistogramMetaStatement(self, ctx:StarRocksParser.ShowHistogramMetaStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#showHistogramMetaStatement.
    def exitShowHistogramMetaStatement(self, ctx:StarRocksParser.ShowHistogramMetaStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#killAnalyzeStatement.
    def enterKillAnalyzeStatement(self, ctx:StarRocksParser.KillAnalyzeStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#killAnalyzeStatement.
    def exitKillAnalyzeStatement(self, ctx:StarRocksParser.KillAnalyzeStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#analyzeProfileStatement.
    def enterAnalyzeProfileStatement(self, ctx:StarRocksParser.AnalyzeProfileStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#analyzeProfileStatement.
    def exitAnalyzeProfileStatement(self, ctx:StarRocksParser.AnalyzeProfileStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#createResourceGroupStatement.
    def enterCreateResourceGroupStatement(self, ctx:StarRocksParser.CreateResourceGroupStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#createResourceGroupStatement.
    def exitCreateResourceGroupStatement(self, ctx:StarRocksParser.CreateResourceGroupStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#dropResourceGroupStatement.
    def enterDropResourceGroupStatement(self, ctx:StarRocksParser.DropResourceGroupStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#dropResourceGroupStatement.
    def exitDropResourceGroupStatement(self, ctx:StarRocksParser.DropResourceGroupStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#alterResourceGroupStatement.
    def enterAlterResourceGroupStatement(self, ctx:StarRocksParser.AlterResourceGroupStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#alterResourceGroupStatement.
    def exitAlterResourceGroupStatement(self, ctx:StarRocksParser.AlterResourceGroupStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#showResourceGroupStatement.
    def enterShowResourceGroupStatement(self, ctx:StarRocksParser.ShowResourceGroupStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#showResourceGroupStatement.
    def exitShowResourceGroupStatement(self, ctx:StarRocksParser.ShowResourceGroupStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#showResourceGroupUsageStatement.
    def enterShowResourceGroupUsageStatement(self, ctx:StarRocksParser.ShowResourceGroupUsageStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#showResourceGroupUsageStatement.
    def exitShowResourceGroupUsageStatement(self, ctx:StarRocksParser.ShowResourceGroupUsageStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#createResourceStatement.
    def enterCreateResourceStatement(self, ctx:StarRocksParser.CreateResourceStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#createResourceStatement.
    def exitCreateResourceStatement(self, ctx:StarRocksParser.CreateResourceStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#alterResourceStatement.
    def enterAlterResourceStatement(self, ctx:StarRocksParser.AlterResourceStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#alterResourceStatement.
    def exitAlterResourceStatement(self, ctx:StarRocksParser.AlterResourceStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#dropResourceStatement.
    def enterDropResourceStatement(self, ctx:StarRocksParser.DropResourceStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#dropResourceStatement.
    def exitDropResourceStatement(self, ctx:StarRocksParser.DropResourceStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#showResourceStatement.
    def enterShowResourceStatement(self, ctx:StarRocksParser.ShowResourceStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#showResourceStatement.
    def exitShowResourceStatement(self, ctx:StarRocksParser.ShowResourceStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#classifier.
    def enterClassifier(self, ctx:StarRocksParser.ClassifierContext):
        pass

    # Exit a parse tree produced by StarRocksParser#classifier.
    def exitClassifier(self, ctx:StarRocksParser.ClassifierContext):
        pass


    # Enter a parse tree produced by StarRocksParser#showFunctionsStatement.
    def enterShowFunctionsStatement(self, ctx:StarRocksParser.ShowFunctionsStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#showFunctionsStatement.
    def exitShowFunctionsStatement(self, ctx:StarRocksParser.ShowFunctionsStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#dropFunctionStatement.
    def enterDropFunctionStatement(self, ctx:StarRocksParser.DropFunctionStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#dropFunctionStatement.
    def exitDropFunctionStatement(self, ctx:StarRocksParser.DropFunctionStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#createFunctionStatement.
    def enterCreateFunctionStatement(self, ctx:StarRocksParser.CreateFunctionStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#createFunctionStatement.
    def exitCreateFunctionStatement(self, ctx:StarRocksParser.CreateFunctionStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#typeList.
    def enterTypeList(self, ctx:StarRocksParser.TypeListContext):
        pass

    # Exit a parse tree produced by StarRocksParser#typeList.
    def exitTypeList(self, ctx:StarRocksParser.TypeListContext):
        pass


    # Enter a parse tree produced by StarRocksParser#loadStatement.
    def enterLoadStatement(self, ctx:StarRocksParser.LoadStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#loadStatement.
    def exitLoadStatement(self, ctx:StarRocksParser.LoadStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#labelName.
    def enterLabelName(self, ctx:StarRocksParser.LabelNameContext):
        pass

    # Exit a parse tree produced by StarRocksParser#labelName.
    def exitLabelName(self, ctx:StarRocksParser.LabelNameContext):
        pass


    # Enter a parse tree produced by StarRocksParser#dataDescList.
    def enterDataDescList(self, ctx:StarRocksParser.DataDescListContext):
        pass

    # Exit a parse tree produced by StarRocksParser#dataDescList.
    def exitDataDescList(self, ctx:StarRocksParser.DataDescListContext):
        pass


    # Enter a parse tree produced by StarRocksParser#dataDesc.
    def enterDataDesc(self, ctx:StarRocksParser.DataDescContext):
        pass

    # Exit a parse tree produced by StarRocksParser#dataDesc.
    def exitDataDesc(self, ctx:StarRocksParser.DataDescContext):
        pass


    # Enter a parse tree produced by StarRocksParser#formatProps.
    def enterFormatProps(self, ctx:StarRocksParser.FormatPropsContext):
        pass

    # Exit a parse tree produced by StarRocksParser#formatProps.
    def exitFormatProps(self, ctx:StarRocksParser.FormatPropsContext):
        pass


    # Enter a parse tree produced by StarRocksParser#brokerDesc.
    def enterBrokerDesc(self, ctx:StarRocksParser.BrokerDescContext):
        pass

    # Exit a parse tree produced by StarRocksParser#brokerDesc.
    def exitBrokerDesc(self, ctx:StarRocksParser.BrokerDescContext):
        pass


    # Enter a parse tree produced by StarRocksParser#resourceDesc.
    def enterResourceDesc(self, ctx:StarRocksParser.ResourceDescContext):
        pass

    # Exit a parse tree produced by StarRocksParser#resourceDesc.
    def exitResourceDesc(self, ctx:StarRocksParser.ResourceDescContext):
        pass


    # Enter a parse tree produced by StarRocksParser#showLoadStatement.
    def enterShowLoadStatement(self, ctx:StarRocksParser.ShowLoadStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#showLoadStatement.
    def exitShowLoadStatement(self, ctx:StarRocksParser.ShowLoadStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#showLoadWarningsStatement.
    def enterShowLoadWarningsStatement(self, ctx:StarRocksParser.ShowLoadWarningsStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#showLoadWarningsStatement.
    def exitShowLoadWarningsStatement(self, ctx:StarRocksParser.ShowLoadWarningsStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#cancelLoadStatement.
    def enterCancelLoadStatement(self, ctx:StarRocksParser.CancelLoadStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#cancelLoadStatement.
    def exitCancelLoadStatement(self, ctx:StarRocksParser.CancelLoadStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#alterLoadStatement.
    def enterAlterLoadStatement(self, ctx:StarRocksParser.AlterLoadStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#alterLoadStatement.
    def exitAlterLoadStatement(self, ctx:StarRocksParser.AlterLoadStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#cancelCompactionStatement.
    def enterCancelCompactionStatement(self, ctx:StarRocksParser.CancelCompactionStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#cancelCompactionStatement.
    def exitCancelCompactionStatement(self, ctx:StarRocksParser.CancelCompactionStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#showAuthorStatement.
    def enterShowAuthorStatement(self, ctx:StarRocksParser.ShowAuthorStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#showAuthorStatement.
    def exitShowAuthorStatement(self, ctx:StarRocksParser.ShowAuthorStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#showBackendsStatement.
    def enterShowBackendsStatement(self, ctx:StarRocksParser.ShowBackendsStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#showBackendsStatement.
    def exitShowBackendsStatement(self, ctx:StarRocksParser.ShowBackendsStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#showBrokerStatement.
    def enterShowBrokerStatement(self, ctx:StarRocksParser.ShowBrokerStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#showBrokerStatement.
    def exitShowBrokerStatement(self, ctx:StarRocksParser.ShowBrokerStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#showCharsetStatement.
    def enterShowCharsetStatement(self, ctx:StarRocksParser.ShowCharsetStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#showCharsetStatement.
    def exitShowCharsetStatement(self, ctx:StarRocksParser.ShowCharsetStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#showCollationStatement.
    def enterShowCollationStatement(self, ctx:StarRocksParser.ShowCollationStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#showCollationStatement.
    def exitShowCollationStatement(self, ctx:StarRocksParser.ShowCollationStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#showDeleteStatement.
    def enterShowDeleteStatement(self, ctx:StarRocksParser.ShowDeleteStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#showDeleteStatement.
    def exitShowDeleteStatement(self, ctx:StarRocksParser.ShowDeleteStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#showDynamicPartitionStatement.
    def enterShowDynamicPartitionStatement(self, ctx:StarRocksParser.ShowDynamicPartitionStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#showDynamicPartitionStatement.
    def exitShowDynamicPartitionStatement(self, ctx:StarRocksParser.ShowDynamicPartitionStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#showEventsStatement.
    def enterShowEventsStatement(self, ctx:StarRocksParser.ShowEventsStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#showEventsStatement.
    def exitShowEventsStatement(self, ctx:StarRocksParser.ShowEventsStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#showEnginesStatement.
    def enterShowEnginesStatement(self, ctx:StarRocksParser.ShowEnginesStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#showEnginesStatement.
    def exitShowEnginesStatement(self, ctx:StarRocksParser.ShowEnginesStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#showFrontendsStatement.
    def enterShowFrontendsStatement(self, ctx:StarRocksParser.ShowFrontendsStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#showFrontendsStatement.
    def exitShowFrontendsStatement(self, ctx:StarRocksParser.ShowFrontendsStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#showPluginsStatement.
    def enterShowPluginsStatement(self, ctx:StarRocksParser.ShowPluginsStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#showPluginsStatement.
    def exitShowPluginsStatement(self, ctx:StarRocksParser.ShowPluginsStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#showRepositoriesStatement.
    def enterShowRepositoriesStatement(self, ctx:StarRocksParser.ShowRepositoriesStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#showRepositoriesStatement.
    def exitShowRepositoriesStatement(self, ctx:StarRocksParser.ShowRepositoriesStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#showOpenTableStatement.
    def enterShowOpenTableStatement(self, ctx:StarRocksParser.ShowOpenTableStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#showOpenTableStatement.
    def exitShowOpenTableStatement(self, ctx:StarRocksParser.ShowOpenTableStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#showPrivilegesStatement.
    def enterShowPrivilegesStatement(self, ctx:StarRocksParser.ShowPrivilegesStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#showPrivilegesStatement.
    def exitShowPrivilegesStatement(self, ctx:StarRocksParser.ShowPrivilegesStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#showProcedureStatement.
    def enterShowProcedureStatement(self, ctx:StarRocksParser.ShowProcedureStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#showProcedureStatement.
    def exitShowProcedureStatement(self, ctx:StarRocksParser.ShowProcedureStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#showProcStatement.
    def enterShowProcStatement(self, ctx:StarRocksParser.ShowProcStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#showProcStatement.
    def exitShowProcStatement(self, ctx:StarRocksParser.ShowProcStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#showProcesslistStatement.
    def enterShowProcesslistStatement(self, ctx:StarRocksParser.ShowProcesslistStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#showProcesslistStatement.
    def exitShowProcesslistStatement(self, ctx:StarRocksParser.ShowProcesslistStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#showProfilelistStatement.
    def enterShowProfilelistStatement(self, ctx:StarRocksParser.ShowProfilelistStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#showProfilelistStatement.
    def exitShowProfilelistStatement(self, ctx:StarRocksParser.ShowProfilelistStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#showRunningQueriesStatement.
    def enterShowRunningQueriesStatement(self, ctx:StarRocksParser.ShowRunningQueriesStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#showRunningQueriesStatement.
    def exitShowRunningQueriesStatement(self, ctx:StarRocksParser.ShowRunningQueriesStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#showStatusStatement.
    def enterShowStatusStatement(self, ctx:StarRocksParser.ShowStatusStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#showStatusStatement.
    def exitShowStatusStatement(self, ctx:StarRocksParser.ShowStatusStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#showTabletStatement.
    def enterShowTabletStatement(self, ctx:StarRocksParser.ShowTabletStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#showTabletStatement.
    def exitShowTabletStatement(self, ctx:StarRocksParser.ShowTabletStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#showTransactionStatement.
    def enterShowTransactionStatement(self, ctx:StarRocksParser.ShowTransactionStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#showTransactionStatement.
    def exitShowTransactionStatement(self, ctx:StarRocksParser.ShowTransactionStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#showTriggersStatement.
    def enterShowTriggersStatement(self, ctx:StarRocksParser.ShowTriggersStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#showTriggersStatement.
    def exitShowTriggersStatement(self, ctx:StarRocksParser.ShowTriggersStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#showUserPropertyStatement.
    def enterShowUserPropertyStatement(self, ctx:StarRocksParser.ShowUserPropertyStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#showUserPropertyStatement.
    def exitShowUserPropertyStatement(self, ctx:StarRocksParser.ShowUserPropertyStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#showVariablesStatement.
    def enterShowVariablesStatement(self, ctx:StarRocksParser.ShowVariablesStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#showVariablesStatement.
    def exitShowVariablesStatement(self, ctx:StarRocksParser.ShowVariablesStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#showWarningStatement.
    def enterShowWarningStatement(self, ctx:StarRocksParser.ShowWarningStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#showWarningStatement.
    def exitShowWarningStatement(self, ctx:StarRocksParser.ShowWarningStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#helpStatement.
    def enterHelpStatement(self, ctx:StarRocksParser.HelpStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#helpStatement.
    def exitHelpStatement(self, ctx:StarRocksParser.HelpStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#createUserStatement.
    def enterCreateUserStatement(self, ctx:StarRocksParser.CreateUserStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#createUserStatement.
    def exitCreateUserStatement(self, ctx:StarRocksParser.CreateUserStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#dropUserStatement.
    def enterDropUserStatement(self, ctx:StarRocksParser.DropUserStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#dropUserStatement.
    def exitDropUserStatement(self, ctx:StarRocksParser.DropUserStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#alterUserStatement.
    def enterAlterUserStatement(self, ctx:StarRocksParser.AlterUserStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#alterUserStatement.
    def exitAlterUserStatement(self, ctx:StarRocksParser.AlterUserStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#showUserStatement.
    def enterShowUserStatement(self, ctx:StarRocksParser.ShowUserStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#showUserStatement.
    def exitShowUserStatement(self, ctx:StarRocksParser.ShowUserStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#showAllAuthentication.
    def enterShowAllAuthentication(self, ctx:StarRocksParser.ShowAllAuthenticationContext):
        pass

    # Exit a parse tree produced by StarRocksParser#showAllAuthentication.
    def exitShowAllAuthentication(self, ctx:StarRocksParser.ShowAllAuthenticationContext):
        pass


    # Enter a parse tree produced by StarRocksParser#showAuthenticationForUser.
    def enterShowAuthenticationForUser(self, ctx:StarRocksParser.ShowAuthenticationForUserContext):
        pass

    # Exit a parse tree produced by StarRocksParser#showAuthenticationForUser.
    def exitShowAuthenticationForUser(self, ctx:StarRocksParser.ShowAuthenticationForUserContext):
        pass


    # Enter a parse tree produced by StarRocksParser#executeAsStatement.
    def enterExecuteAsStatement(self, ctx:StarRocksParser.ExecuteAsStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#executeAsStatement.
    def exitExecuteAsStatement(self, ctx:StarRocksParser.ExecuteAsStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#createRoleStatement.
    def enterCreateRoleStatement(self, ctx:StarRocksParser.CreateRoleStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#createRoleStatement.
    def exitCreateRoleStatement(self, ctx:StarRocksParser.CreateRoleStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#alterRoleStatement.
    def enterAlterRoleStatement(self, ctx:StarRocksParser.AlterRoleStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#alterRoleStatement.
    def exitAlterRoleStatement(self, ctx:StarRocksParser.AlterRoleStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#dropRoleStatement.
    def enterDropRoleStatement(self, ctx:StarRocksParser.DropRoleStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#dropRoleStatement.
    def exitDropRoleStatement(self, ctx:StarRocksParser.DropRoleStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#showRolesStatement.
    def enterShowRolesStatement(self, ctx:StarRocksParser.ShowRolesStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#showRolesStatement.
    def exitShowRolesStatement(self, ctx:StarRocksParser.ShowRolesStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#grantRoleToUser.
    def enterGrantRoleToUser(self, ctx:StarRocksParser.GrantRoleToUserContext):
        pass

    # Exit a parse tree produced by StarRocksParser#grantRoleToUser.
    def exitGrantRoleToUser(self, ctx:StarRocksParser.GrantRoleToUserContext):
        pass


    # Enter a parse tree produced by StarRocksParser#grantRoleToRole.
    def enterGrantRoleToRole(self, ctx:StarRocksParser.GrantRoleToRoleContext):
        pass

    # Exit a parse tree produced by StarRocksParser#grantRoleToRole.
    def exitGrantRoleToRole(self, ctx:StarRocksParser.GrantRoleToRoleContext):
        pass


    # Enter a parse tree produced by StarRocksParser#revokeRoleFromUser.
    def enterRevokeRoleFromUser(self, ctx:StarRocksParser.RevokeRoleFromUserContext):
        pass

    # Exit a parse tree produced by StarRocksParser#revokeRoleFromUser.
    def exitRevokeRoleFromUser(self, ctx:StarRocksParser.RevokeRoleFromUserContext):
        pass


    # Enter a parse tree produced by StarRocksParser#revokeRoleFromRole.
    def enterRevokeRoleFromRole(self, ctx:StarRocksParser.RevokeRoleFromRoleContext):
        pass

    # Exit a parse tree produced by StarRocksParser#revokeRoleFromRole.
    def exitRevokeRoleFromRole(self, ctx:StarRocksParser.RevokeRoleFromRoleContext):
        pass


    # Enter a parse tree produced by StarRocksParser#setRoleStatement.
    def enterSetRoleStatement(self, ctx:StarRocksParser.SetRoleStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#setRoleStatement.
    def exitSetRoleStatement(self, ctx:StarRocksParser.SetRoleStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#setDefaultRoleStatement.
    def enterSetDefaultRoleStatement(self, ctx:StarRocksParser.SetDefaultRoleStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#setDefaultRoleStatement.
    def exitSetDefaultRoleStatement(self, ctx:StarRocksParser.SetDefaultRoleStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#grantRevokeClause.
    def enterGrantRevokeClause(self, ctx:StarRocksParser.GrantRevokeClauseContext):
        pass

    # Exit a parse tree produced by StarRocksParser#grantRevokeClause.
    def exitGrantRevokeClause(self, ctx:StarRocksParser.GrantRevokeClauseContext):
        pass


    # Enter a parse tree produced by StarRocksParser#grantOnUser.
    def enterGrantOnUser(self, ctx:StarRocksParser.GrantOnUserContext):
        pass

    # Exit a parse tree produced by StarRocksParser#grantOnUser.
    def exitGrantOnUser(self, ctx:StarRocksParser.GrantOnUserContext):
        pass


    # Enter a parse tree produced by StarRocksParser#grantOnTableBrief.
    def enterGrantOnTableBrief(self, ctx:StarRocksParser.GrantOnTableBriefContext):
        pass

    # Exit a parse tree produced by StarRocksParser#grantOnTableBrief.
    def exitGrantOnTableBrief(self, ctx:StarRocksParser.GrantOnTableBriefContext):
        pass


    # Enter a parse tree produced by StarRocksParser#grantOnFunc.
    def enterGrantOnFunc(self, ctx:StarRocksParser.GrantOnFuncContext):
        pass

    # Exit a parse tree produced by StarRocksParser#grantOnFunc.
    def exitGrantOnFunc(self, ctx:StarRocksParser.GrantOnFuncContext):
        pass


    # Enter a parse tree produced by StarRocksParser#grantOnSystem.
    def enterGrantOnSystem(self, ctx:StarRocksParser.GrantOnSystemContext):
        pass

    # Exit a parse tree produced by StarRocksParser#grantOnSystem.
    def exitGrantOnSystem(self, ctx:StarRocksParser.GrantOnSystemContext):
        pass


    # Enter a parse tree produced by StarRocksParser#grantOnPrimaryObj.
    def enterGrantOnPrimaryObj(self, ctx:StarRocksParser.GrantOnPrimaryObjContext):
        pass

    # Exit a parse tree produced by StarRocksParser#grantOnPrimaryObj.
    def exitGrantOnPrimaryObj(self, ctx:StarRocksParser.GrantOnPrimaryObjContext):
        pass


    # Enter a parse tree produced by StarRocksParser#grantOnAll.
    def enterGrantOnAll(self, ctx:StarRocksParser.GrantOnAllContext):
        pass

    # Exit a parse tree produced by StarRocksParser#grantOnAll.
    def exitGrantOnAll(self, ctx:StarRocksParser.GrantOnAllContext):
        pass


    # Enter a parse tree produced by StarRocksParser#revokeOnUser.
    def enterRevokeOnUser(self, ctx:StarRocksParser.RevokeOnUserContext):
        pass

    # Exit a parse tree produced by StarRocksParser#revokeOnUser.
    def exitRevokeOnUser(self, ctx:StarRocksParser.RevokeOnUserContext):
        pass


    # Enter a parse tree produced by StarRocksParser#revokeOnTableBrief.
    def enterRevokeOnTableBrief(self, ctx:StarRocksParser.RevokeOnTableBriefContext):
        pass

    # Exit a parse tree produced by StarRocksParser#revokeOnTableBrief.
    def exitRevokeOnTableBrief(self, ctx:StarRocksParser.RevokeOnTableBriefContext):
        pass


    # Enter a parse tree produced by StarRocksParser#revokeOnFunc.
    def enterRevokeOnFunc(self, ctx:StarRocksParser.RevokeOnFuncContext):
        pass

    # Exit a parse tree produced by StarRocksParser#revokeOnFunc.
    def exitRevokeOnFunc(self, ctx:StarRocksParser.RevokeOnFuncContext):
        pass


    # Enter a parse tree produced by StarRocksParser#revokeOnSystem.
    def enterRevokeOnSystem(self, ctx:StarRocksParser.RevokeOnSystemContext):
        pass

    # Exit a parse tree produced by StarRocksParser#revokeOnSystem.
    def exitRevokeOnSystem(self, ctx:StarRocksParser.RevokeOnSystemContext):
        pass


    # Enter a parse tree produced by StarRocksParser#revokeOnPrimaryObj.
    def enterRevokeOnPrimaryObj(self, ctx:StarRocksParser.RevokeOnPrimaryObjContext):
        pass

    # Exit a parse tree produced by StarRocksParser#revokeOnPrimaryObj.
    def exitRevokeOnPrimaryObj(self, ctx:StarRocksParser.RevokeOnPrimaryObjContext):
        pass


    # Enter a parse tree produced by StarRocksParser#revokeOnAll.
    def enterRevokeOnAll(self, ctx:StarRocksParser.RevokeOnAllContext):
        pass

    # Exit a parse tree produced by StarRocksParser#revokeOnAll.
    def exitRevokeOnAll(self, ctx:StarRocksParser.RevokeOnAllContext):
        pass


    # Enter a parse tree produced by StarRocksParser#showGrantsStatement.
    def enterShowGrantsStatement(self, ctx:StarRocksParser.ShowGrantsStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#showGrantsStatement.
    def exitShowGrantsStatement(self, ctx:StarRocksParser.ShowGrantsStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#authWithoutPlugin.
    def enterAuthWithoutPlugin(self, ctx:StarRocksParser.AuthWithoutPluginContext):
        pass

    # Exit a parse tree produced by StarRocksParser#authWithoutPlugin.
    def exitAuthWithoutPlugin(self, ctx:StarRocksParser.AuthWithoutPluginContext):
        pass


    # Enter a parse tree produced by StarRocksParser#authWithPlugin.
    def enterAuthWithPlugin(self, ctx:StarRocksParser.AuthWithPluginContext):
        pass

    # Exit a parse tree produced by StarRocksParser#authWithPlugin.
    def exitAuthWithPlugin(self, ctx:StarRocksParser.AuthWithPluginContext):
        pass


    # Enter a parse tree produced by StarRocksParser#privObjectName.
    def enterPrivObjectName(self, ctx:StarRocksParser.PrivObjectNameContext):
        pass

    # Exit a parse tree produced by StarRocksParser#privObjectName.
    def exitPrivObjectName(self, ctx:StarRocksParser.PrivObjectNameContext):
        pass


    # Enter a parse tree produced by StarRocksParser#privObjectNameList.
    def enterPrivObjectNameList(self, ctx:StarRocksParser.PrivObjectNameListContext):
        pass

    # Exit a parse tree produced by StarRocksParser#privObjectNameList.
    def exitPrivObjectNameList(self, ctx:StarRocksParser.PrivObjectNameListContext):
        pass


    # Enter a parse tree produced by StarRocksParser#privFunctionObjectNameList.
    def enterPrivFunctionObjectNameList(self, ctx:StarRocksParser.PrivFunctionObjectNameListContext):
        pass

    # Exit a parse tree produced by StarRocksParser#privFunctionObjectNameList.
    def exitPrivFunctionObjectNameList(self, ctx:StarRocksParser.PrivFunctionObjectNameListContext):
        pass


    # Enter a parse tree produced by StarRocksParser#privilegeTypeList.
    def enterPrivilegeTypeList(self, ctx:StarRocksParser.PrivilegeTypeListContext):
        pass

    # Exit a parse tree produced by StarRocksParser#privilegeTypeList.
    def exitPrivilegeTypeList(self, ctx:StarRocksParser.PrivilegeTypeListContext):
        pass


    # Enter a parse tree produced by StarRocksParser#privilegeType.
    def enterPrivilegeType(self, ctx:StarRocksParser.PrivilegeTypeContext):
        pass

    # Exit a parse tree produced by StarRocksParser#privilegeType.
    def exitPrivilegeType(self, ctx:StarRocksParser.PrivilegeTypeContext):
        pass


    # Enter a parse tree produced by StarRocksParser#privObjectType.
    def enterPrivObjectType(self, ctx:StarRocksParser.PrivObjectTypeContext):
        pass

    # Exit a parse tree produced by StarRocksParser#privObjectType.
    def exitPrivObjectType(self, ctx:StarRocksParser.PrivObjectTypeContext):
        pass


    # Enter a parse tree produced by StarRocksParser#privObjectTypePlural.
    def enterPrivObjectTypePlural(self, ctx:StarRocksParser.PrivObjectTypePluralContext):
        pass

    # Exit a parse tree produced by StarRocksParser#privObjectTypePlural.
    def exitPrivObjectTypePlural(self, ctx:StarRocksParser.PrivObjectTypePluralContext):
        pass


    # Enter a parse tree produced by StarRocksParser#backupStatement.
    def enterBackupStatement(self, ctx:StarRocksParser.BackupStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#backupStatement.
    def exitBackupStatement(self, ctx:StarRocksParser.BackupStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#cancelBackupStatement.
    def enterCancelBackupStatement(self, ctx:StarRocksParser.CancelBackupStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#cancelBackupStatement.
    def exitCancelBackupStatement(self, ctx:StarRocksParser.CancelBackupStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#showBackupStatement.
    def enterShowBackupStatement(self, ctx:StarRocksParser.ShowBackupStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#showBackupStatement.
    def exitShowBackupStatement(self, ctx:StarRocksParser.ShowBackupStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#restoreStatement.
    def enterRestoreStatement(self, ctx:StarRocksParser.RestoreStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#restoreStatement.
    def exitRestoreStatement(self, ctx:StarRocksParser.RestoreStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#cancelRestoreStatement.
    def enterCancelRestoreStatement(self, ctx:StarRocksParser.CancelRestoreStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#cancelRestoreStatement.
    def exitCancelRestoreStatement(self, ctx:StarRocksParser.CancelRestoreStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#showRestoreStatement.
    def enterShowRestoreStatement(self, ctx:StarRocksParser.ShowRestoreStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#showRestoreStatement.
    def exitShowRestoreStatement(self, ctx:StarRocksParser.ShowRestoreStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#showSnapshotStatement.
    def enterShowSnapshotStatement(self, ctx:StarRocksParser.ShowSnapshotStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#showSnapshotStatement.
    def exitShowSnapshotStatement(self, ctx:StarRocksParser.ShowSnapshotStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#createRepositoryStatement.
    def enterCreateRepositoryStatement(self, ctx:StarRocksParser.CreateRepositoryStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#createRepositoryStatement.
    def exitCreateRepositoryStatement(self, ctx:StarRocksParser.CreateRepositoryStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#dropRepositoryStatement.
    def enterDropRepositoryStatement(self, ctx:StarRocksParser.DropRepositoryStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#dropRepositoryStatement.
    def exitDropRepositoryStatement(self, ctx:StarRocksParser.DropRepositoryStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#addSqlBlackListStatement.
    def enterAddSqlBlackListStatement(self, ctx:StarRocksParser.AddSqlBlackListStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#addSqlBlackListStatement.
    def exitAddSqlBlackListStatement(self, ctx:StarRocksParser.AddSqlBlackListStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#delSqlBlackListStatement.
    def enterDelSqlBlackListStatement(self, ctx:StarRocksParser.DelSqlBlackListStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#delSqlBlackListStatement.
    def exitDelSqlBlackListStatement(self, ctx:StarRocksParser.DelSqlBlackListStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#showSqlBlackListStatement.
    def enterShowSqlBlackListStatement(self, ctx:StarRocksParser.ShowSqlBlackListStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#showSqlBlackListStatement.
    def exitShowSqlBlackListStatement(self, ctx:StarRocksParser.ShowSqlBlackListStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#showWhiteListStatement.
    def enterShowWhiteListStatement(self, ctx:StarRocksParser.ShowWhiteListStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#showWhiteListStatement.
    def exitShowWhiteListStatement(self, ctx:StarRocksParser.ShowWhiteListStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#addBackendBlackListStatement.
    def enterAddBackendBlackListStatement(self, ctx:StarRocksParser.AddBackendBlackListStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#addBackendBlackListStatement.
    def exitAddBackendBlackListStatement(self, ctx:StarRocksParser.AddBackendBlackListStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#delBackendBlackListStatement.
    def enterDelBackendBlackListStatement(self, ctx:StarRocksParser.DelBackendBlackListStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#delBackendBlackListStatement.
    def exitDelBackendBlackListStatement(self, ctx:StarRocksParser.DelBackendBlackListStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#showBackendBlackListStatement.
    def enterShowBackendBlackListStatement(self, ctx:StarRocksParser.ShowBackendBlackListStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#showBackendBlackListStatement.
    def exitShowBackendBlackListStatement(self, ctx:StarRocksParser.ShowBackendBlackListStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#dataCacheTarget.
    def enterDataCacheTarget(self, ctx:StarRocksParser.DataCacheTargetContext):
        pass

    # Exit a parse tree produced by StarRocksParser#dataCacheTarget.
    def exitDataCacheTarget(self, ctx:StarRocksParser.DataCacheTargetContext):
        pass


    # Enter a parse tree produced by StarRocksParser#createDataCacheRuleStatement.
    def enterCreateDataCacheRuleStatement(self, ctx:StarRocksParser.CreateDataCacheRuleStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#createDataCacheRuleStatement.
    def exitCreateDataCacheRuleStatement(self, ctx:StarRocksParser.CreateDataCacheRuleStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#showDataCacheRulesStatement.
    def enterShowDataCacheRulesStatement(self, ctx:StarRocksParser.ShowDataCacheRulesStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#showDataCacheRulesStatement.
    def exitShowDataCacheRulesStatement(self, ctx:StarRocksParser.ShowDataCacheRulesStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#dropDataCacheRuleStatement.
    def enterDropDataCacheRuleStatement(self, ctx:StarRocksParser.DropDataCacheRuleStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#dropDataCacheRuleStatement.
    def exitDropDataCacheRuleStatement(self, ctx:StarRocksParser.DropDataCacheRuleStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#clearDataCacheRulesStatement.
    def enterClearDataCacheRulesStatement(self, ctx:StarRocksParser.ClearDataCacheRulesStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#clearDataCacheRulesStatement.
    def exitClearDataCacheRulesStatement(self, ctx:StarRocksParser.ClearDataCacheRulesStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#dataCacheSelectStatement.
    def enterDataCacheSelectStatement(self, ctx:StarRocksParser.DataCacheSelectStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#dataCacheSelectStatement.
    def exitDataCacheSelectStatement(self, ctx:StarRocksParser.DataCacheSelectStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#exportStatement.
    def enterExportStatement(self, ctx:StarRocksParser.ExportStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#exportStatement.
    def exitExportStatement(self, ctx:StarRocksParser.ExportStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#cancelExportStatement.
    def enterCancelExportStatement(self, ctx:StarRocksParser.CancelExportStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#cancelExportStatement.
    def exitCancelExportStatement(self, ctx:StarRocksParser.CancelExportStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#showExportStatement.
    def enterShowExportStatement(self, ctx:StarRocksParser.ShowExportStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#showExportStatement.
    def exitShowExportStatement(self, ctx:StarRocksParser.ShowExportStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#installPluginStatement.
    def enterInstallPluginStatement(self, ctx:StarRocksParser.InstallPluginStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#installPluginStatement.
    def exitInstallPluginStatement(self, ctx:StarRocksParser.InstallPluginStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#uninstallPluginStatement.
    def enterUninstallPluginStatement(self, ctx:StarRocksParser.UninstallPluginStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#uninstallPluginStatement.
    def exitUninstallPluginStatement(self, ctx:StarRocksParser.UninstallPluginStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#createFileStatement.
    def enterCreateFileStatement(self, ctx:StarRocksParser.CreateFileStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#createFileStatement.
    def exitCreateFileStatement(self, ctx:StarRocksParser.CreateFileStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#dropFileStatement.
    def enterDropFileStatement(self, ctx:StarRocksParser.DropFileStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#dropFileStatement.
    def exitDropFileStatement(self, ctx:StarRocksParser.DropFileStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#showSmallFilesStatement.
    def enterShowSmallFilesStatement(self, ctx:StarRocksParser.ShowSmallFilesStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#showSmallFilesStatement.
    def exitShowSmallFilesStatement(self, ctx:StarRocksParser.ShowSmallFilesStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#createPipeStatement.
    def enterCreatePipeStatement(self, ctx:StarRocksParser.CreatePipeStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#createPipeStatement.
    def exitCreatePipeStatement(self, ctx:StarRocksParser.CreatePipeStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#dropPipeStatement.
    def enterDropPipeStatement(self, ctx:StarRocksParser.DropPipeStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#dropPipeStatement.
    def exitDropPipeStatement(self, ctx:StarRocksParser.DropPipeStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#alterPipeClause.
    def enterAlterPipeClause(self, ctx:StarRocksParser.AlterPipeClauseContext):
        pass

    # Exit a parse tree produced by StarRocksParser#alterPipeClause.
    def exitAlterPipeClause(self, ctx:StarRocksParser.AlterPipeClauseContext):
        pass


    # Enter a parse tree produced by StarRocksParser#alterPipeStatement.
    def enterAlterPipeStatement(self, ctx:StarRocksParser.AlterPipeStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#alterPipeStatement.
    def exitAlterPipeStatement(self, ctx:StarRocksParser.AlterPipeStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#descPipeStatement.
    def enterDescPipeStatement(self, ctx:StarRocksParser.DescPipeStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#descPipeStatement.
    def exitDescPipeStatement(self, ctx:StarRocksParser.DescPipeStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#showPipeStatement.
    def enterShowPipeStatement(self, ctx:StarRocksParser.ShowPipeStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#showPipeStatement.
    def exitShowPipeStatement(self, ctx:StarRocksParser.ShowPipeStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#setStatement.
    def enterSetStatement(self, ctx:StarRocksParser.SetStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#setStatement.
    def exitSetStatement(self, ctx:StarRocksParser.SetStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#setNames.
    def enterSetNames(self, ctx:StarRocksParser.SetNamesContext):
        pass

    # Exit a parse tree produced by StarRocksParser#setNames.
    def exitSetNames(self, ctx:StarRocksParser.SetNamesContext):
        pass


    # Enter a parse tree produced by StarRocksParser#setPassword.
    def enterSetPassword(self, ctx:StarRocksParser.SetPasswordContext):
        pass

    # Exit a parse tree produced by StarRocksParser#setPassword.
    def exitSetPassword(self, ctx:StarRocksParser.SetPasswordContext):
        pass


    # Enter a parse tree produced by StarRocksParser#setUserVar.
    def enterSetUserVar(self, ctx:StarRocksParser.SetUserVarContext):
        pass

    # Exit a parse tree produced by StarRocksParser#setUserVar.
    def exitSetUserVar(self, ctx:StarRocksParser.SetUserVarContext):
        pass


    # Enter a parse tree produced by StarRocksParser#setSystemVar.
    def enterSetSystemVar(self, ctx:StarRocksParser.SetSystemVarContext):
        pass

    # Exit a parse tree produced by StarRocksParser#setSystemVar.
    def exitSetSystemVar(self, ctx:StarRocksParser.SetSystemVarContext):
        pass


    # Enter a parse tree produced by StarRocksParser#setTransaction.
    def enterSetTransaction(self, ctx:StarRocksParser.SetTransactionContext):
        pass

    # Exit a parse tree produced by StarRocksParser#setTransaction.
    def exitSetTransaction(self, ctx:StarRocksParser.SetTransactionContext):
        pass


    # Enter a parse tree produced by StarRocksParser#transaction_characteristics.
    def enterTransaction_characteristics(self, ctx:StarRocksParser.Transaction_characteristicsContext):
        pass

    # Exit a parse tree produced by StarRocksParser#transaction_characteristics.
    def exitTransaction_characteristics(self, ctx:StarRocksParser.Transaction_characteristicsContext):
        pass


    # Enter a parse tree produced by StarRocksParser#transaction_access_mode.
    def enterTransaction_access_mode(self, ctx:StarRocksParser.Transaction_access_modeContext):
        pass

    # Exit a parse tree produced by StarRocksParser#transaction_access_mode.
    def exitTransaction_access_mode(self, ctx:StarRocksParser.Transaction_access_modeContext):
        pass


    # Enter a parse tree produced by StarRocksParser#isolation_level.
    def enterIsolation_level(self, ctx:StarRocksParser.Isolation_levelContext):
        pass

    # Exit a parse tree produced by StarRocksParser#isolation_level.
    def exitIsolation_level(self, ctx:StarRocksParser.Isolation_levelContext):
        pass


    # Enter a parse tree produced by StarRocksParser#isolation_types.
    def enterIsolation_types(self, ctx:StarRocksParser.Isolation_typesContext):
        pass

    # Exit a parse tree produced by StarRocksParser#isolation_types.
    def exitIsolation_types(self, ctx:StarRocksParser.Isolation_typesContext):
        pass


    # Enter a parse tree produced by StarRocksParser#setExprOrDefault.
    def enterSetExprOrDefault(self, ctx:StarRocksParser.SetExprOrDefaultContext):
        pass

    # Exit a parse tree produced by StarRocksParser#setExprOrDefault.
    def exitSetExprOrDefault(self, ctx:StarRocksParser.SetExprOrDefaultContext):
        pass


    # Enter a parse tree produced by StarRocksParser#setUserPropertyStatement.
    def enterSetUserPropertyStatement(self, ctx:StarRocksParser.SetUserPropertyStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#setUserPropertyStatement.
    def exitSetUserPropertyStatement(self, ctx:StarRocksParser.SetUserPropertyStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#roleList.
    def enterRoleList(self, ctx:StarRocksParser.RoleListContext):
        pass

    # Exit a parse tree produced by StarRocksParser#roleList.
    def exitRoleList(self, ctx:StarRocksParser.RoleListContext):
        pass


    # Enter a parse tree produced by StarRocksParser#executeScriptStatement.
    def enterExecuteScriptStatement(self, ctx:StarRocksParser.ExecuteScriptStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#executeScriptStatement.
    def exitExecuteScriptStatement(self, ctx:StarRocksParser.ExecuteScriptStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#unsupportedStatement.
    def enterUnsupportedStatement(self, ctx:StarRocksParser.UnsupportedStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#unsupportedStatement.
    def exitUnsupportedStatement(self, ctx:StarRocksParser.UnsupportedStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#lock_item.
    def enterLock_item(self, ctx:StarRocksParser.Lock_itemContext):
        pass

    # Exit a parse tree produced by StarRocksParser#lock_item.
    def exitLock_item(self, ctx:StarRocksParser.Lock_itemContext):
        pass


    # Enter a parse tree produced by StarRocksParser#lock_type.
    def enterLock_type(self, ctx:StarRocksParser.Lock_typeContext):
        pass

    # Exit a parse tree produced by StarRocksParser#lock_type.
    def exitLock_type(self, ctx:StarRocksParser.Lock_typeContext):
        pass


    # Enter a parse tree produced by StarRocksParser#queryStatement.
    def enterQueryStatement(self, ctx:StarRocksParser.QueryStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#queryStatement.
    def exitQueryStatement(self, ctx:StarRocksParser.QueryStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#queryRelation.
    def enterQueryRelation(self, ctx:StarRocksParser.QueryRelationContext):
        pass

    # Exit a parse tree produced by StarRocksParser#queryRelation.
    def exitQueryRelation(self, ctx:StarRocksParser.QueryRelationContext):
        pass


    # Enter a parse tree produced by StarRocksParser#withClause.
    def enterWithClause(self, ctx:StarRocksParser.WithClauseContext):
        pass

    # Exit a parse tree produced by StarRocksParser#withClause.
    def exitWithClause(self, ctx:StarRocksParser.WithClauseContext):
        pass


    # Enter a parse tree produced by StarRocksParser#queryNoWith.
    def enterQueryNoWith(self, ctx:StarRocksParser.QueryNoWithContext):
        pass

    # Exit a parse tree produced by StarRocksParser#queryNoWith.
    def exitQueryNoWith(self, ctx:StarRocksParser.QueryNoWithContext):
        pass


    # Enter a parse tree produced by StarRocksParser#temporalClause.
    def enterTemporalClause(self, ctx:StarRocksParser.TemporalClauseContext):
        pass

    # Exit a parse tree produced by StarRocksParser#temporalClause.
    def exitTemporalClause(self, ctx:StarRocksParser.TemporalClauseContext):
        pass


    # Enter a parse tree produced by StarRocksParser#queryWithParentheses.
    def enterQueryWithParentheses(self, ctx:StarRocksParser.QueryWithParenthesesContext):
        pass

    # Exit a parse tree produced by StarRocksParser#queryWithParentheses.
    def exitQueryWithParentheses(self, ctx:StarRocksParser.QueryWithParenthesesContext):
        pass


    # Enter a parse tree produced by StarRocksParser#setOperation.
    def enterSetOperation(self, ctx:StarRocksParser.SetOperationContext):
        pass

    # Exit a parse tree produced by StarRocksParser#setOperation.
    def exitSetOperation(self, ctx:StarRocksParser.SetOperationContext):
        pass


    # Enter a parse tree produced by StarRocksParser#queryPrimaryDefault.
    def enterQueryPrimaryDefault(self, ctx:StarRocksParser.QueryPrimaryDefaultContext):
        pass

    # Exit a parse tree produced by StarRocksParser#queryPrimaryDefault.
    def exitQueryPrimaryDefault(self, ctx:StarRocksParser.QueryPrimaryDefaultContext):
        pass


    # Enter a parse tree produced by StarRocksParser#subquery.
    def enterSubquery(self, ctx:StarRocksParser.SubqueryContext):
        pass

    # Exit a parse tree produced by StarRocksParser#subquery.
    def exitSubquery(self, ctx:StarRocksParser.SubqueryContext):
        pass


    # Enter a parse tree produced by StarRocksParser#rowConstructor.
    def enterRowConstructor(self, ctx:StarRocksParser.RowConstructorContext):
        pass

    # Exit a parse tree produced by StarRocksParser#rowConstructor.
    def exitRowConstructor(self, ctx:StarRocksParser.RowConstructorContext):
        pass


    # Enter a parse tree produced by StarRocksParser#sortItem.
    def enterSortItem(self, ctx:StarRocksParser.SortItemContext):
        pass

    # Exit a parse tree produced by StarRocksParser#sortItem.
    def exitSortItem(self, ctx:StarRocksParser.SortItemContext):
        pass


    # Enter a parse tree produced by StarRocksParser#limitElement.
    def enterLimitElement(self, ctx:StarRocksParser.LimitElementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#limitElement.
    def exitLimitElement(self, ctx:StarRocksParser.LimitElementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#querySpecification.
    def enterQuerySpecification(self, ctx:StarRocksParser.QuerySpecificationContext):
        pass

    # Exit a parse tree produced by StarRocksParser#querySpecification.
    def exitQuerySpecification(self, ctx:StarRocksParser.QuerySpecificationContext):
        pass


    # Enter a parse tree produced by StarRocksParser#from.
    def enterFrom(self, ctx:StarRocksParser.FromContext):
        pass

    # Exit a parse tree produced by StarRocksParser#from.
    def exitFrom(self, ctx:StarRocksParser.FromContext):
        pass


    # Enter a parse tree produced by StarRocksParser#dual.
    def enterDual(self, ctx:StarRocksParser.DualContext):
        pass

    # Exit a parse tree produced by StarRocksParser#dual.
    def exitDual(self, ctx:StarRocksParser.DualContext):
        pass


    # Enter a parse tree produced by StarRocksParser#rollup.
    def enterRollup(self, ctx:StarRocksParser.RollupContext):
        pass

    # Exit a parse tree produced by StarRocksParser#rollup.
    def exitRollup(self, ctx:StarRocksParser.RollupContext):
        pass


    # Enter a parse tree produced by StarRocksParser#cube.
    def enterCube(self, ctx:StarRocksParser.CubeContext):
        pass

    # Exit a parse tree produced by StarRocksParser#cube.
    def exitCube(self, ctx:StarRocksParser.CubeContext):
        pass


    # Enter a parse tree produced by StarRocksParser#multipleGroupingSets.
    def enterMultipleGroupingSets(self, ctx:StarRocksParser.MultipleGroupingSetsContext):
        pass

    # Exit a parse tree produced by StarRocksParser#multipleGroupingSets.
    def exitMultipleGroupingSets(self, ctx:StarRocksParser.MultipleGroupingSetsContext):
        pass


    # Enter a parse tree produced by StarRocksParser#singleGroupingSet.
    def enterSingleGroupingSet(self, ctx:StarRocksParser.SingleGroupingSetContext):
        pass

    # Exit a parse tree produced by StarRocksParser#singleGroupingSet.
    def exitSingleGroupingSet(self, ctx:StarRocksParser.SingleGroupingSetContext):
        pass


    # Enter a parse tree produced by StarRocksParser#groupingSet.
    def enterGroupingSet(self, ctx:StarRocksParser.GroupingSetContext):
        pass

    # Exit a parse tree produced by StarRocksParser#groupingSet.
    def exitGroupingSet(self, ctx:StarRocksParser.GroupingSetContext):
        pass


    # Enter a parse tree produced by StarRocksParser#commonTableExpression.
    def enterCommonTableExpression(self, ctx:StarRocksParser.CommonTableExpressionContext):
        pass

    # Exit a parse tree produced by StarRocksParser#commonTableExpression.
    def exitCommonTableExpression(self, ctx:StarRocksParser.CommonTableExpressionContext):
        pass


    # Enter a parse tree produced by StarRocksParser#setQuantifier.
    def enterSetQuantifier(self, ctx:StarRocksParser.SetQuantifierContext):
        pass

    # Exit a parse tree produced by StarRocksParser#setQuantifier.
    def exitSetQuantifier(self, ctx:StarRocksParser.SetQuantifierContext):
        pass


    # Enter a parse tree produced by StarRocksParser#selectSingle.
    def enterSelectSingle(self, ctx:StarRocksParser.SelectSingleContext):
        pass

    # Exit a parse tree produced by StarRocksParser#selectSingle.
    def exitSelectSingle(self, ctx:StarRocksParser.SelectSingleContext):
        pass


    # Enter a parse tree produced by StarRocksParser#selectAll.
    def enterSelectAll(self, ctx:StarRocksParser.SelectAllContext):
        pass

    # Exit a parse tree produced by StarRocksParser#selectAll.
    def exitSelectAll(self, ctx:StarRocksParser.SelectAllContext):
        pass


    # Enter a parse tree produced by StarRocksParser#relations.
    def enterRelations(self, ctx:StarRocksParser.RelationsContext):
        pass

    # Exit a parse tree produced by StarRocksParser#relations.
    def exitRelations(self, ctx:StarRocksParser.RelationsContext):
        pass


    # Enter a parse tree produced by StarRocksParser#relation.
    def enterRelation(self, ctx:StarRocksParser.RelationContext):
        pass

    # Exit a parse tree produced by StarRocksParser#relation.
    def exitRelation(self, ctx:StarRocksParser.RelationContext):
        pass


    # Enter a parse tree produced by StarRocksParser#tableAtom.
    def enterTableAtom(self, ctx:StarRocksParser.TableAtomContext):
        pass

    # Exit a parse tree produced by StarRocksParser#tableAtom.
    def exitTableAtom(self, ctx:StarRocksParser.TableAtomContext):
        pass


    # Enter a parse tree produced by StarRocksParser#inlineTable.
    def enterInlineTable(self, ctx:StarRocksParser.InlineTableContext):
        pass

    # Exit a parse tree produced by StarRocksParser#inlineTable.
    def exitInlineTable(self, ctx:StarRocksParser.InlineTableContext):
        pass


    # Enter a parse tree produced by StarRocksParser#subqueryWithAlias.
    def enterSubqueryWithAlias(self, ctx:StarRocksParser.SubqueryWithAliasContext):
        pass

    # Exit a parse tree produced by StarRocksParser#subqueryWithAlias.
    def exitSubqueryWithAlias(self, ctx:StarRocksParser.SubqueryWithAliasContext):
        pass


    # Enter a parse tree produced by StarRocksParser#tableFunction.
    def enterTableFunction(self, ctx:StarRocksParser.TableFunctionContext):
        pass

    # Exit a parse tree produced by StarRocksParser#tableFunction.
    def exitTableFunction(self, ctx:StarRocksParser.TableFunctionContext):
        pass


    # Enter a parse tree produced by StarRocksParser#normalizedTableFunction.
    def enterNormalizedTableFunction(self, ctx:StarRocksParser.NormalizedTableFunctionContext):
        pass

    # Exit a parse tree produced by StarRocksParser#normalizedTableFunction.
    def exitNormalizedTableFunction(self, ctx:StarRocksParser.NormalizedTableFunctionContext):
        pass


    # Enter a parse tree produced by StarRocksParser#fileTableFunction.
    def enterFileTableFunction(self, ctx:StarRocksParser.FileTableFunctionContext):
        pass

    # Exit a parse tree produced by StarRocksParser#fileTableFunction.
    def exitFileTableFunction(self, ctx:StarRocksParser.FileTableFunctionContext):
        pass


    # Enter a parse tree produced by StarRocksParser#parenthesizedRelation.
    def enterParenthesizedRelation(self, ctx:StarRocksParser.ParenthesizedRelationContext):
        pass

    # Exit a parse tree produced by StarRocksParser#parenthesizedRelation.
    def exitParenthesizedRelation(self, ctx:StarRocksParser.ParenthesizedRelationContext):
        pass


    # Enter a parse tree produced by StarRocksParser#pivotClause.
    def enterPivotClause(self, ctx:StarRocksParser.PivotClauseContext):
        pass

    # Exit a parse tree produced by StarRocksParser#pivotClause.
    def exitPivotClause(self, ctx:StarRocksParser.PivotClauseContext):
        pass


    # Enter a parse tree produced by StarRocksParser#pivotAggregationExpression.
    def enterPivotAggregationExpression(self, ctx:StarRocksParser.PivotAggregationExpressionContext):
        pass

    # Exit a parse tree produced by StarRocksParser#pivotAggregationExpression.
    def exitPivotAggregationExpression(self, ctx:StarRocksParser.PivotAggregationExpressionContext):
        pass


    # Enter a parse tree produced by StarRocksParser#pivotValue.
    def enterPivotValue(self, ctx:StarRocksParser.PivotValueContext):
        pass

    # Exit a parse tree produced by StarRocksParser#pivotValue.
    def exitPivotValue(self, ctx:StarRocksParser.PivotValueContext):
        pass


    # Enter a parse tree produced by StarRocksParser#argumentList.
    def enterArgumentList(self, ctx:StarRocksParser.ArgumentListContext):
        pass

    # Exit a parse tree produced by StarRocksParser#argumentList.
    def exitArgumentList(self, ctx:StarRocksParser.ArgumentListContext):
        pass


    # Enter a parse tree produced by StarRocksParser#joinRelation.
    def enterJoinRelation(self, ctx:StarRocksParser.JoinRelationContext):
        pass

    # Exit a parse tree produced by StarRocksParser#joinRelation.
    def exitJoinRelation(self, ctx:StarRocksParser.JoinRelationContext):
        pass


    # Enter a parse tree produced by StarRocksParser#crossOrInnerJoinType.
    def enterCrossOrInnerJoinType(self, ctx:StarRocksParser.CrossOrInnerJoinTypeContext):
        pass

    # Exit a parse tree produced by StarRocksParser#crossOrInnerJoinType.
    def exitCrossOrInnerJoinType(self, ctx:StarRocksParser.CrossOrInnerJoinTypeContext):
        pass


    # Enter a parse tree produced by StarRocksParser#outerAndSemiJoinType.
    def enterOuterAndSemiJoinType(self, ctx:StarRocksParser.OuterAndSemiJoinTypeContext):
        pass

    # Exit a parse tree produced by StarRocksParser#outerAndSemiJoinType.
    def exitOuterAndSemiJoinType(self, ctx:StarRocksParser.OuterAndSemiJoinTypeContext):
        pass


    # Enter a parse tree produced by StarRocksParser#bracketHint.
    def enterBracketHint(self, ctx:StarRocksParser.BracketHintContext):
        pass

    # Exit a parse tree produced by StarRocksParser#bracketHint.
    def exitBracketHint(self, ctx:StarRocksParser.BracketHintContext):
        pass


    # Enter a parse tree produced by StarRocksParser#hintMap.
    def enterHintMap(self, ctx:StarRocksParser.HintMapContext):
        pass

    # Exit a parse tree produced by StarRocksParser#hintMap.
    def exitHintMap(self, ctx:StarRocksParser.HintMapContext):
        pass


    # Enter a parse tree produced by StarRocksParser#joinCriteria.
    def enterJoinCriteria(self, ctx:StarRocksParser.JoinCriteriaContext):
        pass

    # Exit a parse tree produced by StarRocksParser#joinCriteria.
    def exitJoinCriteria(self, ctx:StarRocksParser.JoinCriteriaContext):
        pass


    # Enter a parse tree produced by StarRocksParser#columnAliases.
    def enterColumnAliases(self, ctx:StarRocksParser.ColumnAliasesContext):
        pass

    # Exit a parse tree produced by StarRocksParser#columnAliases.
    def exitColumnAliases(self, ctx:StarRocksParser.ColumnAliasesContext):
        pass


    # Enter a parse tree produced by StarRocksParser#partitionNames.
    def enterPartitionNames(self, ctx:StarRocksParser.PartitionNamesContext):
        pass

    # Exit a parse tree produced by StarRocksParser#partitionNames.
    def exitPartitionNames(self, ctx:StarRocksParser.PartitionNamesContext):
        pass


    # Enter a parse tree produced by StarRocksParser#keyPartitionList.
    def enterKeyPartitionList(self, ctx:StarRocksParser.KeyPartitionListContext):
        pass

    # Exit a parse tree produced by StarRocksParser#keyPartitionList.
    def exitKeyPartitionList(self, ctx:StarRocksParser.KeyPartitionListContext):
        pass


    # Enter a parse tree produced by StarRocksParser#tabletList.
    def enterTabletList(self, ctx:StarRocksParser.TabletListContext):
        pass

    # Exit a parse tree produced by StarRocksParser#tabletList.
    def exitTabletList(self, ctx:StarRocksParser.TabletListContext):
        pass


    # Enter a parse tree produced by StarRocksParser#prepareStatement.
    def enterPrepareStatement(self, ctx:StarRocksParser.PrepareStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#prepareStatement.
    def exitPrepareStatement(self, ctx:StarRocksParser.PrepareStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#prepareSql.
    def enterPrepareSql(self, ctx:StarRocksParser.PrepareSqlContext):
        pass

    # Exit a parse tree produced by StarRocksParser#prepareSql.
    def exitPrepareSql(self, ctx:StarRocksParser.PrepareSqlContext):
        pass


    # Enter a parse tree produced by StarRocksParser#executeStatement.
    def enterExecuteStatement(self, ctx:StarRocksParser.ExecuteStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#executeStatement.
    def exitExecuteStatement(self, ctx:StarRocksParser.ExecuteStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#deallocateStatement.
    def enterDeallocateStatement(self, ctx:StarRocksParser.DeallocateStatementContext):
        pass

    # Exit a parse tree produced by StarRocksParser#deallocateStatement.
    def exitDeallocateStatement(self, ctx:StarRocksParser.DeallocateStatementContext):
        pass


    # Enter a parse tree produced by StarRocksParser#replicaList.
    def enterReplicaList(self, ctx:StarRocksParser.ReplicaListContext):
        pass

    # Exit a parse tree produced by StarRocksParser#replicaList.
    def exitReplicaList(self, ctx:StarRocksParser.ReplicaListContext):
        pass


    # Enter a parse tree produced by StarRocksParser#expressionsWithDefault.
    def enterExpressionsWithDefault(self, ctx:StarRocksParser.ExpressionsWithDefaultContext):
        pass

    # Exit a parse tree produced by StarRocksParser#expressionsWithDefault.
    def exitExpressionsWithDefault(self, ctx:StarRocksParser.ExpressionsWithDefaultContext):
        pass


    # Enter a parse tree produced by StarRocksParser#expressionOrDefault.
    def enterExpressionOrDefault(self, ctx:StarRocksParser.ExpressionOrDefaultContext):
        pass

    # Exit a parse tree produced by StarRocksParser#expressionOrDefault.
    def exitExpressionOrDefault(self, ctx:StarRocksParser.ExpressionOrDefaultContext):
        pass


    # Enter a parse tree produced by StarRocksParser#mapExpressionList.
    def enterMapExpressionList(self, ctx:StarRocksParser.MapExpressionListContext):
        pass

    # Exit a parse tree produced by StarRocksParser#mapExpressionList.
    def exitMapExpressionList(self, ctx:StarRocksParser.MapExpressionListContext):
        pass


    # Enter a parse tree produced by StarRocksParser#mapExpression.
    def enterMapExpression(self, ctx:StarRocksParser.MapExpressionContext):
        pass

    # Exit a parse tree produced by StarRocksParser#mapExpression.
    def exitMapExpression(self, ctx:StarRocksParser.MapExpressionContext):
        pass


    # Enter a parse tree produced by StarRocksParser#expressionSingleton.
    def enterExpressionSingleton(self, ctx:StarRocksParser.ExpressionSingletonContext):
        pass

    # Exit a parse tree produced by StarRocksParser#expressionSingleton.
    def exitExpressionSingleton(self, ctx:StarRocksParser.ExpressionSingletonContext):
        pass


    # Enter a parse tree produced by StarRocksParser#expressionDefault.
    def enterExpressionDefault(self, ctx:StarRocksParser.ExpressionDefaultContext):
        pass

    # Exit a parse tree produced by StarRocksParser#expressionDefault.
    def exitExpressionDefault(self, ctx:StarRocksParser.ExpressionDefaultContext):
        pass


    # Enter a parse tree produced by StarRocksParser#logicalNot.
    def enterLogicalNot(self, ctx:StarRocksParser.LogicalNotContext):
        pass

    # Exit a parse tree produced by StarRocksParser#logicalNot.
    def exitLogicalNot(self, ctx:StarRocksParser.LogicalNotContext):
        pass


    # Enter a parse tree produced by StarRocksParser#logicalBinary.
    def enterLogicalBinary(self, ctx:StarRocksParser.LogicalBinaryContext):
        pass

    # Exit a parse tree produced by StarRocksParser#logicalBinary.
    def exitLogicalBinary(self, ctx:StarRocksParser.LogicalBinaryContext):
        pass


    # Enter a parse tree produced by StarRocksParser#expressionList.
    def enterExpressionList(self, ctx:StarRocksParser.ExpressionListContext):
        pass

    # Exit a parse tree produced by StarRocksParser#expressionList.
    def exitExpressionList(self, ctx:StarRocksParser.ExpressionListContext):
        pass


    # Enter a parse tree produced by StarRocksParser#comparison.
    def enterComparison(self, ctx:StarRocksParser.ComparisonContext):
        pass

    # Exit a parse tree produced by StarRocksParser#comparison.
    def exitComparison(self, ctx:StarRocksParser.ComparisonContext):
        pass


    # Enter a parse tree produced by StarRocksParser#booleanExpressionDefault.
    def enterBooleanExpressionDefault(self, ctx:StarRocksParser.BooleanExpressionDefaultContext):
        pass

    # Exit a parse tree produced by StarRocksParser#booleanExpressionDefault.
    def exitBooleanExpressionDefault(self, ctx:StarRocksParser.BooleanExpressionDefaultContext):
        pass


    # Enter a parse tree produced by StarRocksParser#isNull.
    def enterIsNull(self, ctx:StarRocksParser.IsNullContext):
        pass

    # Exit a parse tree produced by StarRocksParser#isNull.
    def exitIsNull(self, ctx:StarRocksParser.IsNullContext):
        pass


    # Enter a parse tree produced by StarRocksParser#scalarSubquery.
    def enterScalarSubquery(self, ctx:StarRocksParser.ScalarSubqueryContext):
        pass

    # Exit a parse tree produced by StarRocksParser#scalarSubquery.
    def exitScalarSubquery(self, ctx:StarRocksParser.ScalarSubqueryContext):
        pass


    # Enter a parse tree produced by StarRocksParser#predicate.
    def enterPredicate(self, ctx:StarRocksParser.PredicateContext):
        pass

    # Exit a parse tree produced by StarRocksParser#predicate.
    def exitPredicate(self, ctx:StarRocksParser.PredicateContext):
        pass


    # Enter a parse tree produced by StarRocksParser#tupleInSubquery.
    def enterTupleInSubquery(self, ctx:StarRocksParser.TupleInSubqueryContext):
        pass

    # Exit a parse tree produced by StarRocksParser#tupleInSubquery.
    def exitTupleInSubquery(self, ctx:StarRocksParser.TupleInSubqueryContext):
        pass


    # Enter a parse tree produced by StarRocksParser#inSubquery.
    def enterInSubquery(self, ctx:StarRocksParser.InSubqueryContext):
        pass

    # Exit a parse tree produced by StarRocksParser#inSubquery.
    def exitInSubquery(self, ctx:StarRocksParser.InSubqueryContext):
        pass


    # Enter a parse tree produced by StarRocksParser#inList.
    def enterInList(self, ctx:StarRocksParser.InListContext):
        pass

    # Exit a parse tree produced by StarRocksParser#inList.
    def exitInList(self, ctx:StarRocksParser.InListContext):
        pass


    # Enter a parse tree produced by StarRocksParser#between.
    def enterBetween(self, ctx:StarRocksParser.BetweenContext):
        pass

    # Exit a parse tree produced by StarRocksParser#between.
    def exitBetween(self, ctx:StarRocksParser.BetweenContext):
        pass


    # Enter a parse tree produced by StarRocksParser#like.
    def enterLike(self, ctx:StarRocksParser.LikeContext):
        pass

    # Exit a parse tree produced by StarRocksParser#like.
    def exitLike(self, ctx:StarRocksParser.LikeContext):
        pass


    # Enter a parse tree produced by StarRocksParser#valueExpressionDefault.
    def enterValueExpressionDefault(self, ctx:StarRocksParser.ValueExpressionDefaultContext):
        pass

    # Exit a parse tree produced by StarRocksParser#valueExpressionDefault.
    def exitValueExpressionDefault(self, ctx:StarRocksParser.ValueExpressionDefaultContext):
        pass


    # Enter a parse tree produced by StarRocksParser#arithmeticBinary.
    def enterArithmeticBinary(self, ctx:StarRocksParser.ArithmeticBinaryContext):
        pass

    # Exit a parse tree produced by StarRocksParser#arithmeticBinary.
    def exitArithmeticBinary(self, ctx:StarRocksParser.ArithmeticBinaryContext):
        pass


    # Enter a parse tree produced by StarRocksParser#dereference.
    def enterDereference(self, ctx:StarRocksParser.DereferenceContext):
        pass

    # Exit a parse tree produced by StarRocksParser#dereference.
    def exitDereference(self, ctx:StarRocksParser.DereferenceContext):
        pass


    # Enter a parse tree produced by StarRocksParser#odbcFunctionCallExpression.
    def enterOdbcFunctionCallExpression(self, ctx:StarRocksParser.OdbcFunctionCallExpressionContext):
        pass

    # Exit a parse tree produced by StarRocksParser#odbcFunctionCallExpression.
    def exitOdbcFunctionCallExpression(self, ctx:StarRocksParser.OdbcFunctionCallExpressionContext):
        pass


    # Enter a parse tree produced by StarRocksParser#matchExpr.
    def enterMatchExpr(self, ctx:StarRocksParser.MatchExprContext):
        pass

    # Exit a parse tree produced by StarRocksParser#matchExpr.
    def exitMatchExpr(self, ctx:StarRocksParser.MatchExprContext):
        pass


    # Enter a parse tree produced by StarRocksParser#columnRef.
    def enterColumnRef(self, ctx:StarRocksParser.ColumnRefContext):
        pass

    # Exit a parse tree produced by StarRocksParser#columnRef.
    def exitColumnRef(self, ctx:StarRocksParser.ColumnRefContext):
        pass


    # Enter a parse tree produced by StarRocksParser#convert.
    def enterConvert(self, ctx:StarRocksParser.ConvertContext):
        pass

    # Exit a parse tree produced by StarRocksParser#convert.
    def exitConvert(self, ctx:StarRocksParser.ConvertContext):
        pass


    # Enter a parse tree produced by StarRocksParser#collectionSubscript.
    def enterCollectionSubscript(self, ctx:StarRocksParser.CollectionSubscriptContext):
        pass

    # Exit a parse tree produced by StarRocksParser#collectionSubscript.
    def exitCollectionSubscript(self, ctx:StarRocksParser.CollectionSubscriptContext):
        pass


    # Enter a parse tree produced by StarRocksParser#literal.
    def enterLiteral(self, ctx:StarRocksParser.LiteralContext):
        pass

    # Exit a parse tree produced by StarRocksParser#literal.
    def exitLiteral(self, ctx:StarRocksParser.LiteralContext):
        pass


    # Enter a parse tree produced by StarRocksParser#cast.
    def enterCast(self, ctx:StarRocksParser.CastContext):
        pass

    # Exit a parse tree produced by StarRocksParser#cast.
    def exitCast(self, ctx:StarRocksParser.CastContext):
        pass


    # Enter a parse tree produced by StarRocksParser#parenthesizedExpression.
    def enterParenthesizedExpression(self, ctx:StarRocksParser.ParenthesizedExpressionContext):
        pass

    # Exit a parse tree produced by StarRocksParser#parenthesizedExpression.
    def exitParenthesizedExpression(self, ctx:StarRocksParser.ParenthesizedExpressionContext):
        pass


    # Enter a parse tree produced by StarRocksParser#userVariableExpression.
    def enterUserVariableExpression(self, ctx:StarRocksParser.UserVariableExpressionContext):
        pass

    # Exit a parse tree produced by StarRocksParser#userVariableExpression.
    def exitUserVariableExpression(self, ctx:StarRocksParser.UserVariableExpressionContext):
        pass


    # Enter a parse tree produced by StarRocksParser#functionCallExpression.
    def enterFunctionCallExpression(self, ctx:StarRocksParser.FunctionCallExpressionContext):
        pass

    # Exit a parse tree produced by StarRocksParser#functionCallExpression.
    def exitFunctionCallExpression(self, ctx:StarRocksParser.FunctionCallExpressionContext):
        pass


    # Enter a parse tree produced by StarRocksParser#simpleCase.
    def enterSimpleCase(self, ctx:StarRocksParser.SimpleCaseContext):
        pass

    # Exit a parse tree produced by StarRocksParser#simpleCase.
    def exitSimpleCase(self, ctx:StarRocksParser.SimpleCaseContext):
        pass


    # Enter a parse tree produced by StarRocksParser#arrowExpression.
    def enterArrowExpression(self, ctx:StarRocksParser.ArrowExpressionContext):
        pass

    # Exit a parse tree produced by StarRocksParser#arrowExpression.
    def exitArrowExpression(self, ctx:StarRocksParser.ArrowExpressionContext):
        pass


    # Enter a parse tree produced by StarRocksParser#systemVariableExpression.
    def enterSystemVariableExpression(self, ctx:StarRocksParser.SystemVariableExpressionContext):
        pass

    # Exit a parse tree produced by StarRocksParser#systemVariableExpression.
    def exitSystemVariableExpression(self, ctx:StarRocksParser.SystemVariableExpressionContext):
        pass


    # Enter a parse tree produced by StarRocksParser#concat.
    def enterConcat(self, ctx:StarRocksParser.ConcatContext):
        pass

    # Exit a parse tree produced by StarRocksParser#concat.
    def exitConcat(self, ctx:StarRocksParser.ConcatContext):
        pass


    # Enter a parse tree produced by StarRocksParser#subqueryExpression.
    def enterSubqueryExpression(self, ctx:StarRocksParser.SubqueryExpressionContext):
        pass

    # Exit a parse tree produced by StarRocksParser#subqueryExpression.
    def exitSubqueryExpression(self, ctx:StarRocksParser.SubqueryExpressionContext):
        pass


    # Enter a parse tree produced by StarRocksParser#lambdaFunctionExpr.
    def enterLambdaFunctionExpr(self, ctx:StarRocksParser.LambdaFunctionExprContext):
        pass

    # Exit a parse tree produced by StarRocksParser#lambdaFunctionExpr.
    def exitLambdaFunctionExpr(self, ctx:StarRocksParser.LambdaFunctionExprContext):
        pass


    # Enter a parse tree produced by StarRocksParser#dictionaryGetExpr.
    def enterDictionaryGetExpr(self, ctx:StarRocksParser.DictionaryGetExprContext):
        pass

    # Exit a parse tree produced by StarRocksParser#dictionaryGetExpr.
    def exitDictionaryGetExpr(self, ctx:StarRocksParser.DictionaryGetExprContext):
        pass


    # Enter a parse tree produced by StarRocksParser#collate.
    def enterCollate(self, ctx:StarRocksParser.CollateContext):
        pass

    # Exit a parse tree produced by StarRocksParser#collate.
    def exitCollate(self, ctx:StarRocksParser.CollateContext):
        pass


    # Enter a parse tree produced by StarRocksParser#arrayConstructor.
    def enterArrayConstructor(self, ctx:StarRocksParser.ArrayConstructorContext):
        pass

    # Exit a parse tree produced by StarRocksParser#arrayConstructor.
    def exitArrayConstructor(self, ctx:StarRocksParser.ArrayConstructorContext):
        pass


    # Enter a parse tree produced by StarRocksParser#mapConstructor.
    def enterMapConstructor(self, ctx:StarRocksParser.MapConstructorContext):
        pass

    # Exit a parse tree produced by StarRocksParser#mapConstructor.
    def exitMapConstructor(self, ctx:StarRocksParser.MapConstructorContext):
        pass


    # Enter a parse tree produced by StarRocksParser#arraySlice.
    def enterArraySlice(self, ctx:StarRocksParser.ArraySliceContext):
        pass

    # Exit a parse tree produced by StarRocksParser#arraySlice.
    def exitArraySlice(self, ctx:StarRocksParser.ArraySliceContext):
        pass


    # Enter a parse tree produced by StarRocksParser#exists.
    def enterExists(self, ctx:StarRocksParser.ExistsContext):
        pass

    # Exit a parse tree produced by StarRocksParser#exists.
    def exitExists(self, ctx:StarRocksParser.ExistsContext):
        pass


    # Enter a parse tree produced by StarRocksParser#searchedCase.
    def enterSearchedCase(self, ctx:StarRocksParser.SearchedCaseContext):
        pass

    # Exit a parse tree produced by StarRocksParser#searchedCase.
    def exitSearchedCase(self, ctx:StarRocksParser.SearchedCaseContext):
        pass


    # Enter a parse tree produced by StarRocksParser#arithmeticUnary.
    def enterArithmeticUnary(self, ctx:StarRocksParser.ArithmeticUnaryContext):
        pass

    # Exit a parse tree produced by StarRocksParser#arithmeticUnary.
    def exitArithmeticUnary(self, ctx:StarRocksParser.ArithmeticUnaryContext):
        pass


    # Enter a parse tree produced by StarRocksParser#nullLiteral.
    def enterNullLiteral(self, ctx:StarRocksParser.NullLiteralContext):
        pass

    # Exit a parse tree produced by StarRocksParser#nullLiteral.
    def exitNullLiteral(self, ctx:StarRocksParser.NullLiteralContext):
        pass


    # Enter a parse tree produced by StarRocksParser#booleanLiteral.
    def enterBooleanLiteral(self, ctx:StarRocksParser.BooleanLiteralContext):
        pass

    # Exit a parse tree produced by StarRocksParser#booleanLiteral.
    def exitBooleanLiteral(self, ctx:StarRocksParser.BooleanLiteralContext):
        pass


    # Enter a parse tree produced by StarRocksParser#numericLiteral.
    def enterNumericLiteral(self, ctx:StarRocksParser.NumericLiteralContext):
        pass

    # Exit a parse tree produced by StarRocksParser#numericLiteral.
    def exitNumericLiteral(self, ctx:StarRocksParser.NumericLiteralContext):
        pass


    # Enter a parse tree produced by StarRocksParser#dateLiteral.
    def enterDateLiteral(self, ctx:StarRocksParser.DateLiteralContext):
        pass

    # Exit a parse tree produced by StarRocksParser#dateLiteral.
    def exitDateLiteral(self, ctx:StarRocksParser.DateLiteralContext):
        pass


    # Enter a parse tree produced by StarRocksParser#stringLiteral.
    def enterStringLiteral(self, ctx:StarRocksParser.StringLiteralContext):
        pass

    # Exit a parse tree produced by StarRocksParser#stringLiteral.
    def exitStringLiteral(self, ctx:StarRocksParser.StringLiteralContext):
        pass


    # Enter a parse tree produced by StarRocksParser#intervalLiteral.
    def enterIntervalLiteral(self, ctx:StarRocksParser.IntervalLiteralContext):
        pass

    # Exit a parse tree produced by StarRocksParser#intervalLiteral.
    def exitIntervalLiteral(self, ctx:StarRocksParser.IntervalLiteralContext):
        pass


    # Enter a parse tree produced by StarRocksParser#unitBoundaryLiteral.
    def enterUnitBoundaryLiteral(self, ctx:StarRocksParser.UnitBoundaryLiteralContext):
        pass

    # Exit a parse tree produced by StarRocksParser#unitBoundaryLiteral.
    def exitUnitBoundaryLiteral(self, ctx:StarRocksParser.UnitBoundaryLiteralContext):
        pass


    # Enter a parse tree produced by StarRocksParser#binaryLiteral.
    def enterBinaryLiteral(self, ctx:StarRocksParser.BinaryLiteralContext):
        pass

    # Exit a parse tree produced by StarRocksParser#binaryLiteral.
    def exitBinaryLiteral(self, ctx:StarRocksParser.BinaryLiteralContext):
        pass


    # Enter a parse tree produced by StarRocksParser#Parameter.
    def enterParameter(self, ctx:StarRocksParser.ParameterContext):
        pass

    # Exit a parse tree produced by StarRocksParser#Parameter.
    def exitParameter(self, ctx:StarRocksParser.ParameterContext):
        pass


    # Enter a parse tree produced by StarRocksParser#extract.
    def enterExtract(self, ctx:StarRocksParser.ExtractContext):
        pass

    # Exit a parse tree produced by StarRocksParser#extract.
    def exitExtract(self, ctx:StarRocksParser.ExtractContext):
        pass


    # Enter a parse tree produced by StarRocksParser#groupingOperation.
    def enterGroupingOperation(self, ctx:StarRocksParser.GroupingOperationContext):
        pass

    # Exit a parse tree produced by StarRocksParser#groupingOperation.
    def exitGroupingOperation(self, ctx:StarRocksParser.GroupingOperationContext):
        pass


    # Enter a parse tree produced by StarRocksParser#informationFunction.
    def enterInformationFunction(self, ctx:StarRocksParser.InformationFunctionContext):
        pass

    # Exit a parse tree produced by StarRocksParser#informationFunction.
    def exitInformationFunction(self, ctx:StarRocksParser.InformationFunctionContext):
        pass


    # Enter a parse tree produced by StarRocksParser#specialDateTime.
    def enterSpecialDateTime(self, ctx:StarRocksParser.SpecialDateTimeContext):
        pass

    # Exit a parse tree produced by StarRocksParser#specialDateTime.
    def exitSpecialDateTime(self, ctx:StarRocksParser.SpecialDateTimeContext):
        pass


    # Enter a parse tree produced by StarRocksParser#specialFunction.
    def enterSpecialFunction(self, ctx:StarRocksParser.SpecialFunctionContext):
        pass

    # Exit a parse tree produced by StarRocksParser#specialFunction.
    def exitSpecialFunction(self, ctx:StarRocksParser.SpecialFunctionContext):
        pass


    # Enter a parse tree produced by StarRocksParser#aggregationFunctionCall.
    def enterAggregationFunctionCall(self, ctx:StarRocksParser.AggregationFunctionCallContext):
        pass

    # Exit a parse tree produced by StarRocksParser#aggregationFunctionCall.
    def exitAggregationFunctionCall(self, ctx:StarRocksParser.AggregationFunctionCallContext):
        pass


    # Enter a parse tree produced by StarRocksParser#windowFunctionCall.
    def enterWindowFunctionCall(self, ctx:StarRocksParser.WindowFunctionCallContext):
        pass

    # Exit a parse tree produced by StarRocksParser#windowFunctionCall.
    def exitWindowFunctionCall(self, ctx:StarRocksParser.WindowFunctionCallContext):
        pass


    # Enter a parse tree produced by StarRocksParser#simpleFunctionCall.
    def enterSimpleFunctionCall(self, ctx:StarRocksParser.SimpleFunctionCallContext):
        pass

    # Exit a parse tree produced by StarRocksParser#simpleFunctionCall.
    def exitSimpleFunctionCall(self, ctx:StarRocksParser.SimpleFunctionCallContext):
        pass


    # Enter a parse tree produced by StarRocksParser#aggregationFunction.
    def enterAggregationFunction(self, ctx:StarRocksParser.AggregationFunctionContext):
        pass

    # Exit a parse tree produced by StarRocksParser#aggregationFunction.
    def exitAggregationFunction(self, ctx:StarRocksParser.AggregationFunctionContext):
        pass


    # Enter a parse tree produced by StarRocksParser#userVariable.
    def enterUserVariable(self, ctx:StarRocksParser.UserVariableContext):
        pass

    # Exit a parse tree produced by StarRocksParser#userVariable.
    def exitUserVariable(self, ctx:StarRocksParser.UserVariableContext):
        pass


    # Enter a parse tree produced by StarRocksParser#systemVariable.
    def enterSystemVariable(self, ctx:StarRocksParser.SystemVariableContext):
        pass

    # Exit a parse tree produced by StarRocksParser#systemVariable.
    def exitSystemVariable(self, ctx:StarRocksParser.SystemVariableContext):
        pass


    # Enter a parse tree produced by StarRocksParser#columnReference.
    def enterColumnReference(self, ctx:StarRocksParser.ColumnReferenceContext):
        pass

    # Exit a parse tree produced by StarRocksParser#columnReference.
    def exitColumnReference(self, ctx:StarRocksParser.ColumnReferenceContext):
        pass


    # Enter a parse tree produced by StarRocksParser#informationFunctionExpression.
    def enterInformationFunctionExpression(self, ctx:StarRocksParser.InformationFunctionExpressionContext):
        pass

    # Exit a parse tree produced by StarRocksParser#informationFunctionExpression.
    def exitInformationFunctionExpression(self, ctx:StarRocksParser.InformationFunctionExpressionContext):
        pass


    # Enter a parse tree produced by StarRocksParser#specialDateTimeExpression.
    def enterSpecialDateTimeExpression(self, ctx:StarRocksParser.SpecialDateTimeExpressionContext):
        pass

    # Exit a parse tree produced by StarRocksParser#specialDateTimeExpression.
    def exitSpecialDateTimeExpression(self, ctx:StarRocksParser.SpecialDateTimeExpressionContext):
        pass


    # Enter a parse tree produced by StarRocksParser#specialFunctionExpression.
    def enterSpecialFunctionExpression(self, ctx:StarRocksParser.SpecialFunctionExpressionContext):
        pass

    # Exit a parse tree produced by StarRocksParser#specialFunctionExpression.
    def exitSpecialFunctionExpression(self, ctx:StarRocksParser.SpecialFunctionExpressionContext):
        pass


    # Enter a parse tree produced by StarRocksParser#windowFunction.
    def enterWindowFunction(self, ctx:StarRocksParser.WindowFunctionContext):
        pass

    # Exit a parse tree produced by StarRocksParser#windowFunction.
    def exitWindowFunction(self, ctx:StarRocksParser.WindowFunctionContext):
        pass


    # Enter a parse tree produced by StarRocksParser#whenClause.
    def enterWhenClause(self, ctx:StarRocksParser.WhenClauseContext):
        pass

    # Exit a parse tree produced by StarRocksParser#whenClause.
    def exitWhenClause(self, ctx:StarRocksParser.WhenClauseContext):
        pass


    # Enter a parse tree produced by StarRocksParser#over.
    def enterOver(self, ctx:StarRocksParser.OverContext):
        pass

    # Exit a parse tree produced by StarRocksParser#over.
    def exitOver(self, ctx:StarRocksParser.OverContext):
        pass


    # Enter a parse tree produced by StarRocksParser#ignoreNulls.
    def enterIgnoreNulls(self, ctx:StarRocksParser.IgnoreNullsContext):
        pass

    # Exit a parse tree produced by StarRocksParser#ignoreNulls.
    def exitIgnoreNulls(self, ctx:StarRocksParser.IgnoreNullsContext):
        pass


    # Enter a parse tree produced by StarRocksParser#windowFrame.
    def enterWindowFrame(self, ctx:StarRocksParser.WindowFrameContext):
        pass

    # Exit a parse tree produced by StarRocksParser#windowFrame.
    def exitWindowFrame(self, ctx:StarRocksParser.WindowFrameContext):
        pass


    # Enter a parse tree produced by StarRocksParser#unboundedFrame.
    def enterUnboundedFrame(self, ctx:StarRocksParser.UnboundedFrameContext):
        pass

    # Exit a parse tree produced by StarRocksParser#unboundedFrame.
    def exitUnboundedFrame(self, ctx:StarRocksParser.UnboundedFrameContext):
        pass


    # Enter a parse tree produced by StarRocksParser#currentRowBound.
    def enterCurrentRowBound(self, ctx:StarRocksParser.CurrentRowBoundContext):
        pass

    # Exit a parse tree produced by StarRocksParser#currentRowBound.
    def exitCurrentRowBound(self, ctx:StarRocksParser.CurrentRowBoundContext):
        pass


    # Enter a parse tree produced by StarRocksParser#boundedFrame.
    def enterBoundedFrame(self, ctx:StarRocksParser.BoundedFrameContext):
        pass

    # Exit a parse tree produced by StarRocksParser#boundedFrame.
    def exitBoundedFrame(self, ctx:StarRocksParser.BoundedFrameContext):
        pass


    # Enter a parse tree produced by StarRocksParser#tableDesc.
    def enterTableDesc(self, ctx:StarRocksParser.TableDescContext):
        pass

    # Exit a parse tree produced by StarRocksParser#tableDesc.
    def exitTableDesc(self, ctx:StarRocksParser.TableDescContext):
        pass


    # Enter a parse tree produced by StarRocksParser#restoreTableDesc.
    def enterRestoreTableDesc(self, ctx:StarRocksParser.RestoreTableDescContext):
        pass

    # Exit a parse tree produced by StarRocksParser#restoreTableDesc.
    def exitRestoreTableDesc(self, ctx:StarRocksParser.RestoreTableDescContext):
        pass


    # Enter a parse tree produced by StarRocksParser#explainDesc.
    def enterExplainDesc(self, ctx:StarRocksParser.ExplainDescContext):
        pass

    # Exit a parse tree produced by StarRocksParser#explainDesc.
    def exitExplainDesc(self, ctx:StarRocksParser.ExplainDescContext):
        pass


    # Enter a parse tree produced by StarRocksParser#optimizerTrace.
    def enterOptimizerTrace(self, ctx:StarRocksParser.OptimizerTraceContext):
        pass

    # Exit a parse tree produced by StarRocksParser#optimizerTrace.
    def exitOptimizerTrace(self, ctx:StarRocksParser.OptimizerTraceContext):
        pass


    # Enter a parse tree produced by StarRocksParser#partitionDesc.
    def enterPartitionDesc(self, ctx:StarRocksParser.PartitionDescContext):
        pass

    # Exit a parse tree produced by StarRocksParser#partitionDesc.
    def exitPartitionDesc(self, ctx:StarRocksParser.PartitionDescContext):
        pass


    # Enter a parse tree produced by StarRocksParser#listPartitionDesc.
    def enterListPartitionDesc(self, ctx:StarRocksParser.ListPartitionDescContext):
        pass

    # Exit a parse tree produced by StarRocksParser#listPartitionDesc.
    def exitListPartitionDesc(self, ctx:StarRocksParser.ListPartitionDescContext):
        pass


    # Enter a parse tree produced by StarRocksParser#singleItemListPartitionDesc.
    def enterSingleItemListPartitionDesc(self, ctx:StarRocksParser.SingleItemListPartitionDescContext):
        pass

    # Exit a parse tree produced by StarRocksParser#singleItemListPartitionDesc.
    def exitSingleItemListPartitionDesc(self, ctx:StarRocksParser.SingleItemListPartitionDescContext):
        pass


    # Enter a parse tree produced by StarRocksParser#multiItemListPartitionDesc.
    def enterMultiItemListPartitionDesc(self, ctx:StarRocksParser.MultiItemListPartitionDescContext):
        pass

    # Exit a parse tree produced by StarRocksParser#multiItemListPartitionDesc.
    def exitMultiItemListPartitionDesc(self, ctx:StarRocksParser.MultiItemListPartitionDescContext):
        pass


    # Enter a parse tree produced by StarRocksParser#listPartitionValueList.
    def enterListPartitionValueList(self, ctx:StarRocksParser.ListPartitionValueListContext):
        pass

    # Exit a parse tree produced by StarRocksParser#listPartitionValueList.
    def exitListPartitionValueList(self, ctx:StarRocksParser.ListPartitionValueListContext):
        pass


    # Enter a parse tree produced by StarRocksParser#listPartitionValue.
    def enterListPartitionValue(self, ctx:StarRocksParser.ListPartitionValueContext):
        pass

    # Exit a parse tree produced by StarRocksParser#listPartitionValue.
    def exitListPartitionValue(self, ctx:StarRocksParser.ListPartitionValueContext):
        pass


    # Enter a parse tree produced by StarRocksParser#stringList.
    def enterStringList(self, ctx:StarRocksParser.StringListContext):
        pass

    # Exit a parse tree produced by StarRocksParser#stringList.
    def exitStringList(self, ctx:StarRocksParser.StringListContext):
        pass


    # Enter a parse tree produced by StarRocksParser#literalExpressionList.
    def enterLiteralExpressionList(self, ctx:StarRocksParser.LiteralExpressionListContext):
        pass

    # Exit a parse tree produced by StarRocksParser#literalExpressionList.
    def exitLiteralExpressionList(self, ctx:StarRocksParser.LiteralExpressionListContext):
        pass


    # Enter a parse tree produced by StarRocksParser#rangePartitionDesc.
    def enterRangePartitionDesc(self, ctx:StarRocksParser.RangePartitionDescContext):
        pass

    # Exit a parse tree produced by StarRocksParser#rangePartitionDesc.
    def exitRangePartitionDesc(self, ctx:StarRocksParser.RangePartitionDescContext):
        pass


    # Enter a parse tree produced by StarRocksParser#singleRangePartition.
    def enterSingleRangePartition(self, ctx:StarRocksParser.SingleRangePartitionContext):
        pass

    # Exit a parse tree produced by StarRocksParser#singleRangePartition.
    def exitSingleRangePartition(self, ctx:StarRocksParser.SingleRangePartitionContext):
        pass


    # Enter a parse tree produced by StarRocksParser#multiRangePartition.
    def enterMultiRangePartition(self, ctx:StarRocksParser.MultiRangePartitionContext):
        pass

    # Exit a parse tree produced by StarRocksParser#multiRangePartition.
    def exitMultiRangePartition(self, ctx:StarRocksParser.MultiRangePartitionContext):
        pass


    # Enter a parse tree produced by StarRocksParser#partitionRangeDesc.
    def enterPartitionRangeDesc(self, ctx:StarRocksParser.PartitionRangeDescContext):
        pass

    # Exit a parse tree produced by StarRocksParser#partitionRangeDesc.
    def exitPartitionRangeDesc(self, ctx:StarRocksParser.PartitionRangeDescContext):
        pass


    # Enter a parse tree produced by StarRocksParser#partitionKeyDesc.
    def enterPartitionKeyDesc(self, ctx:StarRocksParser.PartitionKeyDescContext):
        pass

    # Exit a parse tree produced by StarRocksParser#partitionKeyDesc.
    def exitPartitionKeyDesc(self, ctx:StarRocksParser.PartitionKeyDescContext):
        pass


    # Enter a parse tree produced by StarRocksParser#partitionValueList.
    def enterPartitionValueList(self, ctx:StarRocksParser.PartitionValueListContext):
        pass

    # Exit a parse tree produced by StarRocksParser#partitionValueList.
    def exitPartitionValueList(self, ctx:StarRocksParser.PartitionValueListContext):
        pass


    # Enter a parse tree produced by StarRocksParser#keyPartition.
    def enterKeyPartition(self, ctx:StarRocksParser.KeyPartitionContext):
        pass

    # Exit a parse tree produced by StarRocksParser#keyPartition.
    def exitKeyPartition(self, ctx:StarRocksParser.KeyPartitionContext):
        pass


    # Enter a parse tree produced by StarRocksParser#partitionValue.
    def enterPartitionValue(self, ctx:StarRocksParser.PartitionValueContext):
        pass

    # Exit a parse tree produced by StarRocksParser#partitionValue.
    def exitPartitionValue(self, ctx:StarRocksParser.PartitionValueContext):
        pass


    # Enter a parse tree produced by StarRocksParser#distributionClause.
    def enterDistributionClause(self, ctx:StarRocksParser.DistributionClauseContext):
        pass

    # Exit a parse tree produced by StarRocksParser#distributionClause.
    def exitDistributionClause(self, ctx:StarRocksParser.DistributionClauseContext):
        pass


    # Enter a parse tree produced by StarRocksParser#distributionDesc.
    def enterDistributionDesc(self, ctx:StarRocksParser.DistributionDescContext):
        pass

    # Exit a parse tree produced by StarRocksParser#distributionDesc.
    def exitDistributionDesc(self, ctx:StarRocksParser.DistributionDescContext):
        pass


    # Enter a parse tree produced by StarRocksParser#refreshSchemeDesc.
    def enterRefreshSchemeDesc(self, ctx:StarRocksParser.RefreshSchemeDescContext):
        pass

    # Exit a parse tree produced by StarRocksParser#refreshSchemeDesc.
    def exitRefreshSchemeDesc(self, ctx:StarRocksParser.RefreshSchemeDescContext):
        pass


    # Enter a parse tree produced by StarRocksParser#statusDesc.
    def enterStatusDesc(self, ctx:StarRocksParser.StatusDescContext):
        pass

    # Exit a parse tree produced by StarRocksParser#statusDesc.
    def exitStatusDesc(self, ctx:StarRocksParser.StatusDescContext):
        pass


    # Enter a parse tree produced by StarRocksParser#properties.
    def enterProperties(self, ctx:StarRocksParser.PropertiesContext):
        pass

    # Exit a parse tree produced by StarRocksParser#properties.
    def exitProperties(self, ctx:StarRocksParser.PropertiesContext):
        pass


    # Enter a parse tree produced by StarRocksParser#extProperties.
    def enterExtProperties(self, ctx:StarRocksParser.ExtPropertiesContext):
        pass

    # Exit a parse tree produced by StarRocksParser#extProperties.
    def exitExtProperties(self, ctx:StarRocksParser.ExtPropertiesContext):
        pass


    # Enter a parse tree produced by StarRocksParser#propertyList.
    def enterPropertyList(self, ctx:StarRocksParser.PropertyListContext):
        pass

    # Exit a parse tree produced by StarRocksParser#propertyList.
    def exitPropertyList(self, ctx:StarRocksParser.PropertyListContext):
        pass


    # Enter a parse tree produced by StarRocksParser#userPropertyList.
    def enterUserPropertyList(self, ctx:StarRocksParser.UserPropertyListContext):
        pass

    # Exit a parse tree produced by StarRocksParser#userPropertyList.
    def exitUserPropertyList(self, ctx:StarRocksParser.UserPropertyListContext):
        pass


    # Enter a parse tree produced by StarRocksParser#property.
    def enterProperty(self, ctx:StarRocksParser.PropertyContext):
        pass

    # Exit a parse tree produced by StarRocksParser#property.
    def exitProperty(self, ctx:StarRocksParser.PropertyContext):
        pass


    # Enter a parse tree produced by StarRocksParser#varType.
    def enterVarType(self, ctx:StarRocksParser.VarTypeContext):
        pass

    # Exit a parse tree produced by StarRocksParser#varType.
    def exitVarType(self, ctx:StarRocksParser.VarTypeContext):
        pass


    # Enter a parse tree produced by StarRocksParser#comment.
    def enterComment(self, ctx:StarRocksParser.CommentContext):
        pass

    # Exit a parse tree produced by StarRocksParser#comment.
    def exitComment(self, ctx:StarRocksParser.CommentContext):
        pass


    # Enter a parse tree produced by StarRocksParser#outfile.
    def enterOutfile(self, ctx:StarRocksParser.OutfileContext):
        pass

    # Exit a parse tree produced by StarRocksParser#outfile.
    def exitOutfile(self, ctx:StarRocksParser.OutfileContext):
        pass


    # Enter a parse tree produced by StarRocksParser#fileFormat.
    def enterFileFormat(self, ctx:StarRocksParser.FileFormatContext):
        pass

    # Exit a parse tree produced by StarRocksParser#fileFormat.
    def exitFileFormat(self, ctx:StarRocksParser.FileFormatContext):
        pass


    # Enter a parse tree produced by StarRocksParser#string_.
    def enterString_(self, ctx:StarRocksParser.String_Context):
        pass

    # Exit a parse tree produced by StarRocksParser#string_.
    def exitString_(self, ctx:StarRocksParser.String_Context):
        pass


    # Enter a parse tree produced by StarRocksParser#binary.
    def enterBinary(self, ctx:StarRocksParser.BinaryContext):
        pass

    # Exit a parse tree produced by StarRocksParser#binary.
    def exitBinary(self, ctx:StarRocksParser.BinaryContext):
        pass


    # Enter a parse tree produced by StarRocksParser#comparisonOperator.
    def enterComparisonOperator(self, ctx:StarRocksParser.ComparisonOperatorContext):
        pass

    # Exit a parse tree produced by StarRocksParser#comparisonOperator.
    def exitComparisonOperator(self, ctx:StarRocksParser.ComparisonOperatorContext):
        pass


    # Enter a parse tree produced by StarRocksParser#booleanValue.
    def enterBooleanValue(self, ctx:StarRocksParser.BooleanValueContext):
        pass

    # Exit a parse tree produced by StarRocksParser#booleanValue.
    def exitBooleanValue(self, ctx:StarRocksParser.BooleanValueContext):
        pass


    # Enter a parse tree produced by StarRocksParser#interval.
    def enterInterval(self, ctx:StarRocksParser.IntervalContext):
        pass

    # Exit a parse tree produced by StarRocksParser#interval.
    def exitInterval(self, ctx:StarRocksParser.IntervalContext):
        pass


    # Enter a parse tree produced by StarRocksParser#taskInterval.
    def enterTaskInterval(self, ctx:StarRocksParser.TaskIntervalContext):
        pass

    # Exit a parse tree produced by StarRocksParser#taskInterval.
    def exitTaskInterval(self, ctx:StarRocksParser.TaskIntervalContext):
        pass


    # Enter a parse tree produced by StarRocksParser#taskUnitIdentifier.
    def enterTaskUnitIdentifier(self, ctx:StarRocksParser.TaskUnitIdentifierContext):
        pass

    # Exit a parse tree produced by StarRocksParser#taskUnitIdentifier.
    def exitTaskUnitIdentifier(self, ctx:StarRocksParser.TaskUnitIdentifierContext):
        pass


    # Enter a parse tree produced by StarRocksParser#unitIdentifier.
    def enterUnitIdentifier(self, ctx:StarRocksParser.UnitIdentifierContext):
        pass

    # Exit a parse tree produced by StarRocksParser#unitIdentifier.
    def exitUnitIdentifier(self, ctx:StarRocksParser.UnitIdentifierContext):
        pass


    # Enter a parse tree produced by StarRocksParser#unitBoundary.
    def enterUnitBoundary(self, ctx:StarRocksParser.UnitBoundaryContext):
        pass

    # Exit a parse tree produced by StarRocksParser#unitBoundary.
    def exitUnitBoundary(self, ctx:StarRocksParser.UnitBoundaryContext):
        pass


    # Enter a parse tree produced by StarRocksParser#type.
    def enterType(self, ctx:StarRocksParser.TypeContext):
        pass

    # Exit a parse tree produced by StarRocksParser#type.
    def exitType(self, ctx:StarRocksParser.TypeContext):
        pass


    # Enter a parse tree produced by StarRocksParser#arrayType.
    def enterArrayType(self, ctx:StarRocksParser.ArrayTypeContext):
        pass

    # Exit a parse tree produced by StarRocksParser#arrayType.
    def exitArrayType(self, ctx:StarRocksParser.ArrayTypeContext):
        pass


    # Enter a parse tree produced by StarRocksParser#mapType.
    def enterMapType(self, ctx:StarRocksParser.MapTypeContext):
        pass

    # Exit a parse tree produced by StarRocksParser#mapType.
    def exitMapType(self, ctx:StarRocksParser.MapTypeContext):
        pass


    # Enter a parse tree produced by StarRocksParser#subfieldDesc.
    def enterSubfieldDesc(self, ctx:StarRocksParser.SubfieldDescContext):
        pass

    # Exit a parse tree produced by StarRocksParser#subfieldDesc.
    def exitSubfieldDesc(self, ctx:StarRocksParser.SubfieldDescContext):
        pass


    # Enter a parse tree produced by StarRocksParser#subfieldDescs.
    def enterSubfieldDescs(self, ctx:StarRocksParser.SubfieldDescsContext):
        pass

    # Exit a parse tree produced by StarRocksParser#subfieldDescs.
    def exitSubfieldDescs(self, ctx:StarRocksParser.SubfieldDescsContext):
        pass


    # Enter a parse tree produced by StarRocksParser#structType.
    def enterStructType(self, ctx:StarRocksParser.StructTypeContext):
        pass

    # Exit a parse tree produced by StarRocksParser#structType.
    def exitStructType(self, ctx:StarRocksParser.StructTypeContext):
        pass


    # Enter a parse tree produced by StarRocksParser#typeParameter.
    def enterTypeParameter(self, ctx:StarRocksParser.TypeParameterContext):
        pass

    # Exit a parse tree produced by StarRocksParser#typeParameter.
    def exitTypeParameter(self, ctx:StarRocksParser.TypeParameterContext):
        pass


    # Enter a parse tree produced by StarRocksParser#baseType.
    def enterBaseType(self, ctx:StarRocksParser.BaseTypeContext):
        pass

    # Exit a parse tree produced by StarRocksParser#baseType.
    def exitBaseType(self, ctx:StarRocksParser.BaseTypeContext):
        pass


    # Enter a parse tree produced by StarRocksParser#decimalType.
    def enterDecimalType(self, ctx:StarRocksParser.DecimalTypeContext):
        pass

    # Exit a parse tree produced by StarRocksParser#decimalType.
    def exitDecimalType(self, ctx:StarRocksParser.DecimalTypeContext):
        pass


    # Enter a parse tree produced by StarRocksParser#qualifiedName.
    def enterQualifiedName(self, ctx:StarRocksParser.QualifiedNameContext):
        pass

    # Exit a parse tree produced by StarRocksParser#qualifiedName.
    def exitQualifiedName(self, ctx:StarRocksParser.QualifiedNameContext):
        pass


    # Enter a parse tree produced by StarRocksParser#unquotedIdentifier.
    def enterUnquotedIdentifier(self, ctx:StarRocksParser.UnquotedIdentifierContext):
        pass

    # Exit a parse tree produced by StarRocksParser#unquotedIdentifier.
    def exitUnquotedIdentifier(self, ctx:StarRocksParser.UnquotedIdentifierContext):
        pass


    # Enter a parse tree produced by StarRocksParser#digitIdentifier.
    def enterDigitIdentifier(self, ctx:StarRocksParser.DigitIdentifierContext):
        pass

    # Exit a parse tree produced by StarRocksParser#digitIdentifier.
    def exitDigitIdentifier(self, ctx:StarRocksParser.DigitIdentifierContext):
        pass


    # Enter a parse tree produced by StarRocksParser#backQuotedIdentifier.
    def enterBackQuotedIdentifier(self, ctx:StarRocksParser.BackQuotedIdentifierContext):
        pass

    # Exit a parse tree produced by StarRocksParser#backQuotedIdentifier.
    def exitBackQuotedIdentifier(self, ctx:StarRocksParser.BackQuotedIdentifierContext):
        pass


    # Enter a parse tree produced by StarRocksParser#identifierList.
    def enterIdentifierList(self, ctx:StarRocksParser.IdentifierListContext):
        pass

    # Exit a parse tree produced by StarRocksParser#identifierList.
    def exitIdentifierList(self, ctx:StarRocksParser.IdentifierListContext):
        pass


    # Enter a parse tree produced by StarRocksParser#identifierOrString.
    def enterIdentifierOrString(self, ctx:StarRocksParser.IdentifierOrStringContext):
        pass

    # Exit a parse tree produced by StarRocksParser#identifierOrString.
    def exitIdentifierOrString(self, ctx:StarRocksParser.IdentifierOrStringContext):
        pass


    # Enter a parse tree produced by StarRocksParser#identifierOrStringList.
    def enterIdentifierOrStringList(self, ctx:StarRocksParser.IdentifierOrStringListContext):
        pass

    # Exit a parse tree produced by StarRocksParser#identifierOrStringList.
    def exitIdentifierOrStringList(self, ctx:StarRocksParser.IdentifierOrStringListContext):
        pass


    # Enter a parse tree produced by StarRocksParser#identifierOrStringOrStar.
    def enterIdentifierOrStringOrStar(self, ctx:StarRocksParser.IdentifierOrStringOrStarContext):
        pass

    # Exit a parse tree produced by StarRocksParser#identifierOrStringOrStar.
    def exitIdentifierOrStringOrStar(self, ctx:StarRocksParser.IdentifierOrStringOrStarContext):
        pass


    # Enter a parse tree produced by StarRocksParser#userWithoutHost.
    def enterUserWithoutHost(self, ctx:StarRocksParser.UserWithoutHostContext):
        pass

    # Exit a parse tree produced by StarRocksParser#userWithoutHost.
    def exitUserWithoutHost(self, ctx:StarRocksParser.UserWithoutHostContext):
        pass


    # Enter a parse tree produced by StarRocksParser#userWithHost.
    def enterUserWithHost(self, ctx:StarRocksParser.UserWithHostContext):
        pass

    # Exit a parse tree produced by StarRocksParser#userWithHost.
    def exitUserWithHost(self, ctx:StarRocksParser.UserWithHostContext):
        pass


    # Enter a parse tree produced by StarRocksParser#userWithHostAndBlanket.
    def enterUserWithHostAndBlanket(self, ctx:StarRocksParser.UserWithHostAndBlanketContext):
        pass

    # Exit a parse tree produced by StarRocksParser#userWithHostAndBlanket.
    def exitUserWithHostAndBlanket(self, ctx:StarRocksParser.UserWithHostAndBlanketContext):
        pass


    # Enter a parse tree produced by StarRocksParser#assignment.
    def enterAssignment(self, ctx:StarRocksParser.AssignmentContext):
        pass

    # Exit a parse tree produced by StarRocksParser#assignment.
    def exitAssignment(self, ctx:StarRocksParser.AssignmentContext):
        pass


    # Enter a parse tree produced by StarRocksParser#assignmentList.
    def enterAssignmentList(self, ctx:StarRocksParser.AssignmentListContext):
        pass

    # Exit a parse tree produced by StarRocksParser#assignmentList.
    def exitAssignmentList(self, ctx:StarRocksParser.AssignmentListContext):
        pass


    # Enter a parse tree produced by StarRocksParser#decimalValue.
    def enterDecimalValue(self, ctx:StarRocksParser.DecimalValueContext):
        pass

    # Exit a parse tree produced by StarRocksParser#decimalValue.
    def exitDecimalValue(self, ctx:StarRocksParser.DecimalValueContext):
        pass


    # Enter a parse tree produced by StarRocksParser#doubleValue.
    def enterDoubleValue(self, ctx:StarRocksParser.DoubleValueContext):
        pass

    # Exit a parse tree produced by StarRocksParser#doubleValue.
    def exitDoubleValue(self, ctx:StarRocksParser.DoubleValueContext):
        pass


    # Enter a parse tree produced by StarRocksParser#integerValue.
    def enterIntegerValue(self, ctx:StarRocksParser.IntegerValueContext):
        pass

    # Exit a parse tree produced by StarRocksParser#integerValue.
    def exitIntegerValue(self, ctx:StarRocksParser.IntegerValueContext):
        pass


    # Enter a parse tree produced by StarRocksParser#nonReserved.
    def enterNonReserved(self, ctx:StarRocksParser.NonReservedContext):
        pass

    # Exit a parse tree produced by StarRocksParser#nonReserved.
    def exitNonReserved(self, ctx:StarRocksParser.NonReservedContext):
        pass



del StarRocksParser