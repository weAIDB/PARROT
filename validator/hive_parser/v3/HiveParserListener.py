# Generated from sql/hive/v3/HiveParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .HiveParser import HiveParser
else:
    from HiveParser import HiveParser

# This class defines a complete listener for a parse tree produced by HiveParser.
class HiveParserListener(ParseTreeListener):

    # Enter a parse tree produced by HiveParser#statements.
    def enterStatements(self, ctx:HiveParser.StatementsContext):
        pass

    # Exit a parse tree produced by HiveParser#statements.
    def exitStatements(self, ctx:HiveParser.StatementsContext):
        pass


    # Enter a parse tree produced by HiveParser#statementSeparator.
    def enterStatementSeparator(self, ctx:HiveParser.StatementSeparatorContext):
        pass

    # Exit a parse tree produced by HiveParser#statementSeparator.
    def exitStatementSeparator(self, ctx:HiveParser.StatementSeparatorContext):
        pass


    # Enter a parse tree produced by HiveParser#statement.
    def enterStatement(self, ctx:HiveParser.StatementContext):
        pass

    # Exit a parse tree produced by HiveParser#statement.
    def exitStatement(self, ctx:HiveParser.StatementContext):
        pass


    # Enter a parse tree produced by HiveParser#explainStatement.
    def enterExplainStatement(self, ctx:HiveParser.ExplainStatementContext):
        pass

    # Exit a parse tree produced by HiveParser#explainStatement.
    def exitExplainStatement(self, ctx:HiveParser.ExplainStatementContext):
        pass


    # Enter a parse tree produced by HiveParser#explainOption.
    def enterExplainOption(self, ctx:HiveParser.ExplainOptionContext):
        pass

    # Exit a parse tree produced by HiveParser#explainOption.
    def exitExplainOption(self, ctx:HiveParser.ExplainOptionContext):
        pass


    # Enter a parse tree produced by HiveParser#vectorizationOnly.
    def enterVectorizationOnly(self, ctx:HiveParser.VectorizationOnlyContext):
        pass

    # Exit a parse tree produced by HiveParser#vectorizationOnly.
    def exitVectorizationOnly(self, ctx:HiveParser.VectorizationOnlyContext):
        pass


    # Enter a parse tree produced by HiveParser#vectorizatonDetail.
    def enterVectorizatonDetail(self, ctx:HiveParser.VectorizatonDetailContext):
        pass

    # Exit a parse tree produced by HiveParser#vectorizatonDetail.
    def exitVectorizatonDetail(self, ctx:HiveParser.VectorizatonDetailContext):
        pass


    # Enter a parse tree produced by HiveParser#execStatement.
    def enterExecStatement(self, ctx:HiveParser.ExecStatementContext):
        pass

    # Exit a parse tree produced by HiveParser#execStatement.
    def exitExecStatement(self, ctx:HiveParser.ExecStatementContext):
        pass


    # Enter a parse tree produced by HiveParser#loadStatement.
    def enterLoadStatement(self, ctx:HiveParser.LoadStatementContext):
        pass

    # Exit a parse tree produced by HiveParser#loadStatement.
    def exitLoadStatement(self, ctx:HiveParser.LoadStatementContext):
        pass


    # Enter a parse tree produced by HiveParser#replicationClause.
    def enterReplicationClause(self, ctx:HiveParser.ReplicationClauseContext):
        pass

    # Exit a parse tree produced by HiveParser#replicationClause.
    def exitReplicationClause(self, ctx:HiveParser.ReplicationClauseContext):
        pass


    # Enter a parse tree produced by HiveParser#exportStatement.
    def enterExportStatement(self, ctx:HiveParser.ExportStatementContext):
        pass

    # Exit a parse tree produced by HiveParser#exportStatement.
    def exitExportStatement(self, ctx:HiveParser.ExportStatementContext):
        pass


    # Enter a parse tree produced by HiveParser#importStatement.
    def enterImportStatement(self, ctx:HiveParser.ImportStatementContext):
        pass

    # Exit a parse tree produced by HiveParser#importStatement.
    def exitImportStatement(self, ctx:HiveParser.ImportStatementContext):
        pass


    # Enter a parse tree produced by HiveParser#replDumpStatement.
    def enterReplDumpStatement(self, ctx:HiveParser.ReplDumpStatementContext):
        pass

    # Exit a parse tree produced by HiveParser#replDumpStatement.
    def exitReplDumpStatement(self, ctx:HiveParser.ReplDumpStatementContext):
        pass


    # Enter a parse tree produced by HiveParser#replLoadStatement.
    def enterReplLoadStatement(self, ctx:HiveParser.ReplLoadStatementContext):
        pass

    # Exit a parse tree produced by HiveParser#replLoadStatement.
    def exitReplLoadStatement(self, ctx:HiveParser.ReplLoadStatementContext):
        pass


    # Enter a parse tree produced by HiveParser#replConfigs.
    def enterReplConfigs(self, ctx:HiveParser.ReplConfigsContext):
        pass

    # Exit a parse tree produced by HiveParser#replConfigs.
    def exitReplConfigs(self, ctx:HiveParser.ReplConfigsContext):
        pass


    # Enter a parse tree produced by HiveParser#replConfigsList.
    def enterReplConfigsList(self, ctx:HiveParser.ReplConfigsListContext):
        pass

    # Exit a parse tree produced by HiveParser#replConfigsList.
    def exitReplConfigsList(self, ctx:HiveParser.ReplConfigsListContext):
        pass


    # Enter a parse tree produced by HiveParser#replStatusStatement.
    def enterReplStatusStatement(self, ctx:HiveParser.ReplStatusStatementContext):
        pass

    # Exit a parse tree produced by HiveParser#replStatusStatement.
    def exitReplStatusStatement(self, ctx:HiveParser.ReplStatusStatementContext):
        pass


    # Enter a parse tree produced by HiveParser#ddlStatement.
    def enterDdlStatement(self, ctx:HiveParser.DdlStatementContext):
        pass

    # Exit a parse tree produced by HiveParser#ddlStatement.
    def exitDdlStatement(self, ctx:HiveParser.DdlStatementContext):
        pass


    # Enter a parse tree produced by HiveParser#ifExists.
    def enterIfExists(self, ctx:HiveParser.IfExistsContext):
        pass

    # Exit a parse tree produced by HiveParser#ifExists.
    def exitIfExists(self, ctx:HiveParser.IfExistsContext):
        pass


    # Enter a parse tree produced by HiveParser#restrictOrCascade.
    def enterRestrictOrCascade(self, ctx:HiveParser.RestrictOrCascadeContext):
        pass

    # Exit a parse tree produced by HiveParser#restrictOrCascade.
    def exitRestrictOrCascade(self, ctx:HiveParser.RestrictOrCascadeContext):
        pass


    # Enter a parse tree produced by HiveParser#ifNotExists.
    def enterIfNotExists(self, ctx:HiveParser.IfNotExistsContext):
        pass

    # Exit a parse tree produced by HiveParser#ifNotExists.
    def exitIfNotExists(self, ctx:HiveParser.IfNotExistsContext):
        pass


    # Enter a parse tree produced by HiveParser#rewriteEnabled.
    def enterRewriteEnabled(self, ctx:HiveParser.RewriteEnabledContext):
        pass

    # Exit a parse tree produced by HiveParser#rewriteEnabled.
    def exitRewriteEnabled(self, ctx:HiveParser.RewriteEnabledContext):
        pass


    # Enter a parse tree produced by HiveParser#rewriteDisabled.
    def enterRewriteDisabled(self, ctx:HiveParser.RewriteDisabledContext):
        pass

    # Exit a parse tree produced by HiveParser#rewriteDisabled.
    def exitRewriteDisabled(self, ctx:HiveParser.RewriteDisabledContext):
        pass


    # Enter a parse tree produced by HiveParser#storedAsDirs.
    def enterStoredAsDirs(self, ctx:HiveParser.StoredAsDirsContext):
        pass

    # Exit a parse tree produced by HiveParser#storedAsDirs.
    def exitStoredAsDirs(self, ctx:HiveParser.StoredAsDirsContext):
        pass


    # Enter a parse tree produced by HiveParser#orReplace.
    def enterOrReplace(self, ctx:HiveParser.OrReplaceContext):
        pass

    # Exit a parse tree produced by HiveParser#orReplace.
    def exitOrReplace(self, ctx:HiveParser.OrReplaceContext):
        pass


    # Enter a parse tree produced by HiveParser#createDatabaseStatement.
    def enterCreateDatabaseStatement(self, ctx:HiveParser.CreateDatabaseStatementContext):
        pass

    # Exit a parse tree produced by HiveParser#createDatabaseStatement.
    def exitCreateDatabaseStatement(self, ctx:HiveParser.CreateDatabaseStatementContext):
        pass


    # Enter a parse tree produced by HiveParser#dbLocation.
    def enterDbLocation(self, ctx:HiveParser.DbLocationContext):
        pass

    # Exit a parse tree produced by HiveParser#dbLocation.
    def exitDbLocation(self, ctx:HiveParser.DbLocationContext):
        pass


    # Enter a parse tree produced by HiveParser#dbProperties.
    def enterDbProperties(self, ctx:HiveParser.DbPropertiesContext):
        pass

    # Exit a parse tree produced by HiveParser#dbProperties.
    def exitDbProperties(self, ctx:HiveParser.DbPropertiesContext):
        pass


    # Enter a parse tree produced by HiveParser#dbPropertiesList.
    def enterDbPropertiesList(self, ctx:HiveParser.DbPropertiesListContext):
        pass

    # Exit a parse tree produced by HiveParser#dbPropertiesList.
    def exitDbPropertiesList(self, ctx:HiveParser.DbPropertiesListContext):
        pass


    # Enter a parse tree produced by HiveParser#switchDatabaseStatement.
    def enterSwitchDatabaseStatement(self, ctx:HiveParser.SwitchDatabaseStatementContext):
        pass

    # Exit a parse tree produced by HiveParser#switchDatabaseStatement.
    def exitSwitchDatabaseStatement(self, ctx:HiveParser.SwitchDatabaseStatementContext):
        pass


    # Enter a parse tree produced by HiveParser#dropDatabaseStatement.
    def enterDropDatabaseStatement(self, ctx:HiveParser.DropDatabaseStatementContext):
        pass

    # Exit a parse tree produced by HiveParser#dropDatabaseStatement.
    def exitDropDatabaseStatement(self, ctx:HiveParser.DropDatabaseStatementContext):
        pass


    # Enter a parse tree produced by HiveParser#databaseComment.
    def enterDatabaseComment(self, ctx:HiveParser.DatabaseCommentContext):
        pass

    # Exit a parse tree produced by HiveParser#databaseComment.
    def exitDatabaseComment(self, ctx:HiveParser.DatabaseCommentContext):
        pass


    # Enter a parse tree produced by HiveParser#createTableStatement.
    def enterCreateTableStatement(self, ctx:HiveParser.CreateTableStatementContext):
        pass

    # Exit a parse tree produced by HiveParser#createTableStatement.
    def exitCreateTableStatement(self, ctx:HiveParser.CreateTableStatementContext):
        pass


    # Enter a parse tree produced by HiveParser#truncateTableStatement.
    def enterTruncateTableStatement(self, ctx:HiveParser.TruncateTableStatementContext):
        pass

    # Exit a parse tree produced by HiveParser#truncateTableStatement.
    def exitTruncateTableStatement(self, ctx:HiveParser.TruncateTableStatementContext):
        pass


    # Enter a parse tree produced by HiveParser#dropTableStatement.
    def enterDropTableStatement(self, ctx:HiveParser.DropTableStatementContext):
        pass

    # Exit a parse tree produced by HiveParser#dropTableStatement.
    def exitDropTableStatement(self, ctx:HiveParser.DropTableStatementContext):
        pass


    # Enter a parse tree produced by HiveParser#alterStatement.
    def enterAlterStatement(self, ctx:HiveParser.AlterStatementContext):
        pass

    # Exit a parse tree produced by HiveParser#alterStatement.
    def exitAlterStatement(self, ctx:HiveParser.AlterStatementContext):
        pass


    # Enter a parse tree produced by HiveParser#alterTableStatementSuffix.
    def enterAlterTableStatementSuffix(self, ctx:HiveParser.AlterTableStatementSuffixContext):
        pass

    # Exit a parse tree produced by HiveParser#alterTableStatementSuffix.
    def exitAlterTableStatementSuffix(self, ctx:HiveParser.AlterTableStatementSuffixContext):
        pass


    # Enter a parse tree produced by HiveParser#alterTblPartitionStatementSuffix.
    def enterAlterTblPartitionStatementSuffix(self, ctx:HiveParser.AlterTblPartitionStatementSuffixContext):
        pass

    # Exit a parse tree produced by HiveParser#alterTblPartitionStatementSuffix.
    def exitAlterTblPartitionStatementSuffix(self, ctx:HiveParser.AlterTblPartitionStatementSuffixContext):
        pass


    # Enter a parse tree produced by HiveParser#alterStatementPartitionKeyType.
    def enterAlterStatementPartitionKeyType(self, ctx:HiveParser.AlterStatementPartitionKeyTypeContext):
        pass

    # Exit a parse tree produced by HiveParser#alterStatementPartitionKeyType.
    def exitAlterStatementPartitionKeyType(self, ctx:HiveParser.AlterStatementPartitionKeyTypeContext):
        pass


    # Enter a parse tree produced by HiveParser#alterViewStatementSuffix.
    def enterAlterViewStatementSuffix(self, ctx:HiveParser.AlterViewStatementSuffixContext):
        pass

    # Exit a parse tree produced by HiveParser#alterViewStatementSuffix.
    def exitAlterViewStatementSuffix(self, ctx:HiveParser.AlterViewStatementSuffixContext):
        pass


    # Enter a parse tree produced by HiveParser#alterMaterializedViewStatementSuffix.
    def enterAlterMaterializedViewStatementSuffix(self, ctx:HiveParser.AlterMaterializedViewStatementSuffixContext):
        pass

    # Exit a parse tree produced by HiveParser#alterMaterializedViewStatementSuffix.
    def exitAlterMaterializedViewStatementSuffix(self, ctx:HiveParser.AlterMaterializedViewStatementSuffixContext):
        pass


    # Enter a parse tree produced by HiveParser#alterDatabaseStatementSuffix.
    def enterAlterDatabaseStatementSuffix(self, ctx:HiveParser.AlterDatabaseStatementSuffixContext):
        pass

    # Exit a parse tree produced by HiveParser#alterDatabaseStatementSuffix.
    def exitAlterDatabaseStatementSuffix(self, ctx:HiveParser.AlterDatabaseStatementSuffixContext):
        pass


    # Enter a parse tree produced by HiveParser#alterDatabaseSuffixProperties.
    def enterAlterDatabaseSuffixProperties(self, ctx:HiveParser.AlterDatabaseSuffixPropertiesContext):
        pass

    # Exit a parse tree produced by HiveParser#alterDatabaseSuffixProperties.
    def exitAlterDatabaseSuffixProperties(self, ctx:HiveParser.AlterDatabaseSuffixPropertiesContext):
        pass


    # Enter a parse tree produced by HiveParser#alterDatabaseSuffixSetOwner.
    def enterAlterDatabaseSuffixSetOwner(self, ctx:HiveParser.AlterDatabaseSuffixSetOwnerContext):
        pass

    # Exit a parse tree produced by HiveParser#alterDatabaseSuffixSetOwner.
    def exitAlterDatabaseSuffixSetOwner(self, ctx:HiveParser.AlterDatabaseSuffixSetOwnerContext):
        pass


    # Enter a parse tree produced by HiveParser#alterDatabaseSuffixSetLocation.
    def enterAlterDatabaseSuffixSetLocation(self, ctx:HiveParser.AlterDatabaseSuffixSetLocationContext):
        pass

    # Exit a parse tree produced by HiveParser#alterDatabaseSuffixSetLocation.
    def exitAlterDatabaseSuffixSetLocation(self, ctx:HiveParser.AlterDatabaseSuffixSetLocationContext):
        pass


    # Enter a parse tree produced by HiveParser#alterStatementSuffixRename.
    def enterAlterStatementSuffixRename(self, ctx:HiveParser.AlterStatementSuffixRenameContext):
        pass

    # Exit a parse tree produced by HiveParser#alterStatementSuffixRename.
    def exitAlterStatementSuffixRename(self, ctx:HiveParser.AlterStatementSuffixRenameContext):
        pass


    # Enter a parse tree produced by HiveParser#alterStatementSuffixAddCol.
    def enterAlterStatementSuffixAddCol(self, ctx:HiveParser.AlterStatementSuffixAddColContext):
        pass

    # Exit a parse tree produced by HiveParser#alterStatementSuffixAddCol.
    def exitAlterStatementSuffixAddCol(self, ctx:HiveParser.AlterStatementSuffixAddColContext):
        pass


    # Enter a parse tree produced by HiveParser#alterStatementSuffixAddConstraint.
    def enterAlterStatementSuffixAddConstraint(self, ctx:HiveParser.AlterStatementSuffixAddConstraintContext):
        pass

    # Exit a parse tree produced by HiveParser#alterStatementSuffixAddConstraint.
    def exitAlterStatementSuffixAddConstraint(self, ctx:HiveParser.AlterStatementSuffixAddConstraintContext):
        pass


    # Enter a parse tree produced by HiveParser#alterStatementSuffixDropConstraint.
    def enterAlterStatementSuffixDropConstraint(self, ctx:HiveParser.AlterStatementSuffixDropConstraintContext):
        pass

    # Exit a parse tree produced by HiveParser#alterStatementSuffixDropConstraint.
    def exitAlterStatementSuffixDropConstraint(self, ctx:HiveParser.AlterStatementSuffixDropConstraintContext):
        pass


    # Enter a parse tree produced by HiveParser#alterStatementSuffixRenameCol.
    def enterAlterStatementSuffixRenameCol(self, ctx:HiveParser.AlterStatementSuffixRenameColContext):
        pass

    # Exit a parse tree produced by HiveParser#alterStatementSuffixRenameCol.
    def exitAlterStatementSuffixRenameCol(self, ctx:HiveParser.AlterStatementSuffixRenameColContext):
        pass


    # Enter a parse tree produced by HiveParser#alterStatementSuffixUpdateStatsCol.
    def enterAlterStatementSuffixUpdateStatsCol(self, ctx:HiveParser.AlterStatementSuffixUpdateStatsColContext):
        pass

    # Exit a parse tree produced by HiveParser#alterStatementSuffixUpdateStatsCol.
    def exitAlterStatementSuffixUpdateStatsCol(self, ctx:HiveParser.AlterStatementSuffixUpdateStatsColContext):
        pass


    # Enter a parse tree produced by HiveParser#alterStatementSuffixUpdateStats.
    def enterAlterStatementSuffixUpdateStats(self, ctx:HiveParser.AlterStatementSuffixUpdateStatsContext):
        pass

    # Exit a parse tree produced by HiveParser#alterStatementSuffixUpdateStats.
    def exitAlterStatementSuffixUpdateStats(self, ctx:HiveParser.AlterStatementSuffixUpdateStatsContext):
        pass


    # Enter a parse tree produced by HiveParser#alterStatementChangeColPosition.
    def enterAlterStatementChangeColPosition(self, ctx:HiveParser.AlterStatementChangeColPositionContext):
        pass

    # Exit a parse tree produced by HiveParser#alterStatementChangeColPosition.
    def exitAlterStatementChangeColPosition(self, ctx:HiveParser.AlterStatementChangeColPositionContext):
        pass


    # Enter a parse tree produced by HiveParser#alterStatementSuffixAddPartitions.
    def enterAlterStatementSuffixAddPartitions(self, ctx:HiveParser.AlterStatementSuffixAddPartitionsContext):
        pass

    # Exit a parse tree produced by HiveParser#alterStatementSuffixAddPartitions.
    def exitAlterStatementSuffixAddPartitions(self, ctx:HiveParser.AlterStatementSuffixAddPartitionsContext):
        pass


    # Enter a parse tree produced by HiveParser#alterStatementSuffixAddPartitionsElement.
    def enterAlterStatementSuffixAddPartitionsElement(self, ctx:HiveParser.AlterStatementSuffixAddPartitionsElementContext):
        pass

    # Exit a parse tree produced by HiveParser#alterStatementSuffixAddPartitionsElement.
    def exitAlterStatementSuffixAddPartitionsElement(self, ctx:HiveParser.AlterStatementSuffixAddPartitionsElementContext):
        pass


    # Enter a parse tree produced by HiveParser#alterStatementSuffixTouch.
    def enterAlterStatementSuffixTouch(self, ctx:HiveParser.AlterStatementSuffixTouchContext):
        pass

    # Exit a parse tree produced by HiveParser#alterStatementSuffixTouch.
    def exitAlterStatementSuffixTouch(self, ctx:HiveParser.AlterStatementSuffixTouchContext):
        pass


    # Enter a parse tree produced by HiveParser#alterStatementSuffixArchive.
    def enterAlterStatementSuffixArchive(self, ctx:HiveParser.AlterStatementSuffixArchiveContext):
        pass

    # Exit a parse tree produced by HiveParser#alterStatementSuffixArchive.
    def exitAlterStatementSuffixArchive(self, ctx:HiveParser.AlterStatementSuffixArchiveContext):
        pass


    # Enter a parse tree produced by HiveParser#alterStatementSuffixUnArchive.
    def enterAlterStatementSuffixUnArchive(self, ctx:HiveParser.AlterStatementSuffixUnArchiveContext):
        pass

    # Exit a parse tree produced by HiveParser#alterStatementSuffixUnArchive.
    def exitAlterStatementSuffixUnArchive(self, ctx:HiveParser.AlterStatementSuffixUnArchiveContext):
        pass


    # Enter a parse tree produced by HiveParser#partitionLocation.
    def enterPartitionLocation(self, ctx:HiveParser.PartitionLocationContext):
        pass

    # Exit a parse tree produced by HiveParser#partitionLocation.
    def exitPartitionLocation(self, ctx:HiveParser.PartitionLocationContext):
        pass


    # Enter a parse tree produced by HiveParser#alterStatementSuffixDropPartitions.
    def enterAlterStatementSuffixDropPartitions(self, ctx:HiveParser.AlterStatementSuffixDropPartitionsContext):
        pass

    # Exit a parse tree produced by HiveParser#alterStatementSuffixDropPartitions.
    def exitAlterStatementSuffixDropPartitions(self, ctx:HiveParser.AlterStatementSuffixDropPartitionsContext):
        pass


    # Enter a parse tree produced by HiveParser#alterStatementSuffixProperties.
    def enterAlterStatementSuffixProperties(self, ctx:HiveParser.AlterStatementSuffixPropertiesContext):
        pass

    # Exit a parse tree produced by HiveParser#alterStatementSuffixProperties.
    def exitAlterStatementSuffixProperties(self, ctx:HiveParser.AlterStatementSuffixPropertiesContext):
        pass


    # Enter a parse tree produced by HiveParser#alterViewSuffixProperties.
    def enterAlterViewSuffixProperties(self, ctx:HiveParser.AlterViewSuffixPropertiesContext):
        pass

    # Exit a parse tree produced by HiveParser#alterViewSuffixProperties.
    def exitAlterViewSuffixProperties(self, ctx:HiveParser.AlterViewSuffixPropertiesContext):
        pass


    # Enter a parse tree produced by HiveParser#alterMaterializedViewSuffixRewrite.
    def enterAlterMaterializedViewSuffixRewrite(self, ctx:HiveParser.AlterMaterializedViewSuffixRewriteContext):
        pass

    # Exit a parse tree produced by HiveParser#alterMaterializedViewSuffixRewrite.
    def exitAlterMaterializedViewSuffixRewrite(self, ctx:HiveParser.AlterMaterializedViewSuffixRewriteContext):
        pass


    # Enter a parse tree produced by HiveParser#alterMaterializedViewSuffixRebuild.
    def enterAlterMaterializedViewSuffixRebuild(self, ctx:HiveParser.AlterMaterializedViewSuffixRebuildContext):
        pass

    # Exit a parse tree produced by HiveParser#alterMaterializedViewSuffixRebuild.
    def exitAlterMaterializedViewSuffixRebuild(self, ctx:HiveParser.AlterMaterializedViewSuffixRebuildContext):
        pass


    # Enter a parse tree produced by HiveParser#alterStatementSuffixSerdeProperties.
    def enterAlterStatementSuffixSerdeProperties(self, ctx:HiveParser.AlterStatementSuffixSerdePropertiesContext):
        pass

    # Exit a parse tree produced by HiveParser#alterStatementSuffixSerdeProperties.
    def exitAlterStatementSuffixSerdeProperties(self, ctx:HiveParser.AlterStatementSuffixSerdePropertiesContext):
        pass


    # Enter a parse tree produced by HiveParser#alterIndexStatementSuffix.
    def enterAlterIndexStatementSuffix(self, ctx:HiveParser.AlterIndexStatementSuffixContext):
        pass

    # Exit a parse tree produced by HiveParser#alterIndexStatementSuffix.
    def exitAlterIndexStatementSuffix(self, ctx:HiveParser.AlterIndexStatementSuffixContext):
        pass


    # Enter a parse tree produced by HiveParser#alterStatementSuffixFileFormat.
    def enterAlterStatementSuffixFileFormat(self, ctx:HiveParser.AlterStatementSuffixFileFormatContext):
        pass

    # Exit a parse tree produced by HiveParser#alterStatementSuffixFileFormat.
    def exitAlterStatementSuffixFileFormat(self, ctx:HiveParser.AlterStatementSuffixFileFormatContext):
        pass


    # Enter a parse tree produced by HiveParser#alterStatementSuffixClusterbySortby.
    def enterAlterStatementSuffixClusterbySortby(self, ctx:HiveParser.AlterStatementSuffixClusterbySortbyContext):
        pass

    # Exit a parse tree produced by HiveParser#alterStatementSuffixClusterbySortby.
    def exitAlterStatementSuffixClusterbySortby(self, ctx:HiveParser.AlterStatementSuffixClusterbySortbyContext):
        pass


    # Enter a parse tree produced by HiveParser#alterTblPartitionStatementSuffixSkewedLocation.
    def enterAlterTblPartitionStatementSuffixSkewedLocation(self, ctx:HiveParser.AlterTblPartitionStatementSuffixSkewedLocationContext):
        pass

    # Exit a parse tree produced by HiveParser#alterTblPartitionStatementSuffixSkewedLocation.
    def exitAlterTblPartitionStatementSuffixSkewedLocation(self, ctx:HiveParser.AlterTblPartitionStatementSuffixSkewedLocationContext):
        pass


    # Enter a parse tree produced by HiveParser#skewedLocations.
    def enterSkewedLocations(self, ctx:HiveParser.SkewedLocationsContext):
        pass

    # Exit a parse tree produced by HiveParser#skewedLocations.
    def exitSkewedLocations(self, ctx:HiveParser.SkewedLocationsContext):
        pass


    # Enter a parse tree produced by HiveParser#skewedLocationsList.
    def enterSkewedLocationsList(self, ctx:HiveParser.SkewedLocationsListContext):
        pass

    # Exit a parse tree produced by HiveParser#skewedLocationsList.
    def exitSkewedLocationsList(self, ctx:HiveParser.SkewedLocationsListContext):
        pass


    # Enter a parse tree produced by HiveParser#skewedLocationMap.
    def enterSkewedLocationMap(self, ctx:HiveParser.SkewedLocationMapContext):
        pass

    # Exit a parse tree produced by HiveParser#skewedLocationMap.
    def exitSkewedLocationMap(self, ctx:HiveParser.SkewedLocationMapContext):
        pass


    # Enter a parse tree produced by HiveParser#alterStatementSuffixLocation.
    def enterAlterStatementSuffixLocation(self, ctx:HiveParser.AlterStatementSuffixLocationContext):
        pass

    # Exit a parse tree produced by HiveParser#alterStatementSuffixLocation.
    def exitAlterStatementSuffixLocation(self, ctx:HiveParser.AlterStatementSuffixLocationContext):
        pass


    # Enter a parse tree produced by HiveParser#alterStatementSuffixSkewedby.
    def enterAlterStatementSuffixSkewedby(self, ctx:HiveParser.AlterStatementSuffixSkewedbyContext):
        pass

    # Exit a parse tree produced by HiveParser#alterStatementSuffixSkewedby.
    def exitAlterStatementSuffixSkewedby(self, ctx:HiveParser.AlterStatementSuffixSkewedbyContext):
        pass


    # Enter a parse tree produced by HiveParser#alterStatementSuffixExchangePartition.
    def enterAlterStatementSuffixExchangePartition(self, ctx:HiveParser.AlterStatementSuffixExchangePartitionContext):
        pass

    # Exit a parse tree produced by HiveParser#alterStatementSuffixExchangePartition.
    def exitAlterStatementSuffixExchangePartition(self, ctx:HiveParser.AlterStatementSuffixExchangePartitionContext):
        pass


    # Enter a parse tree produced by HiveParser#alterStatementSuffixRenamePart.
    def enterAlterStatementSuffixRenamePart(self, ctx:HiveParser.AlterStatementSuffixRenamePartContext):
        pass

    # Exit a parse tree produced by HiveParser#alterStatementSuffixRenamePart.
    def exitAlterStatementSuffixRenamePart(self, ctx:HiveParser.AlterStatementSuffixRenamePartContext):
        pass


    # Enter a parse tree produced by HiveParser#alterStatementSuffixStatsPart.
    def enterAlterStatementSuffixStatsPart(self, ctx:HiveParser.AlterStatementSuffixStatsPartContext):
        pass

    # Exit a parse tree produced by HiveParser#alterStatementSuffixStatsPart.
    def exitAlterStatementSuffixStatsPart(self, ctx:HiveParser.AlterStatementSuffixStatsPartContext):
        pass


    # Enter a parse tree produced by HiveParser#alterStatementSuffixMergeFiles.
    def enterAlterStatementSuffixMergeFiles(self, ctx:HiveParser.AlterStatementSuffixMergeFilesContext):
        pass

    # Exit a parse tree produced by HiveParser#alterStatementSuffixMergeFiles.
    def exitAlterStatementSuffixMergeFiles(self, ctx:HiveParser.AlterStatementSuffixMergeFilesContext):
        pass


    # Enter a parse tree produced by HiveParser#alterStatementSuffixBucketNum.
    def enterAlterStatementSuffixBucketNum(self, ctx:HiveParser.AlterStatementSuffixBucketNumContext):
        pass

    # Exit a parse tree produced by HiveParser#alterStatementSuffixBucketNum.
    def exitAlterStatementSuffixBucketNum(self, ctx:HiveParser.AlterStatementSuffixBucketNumContext):
        pass


    # Enter a parse tree produced by HiveParser#createIndexStatement.
    def enterCreateIndexStatement(self, ctx:HiveParser.CreateIndexStatementContext):
        pass

    # Exit a parse tree produced by HiveParser#createIndexStatement.
    def exitCreateIndexStatement(self, ctx:HiveParser.CreateIndexStatementContext):
        pass


    # Enter a parse tree produced by HiveParser#locationPath.
    def enterLocationPath(self, ctx:HiveParser.LocationPathContext):
        pass

    # Exit a parse tree produced by HiveParser#locationPath.
    def exitLocationPath(self, ctx:HiveParser.LocationPathContext):
        pass


    # Enter a parse tree produced by HiveParser#dropIndexStatement.
    def enterDropIndexStatement(self, ctx:HiveParser.DropIndexStatementContext):
        pass

    # Exit a parse tree produced by HiveParser#dropIndexStatement.
    def exitDropIndexStatement(self, ctx:HiveParser.DropIndexStatementContext):
        pass


    # Enter a parse tree produced by HiveParser#tablePartitionPrefix.
    def enterTablePartitionPrefix(self, ctx:HiveParser.TablePartitionPrefixContext):
        pass

    # Exit a parse tree produced by HiveParser#tablePartitionPrefix.
    def exitTablePartitionPrefix(self, ctx:HiveParser.TablePartitionPrefixContext):
        pass


    # Enter a parse tree produced by HiveParser#blocking.
    def enterBlocking(self, ctx:HiveParser.BlockingContext):
        pass

    # Exit a parse tree produced by HiveParser#blocking.
    def exitBlocking(self, ctx:HiveParser.BlockingContext):
        pass


    # Enter a parse tree produced by HiveParser#alterStatementSuffixCompact.
    def enterAlterStatementSuffixCompact(self, ctx:HiveParser.AlterStatementSuffixCompactContext):
        pass

    # Exit a parse tree produced by HiveParser#alterStatementSuffixCompact.
    def exitAlterStatementSuffixCompact(self, ctx:HiveParser.AlterStatementSuffixCompactContext):
        pass


    # Enter a parse tree produced by HiveParser#alterStatementSuffixSetOwner.
    def enterAlterStatementSuffixSetOwner(self, ctx:HiveParser.AlterStatementSuffixSetOwnerContext):
        pass

    # Exit a parse tree produced by HiveParser#alterStatementSuffixSetOwner.
    def exitAlterStatementSuffixSetOwner(self, ctx:HiveParser.AlterStatementSuffixSetOwnerContext):
        pass


    # Enter a parse tree produced by HiveParser#fileFormat.
    def enterFileFormat(self, ctx:HiveParser.FileFormatContext):
        pass

    # Exit a parse tree produced by HiveParser#fileFormat.
    def exitFileFormat(self, ctx:HiveParser.FileFormatContext):
        pass


    # Enter a parse tree produced by HiveParser#inputFileFormat.
    def enterInputFileFormat(self, ctx:HiveParser.InputFileFormatContext):
        pass

    # Exit a parse tree produced by HiveParser#inputFileFormat.
    def exitInputFileFormat(self, ctx:HiveParser.InputFileFormatContext):
        pass


    # Enter a parse tree produced by HiveParser#tabTypeExpr.
    def enterTabTypeExpr(self, ctx:HiveParser.TabTypeExprContext):
        pass

    # Exit a parse tree produced by HiveParser#tabTypeExpr.
    def exitTabTypeExpr(self, ctx:HiveParser.TabTypeExprContext):
        pass


    # Enter a parse tree produced by HiveParser#partTypeExpr.
    def enterPartTypeExpr(self, ctx:HiveParser.PartTypeExprContext):
        pass

    # Exit a parse tree produced by HiveParser#partTypeExpr.
    def exitPartTypeExpr(self, ctx:HiveParser.PartTypeExprContext):
        pass


    # Enter a parse tree produced by HiveParser#tabPartColTypeExpr.
    def enterTabPartColTypeExpr(self, ctx:HiveParser.TabPartColTypeExprContext):
        pass

    # Exit a parse tree produced by HiveParser#tabPartColTypeExpr.
    def exitTabPartColTypeExpr(self, ctx:HiveParser.TabPartColTypeExprContext):
        pass


    # Enter a parse tree produced by HiveParser#descStatement.
    def enterDescStatement(self, ctx:HiveParser.DescStatementContext):
        pass

    # Exit a parse tree produced by HiveParser#descStatement.
    def exitDescStatement(self, ctx:HiveParser.DescStatementContext):
        pass


    # Enter a parse tree produced by HiveParser#analyzeStatement.
    def enterAnalyzeStatement(self, ctx:HiveParser.AnalyzeStatementContext):
        pass

    # Exit a parse tree produced by HiveParser#analyzeStatement.
    def exitAnalyzeStatement(self, ctx:HiveParser.AnalyzeStatementContext):
        pass


    # Enter a parse tree produced by HiveParser#showStatement.
    def enterShowStatement(self, ctx:HiveParser.ShowStatementContext):
        pass

    # Exit a parse tree produced by HiveParser#showStatement.
    def exitShowStatement(self, ctx:HiveParser.ShowStatementContext):
        pass


    # Enter a parse tree produced by HiveParser#lockStatement.
    def enterLockStatement(self, ctx:HiveParser.LockStatementContext):
        pass

    # Exit a parse tree produced by HiveParser#lockStatement.
    def exitLockStatement(self, ctx:HiveParser.LockStatementContext):
        pass


    # Enter a parse tree produced by HiveParser#lockDatabase.
    def enterLockDatabase(self, ctx:HiveParser.LockDatabaseContext):
        pass

    # Exit a parse tree produced by HiveParser#lockDatabase.
    def exitLockDatabase(self, ctx:HiveParser.LockDatabaseContext):
        pass


    # Enter a parse tree produced by HiveParser#lockMode.
    def enterLockMode(self, ctx:HiveParser.LockModeContext):
        pass

    # Exit a parse tree produced by HiveParser#lockMode.
    def exitLockMode(self, ctx:HiveParser.LockModeContext):
        pass


    # Enter a parse tree produced by HiveParser#unlockStatement.
    def enterUnlockStatement(self, ctx:HiveParser.UnlockStatementContext):
        pass

    # Exit a parse tree produced by HiveParser#unlockStatement.
    def exitUnlockStatement(self, ctx:HiveParser.UnlockStatementContext):
        pass


    # Enter a parse tree produced by HiveParser#unlockDatabase.
    def enterUnlockDatabase(self, ctx:HiveParser.UnlockDatabaseContext):
        pass

    # Exit a parse tree produced by HiveParser#unlockDatabase.
    def exitUnlockDatabase(self, ctx:HiveParser.UnlockDatabaseContext):
        pass


    # Enter a parse tree produced by HiveParser#createRoleStatement.
    def enterCreateRoleStatement(self, ctx:HiveParser.CreateRoleStatementContext):
        pass

    # Exit a parse tree produced by HiveParser#createRoleStatement.
    def exitCreateRoleStatement(self, ctx:HiveParser.CreateRoleStatementContext):
        pass


    # Enter a parse tree produced by HiveParser#dropRoleStatement.
    def enterDropRoleStatement(self, ctx:HiveParser.DropRoleStatementContext):
        pass

    # Exit a parse tree produced by HiveParser#dropRoleStatement.
    def exitDropRoleStatement(self, ctx:HiveParser.DropRoleStatementContext):
        pass


    # Enter a parse tree produced by HiveParser#grantPrivileges.
    def enterGrantPrivileges(self, ctx:HiveParser.GrantPrivilegesContext):
        pass

    # Exit a parse tree produced by HiveParser#grantPrivileges.
    def exitGrantPrivileges(self, ctx:HiveParser.GrantPrivilegesContext):
        pass


    # Enter a parse tree produced by HiveParser#revokePrivileges.
    def enterRevokePrivileges(self, ctx:HiveParser.RevokePrivilegesContext):
        pass

    # Exit a parse tree produced by HiveParser#revokePrivileges.
    def exitRevokePrivileges(self, ctx:HiveParser.RevokePrivilegesContext):
        pass


    # Enter a parse tree produced by HiveParser#grantRole.
    def enterGrantRole(self, ctx:HiveParser.GrantRoleContext):
        pass

    # Exit a parse tree produced by HiveParser#grantRole.
    def exitGrantRole(self, ctx:HiveParser.GrantRoleContext):
        pass


    # Enter a parse tree produced by HiveParser#revokeRole.
    def enterRevokeRole(self, ctx:HiveParser.RevokeRoleContext):
        pass

    # Exit a parse tree produced by HiveParser#revokeRole.
    def exitRevokeRole(self, ctx:HiveParser.RevokeRoleContext):
        pass


    # Enter a parse tree produced by HiveParser#showRoleGrants.
    def enterShowRoleGrants(self, ctx:HiveParser.ShowRoleGrantsContext):
        pass

    # Exit a parse tree produced by HiveParser#showRoleGrants.
    def exitShowRoleGrants(self, ctx:HiveParser.ShowRoleGrantsContext):
        pass


    # Enter a parse tree produced by HiveParser#showRoles.
    def enterShowRoles(self, ctx:HiveParser.ShowRolesContext):
        pass

    # Exit a parse tree produced by HiveParser#showRoles.
    def exitShowRoles(self, ctx:HiveParser.ShowRolesContext):
        pass


    # Enter a parse tree produced by HiveParser#showCurrentRole.
    def enterShowCurrentRole(self, ctx:HiveParser.ShowCurrentRoleContext):
        pass

    # Exit a parse tree produced by HiveParser#showCurrentRole.
    def exitShowCurrentRole(self, ctx:HiveParser.ShowCurrentRoleContext):
        pass


    # Enter a parse tree produced by HiveParser#setRole.
    def enterSetRole(self, ctx:HiveParser.SetRoleContext):
        pass

    # Exit a parse tree produced by HiveParser#setRole.
    def exitSetRole(self, ctx:HiveParser.SetRoleContext):
        pass


    # Enter a parse tree produced by HiveParser#showGrants.
    def enterShowGrants(self, ctx:HiveParser.ShowGrantsContext):
        pass

    # Exit a parse tree produced by HiveParser#showGrants.
    def exitShowGrants(self, ctx:HiveParser.ShowGrantsContext):
        pass


    # Enter a parse tree produced by HiveParser#showRolePrincipals.
    def enterShowRolePrincipals(self, ctx:HiveParser.ShowRolePrincipalsContext):
        pass

    # Exit a parse tree produced by HiveParser#showRolePrincipals.
    def exitShowRolePrincipals(self, ctx:HiveParser.ShowRolePrincipalsContext):
        pass


    # Enter a parse tree produced by HiveParser#privilegeIncludeColObject.
    def enterPrivilegeIncludeColObject(self, ctx:HiveParser.PrivilegeIncludeColObjectContext):
        pass

    # Exit a parse tree produced by HiveParser#privilegeIncludeColObject.
    def exitPrivilegeIncludeColObject(self, ctx:HiveParser.PrivilegeIncludeColObjectContext):
        pass


    # Enter a parse tree produced by HiveParser#privilegeObject.
    def enterPrivilegeObject(self, ctx:HiveParser.PrivilegeObjectContext):
        pass

    # Exit a parse tree produced by HiveParser#privilegeObject.
    def exitPrivilegeObject(self, ctx:HiveParser.PrivilegeObjectContext):
        pass


    # Enter a parse tree produced by HiveParser#privObject.
    def enterPrivObject(self, ctx:HiveParser.PrivObjectContext):
        pass

    # Exit a parse tree produced by HiveParser#privObject.
    def exitPrivObject(self, ctx:HiveParser.PrivObjectContext):
        pass


    # Enter a parse tree produced by HiveParser#privObjectCols.
    def enterPrivObjectCols(self, ctx:HiveParser.PrivObjectColsContext):
        pass

    # Exit a parse tree produced by HiveParser#privObjectCols.
    def exitPrivObjectCols(self, ctx:HiveParser.PrivObjectColsContext):
        pass


    # Enter a parse tree produced by HiveParser#privilegeList.
    def enterPrivilegeList(self, ctx:HiveParser.PrivilegeListContext):
        pass

    # Exit a parse tree produced by HiveParser#privilegeList.
    def exitPrivilegeList(self, ctx:HiveParser.PrivilegeListContext):
        pass


    # Enter a parse tree produced by HiveParser#privlegeDef.
    def enterPrivlegeDef(self, ctx:HiveParser.PrivlegeDefContext):
        pass

    # Exit a parse tree produced by HiveParser#privlegeDef.
    def exitPrivlegeDef(self, ctx:HiveParser.PrivlegeDefContext):
        pass


    # Enter a parse tree produced by HiveParser#privilegeType.
    def enterPrivilegeType(self, ctx:HiveParser.PrivilegeTypeContext):
        pass

    # Exit a parse tree produced by HiveParser#privilegeType.
    def exitPrivilegeType(self, ctx:HiveParser.PrivilegeTypeContext):
        pass


    # Enter a parse tree produced by HiveParser#principalSpecification.
    def enterPrincipalSpecification(self, ctx:HiveParser.PrincipalSpecificationContext):
        pass

    # Exit a parse tree produced by HiveParser#principalSpecification.
    def exitPrincipalSpecification(self, ctx:HiveParser.PrincipalSpecificationContext):
        pass


    # Enter a parse tree produced by HiveParser#principalName.
    def enterPrincipalName(self, ctx:HiveParser.PrincipalNameContext):
        pass

    # Exit a parse tree produced by HiveParser#principalName.
    def exitPrincipalName(self, ctx:HiveParser.PrincipalNameContext):
        pass


    # Enter a parse tree produced by HiveParser#withGrantOption.
    def enterWithGrantOption(self, ctx:HiveParser.WithGrantOptionContext):
        pass

    # Exit a parse tree produced by HiveParser#withGrantOption.
    def exitWithGrantOption(self, ctx:HiveParser.WithGrantOptionContext):
        pass


    # Enter a parse tree produced by HiveParser#grantOptionFor.
    def enterGrantOptionFor(self, ctx:HiveParser.GrantOptionForContext):
        pass

    # Exit a parse tree produced by HiveParser#grantOptionFor.
    def exitGrantOptionFor(self, ctx:HiveParser.GrantOptionForContext):
        pass


    # Enter a parse tree produced by HiveParser#adminOptionFor.
    def enterAdminOptionFor(self, ctx:HiveParser.AdminOptionForContext):
        pass

    # Exit a parse tree produced by HiveParser#adminOptionFor.
    def exitAdminOptionFor(self, ctx:HiveParser.AdminOptionForContext):
        pass


    # Enter a parse tree produced by HiveParser#withAdminOption.
    def enterWithAdminOption(self, ctx:HiveParser.WithAdminOptionContext):
        pass

    # Exit a parse tree produced by HiveParser#withAdminOption.
    def exitWithAdminOption(self, ctx:HiveParser.WithAdminOptionContext):
        pass


    # Enter a parse tree produced by HiveParser#metastoreCheck.
    def enterMetastoreCheck(self, ctx:HiveParser.MetastoreCheckContext):
        pass

    # Exit a parse tree produced by HiveParser#metastoreCheck.
    def exitMetastoreCheck(self, ctx:HiveParser.MetastoreCheckContext):
        pass


    # Enter a parse tree produced by HiveParser#resourceList.
    def enterResourceList(self, ctx:HiveParser.ResourceListContext):
        pass

    # Exit a parse tree produced by HiveParser#resourceList.
    def exitResourceList(self, ctx:HiveParser.ResourceListContext):
        pass


    # Enter a parse tree produced by HiveParser#resource.
    def enterResource(self, ctx:HiveParser.ResourceContext):
        pass

    # Exit a parse tree produced by HiveParser#resource.
    def exitResource(self, ctx:HiveParser.ResourceContext):
        pass


    # Enter a parse tree produced by HiveParser#resourceType.
    def enterResourceType(self, ctx:HiveParser.ResourceTypeContext):
        pass

    # Exit a parse tree produced by HiveParser#resourceType.
    def exitResourceType(self, ctx:HiveParser.ResourceTypeContext):
        pass


    # Enter a parse tree produced by HiveParser#createFunctionStatement.
    def enterCreateFunctionStatement(self, ctx:HiveParser.CreateFunctionStatementContext):
        pass

    # Exit a parse tree produced by HiveParser#createFunctionStatement.
    def exitCreateFunctionStatement(self, ctx:HiveParser.CreateFunctionStatementContext):
        pass


    # Enter a parse tree produced by HiveParser#dropFunctionStatement.
    def enterDropFunctionStatement(self, ctx:HiveParser.DropFunctionStatementContext):
        pass

    # Exit a parse tree produced by HiveParser#dropFunctionStatement.
    def exitDropFunctionStatement(self, ctx:HiveParser.DropFunctionStatementContext):
        pass


    # Enter a parse tree produced by HiveParser#reloadFunctionStatement.
    def enterReloadFunctionStatement(self, ctx:HiveParser.ReloadFunctionStatementContext):
        pass

    # Exit a parse tree produced by HiveParser#reloadFunctionStatement.
    def exitReloadFunctionStatement(self, ctx:HiveParser.ReloadFunctionStatementContext):
        pass


    # Enter a parse tree produced by HiveParser#createMacroStatement.
    def enterCreateMacroStatement(self, ctx:HiveParser.CreateMacroStatementContext):
        pass

    # Exit a parse tree produced by HiveParser#createMacroStatement.
    def exitCreateMacroStatement(self, ctx:HiveParser.CreateMacroStatementContext):
        pass


    # Enter a parse tree produced by HiveParser#dropMacroStatement.
    def enterDropMacroStatement(self, ctx:HiveParser.DropMacroStatementContext):
        pass

    # Exit a parse tree produced by HiveParser#dropMacroStatement.
    def exitDropMacroStatement(self, ctx:HiveParser.DropMacroStatementContext):
        pass


    # Enter a parse tree produced by HiveParser#createViewStatement.
    def enterCreateViewStatement(self, ctx:HiveParser.CreateViewStatementContext):
        pass

    # Exit a parse tree produced by HiveParser#createViewStatement.
    def exitCreateViewStatement(self, ctx:HiveParser.CreateViewStatementContext):
        pass


    # Enter a parse tree produced by HiveParser#createMaterializedViewStatement.
    def enterCreateMaterializedViewStatement(self, ctx:HiveParser.CreateMaterializedViewStatementContext):
        pass

    # Exit a parse tree produced by HiveParser#createMaterializedViewStatement.
    def exitCreateMaterializedViewStatement(self, ctx:HiveParser.CreateMaterializedViewStatementContext):
        pass


    # Enter a parse tree produced by HiveParser#viewPartition.
    def enterViewPartition(self, ctx:HiveParser.ViewPartitionContext):
        pass

    # Exit a parse tree produced by HiveParser#viewPartition.
    def exitViewPartition(self, ctx:HiveParser.ViewPartitionContext):
        pass


    # Enter a parse tree produced by HiveParser#dropViewStatement.
    def enterDropViewStatement(self, ctx:HiveParser.DropViewStatementContext):
        pass

    # Exit a parse tree produced by HiveParser#dropViewStatement.
    def exitDropViewStatement(self, ctx:HiveParser.DropViewStatementContext):
        pass


    # Enter a parse tree produced by HiveParser#dropMaterializedViewStatement.
    def enterDropMaterializedViewStatement(self, ctx:HiveParser.DropMaterializedViewStatementContext):
        pass

    # Exit a parse tree produced by HiveParser#dropMaterializedViewStatement.
    def exitDropMaterializedViewStatement(self, ctx:HiveParser.DropMaterializedViewStatementContext):
        pass


    # Enter a parse tree produced by HiveParser#showFunctionIdentifier.
    def enterShowFunctionIdentifier(self, ctx:HiveParser.ShowFunctionIdentifierContext):
        pass

    # Exit a parse tree produced by HiveParser#showFunctionIdentifier.
    def exitShowFunctionIdentifier(self, ctx:HiveParser.ShowFunctionIdentifierContext):
        pass


    # Enter a parse tree produced by HiveParser#showStmtIdentifier.
    def enterShowStmtIdentifier(self, ctx:HiveParser.ShowStmtIdentifierContext):
        pass

    # Exit a parse tree produced by HiveParser#showStmtIdentifier.
    def exitShowStmtIdentifier(self, ctx:HiveParser.ShowStmtIdentifierContext):
        pass


    # Enter a parse tree produced by HiveParser#tableComment.
    def enterTableComment(self, ctx:HiveParser.TableCommentContext):
        pass

    # Exit a parse tree produced by HiveParser#tableComment.
    def exitTableComment(self, ctx:HiveParser.TableCommentContext):
        pass


    # Enter a parse tree produced by HiveParser#tablePartition.
    def enterTablePartition(self, ctx:HiveParser.TablePartitionContext):
        pass

    # Exit a parse tree produced by HiveParser#tablePartition.
    def exitTablePartition(self, ctx:HiveParser.TablePartitionContext):
        pass


    # Enter a parse tree produced by HiveParser#tableBuckets.
    def enterTableBuckets(self, ctx:HiveParser.TableBucketsContext):
        pass

    # Exit a parse tree produced by HiveParser#tableBuckets.
    def exitTableBuckets(self, ctx:HiveParser.TableBucketsContext):
        pass


    # Enter a parse tree produced by HiveParser#tableSkewed.
    def enterTableSkewed(self, ctx:HiveParser.TableSkewedContext):
        pass

    # Exit a parse tree produced by HiveParser#tableSkewed.
    def exitTableSkewed(self, ctx:HiveParser.TableSkewedContext):
        pass


    # Enter a parse tree produced by HiveParser#rowFormat.
    def enterRowFormat(self, ctx:HiveParser.RowFormatContext):
        pass

    # Exit a parse tree produced by HiveParser#rowFormat.
    def exitRowFormat(self, ctx:HiveParser.RowFormatContext):
        pass


    # Enter a parse tree produced by HiveParser#recordReader.
    def enterRecordReader(self, ctx:HiveParser.RecordReaderContext):
        pass

    # Exit a parse tree produced by HiveParser#recordReader.
    def exitRecordReader(self, ctx:HiveParser.RecordReaderContext):
        pass


    # Enter a parse tree produced by HiveParser#recordWriter.
    def enterRecordWriter(self, ctx:HiveParser.RecordWriterContext):
        pass

    # Exit a parse tree produced by HiveParser#recordWriter.
    def exitRecordWriter(self, ctx:HiveParser.RecordWriterContext):
        pass


    # Enter a parse tree produced by HiveParser#rowFormatSerde.
    def enterRowFormatSerde(self, ctx:HiveParser.RowFormatSerdeContext):
        pass

    # Exit a parse tree produced by HiveParser#rowFormatSerde.
    def exitRowFormatSerde(self, ctx:HiveParser.RowFormatSerdeContext):
        pass


    # Enter a parse tree produced by HiveParser#rowFormatDelimited.
    def enterRowFormatDelimited(self, ctx:HiveParser.RowFormatDelimitedContext):
        pass

    # Exit a parse tree produced by HiveParser#rowFormatDelimited.
    def exitRowFormatDelimited(self, ctx:HiveParser.RowFormatDelimitedContext):
        pass


    # Enter a parse tree produced by HiveParser#tableRowFormat.
    def enterTableRowFormat(self, ctx:HiveParser.TableRowFormatContext):
        pass

    # Exit a parse tree produced by HiveParser#tableRowFormat.
    def exitTableRowFormat(self, ctx:HiveParser.TableRowFormatContext):
        pass


    # Enter a parse tree produced by HiveParser#tablePropertiesPrefixed.
    def enterTablePropertiesPrefixed(self, ctx:HiveParser.TablePropertiesPrefixedContext):
        pass

    # Exit a parse tree produced by HiveParser#tablePropertiesPrefixed.
    def exitTablePropertiesPrefixed(self, ctx:HiveParser.TablePropertiesPrefixedContext):
        pass


    # Enter a parse tree produced by HiveParser#tableProperties.
    def enterTableProperties(self, ctx:HiveParser.TablePropertiesContext):
        pass

    # Exit a parse tree produced by HiveParser#tableProperties.
    def exitTableProperties(self, ctx:HiveParser.TablePropertiesContext):
        pass


    # Enter a parse tree produced by HiveParser#tablePropertiesList.
    def enterTablePropertiesList(self, ctx:HiveParser.TablePropertiesListContext):
        pass

    # Exit a parse tree produced by HiveParser#tablePropertiesList.
    def exitTablePropertiesList(self, ctx:HiveParser.TablePropertiesListContext):
        pass


    # Enter a parse tree produced by HiveParser#keyValueProperty.
    def enterKeyValueProperty(self, ctx:HiveParser.KeyValuePropertyContext):
        pass

    # Exit a parse tree produced by HiveParser#keyValueProperty.
    def exitKeyValueProperty(self, ctx:HiveParser.KeyValuePropertyContext):
        pass


    # Enter a parse tree produced by HiveParser#keyProperty.
    def enterKeyProperty(self, ctx:HiveParser.KeyPropertyContext):
        pass

    # Exit a parse tree produced by HiveParser#keyProperty.
    def exitKeyProperty(self, ctx:HiveParser.KeyPropertyContext):
        pass


    # Enter a parse tree produced by HiveParser#tableRowFormatFieldIdentifier.
    def enterTableRowFormatFieldIdentifier(self, ctx:HiveParser.TableRowFormatFieldIdentifierContext):
        pass

    # Exit a parse tree produced by HiveParser#tableRowFormatFieldIdentifier.
    def exitTableRowFormatFieldIdentifier(self, ctx:HiveParser.TableRowFormatFieldIdentifierContext):
        pass


    # Enter a parse tree produced by HiveParser#tableRowFormatCollItemsIdentifier.
    def enterTableRowFormatCollItemsIdentifier(self, ctx:HiveParser.TableRowFormatCollItemsIdentifierContext):
        pass

    # Exit a parse tree produced by HiveParser#tableRowFormatCollItemsIdentifier.
    def exitTableRowFormatCollItemsIdentifier(self, ctx:HiveParser.TableRowFormatCollItemsIdentifierContext):
        pass


    # Enter a parse tree produced by HiveParser#tableRowFormatMapKeysIdentifier.
    def enterTableRowFormatMapKeysIdentifier(self, ctx:HiveParser.TableRowFormatMapKeysIdentifierContext):
        pass

    # Exit a parse tree produced by HiveParser#tableRowFormatMapKeysIdentifier.
    def exitTableRowFormatMapKeysIdentifier(self, ctx:HiveParser.TableRowFormatMapKeysIdentifierContext):
        pass


    # Enter a parse tree produced by HiveParser#tableRowFormatLinesIdentifier.
    def enterTableRowFormatLinesIdentifier(self, ctx:HiveParser.TableRowFormatLinesIdentifierContext):
        pass

    # Exit a parse tree produced by HiveParser#tableRowFormatLinesIdentifier.
    def exitTableRowFormatLinesIdentifier(self, ctx:HiveParser.TableRowFormatLinesIdentifierContext):
        pass


    # Enter a parse tree produced by HiveParser#tableRowNullFormat.
    def enterTableRowNullFormat(self, ctx:HiveParser.TableRowNullFormatContext):
        pass

    # Exit a parse tree produced by HiveParser#tableRowNullFormat.
    def exitTableRowNullFormat(self, ctx:HiveParser.TableRowNullFormatContext):
        pass


    # Enter a parse tree produced by HiveParser#tableFileFormat.
    def enterTableFileFormat(self, ctx:HiveParser.TableFileFormatContext):
        pass

    # Exit a parse tree produced by HiveParser#tableFileFormat.
    def exitTableFileFormat(self, ctx:HiveParser.TableFileFormatContext):
        pass


    # Enter a parse tree produced by HiveParser#tableLocation.
    def enterTableLocation(self, ctx:HiveParser.TableLocationContext):
        pass

    # Exit a parse tree produced by HiveParser#tableLocation.
    def exitTableLocation(self, ctx:HiveParser.TableLocationContext):
        pass


    # Enter a parse tree produced by HiveParser#columnNameTypeList.
    def enterColumnNameTypeList(self, ctx:HiveParser.ColumnNameTypeListContext):
        pass

    # Exit a parse tree produced by HiveParser#columnNameTypeList.
    def exitColumnNameTypeList(self, ctx:HiveParser.ColumnNameTypeListContext):
        pass


    # Enter a parse tree produced by HiveParser#columnNameTypeOrConstraintList.
    def enterColumnNameTypeOrConstraintList(self, ctx:HiveParser.ColumnNameTypeOrConstraintListContext):
        pass

    # Exit a parse tree produced by HiveParser#columnNameTypeOrConstraintList.
    def exitColumnNameTypeOrConstraintList(self, ctx:HiveParser.ColumnNameTypeOrConstraintListContext):
        pass


    # Enter a parse tree produced by HiveParser#columnNameColonTypeList.
    def enterColumnNameColonTypeList(self, ctx:HiveParser.ColumnNameColonTypeListContext):
        pass

    # Exit a parse tree produced by HiveParser#columnNameColonTypeList.
    def exitColumnNameColonTypeList(self, ctx:HiveParser.ColumnNameColonTypeListContext):
        pass


    # Enter a parse tree produced by HiveParser#columnNameList.
    def enterColumnNameList(self, ctx:HiveParser.ColumnNameListContext):
        pass

    # Exit a parse tree produced by HiveParser#columnNameList.
    def exitColumnNameList(self, ctx:HiveParser.ColumnNameListContext):
        pass


    # Enter a parse tree produced by HiveParser#columnName.
    def enterColumnName(self, ctx:HiveParser.ColumnNameContext):
        pass

    # Exit a parse tree produced by HiveParser#columnName.
    def exitColumnName(self, ctx:HiveParser.ColumnNameContext):
        pass


    # Enter a parse tree produced by HiveParser#extColumnName.
    def enterExtColumnName(self, ctx:HiveParser.ExtColumnNameContext):
        pass

    # Exit a parse tree produced by HiveParser#extColumnName.
    def exitExtColumnName(self, ctx:HiveParser.ExtColumnNameContext):
        pass


    # Enter a parse tree produced by HiveParser#columnNameOrderList.
    def enterColumnNameOrderList(self, ctx:HiveParser.ColumnNameOrderListContext):
        pass

    # Exit a parse tree produced by HiveParser#columnNameOrderList.
    def exitColumnNameOrderList(self, ctx:HiveParser.ColumnNameOrderListContext):
        pass


    # Enter a parse tree produced by HiveParser#columnParenthesesList.
    def enterColumnParenthesesList(self, ctx:HiveParser.ColumnParenthesesListContext):
        pass

    # Exit a parse tree produced by HiveParser#columnParenthesesList.
    def exitColumnParenthesesList(self, ctx:HiveParser.ColumnParenthesesListContext):
        pass


    # Enter a parse tree produced by HiveParser#enableValidateSpecification.
    def enterEnableValidateSpecification(self, ctx:HiveParser.EnableValidateSpecificationContext):
        pass

    # Exit a parse tree produced by HiveParser#enableValidateSpecification.
    def exitEnableValidateSpecification(self, ctx:HiveParser.EnableValidateSpecificationContext):
        pass


    # Enter a parse tree produced by HiveParser#enableSpecification.
    def enterEnableSpecification(self, ctx:HiveParser.EnableSpecificationContext):
        pass

    # Exit a parse tree produced by HiveParser#enableSpecification.
    def exitEnableSpecification(self, ctx:HiveParser.EnableSpecificationContext):
        pass


    # Enter a parse tree produced by HiveParser#validateSpecification.
    def enterValidateSpecification(self, ctx:HiveParser.ValidateSpecificationContext):
        pass

    # Exit a parse tree produced by HiveParser#validateSpecification.
    def exitValidateSpecification(self, ctx:HiveParser.ValidateSpecificationContext):
        pass


    # Enter a parse tree produced by HiveParser#enforcedSpecification.
    def enterEnforcedSpecification(self, ctx:HiveParser.EnforcedSpecificationContext):
        pass

    # Exit a parse tree produced by HiveParser#enforcedSpecification.
    def exitEnforcedSpecification(self, ctx:HiveParser.EnforcedSpecificationContext):
        pass


    # Enter a parse tree produced by HiveParser#relySpecification.
    def enterRelySpecification(self, ctx:HiveParser.RelySpecificationContext):
        pass

    # Exit a parse tree produced by HiveParser#relySpecification.
    def exitRelySpecification(self, ctx:HiveParser.RelySpecificationContext):
        pass


    # Enter a parse tree produced by HiveParser#createConstraint.
    def enterCreateConstraint(self, ctx:HiveParser.CreateConstraintContext):
        pass

    # Exit a parse tree produced by HiveParser#createConstraint.
    def exitCreateConstraint(self, ctx:HiveParser.CreateConstraintContext):
        pass


    # Enter a parse tree produced by HiveParser#alterConstraintWithName.
    def enterAlterConstraintWithName(self, ctx:HiveParser.AlterConstraintWithNameContext):
        pass

    # Exit a parse tree produced by HiveParser#alterConstraintWithName.
    def exitAlterConstraintWithName(self, ctx:HiveParser.AlterConstraintWithNameContext):
        pass


    # Enter a parse tree produced by HiveParser#pkConstraint.
    def enterPkConstraint(self, ctx:HiveParser.PkConstraintContext):
        pass

    # Exit a parse tree produced by HiveParser#pkConstraint.
    def exitPkConstraint(self, ctx:HiveParser.PkConstraintContext):
        pass


    # Enter a parse tree produced by HiveParser#createForeignKey.
    def enterCreateForeignKey(self, ctx:HiveParser.CreateForeignKeyContext):
        pass

    # Exit a parse tree produced by HiveParser#createForeignKey.
    def exitCreateForeignKey(self, ctx:HiveParser.CreateForeignKeyContext):
        pass


    # Enter a parse tree produced by HiveParser#alterForeignKeyWithName.
    def enterAlterForeignKeyWithName(self, ctx:HiveParser.AlterForeignKeyWithNameContext):
        pass

    # Exit a parse tree produced by HiveParser#alterForeignKeyWithName.
    def exitAlterForeignKeyWithName(self, ctx:HiveParser.AlterForeignKeyWithNameContext):
        pass


    # Enter a parse tree produced by HiveParser#skewedValueElement.
    def enterSkewedValueElement(self, ctx:HiveParser.SkewedValueElementContext):
        pass

    # Exit a parse tree produced by HiveParser#skewedValueElement.
    def exitSkewedValueElement(self, ctx:HiveParser.SkewedValueElementContext):
        pass


    # Enter a parse tree produced by HiveParser#skewedColumnValuePairList.
    def enterSkewedColumnValuePairList(self, ctx:HiveParser.SkewedColumnValuePairListContext):
        pass

    # Exit a parse tree produced by HiveParser#skewedColumnValuePairList.
    def exitSkewedColumnValuePairList(self, ctx:HiveParser.SkewedColumnValuePairListContext):
        pass


    # Enter a parse tree produced by HiveParser#skewedColumnValuePair.
    def enterSkewedColumnValuePair(self, ctx:HiveParser.SkewedColumnValuePairContext):
        pass

    # Exit a parse tree produced by HiveParser#skewedColumnValuePair.
    def exitSkewedColumnValuePair(self, ctx:HiveParser.SkewedColumnValuePairContext):
        pass


    # Enter a parse tree produced by HiveParser#skewedColumnValues.
    def enterSkewedColumnValues(self, ctx:HiveParser.SkewedColumnValuesContext):
        pass

    # Exit a parse tree produced by HiveParser#skewedColumnValues.
    def exitSkewedColumnValues(self, ctx:HiveParser.SkewedColumnValuesContext):
        pass


    # Enter a parse tree produced by HiveParser#skewedColumnValue.
    def enterSkewedColumnValue(self, ctx:HiveParser.SkewedColumnValueContext):
        pass

    # Exit a parse tree produced by HiveParser#skewedColumnValue.
    def exitSkewedColumnValue(self, ctx:HiveParser.SkewedColumnValueContext):
        pass


    # Enter a parse tree produced by HiveParser#skewedValueLocationElement.
    def enterSkewedValueLocationElement(self, ctx:HiveParser.SkewedValueLocationElementContext):
        pass

    # Exit a parse tree produced by HiveParser#skewedValueLocationElement.
    def exitSkewedValueLocationElement(self, ctx:HiveParser.SkewedValueLocationElementContext):
        pass


    # Enter a parse tree produced by HiveParser#orderSpecification.
    def enterOrderSpecification(self, ctx:HiveParser.OrderSpecificationContext):
        pass

    # Exit a parse tree produced by HiveParser#orderSpecification.
    def exitOrderSpecification(self, ctx:HiveParser.OrderSpecificationContext):
        pass


    # Enter a parse tree produced by HiveParser#nullOrdering.
    def enterNullOrdering(self, ctx:HiveParser.NullOrderingContext):
        pass

    # Exit a parse tree produced by HiveParser#nullOrdering.
    def exitNullOrdering(self, ctx:HiveParser.NullOrderingContext):
        pass


    # Enter a parse tree produced by HiveParser#columnNameOrder.
    def enterColumnNameOrder(self, ctx:HiveParser.ColumnNameOrderContext):
        pass

    # Exit a parse tree produced by HiveParser#columnNameOrder.
    def exitColumnNameOrder(self, ctx:HiveParser.ColumnNameOrderContext):
        pass


    # Enter a parse tree produced by HiveParser#columnNameCommentList.
    def enterColumnNameCommentList(self, ctx:HiveParser.ColumnNameCommentListContext):
        pass

    # Exit a parse tree produced by HiveParser#columnNameCommentList.
    def exitColumnNameCommentList(self, ctx:HiveParser.ColumnNameCommentListContext):
        pass


    # Enter a parse tree produced by HiveParser#columnNameComment.
    def enterColumnNameComment(self, ctx:HiveParser.ColumnNameCommentContext):
        pass

    # Exit a parse tree produced by HiveParser#columnNameComment.
    def exitColumnNameComment(self, ctx:HiveParser.ColumnNameCommentContext):
        pass


    # Enter a parse tree produced by HiveParser#columnRefOrder.
    def enterColumnRefOrder(self, ctx:HiveParser.ColumnRefOrderContext):
        pass

    # Exit a parse tree produced by HiveParser#columnRefOrder.
    def exitColumnRefOrder(self, ctx:HiveParser.ColumnRefOrderContext):
        pass


    # Enter a parse tree produced by HiveParser#columnNameType.
    def enterColumnNameType(self, ctx:HiveParser.ColumnNameTypeContext):
        pass

    # Exit a parse tree produced by HiveParser#columnNameType.
    def exitColumnNameType(self, ctx:HiveParser.ColumnNameTypeContext):
        pass


    # Enter a parse tree produced by HiveParser#columnNameTypeOrConstraint.
    def enterColumnNameTypeOrConstraint(self, ctx:HiveParser.ColumnNameTypeOrConstraintContext):
        pass

    # Exit a parse tree produced by HiveParser#columnNameTypeOrConstraint.
    def exitColumnNameTypeOrConstraint(self, ctx:HiveParser.ColumnNameTypeOrConstraintContext):
        pass


    # Enter a parse tree produced by HiveParser#tableConstraint.
    def enterTableConstraint(self, ctx:HiveParser.TableConstraintContext):
        pass

    # Exit a parse tree produced by HiveParser#tableConstraint.
    def exitTableConstraint(self, ctx:HiveParser.TableConstraintContext):
        pass


    # Enter a parse tree produced by HiveParser#columnNameTypeConstraint.
    def enterColumnNameTypeConstraint(self, ctx:HiveParser.ColumnNameTypeConstraintContext):
        pass

    # Exit a parse tree produced by HiveParser#columnNameTypeConstraint.
    def exitColumnNameTypeConstraint(self, ctx:HiveParser.ColumnNameTypeConstraintContext):
        pass


    # Enter a parse tree produced by HiveParser#columnConstraint.
    def enterColumnConstraint(self, ctx:HiveParser.ColumnConstraintContext):
        pass

    # Exit a parse tree produced by HiveParser#columnConstraint.
    def exitColumnConstraint(self, ctx:HiveParser.ColumnConstraintContext):
        pass


    # Enter a parse tree produced by HiveParser#foreignKeyConstraint.
    def enterForeignKeyConstraint(self, ctx:HiveParser.ForeignKeyConstraintContext):
        pass

    # Exit a parse tree produced by HiveParser#foreignKeyConstraint.
    def exitForeignKeyConstraint(self, ctx:HiveParser.ForeignKeyConstraintContext):
        pass


    # Enter a parse tree produced by HiveParser#colConstraint.
    def enterColConstraint(self, ctx:HiveParser.ColConstraintContext):
        pass

    # Exit a parse tree produced by HiveParser#colConstraint.
    def exitColConstraint(self, ctx:HiveParser.ColConstraintContext):
        pass


    # Enter a parse tree produced by HiveParser#alterColumnConstraint.
    def enterAlterColumnConstraint(self, ctx:HiveParser.AlterColumnConstraintContext):
        pass

    # Exit a parse tree produced by HiveParser#alterColumnConstraint.
    def exitAlterColumnConstraint(self, ctx:HiveParser.AlterColumnConstraintContext):
        pass


    # Enter a parse tree produced by HiveParser#alterForeignKeyConstraint.
    def enterAlterForeignKeyConstraint(self, ctx:HiveParser.AlterForeignKeyConstraintContext):
        pass

    # Exit a parse tree produced by HiveParser#alterForeignKeyConstraint.
    def exitAlterForeignKeyConstraint(self, ctx:HiveParser.AlterForeignKeyConstraintContext):
        pass


    # Enter a parse tree produced by HiveParser#alterColConstraint.
    def enterAlterColConstraint(self, ctx:HiveParser.AlterColConstraintContext):
        pass

    # Exit a parse tree produced by HiveParser#alterColConstraint.
    def exitAlterColConstraint(self, ctx:HiveParser.AlterColConstraintContext):
        pass


    # Enter a parse tree produced by HiveParser#tableConstraintPrimaryKey.
    def enterTableConstraintPrimaryKey(self, ctx:HiveParser.TableConstraintPrimaryKeyContext):
        pass

    # Exit a parse tree produced by HiveParser#tableConstraintPrimaryKey.
    def exitTableConstraintPrimaryKey(self, ctx:HiveParser.TableConstraintPrimaryKeyContext):
        pass


    # Enter a parse tree produced by HiveParser#constraintOptsCreate.
    def enterConstraintOptsCreate(self, ctx:HiveParser.ConstraintOptsCreateContext):
        pass

    # Exit a parse tree produced by HiveParser#constraintOptsCreate.
    def exitConstraintOptsCreate(self, ctx:HiveParser.ConstraintOptsCreateContext):
        pass


    # Enter a parse tree produced by HiveParser#constraintOptsAlter.
    def enterConstraintOptsAlter(self, ctx:HiveParser.ConstraintOptsAlterContext):
        pass

    # Exit a parse tree produced by HiveParser#constraintOptsAlter.
    def exitConstraintOptsAlter(self, ctx:HiveParser.ConstraintOptsAlterContext):
        pass


    # Enter a parse tree produced by HiveParser#columnNameColonType.
    def enterColumnNameColonType(self, ctx:HiveParser.ColumnNameColonTypeContext):
        pass

    # Exit a parse tree produced by HiveParser#columnNameColonType.
    def exitColumnNameColonType(self, ctx:HiveParser.ColumnNameColonTypeContext):
        pass


    # Enter a parse tree produced by HiveParser#colType.
    def enterColType(self, ctx:HiveParser.ColTypeContext):
        pass

    # Exit a parse tree produced by HiveParser#colType.
    def exitColType(self, ctx:HiveParser.ColTypeContext):
        pass


    # Enter a parse tree produced by HiveParser#colTypeList.
    def enterColTypeList(self, ctx:HiveParser.ColTypeListContext):
        pass

    # Exit a parse tree produced by HiveParser#colTypeList.
    def exitColTypeList(self, ctx:HiveParser.ColTypeListContext):
        pass


    # Enter a parse tree produced by HiveParser#type_db_col.
    def enterType_db_col(self, ctx:HiveParser.Type_db_colContext):
        pass

    # Exit a parse tree produced by HiveParser#type_db_col.
    def exitType_db_col(self, ctx:HiveParser.Type_db_colContext):
        pass


    # Enter a parse tree produced by HiveParser#primitiveType.
    def enterPrimitiveType(self, ctx:HiveParser.PrimitiveTypeContext):
        pass

    # Exit a parse tree produced by HiveParser#primitiveType.
    def exitPrimitiveType(self, ctx:HiveParser.PrimitiveTypeContext):
        pass


    # Enter a parse tree produced by HiveParser#listType.
    def enterListType(self, ctx:HiveParser.ListTypeContext):
        pass

    # Exit a parse tree produced by HiveParser#listType.
    def exitListType(self, ctx:HiveParser.ListTypeContext):
        pass


    # Enter a parse tree produced by HiveParser#structType.
    def enterStructType(self, ctx:HiveParser.StructTypeContext):
        pass

    # Exit a parse tree produced by HiveParser#structType.
    def exitStructType(self, ctx:HiveParser.StructTypeContext):
        pass


    # Enter a parse tree produced by HiveParser#mapType.
    def enterMapType(self, ctx:HiveParser.MapTypeContext):
        pass

    # Exit a parse tree produced by HiveParser#mapType.
    def exitMapType(self, ctx:HiveParser.MapTypeContext):
        pass


    # Enter a parse tree produced by HiveParser#unionType.
    def enterUnionType(self, ctx:HiveParser.UnionTypeContext):
        pass

    # Exit a parse tree produced by HiveParser#unionType.
    def exitUnionType(self, ctx:HiveParser.UnionTypeContext):
        pass


    # Enter a parse tree produced by HiveParser#setOperator.
    def enterSetOperator(self, ctx:HiveParser.SetOperatorContext):
        pass

    # Exit a parse tree produced by HiveParser#setOperator.
    def exitSetOperator(self, ctx:HiveParser.SetOperatorContext):
        pass


    # Enter a parse tree produced by HiveParser#queryStatementExpression.
    def enterQueryStatementExpression(self, ctx:HiveParser.QueryStatementExpressionContext):
        pass

    # Exit a parse tree produced by HiveParser#queryStatementExpression.
    def exitQueryStatementExpression(self, ctx:HiveParser.QueryStatementExpressionContext):
        pass


    # Enter a parse tree produced by HiveParser#queryStatementExpressionBody.
    def enterQueryStatementExpressionBody(self, ctx:HiveParser.QueryStatementExpressionBodyContext):
        pass

    # Exit a parse tree produced by HiveParser#queryStatementExpressionBody.
    def exitQueryStatementExpressionBody(self, ctx:HiveParser.QueryStatementExpressionBodyContext):
        pass


    # Enter a parse tree produced by HiveParser#withClause.
    def enterWithClause(self, ctx:HiveParser.WithClauseContext):
        pass

    # Exit a parse tree produced by HiveParser#withClause.
    def exitWithClause(self, ctx:HiveParser.WithClauseContext):
        pass


    # Enter a parse tree produced by HiveParser#cteStatement.
    def enterCteStatement(self, ctx:HiveParser.CteStatementContext):
        pass

    # Exit a parse tree produced by HiveParser#cteStatement.
    def exitCteStatement(self, ctx:HiveParser.CteStatementContext):
        pass


    # Enter a parse tree produced by HiveParser#fromStatement.
    def enterFromStatement(self, ctx:HiveParser.FromStatementContext):
        pass

    # Exit a parse tree produced by HiveParser#fromStatement.
    def exitFromStatement(self, ctx:HiveParser.FromStatementContext):
        pass


    # Enter a parse tree produced by HiveParser#singleFromStatement.
    def enterSingleFromStatement(self, ctx:HiveParser.SingleFromStatementContext):
        pass

    # Exit a parse tree produced by HiveParser#singleFromStatement.
    def exitSingleFromStatement(self, ctx:HiveParser.SingleFromStatementContext):
        pass


    # Enter a parse tree produced by HiveParser#regularBody.
    def enterRegularBody(self, ctx:HiveParser.RegularBodyContext):
        pass

    # Exit a parse tree produced by HiveParser#regularBody.
    def exitRegularBody(self, ctx:HiveParser.RegularBodyContext):
        pass


    # Enter a parse tree produced by HiveParser#atomSelectStatement.
    def enterAtomSelectStatement(self, ctx:HiveParser.AtomSelectStatementContext):
        pass

    # Exit a parse tree produced by HiveParser#atomSelectStatement.
    def exitAtomSelectStatement(self, ctx:HiveParser.AtomSelectStatementContext):
        pass


    # Enter a parse tree produced by HiveParser#selectStatement.
    def enterSelectStatement(self, ctx:HiveParser.SelectStatementContext):
        pass

    # Exit a parse tree produced by HiveParser#selectStatement.
    def exitSelectStatement(self, ctx:HiveParser.SelectStatementContext):
        pass


    # Enter a parse tree produced by HiveParser#setOpSelectStatement.
    def enterSetOpSelectStatement(self, ctx:HiveParser.SetOpSelectStatementContext):
        pass

    # Exit a parse tree produced by HiveParser#setOpSelectStatement.
    def exitSetOpSelectStatement(self, ctx:HiveParser.SetOpSelectStatementContext):
        pass


    # Enter a parse tree produced by HiveParser#selectStatementWithCTE.
    def enterSelectStatementWithCTE(self, ctx:HiveParser.SelectStatementWithCTEContext):
        pass

    # Exit a parse tree produced by HiveParser#selectStatementWithCTE.
    def exitSelectStatementWithCTE(self, ctx:HiveParser.SelectStatementWithCTEContext):
        pass


    # Enter a parse tree produced by HiveParser#body.
    def enterBody(self, ctx:HiveParser.BodyContext):
        pass

    # Exit a parse tree produced by HiveParser#body.
    def exitBody(self, ctx:HiveParser.BodyContext):
        pass


    # Enter a parse tree produced by HiveParser#insertClause.
    def enterInsertClause(self, ctx:HiveParser.InsertClauseContext):
        pass

    # Exit a parse tree produced by HiveParser#insertClause.
    def exitInsertClause(self, ctx:HiveParser.InsertClauseContext):
        pass


    # Enter a parse tree produced by HiveParser#destination.
    def enterDestination(self, ctx:HiveParser.DestinationContext):
        pass

    # Exit a parse tree produced by HiveParser#destination.
    def exitDestination(self, ctx:HiveParser.DestinationContext):
        pass


    # Enter a parse tree produced by HiveParser#limitClause.
    def enterLimitClause(self, ctx:HiveParser.LimitClauseContext):
        pass

    # Exit a parse tree produced by HiveParser#limitClause.
    def exitLimitClause(self, ctx:HiveParser.LimitClauseContext):
        pass


    # Enter a parse tree produced by HiveParser#deleteStatement.
    def enterDeleteStatement(self, ctx:HiveParser.DeleteStatementContext):
        pass

    # Exit a parse tree produced by HiveParser#deleteStatement.
    def exitDeleteStatement(self, ctx:HiveParser.DeleteStatementContext):
        pass


    # Enter a parse tree produced by HiveParser#columnAssignmentClause.
    def enterColumnAssignmentClause(self, ctx:HiveParser.ColumnAssignmentClauseContext):
        pass

    # Exit a parse tree produced by HiveParser#columnAssignmentClause.
    def exitColumnAssignmentClause(self, ctx:HiveParser.ColumnAssignmentClauseContext):
        pass


    # Enter a parse tree produced by HiveParser#setColumnsClause.
    def enterSetColumnsClause(self, ctx:HiveParser.SetColumnsClauseContext):
        pass

    # Exit a parse tree produced by HiveParser#setColumnsClause.
    def exitSetColumnsClause(self, ctx:HiveParser.SetColumnsClauseContext):
        pass


    # Enter a parse tree produced by HiveParser#updateStatement.
    def enterUpdateStatement(self, ctx:HiveParser.UpdateStatementContext):
        pass

    # Exit a parse tree produced by HiveParser#updateStatement.
    def exitUpdateStatement(self, ctx:HiveParser.UpdateStatementContext):
        pass


    # Enter a parse tree produced by HiveParser#sqlTransactionStatement.
    def enterSqlTransactionStatement(self, ctx:HiveParser.SqlTransactionStatementContext):
        pass

    # Exit a parse tree produced by HiveParser#sqlTransactionStatement.
    def exitSqlTransactionStatement(self, ctx:HiveParser.SqlTransactionStatementContext):
        pass


    # Enter a parse tree produced by HiveParser#startTransactionStatement.
    def enterStartTransactionStatement(self, ctx:HiveParser.StartTransactionStatementContext):
        pass

    # Exit a parse tree produced by HiveParser#startTransactionStatement.
    def exitStartTransactionStatement(self, ctx:HiveParser.StartTransactionStatementContext):
        pass


    # Enter a parse tree produced by HiveParser#transactionMode.
    def enterTransactionMode(self, ctx:HiveParser.TransactionModeContext):
        pass

    # Exit a parse tree produced by HiveParser#transactionMode.
    def exitTransactionMode(self, ctx:HiveParser.TransactionModeContext):
        pass


    # Enter a parse tree produced by HiveParser#transactionAccessMode.
    def enterTransactionAccessMode(self, ctx:HiveParser.TransactionAccessModeContext):
        pass

    # Exit a parse tree produced by HiveParser#transactionAccessMode.
    def exitTransactionAccessMode(self, ctx:HiveParser.TransactionAccessModeContext):
        pass


    # Enter a parse tree produced by HiveParser#isolationLevel.
    def enterIsolationLevel(self, ctx:HiveParser.IsolationLevelContext):
        pass

    # Exit a parse tree produced by HiveParser#isolationLevel.
    def exitIsolationLevel(self, ctx:HiveParser.IsolationLevelContext):
        pass


    # Enter a parse tree produced by HiveParser#levelOfIsolation.
    def enterLevelOfIsolation(self, ctx:HiveParser.LevelOfIsolationContext):
        pass

    # Exit a parse tree produced by HiveParser#levelOfIsolation.
    def exitLevelOfIsolation(self, ctx:HiveParser.LevelOfIsolationContext):
        pass


    # Enter a parse tree produced by HiveParser#commitStatement.
    def enterCommitStatement(self, ctx:HiveParser.CommitStatementContext):
        pass

    # Exit a parse tree produced by HiveParser#commitStatement.
    def exitCommitStatement(self, ctx:HiveParser.CommitStatementContext):
        pass


    # Enter a parse tree produced by HiveParser#rollbackStatement.
    def enterRollbackStatement(self, ctx:HiveParser.RollbackStatementContext):
        pass

    # Exit a parse tree produced by HiveParser#rollbackStatement.
    def exitRollbackStatement(self, ctx:HiveParser.RollbackStatementContext):
        pass


    # Enter a parse tree produced by HiveParser#setAutoCommitStatement.
    def enterSetAutoCommitStatement(self, ctx:HiveParser.SetAutoCommitStatementContext):
        pass

    # Exit a parse tree produced by HiveParser#setAutoCommitStatement.
    def exitSetAutoCommitStatement(self, ctx:HiveParser.SetAutoCommitStatementContext):
        pass


    # Enter a parse tree produced by HiveParser#abortTransactionStatement.
    def enterAbortTransactionStatement(self, ctx:HiveParser.AbortTransactionStatementContext):
        pass

    # Exit a parse tree produced by HiveParser#abortTransactionStatement.
    def exitAbortTransactionStatement(self, ctx:HiveParser.AbortTransactionStatementContext):
        pass


    # Enter a parse tree produced by HiveParser#mergeStatement.
    def enterMergeStatement(self, ctx:HiveParser.MergeStatementContext):
        pass

    # Exit a parse tree produced by HiveParser#mergeStatement.
    def exitMergeStatement(self, ctx:HiveParser.MergeStatementContext):
        pass


    # Enter a parse tree produced by HiveParser#whenClauses.
    def enterWhenClauses(self, ctx:HiveParser.WhenClausesContext):
        pass

    # Exit a parse tree produced by HiveParser#whenClauses.
    def exitWhenClauses(self, ctx:HiveParser.WhenClausesContext):
        pass


    # Enter a parse tree produced by HiveParser#whenNotMatchedClause.
    def enterWhenNotMatchedClause(self, ctx:HiveParser.WhenNotMatchedClauseContext):
        pass

    # Exit a parse tree produced by HiveParser#whenNotMatchedClause.
    def exitWhenNotMatchedClause(self, ctx:HiveParser.WhenNotMatchedClauseContext):
        pass


    # Enter a parse tree produced by HiveParser#whenMatchedAndClause.
    def enterWhenMatchedAndClause(self, ctx:HiveParser.WhenMatchedAndClauseContext):
        pass

    # Exit a parse tree produced by HiveParser#whenMatchedAndClause.
    def exitWhenMatchedAndClause(self, ctx:HiveParser.WhenMatchedAndClauseContext):
        pass


    # Enter a parse tree produced by HiveParser#whenMatchedThenClause.
    def enterWhenMatchedThenClause(self, ctx:HiveParser.WhenMatchedThenClauseContext):
        pass

    # Exit a parse tree produced by HiveParser#whenMatchedThenClause.
    def exitWhenMatchedThenClause(self, ctx:HiveParser.WhenMatchedThenClauseContext):
        pass


    # Enter a parse tree produced by HiveParser#updateOrDelete.
    def enterUpdateOrDelete(self, ctx:HiveParser.UpdateOrDeleteContext):
        pass

    # Exit a parse tree produced by HiveParser#updateOrDelete.
    def exitUpdateOrDelete(self, ctx:HiveParser.UpdateOrDeleteContext):
        pass


    # Enter a parse tree produced by HiveParser#killQueryStatement.
    def enterKillQueryStatement(self, ctx:HiveParser.KillQueryStatementContext):
        pass

    # Exit a parse tree produced by HiveParser#killQueryStatement.
    def exitKillQueryStatement(self, ctx:HiveParser.KillQueryStatementContext):
        pass


    # Enter a parse tree produced by HiveParser#selectClause.
    def enterSelectClause(self, ctx:HiveParser.SelectClauseContext):
        pass

    # Exit a parse tree produced by HiveParser#selectClause.
    def exitSelectClause(self, ctx:HiveParser.SelectClauseContext):
        pass


    # Enter a parse tree produced by HiveParser#selectList.
    def enterSelectList(self, ctx:HiveParser.SelectListContext):
        pass

    # Exit a parse tree produced by HiveParser#selectList.
    def exitSelectList(self, ctx:HiveParser.SelectListContext):
        pass


    # Enter a parse tree produced by HiveParser#selectTrfmClause.
    def enterSelectTrfmClause(self, ctx:HiveParser.SelectTrfmClauseContext):
        pass

    # Exit a parse tree produced by HiveParser#selectTrfmClause.
    def exitSelectTrfmClause(self, ctx:HiveParser.SelectTrfmClauseContext):
        pass


    # Enter a parse tree produced by HiveParser#selectItem.
    def enterSelectItem(self, ctx:HiveParser.SelectItemContext):
        pass

    # Exit a parse tree produced by HiveParser#selectItem.
    def exitSelectItem(self, ctx:HiveParser.SelectItemContext):
        pass


    # Enter a parse tree produced by HiveParser#trfmClause.
    def enterTrfmClause(self, ctx:HiveParser.TrfmClauseContext):
        pass

    # Exit a parse tree produced by HiveParser#trfmClause.
    def exitTrfmClause(self, ctx:HiveParser.TrfmClauseContext):
        pass


    # Enter a parse tree produced by HiveParser#selectExpression.
    def enterSelectExpression(self, ctx:HiveParser.SelectExpressionContext):
        pass

    # Exit a parse tree produced by HiveParser#selectExpression.
    def exitSelectExpression(self, ctx:HiveParser.SelectExpressionContext):
        pass


    # Enter a parse tree produced by HiveParser#selectExpressionList.
    def enterSelectExpressionList(self, ctx:HiveParser.SelectExpressionListContext):
        pass

    # Exit a parse tree produced by HiveParser#selectExpressionList.
    def exitSelectExpressionList(self, ctx:HiveParser.SelectExpressionListContext):
        pass


    # Enter a parse tree produced by HiveParser#window_clause.
    def enterWindow_clause(self, ctx:HiveParser.Window_clauseContext):
        pass

    # Exit a parse tree produced by HiveParser#window_clause.
    def exitWindow_clause(self, ctx:HiveParser.Window_clauseContext):
        pass


    # Enter a parse tree produced by HiveParser#window_defn.
    def enterWindow_defn(self, ctx:HiveParser.Window_defnContext):
        pass

    # Exit a parse tree produced by HiveParser#window_defn.
    def exitWindow_defn(self, ctx:HiveParser.Window_defnContext):
        pass


    # Enter a parse tree produced by HiveParser#window_specification.
    def enterWindow_specification(self, ctx:HiveParser.Window_specificationContext):
        pass

    # Exit a parse tree produced by HiveParser#window_specification.
    def exitWindow_specification(self, ctx:HiveParser.Window_specificationContext):
        pass


    # Enter a parse tree produced by HiveParser#window_frame.
    def enterWindow_frame(self, ctx:HiveParser.Window_frameContext):
        pass

    # Exit a parse tree produced by HiveParser#window_frame.
    def exitWindow_frame(self, ctx:HiveParser.Window_frameContext):
        pass


    # Enter a parse tree produced by HiveParser#window_range_expression.
    def enterWindow_range_expression(self, ctx:HiveParser.Window_range_expressionContext):
        pass

    # Exit a parse tree produced by HiveParser#window_range_expression.
    def exitWindow_range_expression(self, ctx:HiveParser.Window_range_expressionContext):
        pass


    # Enter a parse tree produced by HiveParser#window_value_expression.
    def enterWindow_value_expression(self, ctx:HiveParser.Window_value_expressionContext):
        pass

    # Exit a parse tree produced by HiveParser#window_value_expression.
    def exitWindow_value_expression(self, ctx:HiveParser.Window_value_expressionContext):
        pass


    # Enter a parse tree produced by HiveParser#window_frame_start_boundary.
    def enterWindow_frame_start_boundary(self, ctx:HiveParser.Window_frame_start_boundaryContext):
        pass

    # Exit a parse tree produced by HiveParser#window_frame_start_boundary.
    def exitWindow_frame_start_boundary(self, ctx:HiveParser.Window_frame_start_boundaryContext):
        pass


    # Enter a parse tree produced by HiveParser#window_frame_boundary.
    def enterWindow_frame_boundary(self, ctx:HiveParser.Window_frame_boundaryContext):
        pass

    # Exit a parse tree produced by HiveParser#window_frame_boundary.
    def exitWindow_frame_boundary(self, ctx:HiveParser.Window_frame_boundaryContext):
        pass


    # Enter a parse tree produced by HiveParser#tableAllColumns.
    def enterTableAllColumns(self, ctx:HiveParser.TableAllColumnsContext):
        pass

    # Exit a parse tree produced by HiveParser#tableAllColumns.
    def exitTableAllColumns(self, ctx:HiveParser.TableAllColumnsContext):
        pass


    # Enter a parse tree produced by HiveParser#tableOrColumn.
    def enterTableOrColumn(self, ctx:HiveParser.TableOrColumnContext):
        pass

    # Exit a parse tree produced by HiveParser#tableOrColumn.
    def exitTableOrColumn(self, ctx:HiveParser.TableOrColumnContext):
        pass


    # Enter a parse tree produced by HiveParser#expressionList.
    def enterExpressionList(self, ctx:HiveParser.ExpressionListContext):
        pass

    # Exit a parse tree produced by HiveParser#expressionList.
    def exitExpressionList(self, ctx:HiveParser.ExpressionListContext):
        pass


    # Enter a parse tree produced by HiveParser#aliasList.
    def enterAliasList(self, ctx:HiveParser.AliasListContext):
        pass

    # Exit a parse tree produced by HiveParser#aliasList.
    def exitAliasList(self, ctx:HiveParser.AliasListContext):
        pass


    # Enter a parse tree produced by HiveParser#fromClause.
    def enterFromClause(self, ctx:HiveParser.FromClauseContext):
        pass

    # Exit a parse tree produced by HiveParser#fromClause.
    def exitFromClause(self, ctx:HiveParser.FromClauseContext):
        pass


    # Enter a parse tree produced by HiveParser#fromSource.
    def enterFromSource(self, ctx:HiveParser.FromSourceContext):
        pass

    # Exit a parse tree produced by HiveParser#fromSource.
    def exitFromSource(self, ctx:HiveParser.FromSourceContext):
        pass


    # Enter a parse tree produced by HiveParser#atomjoinSource.
    def enterAtomjoinSource(self, ctx:HiveParser.AtomjoinSourceContext):
        pass

    # Exit a parse tree produced by HiveParser#atomjoinSource.
    def exitAtomjoinSource(self, ctx:HiveParser.AtomjoinSourceContext):
        pass


    # Enter a parse tree produced by HiveParser#joinSource.
    def enterJoinSource(self, ctx:HiveParser.JoinSourceContext):
        pass

    # Exit a parse tree produced by HiveParser#joinSource.
    def exitJoinSource(self, ctx:HiveParser.JoinSourceContext):
        pass


    # Enter a parse tree produced by HiveParser#joinSourcePart.
    def enterJoinSourcePart(self, ctx:HiveParser.JoinSourcePartContext):
        pass

    # Exit a parse tree produced by HiveParser#joinSourcePart.
    def exitJoinSourcePart(self, ctx:HiveParser.JoinSourcePartContext):
        pass


    # Enter a parse tree produced by HiveParser#uniqueJoinSource.
    def enterUniqueJoinSource(self, ctx:HiveParser.UniqueJoinSourceContext):
        pass

    # Exit a parse tree produced by HiveParser#uniqueJoinSource.
    def exitUniqueJoinSource(self, ctx:HiveParser.UniqueJoinSourceContext):
        pass


    # Enter a parse tree produced by HiveParser#uniqueJoinExpr.
    def enterUniqueJoinExpr(self, ctx:HiveParser.UniqueJoinExprContext):
        pass

    # Exit a parse tree produced by HiveParser#uniqueJoinExpr.
    def exitUniqueJoinExpr(self, ctx:HiveParser.UniqueJoinExprContext):
        pass


    # Enter a parse tree produced by HiveParser#uniqueJoinToken.
    def enterUniqueJoinToken(self, ctx:HiveParser.UniqueJoinTokenContext):
        pass

    # Exit a parse tree produced by HiveParser#uniqueJoinToken.
    def exitUniqueJoinToken(self, ctx:HiveParser.UniqueJoinTokenContext):
        pass


    # Enter a parse tree produced by HiveParser#joinToken.
    def enterJoinToken(self, ctx:HiveParser.JoinTokenContext):
        pass

    # Exit a parse tree produced by HiveParser#joinToken.
    def exitJoinToken(self, ctx:HiveParser.JoinTokenContext):
        pass


    # Enter a parse tree produced by HiveParser#lateralView.
    def enterLateralView(self, ctx:HiveParser.LateralViewContext):
        pass

    # Exit a parse tree produced by HiveParser#lateralView.
    def exitLateralView(self, ctx:HiveParser.LateralViewContext):
        pass


    # Enter a parse tree produced by HiveParser#tableAlias.
    def enterTableAlias(self, ctx:HiveParser.TableAliasContext):
        pass

    # Exit a parse tree produced by HiveParser#tableAlias.
    def exitTableAlias(self, ctx:HiveParser.TableAliasContext):
        pass


    # Enter a parse tree produced by HiveParser#tableBucketSample.
    def enterTableBucketSample(self, ctx:HiveParser.TableBucketSampleContext):
        pass

    # Exit a parse tree produced by HiveParser#tableBucketSample.
    def exitTableBucketSample(self, ctx:HiveParser.TableBucketSampleContext):
        pass


    # Enter a parse tree produced by HiveParser#splitSample.
    def enterSplitSample(self, ctx:HiveParser.SplitSampleContext):
        pass

    # Exit a parse tree produced by HiveParser#splitSample.
    def exitSplitSample(self, ctx:HiveParser.SplitSampleContext):
        pass


    # Enter a parse tree produced by HiveParser#tableSample.
    def enterTableSample(self, ctx:HiveParser.TableSampleContext):
        pass

    # Exit a parse tree produced by HiveParser#tableSample.
    def exitTableSample(self, ctx:HiveParser.TableSampleContext):
        pass


    # Enter a parse tree produced by HiveParser#tableSource.
    def enterTableSource(self, ctx:HiveParser.TableSourceContext):
        pass

    # Exit a parse tree produced by HiveParser#tableSource.
    def exitTableSource(self, ctx:HiveParser.TableSourceContext):
        pass


    # Enter a parse tree produced by HiveParser#uniqueJoinTableSource.
    def enterUniqueJoinTableSource(self, ctx:HiveParser.UniqueJoinTableSourceContext):
        pass

    # Exit a parse tree produced by HiveParser#uniqueJoinTableSource.
    def exitUniqueJoinTableSource(self, ctx:HiveParser.UniqueJoinTableSourceContext):
        pass


    # Enter a parse tree produced by HiveParser#tableName.
    def enterTableName(self, ctx:HiveParser.TableNameContext):
        pass

    # Exit a parse tree produced by HiveParser#tableName.
    def exitTableName(self, ctx:HiveParser.TableNameContext):
        pass


    # Enter a parse tree produced by HiveParser#viewName.
    def enterViewName(self, ctx:HiveParser.ViewNameContext):
        pass

    # Exit a parse tree produced by HiveParser#viewName.
    def exitViewName(self, ctx:HiveParser.ViewNameContext):
        pass


    # Enter a parse tree produced by HiveParser#subQuerySource.
    def enterSubQuerySource(self, ctx:HiveParser.SubQuerySourceContext):
        pass

    # Exit a parse tree produced by HiveParser#subQuerySource.
    def exitSubQuerySource(self, ctx:HiveParser.SubQuerySourceContext):
        pass


    # Enter a parse tree produced by HiveParser#partitioningSpec.
    def enterPartitioningSpec(self, ctx:HiveParser.PartitioningSpecContext):
        pass

    # Exit a parse tree produced by HiveParser#partitioningSpec.
    def exitPartitioningSpec(self, ctx:HiveParser.PartitioningSpecContext):
        pass


    # Enter a parse tree produced by HiveParser#partitionTableFunctionSource.
    def enterPartitionTableFunctionSource(self, ctx:HiveParser.PartitionTableFunctionSourceContext):
        pass

    # Exit a parse tree produced by HiveParser#partitionTableFunctionSource.
    def exitPartitionTableFunctionSource(self, ctx:HiveParser.PartitionTableFunctionSourceContext):
        pass


    # Enter a parse tree produced by HiveParser#partitionedTableFunction.
    def enterPartitionedTableFunction(self, ctx:HiveParser.PartitionedTableFunctionContext):
        pass

    # Exit a parse tree produced by HiveParser#partitionedTableFunction.
    def exitPartitionedTableFunction(self, ctx:HiveParser.PartitionedTableFunctionContext):
        pass


    # Enter a parse tree produced by HiveParser#whereClause.
    def enterWhereClause(self, ctx:HiveParser.WhereClauseContext):
        pass

    # Exit a parse tree produced by HiveParser#whereClause.
    def exitWhereClause(self, ctx:HiveParser.WhereClauseContext):
        pass


    # Enter a parse tree produced by HiveParser#searchCondition.
    def enterSearchCondition(self, ctx:HiveParser.SearchConditionContext):
        pass

    # Exit a parse tree produced by HiveParser#searchCondition.
    def exitSearchCondition(self, ctx:HiveParser.SearchConditionContext):
        pass


    # Enter a parse tree produced by HiveParser#valuesClause.
    def enterValuesClause(self, ctx:HiveParser.ValuesClauseContext):
        pass

    # Exit a parse tree produced by HiveParser#valuesClause.
    def exitValuesClause(self, ctx:HiveParser.ValuesClauseContext):
        pass


    # Enter a parse tree produced by HiveParser#valuesTableConstructor.
    def enterValuesTableConstructor(self, ctx:HiveParser.ValuesTableConstructorContext):
        pass

    # Exit a parse tree produced by HiveParser#valuesTableConstructor.
    def exitValuesTableConstructor(self, ctx:HiveParser.ValuesTableConstructorContext):
        pass


    # Enter a parse tree produced by HiveParser#valueRowConstructor.
    def enterValueRowConstructor(self, ctx:HiveParser.ValueRowConstructorContext):
        pass

    # Exit a parse tree produced by HiveParser#valueRowConstructor.
    def exitValueRowConstructor(self, ctx:HiveParser.ValueRowConstructorContext):
        pass


    # Enter a parse tree produced by HiveParser#virtualTableSource.
    def enterVirtualTableSource(self, ctx:HiveParser.VirtualTableSourceContext):
        pass

    # Exit a parse tree produced by HiveParser#virtualTableSource.
    def exitVirtualTableSource(self, ctx:HiveParser.VirtualTableSourceContext):
        pass


    # Enter a parse tree produced by HiveParser#groupByClause.
    def enterGroupByClause(self, ctx:HiveParser.GroupByClauseContext):
        pass

    # Exit a parse tree produced by HiveParser#groupByClause.
    def exitGroupByClause(self, ctx:HiveParser.GroupByClauseContext):
        pass


    # Enter a parse tree produced by HiveParser#groupby_expression.
    def enterGroupby_expression(self, ctx:HiveParser.Groupby_expressionContext):
        pass

    # Exit a parse tree produced by HiveParser#groupby_expression.
    def exitGroupby_expression(self, ctx:HiveParser.Groupby_expressionContext):
        pass


    # Enter a parse tree produced by HiveParser#groupByEmpty.
    def enterGroupByEmpty(self, ctx:HiveParser.GroupByEmptyContext):
        pass

    # Exit a parse tree produced by HiveParser#groupByEmpty.
    def exitGroupByEmpty(self, ctx:HiveParser.GroupByEmptyContext):
        pass


    # Enter a parse tree produced by HiveParser#rollupStandard.
    def enterRollupStandard(self, ctx:HiveParser.RollupStandardContext):
        pass

    # Exit a parse tree produced by HiveParser#rollupStandard.
    def exitRollupStandard(self, ctx:HiveParser.RollupStandardContext):
        pass


    # Enter a parse tree produced by HiveParser#rollupOldSyntax.
    def enterRollupOldSyntax(self, ctx:HiveParser.RollupOldSyntaxContext):
        pass

    # Exit a parse tree produced by HiveParser#rollupOldSyntax.
    def exitRollupOldSyntax(self, ctx:HiveParser.RollupOldSyntaxContext):
        pass


    # Enter a parse tree produced by HiveParser#groupingSetExpression.
    def enterGroupingSetExpression(self, ctx:HiveParser.GroupingSetExpressionContext):
        pass

    # Exit a parse tree produced by HiveParser#groupingSetExpression.
    def exitGroupingSetExpression(self, ctx:HiveParser.GroupingSetExpressionContext):
        pass


    # Enter a parse tree produced by HiveParser#groupingSetExpressionMultiple.
    def enterGroupingSetExpressionMultiple(self, ctx:HiveParser.GroupingSetExpressionMultipleContext):
        pass

    # Exit a parse tree produced by HiveParser#groupingSetExpressionMultiple.
    def exitGroupingSetExpressionMultiple(self, ctx:HiveParser.GroupingSetExpressionMultipleContext):
        pass


    # Enter a parse tree produced by HiveParser#groupingExpressionSingle.
    def enterGroupingExpressionSingle(self, ctx:HiveParser.GroupingExpressionSingleContext):
        pass

    # Exit a parse tree produced by HiveParser#groupingExpressionSingle.
    def exitGroupingExpressionSingle(self, ctx:HiveParser.GroupingExpressionSingleContext):
        pass


    # Enter a parse tree produced by HiveParser#havingClause.
    def enterHavingClause(self, ctx:HiveParser.HavingClauseContext):
        pass

    # Exit a parse tree produced by HiveParser#havingClause.
    def exitHavingClause(self, ctx:HiveParser.HavingClauseContext):
        pass


    # Enter a parse tree produced by HiveParser#havingCondition.
    def enterHavingCondition(self, ctx:HiveParser.HavingConditionContext):
        pass

    # Exit a parse tree produced by HiveParser#havingCondition.
    def exitHavingCondition(self, ctx:HiveParser.HavingConditionContext):
        pass


    # Enter a parse tree produced by HiveParser#expressionsInParenthesis.
    def enterExpressionsInParenthesis(self, ctx:HiveParser.ExpressionsInParenthesisContext):
        pass

    # Exit a parse tree produced by HiveParser#expressionsInParenthesis.
    def exitExpressionsInParenthesis(self, ctx:HiveParser.ExpressionsInParenthesisContext):
        pass


    # Enter a parse tree produced by HiveParser#expressionsNotInParenthesis.
    def enterExpressionsNotInParenthesis(self, ctx:HiveParser.ExpressionsNotInParenthesisContext):
        pass

    # Exit a parse tree produced by HiveParser#expressionsNotInParenthesis.
    def exitExpressionsNotInParenthesis(self, ctx:HiveParser.ExpressionsNotInParenthesisContext):
        pass


    # Enter a parse tree produced by HiveParser#expressionPart.
    def enterExpressionPart(self, ctx:HiveParser.ExpressionPartContext):
        pass

    # Exit a parse tree produced by HiveParser#expressionPart.
    def exitExpressionPart(self, ctx:HiveParser.ExpressionPartContext):
        pass


    # Enter a parse tree produced by HiveParser#expressions.
    def enterExpressions(self, ctx:HiveParser.ExpressionsContext):
        pass

    # Exit a parse tree produced by HiveParser#expressions.
    def exitExpressions(self, ctx:HiveParser.ExpressionsContext):
        pass


    # Enter a parse tree produced by HiveParser#columnRefOrderInParenthesis.
    def enterColumnRefOrderInParenthesis(self, ctx:HiveParser.ColumnRefOrderInParenthesisContext):
        pass

    # Exit a parse tree produced by HiveParser#columnRefOrderInParenthesis.
    def exitColumnRefOrderInParenthesis(self, ctx:HiveParser.ColumnRefOrderInParenthesisContext):
        pass


    # Enter a parse tree produced by HiveParser#columnRefOrderNotInParenthesis.
    def enterColumnRefOrderNotInParenthesis(self, ctx:HiveParser.ColumnRefOrderNotInParenthesisContext):
        pass

    # Exit a parse tree produced by HiveParser#columnRefOrderNotInParenthesis.
    def exitColumnRefOrderNotInParenthesis(self, ctx:HiveParser.ColumnRefOrderNotInParenthesisContext):
        pass


    # Enter a parse tree produced by HiveParser#orderByClause.
    def enterOrderByClause(self, ctx:HiveParser.OrderByClauseContext):
        pass

    # Exit a parse tree produced by HiveParser#orderByClause.
    def exitOrderByClause(self, ctx:HiveParser.OrderByClauseContext):
        pass


    # Enter a parse tree produced by HiveParser#clusterByClause.
    def enterClusterByClause(self, ctx:HiveParser.ClusterByClauseContext):
        pass

    # Exit a parse tree produced by HiveParser#clusterByClause.
    def exitClusterByClause(self, ctx:HiveParser.ClusterByClauseContext):
        pass


    # Enter a parse tree produced by HiveParser#partitionByClause.
    def enterPartitionByClause(self, ctx:HiveParser.PartitionByClauseContext):
        pass

    # Exit a parse tree produced by HiveParser#partitionByClause.
    def exitPartitionByClause(self, ctx:HiveParser.PartitionByClauseContext):
        pass


    # Enter a parse tree produced by HiveParser#distributeByClause.
    def enterDistributeByClause(self, ctx:HiveParser.DistributeByClauseContext):
        pass

    # Exit a parse tree produced by HiveParser#distributeByClause.
    def exitDistributeByClause(self, ctx:HiveParser.DistributeByClauseContext):
        pass


    # Enter a parse tree produced by HiveParser#sortByClause.
    def enterSortByClause(self, ctx:HiveParser.SortByClauseContext):
        pass

    # Exit a parse tree produced by HiveParser#sortByClause.
    def exitSortByClause(self, ctx:HiveParser.SortByClauseContext):
        pass


    # Enter a parse tree produced by HiveParser#function_.
    def enterFunction_(self, ctx:HiveParser.Function_Context):
        pass

    # Exit a parse tree produced by HiveParser#function_.
    def exitFunction_(self, ctx:HiveParser.Function_Context):
        pass


    # Enter a parse tree produced by HiveParser#functionName.
    def enterFunctionName(self, ctx:HiveParser.FunctionNameContext):
        pass

    # Exit a parse tree produced by HiveParser#functionName.
    def exitFunctionName(self, ctx:HiveParser.FunctionNameContext):
        pass


    # Enter a parse tree produced by HiveParser#castExpression.
    def enterCastExpression(self, ctx:HiveParser.CastExpressionContext):
        pass

    # Exit a parse tree produced by HiveParser#castExpression.
    def exitCastExpression(self, ctx:HiveParser.CastExpressionContext):
        pass


    # Enter a parse tree produced by HiveParser#caseExpression.
    def enterCaseExpression(self, ctx:HiveParser.CaseExpressionContext):
        pass

    # Exit a parse tree produced by HiveParser#caseExpression.
    def exitCaseExpression(self, ctx:HiveParser.CaseExpressionContext):
        pass


    # Enter a parse tree produced by HiveParser#whenExpression.
    def enterWhenExpression(self, ctx:HiveParser.WhenExpressionContext):
        pass

    # Exit a parse tree produced by HiveParser#whenExpression.
    def exitWhenExpression(self, ctx:HiveParser.WhenExpressionContext):
        pass


    # Enter a parse tree produced by HiveParser#floorExpression.
    def enterFloorExpression(self, ctx:HiveParser.FloorExpressionContext):
        pass

    # Exit a parse tree produced by HiveParser#floorExpression.
    def exitFloorExpression(self, ctx:HiveParser.FloorExpressionContext):
        pass


    # Enter a parse tree produced by HiveParser#floorDateQualifiers.
    def enterFloorDateQualifiers(self, ctx:HiveParser.FloorDateQualifiersContext):
        pass

    # Exit a parse tree produced by HiveParser#floorDateQualifiers.
    def exitFloorDateQualifiers(self, ctx:HiveParser.FloorDateQualifiersContext):
        pass


    # Enter a parse tree produced by HiveParser#extractExpression.
    def enterExtractExpression(self, ctx:HiveParser.ExtractExpressionContext):
        pass

    # Exit a parse tree produced by HiveParser#extractExpression.
    def exitExtractExpression(self, ctx:HiveParser.ExtractExpressionContext):
        pass


    # Enter a parse tree produced by HiveParser#timeQualifiers.
    def enterTimeQualifiers(self, ctx:HiveParser.TimeQualifiersContext):
        pass

    # Exit a parse tree produced by HiveParser#timeQualifiers.
    def exitTimeQualifiers(self, ctx:HiveParser.TimeQualifiersContext):
        pass


    # Enter a parse tree produced by HiveParser#constant.
    def enterConstant(self, ctx:HiveParser.ConstantContext):
        pass

    # Exit a parse tree produced by HiveParser#constant.
    def exitConstant(self, ctx:HiveParser.ConstantContext):
        pass


    # Enter a parse tree produced by HiveParser#stringLiteralSequence.
    def enterStringLiteralSequence(self, ctx:HiveParser.StringLiteralSequenceContext):
        pass

    # Exit a parse tree produced by HiveParser#stringLiteralSequence.
    def exitStringLiteralSequence(self, ctx:HiveParser.StringLiteralSequenceContext):
        pass


    # Enter a parse tree produced by HiveParser#charSetStringLiteral.
    def enterCharSetStringLiteral(self, ctx:HiveParser.CharSetStringLiteralContext):
        pass

    # Exit a parse tree produced by HiveParser#charSetStringLiteral.
    def exitCharSetStringLiteral(self, ctx:HiveParser.CharSetStringLiteralContext):
        pass


    # Enter a parse tree produced by HiveParser#dateLiteral.
    def enterDateLiteral(self, ctx:HiveParser.DateLiteralContext):
        pass

    # Exit a parse tree produced by HiveParser#dateLiteral.
    def exitDateLiteral(self, ctx:HiveParser.DateLiteralContext):
        pass


    # Enter a parse tree produced by HiveParser#timestampLiteral.
    def enterTimestampLiteral(self, ctx:HiveParser.TimestampLiteralContext):
        pass

    # Exit a parse tree produced by HiveParser#timestampLiteral.
    def exitTimestampLiteral(self, ctx:HiveParser.TimestampLiteralContext):
        pass


    # Enter a parse tree produced by HiveParser#timestampLocalTZLiteral.
    def enterTimestampLocalTZLiteral(self, ctx:HiveParser.TimestampLocalTZLiteralContext):
        pass

    # Exit a parse tree produced by HiveParser#timestampLocalTZLiteral.
    def exitTimestampLocalTZLiteral(self, ctx:HiveParser.TimestampLocalTZLiteralContext):
        pass


    # Enter a parse tree produced by HiveParser#intervalValue.
    def enterIntervalValue(self, ctx:HiveParser.IntervalValueContext):
        pass

    # Exit a parse tree produced by HiveParser#intervalValue.
    def exitIntervalValue(self, ctx:HiveParser.IntervalValueContext):
        pass


    # Enter a parse tree produced by HiveParser#intervalLiteral.
    def enterIntervalLiteral(self, ctx:HiveParser.IntervalLiteralContext):
        pass

    # Exit a parse tree produced by HiveParser#intervalLiteral.
    def exitIntervalLiteral(self, ctx:HiveParser.IntervalLiteralContext):
        pass


    # Enter a parse tree produced by HiveParser#intervalExpression.
    def enterIntervalExpression(self, ctx:HiveParser.IntervalExpressionContext):
        pass

    # Exit a parse tree produced by HiveParser#intervalExpression.
    def exitIntervalExpression(self, ctx:HiveParser.IntervalExpressionContext):
        pass


    # Enter a parse tree produced by HiveParser#intervalQualifiers.
    def enterIntervalQualifiers(self, ctx:HiveParser.IntervalQualifiersContext):
        pass

    # Exit a parse tree produced by HiveParser#intervalQualifiers.
    def exitIntervalQualifiers(self, ctx:HiveParser.IntervalQualifiersContext):
        pass


    # Enter a parse tree produced by HiveParser#atomExpression.
    def enterAtomExpression(self, ctx:HiveParser.AtomExpressionContext):
        pass

    # Exit a parse tree produced by HiveParser#atomExpression.
    def exitAtomExpression(self, ctx:HiveParser.AtomExpressionContext):
        pass


    # Enter a parse tree produced by HiveParser#precedenceUnaryOperator.
    def enterPrecedenceUnaryOperator(self, ctx:HiveParser.PrecedenceUnaryOperatorContext):
        pass

    # Exit a parse tree produced by HiveParser#precedenceUnaryOperator.
    def exitPrecedenceUnaryOperator(self, ctx:HiveParser.PrecedenceUnaryOperatorContext):
        pass


    # Enter a parse tree produced by HiveParser#isCondition.
    def enterIsCondition(self, ctx:HiveParser.IsConditionContext):
        pass

    # Exit a parse tree produced by HiveParser#isCondition.
    def exitIsCondition(self, ctx:HiveParser.IsConditionContext):
        pass


    # Enter a parse tree produced by HiveParser#precedenceBitwiseXorOperator.
    def enterPrecedenceBitwiseXorOperator(self, ctx:HiveParser.PrecedenceBitwiseXorOperatorContext):
        pass

    # Exit a parse tree produced by HiveParser#precedenceBitwiseXorOperator.
    def exitPrecedenceBitwiseXorOperator(self, ctx:HiveParser.PrecedenceBitwiseXorOperatorContext):
        pass


    # Enter a parse tree produced by HiveParser#precedenceStarOperator.
    def enterPrecedenceStarOperator(self, ctx:HiveParser.PrecedenceStarOperatorContext):
        pass

    # Exit a parse tree produced by HiveParser#precedenceStarOperator.
    def exitPrecedenceStarOperator(self, ctx:HiveParser.PrecedenceStarOperatorContext):
        pass


    # Enter a parse tree produced by HiveParser#precedencePlusOperator.
    def enterPrecedencePlusOperator(self, ctx:HiveParser.PrecedencePlusOperatorContext):
        pass

    # Exit a parse tree produced by HiveParser#precedencePlusOperator.
    def exitPrecedencePlusOperator(self, ctx:HiveParser.PrecedencePlusOperatorContext):
        pass


    # Enter a parse tree produced by HiveParser#precedenceConcatenateOperator.
    def enterPrecedenceConcatenateOperator(self, ctx:HiveParser.PrecedenceConcatenateOperatorContext):
        pass

    # Exit a parse tree produced by HiveParser#precedenceConcatenateOperator.
    def exitPrecedenceConcatenateOperator(self, ctx:HiveParser.PrecedenceConcatenateOperatorContext):
        pass


    # Enter a parse tree produced by HiveParser#precedenceAmpersandOperator.
    def enterPrecedenceAmpersandOperator(self, ctx:HiveParser.PrecedenceAmpersandOperatorContext):
        pass

    # Exit a parse tree produced by HiveParser#precedenceAmpersandOperator.
    def exitPrecedenceAmpersandOperator(self, ctx:HiveParser.PrecedenceAmpersandOperatorContext):
        pass


    # Enter a parse tree produced by HiveParser#precedenceBitwiseOrOperator.
    def enterPrecedenceBitwiseOrOperator(self, ctx:HiveParser.PrecedenceBitwiseOrOperatorContext):
        pass

    # Exit a parse tree produced by HiveParser#precedenceBitwiseOrOperator.
    def exitPrecedenceBitwiseOrOperator(self, ctx:HiveParser.PrecedenceBitwiseOrOperatorContext):
        pass


    # Enter a parse tree produced by HiveParser#precedenceRegexpOperator.
    def enterPrecedenceRegexpOperator(self, ctx:HiveParser.PrecedenceRegexpOperatorContext):
        pass

    # Exit a parse tree produced by HiveParser#precedenceRegexpOperator.
    def exitPrecedenceRegexpOperator(self, ctx:HiveParser.PrecedenceRegexpOperatorContext):
        pass


    # Enter a parse tree produced by HiveParser#precedenceComparisonOperator.
    def enterPrecedenceComparisonOperator(self, ctx:HiveParser.PrecedenceComparisonOperatorContext):
        pass

    # Exit a parse tree produced by HiveParser#precedenceComparisonOperator.
    def exitPrecedenceComparisonOperator(self, ctx:HiveParser.PrecedenceComparisonOperatorContext):
        pass


    # Enter a parse tree produced by HiveParser#precedenceNotOperator.
    def enterPrecedenceNotOperator(self, ctx:HiveParser.PrecedenceNotOperatorContext):
        pass

    # Exit a parse tree produced by HiveParser#precedenceNotOperator.
    def exitPrecedenceNotOperator(self, ctx:HiveParser.PrecedenceNotOperatorContext):
        pass


    # Enter a parse tree produced by HiveParser#precedenceLogicOperator.
    def enterPrecedenceLogicOperator(self, ctx:HiveParser.PrecedenceLogicOperatorContext):
        pass

    # Exit a parse tree produced by HiveParser#precedenceLogicOperator.
    def exitPrecedenceLogicOperator(self, ctx:HiveParser.PrecedenceLogicOperatorContext):
        pass


    # Enter a parse tree produced by HiveParser#expression.
    def enterExpression(self, ctx:HiveParser.ExpressionContext):
        pass

    # Exit a parse tree produced by HiveParser#expression.
    def exitExpression(self, ctx:HiveParser.ExpressionContext):
        pass


    # Enter a parse tree produced by HiveParser#precedenceExpression.
    def enterPrecedenceExpression(self, ctx:HiveParser.PrecedenceExpressionContext):
        pass

    # Exit a parse tree produced by HiveParser#precedenceExpression.
    def exitPrecedenceExpression(self, ctx:HiveParser.PrecedenceExpressionContext):
        pass


    # Enter a parse tree produced by HiveParser#precedenceSimilarExpressionIn.
    def enterPrecedenceSimilarExpressionIn(self, ctx:HiveParser.PrecedenceSimilarExpressionInContext):
        pass

    # Exit a parse tree produced by HiveParser#precedenceSimilarExpressionIn.
    def exitPrecedenceSimilarExpressionIn(self, ctx:HiveParser.PrecedenceSimilarExpressionInContext):
        pass


    # Enter a parse tree produced by HiveParser#subQueryExpression.
    def enterSubQueryExpression(self, ctx:HiveParser.SubQueryExpressionContext):
        pass

    # Exit a parse tree produced by HiveParser#subQueryExpression.
    def exitSubQueryExpression(self, ctx:HiveParser.SubQueryExpressionContext):
        pass


    # Enter a parse tree produced by HiveParser#booleanValue.
    def enterBooleanValue(self, ctx:HiveParser.BooleanValueContext):
        pass

    # Exit a parse tree produced by HiveParser#booleanValue.
    def exitBooleanValue(self, ctx:HiveParser.BooleanValueContext):
        pass


    # Enter a parse tree produced by HiveParser#booleanValueTok.
    def enterBooleanValueTok(self, ctx:HiveParser.BooleanValueTokContext):
        pass

    # Exit a parse tree produced by HiveParser#booleanValueTok.
    def exitBooleanValueTok(self, ctx:HiveParser.BooleanValueTokContext):
        pass


    # Enter a parse tree produced by HiveParser#tableOrPartition.
    def enterTableOrPartition(self, ctx:HiveParser.TableOrPartitionContext):
        pass

    # Exit a parse tree produced by HiveParser#tableOrPartition.
    def exitTableOrPartition(self, ctx:HiveParser.TableOrPartitionContext):
        pass


    # Enter a parse tree produced by HiveParser#partitionSpec.
    def enterPartitionSpec(self, ctx:HiveParser.PartitionSpecContext):
        pass

    # Exit a parse tree produced by HiveParser#partitionSpec.
    def exitPartitionSpec(self, ctx:HiveParser.PartitionSpecContext):
        pass


    # Enter a parse tree produced by HiveParser#partitionVal.
    def enterPartitionVal(self, ctx:HiveParser.PartitionValContext):
        pass

    # Exit a parse tree produced by HiveParser#partitionVal.
    def exitPartitionVal(self, ctx:HiveParser.PartitionValContext):
        pass


    # Enter a parse tree produced by HiveParser#dropPartitionSpec.
    def enterDropPartitionSpec(self, ctx:HiveParser.DropPartitionSpecContext):
        pass

    # Exit a parse tree produced by HiveParser#dropPartitionSpec.
    def exitDropPartitionSpec(self, ctx:HiveParser.DropPartitionSpecContext):
        pass


    # Enter a parse tree produced by HiveParser#dropPartitionVal.
    def enterDropPartitionVal(self, ctx:HiveParser.DropPartitionValContext):
        pass

    # Exit a parse tree produced by HiveParser#dropPartitionVal.
    def exitDropPartitionVal(self, ctx:HiveParser.DropPartitionValContext):
        pass


    # Enter a parse tree produced by HiveParser#dropPartitionOperator.
    def enterDropPartitionOperator(self, ctx:HiveParser.DropPartitionOperatorContext):
        pass

    # Exit a parse tree produced by HiveParser#dropPartitionOperator.
    def exitDropPartitionOperator(self, ctx:HiveParser.DropPartitionOperatorContext):
        pass


    # Enter a parse tree produced by HiveParser#sysFuncNames.
    def enterSysFuncNames(self, ctx:HiveParser.SysFuncNamesContext):
        pass

    # Exit a parse tree produced by HiveParser#sysFuncNames.
    def exitSysFuncNames(self, ctx:HiveParser.SysFuncNamesContext):
        pass


    # Enter a parse tree produced by HiveParser#descFuncNames.
    def enterDescFuncNames(self, ctx:HiveParser.DescFuncNamesContext):
        pass

    # Exit a parse tree produced by HiveParser#descFuncNames.
    def exitDescFuncNames(self, ctx:HiveParser.DescFuncNamesContext):
        pass


    # Enter a parse tree produced by HiveParser#identifier.
    def enterIdentifier(self, ctx:HiveParser.IdentifierContext):
        pass

    # Exit a parse tree produced by HiveParser#identifier.
    def exitIdentifier(self, ctx:HiveParser.IdentifierContext):
        pass


    # Enter a parse tree produced by HiveParser#functionIdentifier.
    def enterFunctionIdentifier(self, ctx:HiveParser.FunctionIdentifierContext):
        pass

    # Exit a parse tree produced by HiveParser#functionIdentifier.
    def exitFunctionIdentifier(self, ctx:HiveParser.FunctionIdentifierContext):
        pass


    # Enter a parse tree produced by HiveParser#principalIdentifier.
    def enterPrincipalIdentifier(self, ctx:HiveParser.PrincipalIdentifierContext):
        pass

    # Exit a parse tree produced by HiveParser#principalIdentifier.
    def exitPrincipalIdentifier(self, ctx:HiveParser.PrincipalIdentifierContext):
        pass


    # Enter a parse tree produced by HiveParser#nonReserved.
    def enterNonReserved(self, ctx:HiveParser.NonReservedContext):
        pass

    # Exit a parse tree produced by HiveParser#nonReserved.
    def exitNonReserved(self, ctx:HiveParser.NonReservedContext):
        pass


    # Enter a parse tree produced by HiveParser#sql11ReservedKeywordsUsedAsFunctionName.
    def enterSql11ReservedKeywordsUsedAsFunctionName(self, ctx:HiveParser.Sql11ReservedKeywordsUsedAsFunctionNameContext):
        pass

    # Exit a parse tree produced by HiveParser#sql11ReservedKeywordsUsedAsFunctionName.
    def exitSql11ReservedKeywordsUsedAsFunctionName(self, ctx:HiveParser.Sql11ReservedKeywordsUsedAsFunctionNameContext):
        pass



del HiveParser