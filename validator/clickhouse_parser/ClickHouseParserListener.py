# Generated from ClickHouseParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ClickHouseParser import ClickHouseParser
else:
    from ClickHouseParser import ClickHouseParser

# This class defines a complete listener for a parse tree produced by ClickHouseParser.
class ClickHouseParserListener(ParseTreeListener):

    # Enter a parse tree produced by ClickHouseParser#queryStmt.
    def enterQueryStmt(self, ctx:ClickHouseParser.QueryStmtContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#queryStmt.
    def exitQueryStmt(self, ctx:ClickHouseParser.QueryStmtContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#query.
    def enterQuery(self, ctx:ClickHouseParser.QueryContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#query.
    def exitQuery(self, ctx:ClickHouseParser.QueryContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#ctes.
    def enterCtes(self, ctx:ClickHouseParser.CtesContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#ctes.
    def exitCtes(self, ctx:ClickHouseParser.CtesContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#namedQuery.
    def enterNamedQuery(self, ctx:ClickHouseParser.NamedQueryContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#namedQuery.
    def exitNamedQuery(self, ctx:ClickHouseParser.NamedQueryContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#columnAliases.
    def enterColumnAliases(self, ctx:ClickHouseParser.ColumnAliasesContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#columnAliases.
    def exitColumnAliases(self, ctx:ClickHouseParser.ColumnAliasesContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#AlterTableStmt.
    def enterAlterTableStmt(self, ctx:ClickHouseParser.AlterTableStmtContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#AlterTableStmt.
    def exitAlterTableStmt(self, ctx:ClickHouseParser.AlterTableStmtContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#AlterTableClauseAddColumn.
    def enterAlterTableClauseAddColumn(self, ctx:ClickHouseParser.AlterTableClauseAddColumnContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#AlterTableClauseAddColumn.
    def exitAlterTableClauseAddColumn(self, ctx:ClickHouseParser.AlterTableClauseAddColumnContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#AlterTableClauseAddIndex.
    def enterAlterTableClauseAddIndex(self, ctx:ClickHouseParser.AlterTableClauseAddIndexContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#AlterTableClauseAddIndex.
    def exitAlterTableClauseAddIndex(self, ctx:ClickHouseParser.AlterTableClauseAddIndexContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#AlterTableClauseAddProjection.
    def enterAlterTableClauseAddProjection(self, ctx:ClickHouseParser.AlterTableClauseAddProjectionContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#AlterTableClauseAddProjection.
    def exitAlterTableClauseAddProjection(self, ctx:ClickHouseParser.AlterTableClauseAddProjectionContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#AlterTableClauseAttach.
    def enterAlterTableClauseAttach(self, ctx:ClickHouseParser.AlterTableClauseAttachContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#AlterTableClauseAttach.
    def exitAlterTableClauseAttach(self, ctx:ClickHouseParser.AlterTableClauseAttachContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#AlterTableClauseClearColumn.
    def enterAlterTableClauseClearColumn(self, ctx:ClickHouseParser.AlterTableClauseClearColumnContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#AlterTableClauseClearColumn.
    def exitAlterTableClauseClearColumn(self, ctx:ClickHouseParser.AlterTableClauseClearColumnContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#AlterTableClauseClearIndex.
    def enterAlterTableClauseClearIndex(self, ctx:ClickHouseParser.AlterTableClauseClearIndexContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#AlterTableClauseClearIndex.
    def exitAlterTableClauseClearIndex(self, ctx:ClickHouseParser.AlterTableClauseClearIndexContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#AlterTableClauseClearProjection.
    def enterAlterTableClauseClearProjection(self, ctx:ClickHouseParser.AlterTableClauseClearProjectionContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#AlterTableClauseClearProjection.
    def exitAlterTableClauseClearProjection(self, ctx:ClickHouseParser.AlterTableClauseClearProjectionContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#AlterTableClauseComment.
    def enterAlterTableClauseComment(self, ctx:ClickHouseParser.AlterTableClauseCommentContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#AlterTableClauseComment.
    def exitAlterTableClauseComment(self, ctx:ClickHouseParser.AlterTableClauseCommentContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#AlterTableClauseDelete.
    def enterAlterTableClauseDelete(self, ctx:ClickHouseParser.AlterTableClauseDeleteContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#AlterTableClauseDelete.
    def exitAlterTableClauseDelete(self, ctx:ClickHouseParser.AlterTableClauseDeleteContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#AlterTableClauseDetach.
    def enterAlterTableClauseDetach(self, ctx:ClickHouseParser.AlterTableClauseDetachContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#AlterTableClauseDetach.
    def exitAlterTableClauseDetach(self, ctx:ClickHouseParser.AlterTableClauseDetachContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#AlterTableClauseDropColumn.
    def enterAlterTableClauseDropColumn(self, ctx:ClickHouseParser.AlterTableClauseDropColumnContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#AlterTableClauseDropColumn.
    def exitAlterTableClauseDropColumn(self, ctx:ClickHouseParser.AlterTableClauseDropColumnContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#AlterTableClauseDropIndex.
    def enterAlterTableClauseDropIndex(self, ctx:ClickHouseParser.AlterTableClauseDropIndexContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#AlterTableClauseDropIndex.
    def exitAlterTableClauseDropIndex(self, ctx:ClickHouseParser.AlterTableClauseDropIndexContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#AlterTableClauseDropProjection.
    def enterAlterTableClauseDropProjection(self, ctx:ClickHouseParser.AlterTableClauseDropProjectionContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#AlterTableClauseDropProjection.
    def exitAlterTableClauseDropProjection(self, ctx:ClickHouseParser.AlterTableClauseDropProjectionContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#AlterTableClauseDropPartition.
    def enterAlterTableClauseDropPartition(self, ctx:ClickHouseParser.AlterTableClauseDropPartitionContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#AlterTableClauseDropPartition.
    def exitAlterTableClauseDropPartition(self, ctx:ClickHouseParser.AlterTableClauseDropPartitionContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#AlterTableClauseFreezePartition.
    def enterAlterTableClauseFreezePartition(self, ctx:ClickHouseParser.AlterTableClauseFreezePartitionContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#AlterTableClauseFreezePartition.
    def exitAlterTableClauseFreezePartition(self, ctx:ClickHouseParser.AlterTableClauseFreezePartitionContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#AlterTableClauseMaterializeIndex.
    def enterAlterTableClauseMaterializeIndex(self, ctx:ClickHouseParser.AlterTableClauseMaterializeIndexContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#AlterTableClauseMaterializeIndex.
    def exitAlterTableClauseMaterializeIndex(self, ctx:ClickHouseParser.AlterTableClauseMaterializeIndexContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#AlterTableClauseMaterializeProjection.
    def enterAlterTableClauseMaterializeProjection(self, ctx:ClickHouseParser.AlterTableClauseMaterializeProjectionContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#AlterTableClauseMaterializeProjection.
    def exitAlterTableClauseMaterializeProjection(self, ctx:ClickHouseParser.AlterTableClauseMaterializeProjectionContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#AlterTableClauseModifyCodec.
    def enterAlterTableClauseModifyCodec(self, ctx:ClickHouseParser.AlterTableClauseModifyCodecContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#AlterTableClauseModifyCodec.
    def exitAlterTableClauseModifyCodec(self, ctx:ClickHouseParser.AlterTableClauseModifyCodecContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#AlterTableClauseModifyComment.
    def enterAlterTableClauseModifyComment(self, ctx:ClickHouseParser.AlterTableClauseModifyCommentContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#AlterTableClauseModifyComment.
    def exitAlterTableClauseModifyComment(self, ctx:ClickHouseParser.AlterTableClauseModifyCommentContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#AlterTableClauseModifyRemove.
    def enterAlterTableClauseModifyRemove(self, ctx:ClickHouseParser.AlterTableClauseModifyRemoveContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#AlterTableClauseModifyRemove.
    def exitAlterTableClauseModifyRemove(self, ctx:ClickHouseParser.AlterTableClauseModifyRemoveContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#AlterTableClauseModify.
    def enterAlterTableClauseModify(self, ctx:ClickHouseParser.AlterTableClauseModifyContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#AlterTableClauseModify.
    def exitAlterTableClauseModify(self, ctx:ClickHouseParser.AlterTableClauseModifyContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#AlterTableClauseModifyOrderBy.
    def enterAlterTableClauseModifyOrderBy(self, ctx:ClickHouseParser.AlterTableClauseModifyOrderByContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#AlterTableClauseModifyOrderBy.
    def exitAlterTableClauseModifyOrderBy(self, ctx:ClickHouseParser.AlterTableClauseModifyOrderByContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#AlterTableClauseModifyTTL.
    def enterAlterTableClauseModifyTTL(self, ctx:ClickHouseParser.AlterTableClauseModifyTTLContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#AlterTableClauseModifyTTL.
    def exitAlterTableClauseModifyTTL(self, ctx:ClickHouseParser.AlterTableClauseModifyTTLContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#AlterTableClauseMovePartition.
    def enterAlterTableClauseMovePartition(self, ctx:ClickHouseParser.AlterTableClauseMovePartitionContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#AlterTableClauseMovePartition.
    def exitAlterTableClauseMovePartition(self, ctx:ClickHouseParser.AlterTableClauseMovePartitionContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#AlterTableClauseRemoveTTL.
    def enterAlterTableClauseRemoveTTL(self, ctx:ClickHouseParser.AlterTableClauseRemoveTTLContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#AlterTableClauseRemoveTTL.
    def exitAlterTableClauseRemoveTTL(self, ctx:ClickHouseParser.AlterTableClauseRemoveTTLContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#AlterTableClauseRename.
    def enterAlterTableClauseRename(self, ctx:ClickHouseParser.AlterTableClauseRenameContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#AlterTableClauseRename.
    def exitAlterTableClauseRename(self, ctx:ClickHouseParser.AlterTableClauseRenameContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#AlterTableClauseReplace.
    def enterAlterTableClauseReplace(self, ctx:ClickHouseParser.AlterTableClauseReplaceContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#AlterTableClauseReplace.
    def exitAlterTableClauseReplace(self, ctx:ClickHouseParser.AlterTableClauseReplaceContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#AlterTableClauseUpdate.
    def enterAlterTableClauseUpdate(self, ctx:ClickHouseParser.AlterTableClauseUpdateContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#AlterTableClauseUpdate.
    def exitAlterTableClauseUpdate(self, ctx:ClickHouseParser.AlterTableClauseUpdateContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#assignmentExprList.
    def enterAssignmentExprList(self, ctx:ClickHouseParser.AssignmentExprListContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#assignmentExprList.
    def exitAssignmentExprList(self, ctx:ClickHouseParser.AssignmentExprListContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#assignmentExpr.
    def enterAssignmentExpr(self, ctx:ClickHouseParser.AssignmentExprContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#assignmentExpr.
    def exitAssignmentExpr(self, ctx:ClickHouseParser.AssignmentExprContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#tableColumnPropertyType.
    def enterTableColumnPropertyType(self, ctx:ClickHouseParser.TableColumnPropertyTypeContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#tableColumnPropertyType.
    def exitTableColumnPropertyType(self, ctx:ClickHouseParser.TableColumnPropertyTypeContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#partitionClause.
    def enterPartitionClause(self, ctx:ClickHouseParser.PartitionClauseContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#partitionClause.
    def exitPartitionClause(self, ctx:ClickHouseParser.PartitionClauseContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#AttachDictionaryStmt.
    def enterAttachDictionaryStmt(self, ctx:ClickHouseParser.AttachDictionaryStmtContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#AttachDictionaryStmt.
    def exitAttachDictionaryStmt(self, ctx:ClickHouseParser.AttachDictionaryStmtContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#checkStmt.
    def enterCheckStmt(self, ctx:ClickHouseParser.CheckStmtContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#checkStmt.
    def exitCheckStmt(self, ctx:ClickHouseParser.CheckStmtContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#CreateDatabaseStmt.
    def enterCreateDatabaseStmt(self, ctx:ClickHouseParser.CreateDatabaseStmtContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#CreateDatabaseStmt.
    def exitCreateDatabaseStmt(self, ctx:ClickHouseParser.CreateDatabaseStmtContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#CreateDictionaryStmt.
    def enterCreateDictionaryStmt(self, ctx:ClickHouseParser.CreateDictionaryStmtContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#CreateDictionaryStmt.
    def exitCreateDictionaryStmt(self, ctx:ClickHouseParser.CreateDictionaryStmtContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#CreateLiveViewStmt.
    def enterCreateLiveViewStmt(self, ctx:ClickHouseParser.CreateLiveViewStmtContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#CreateLiveViewStmt.
    def exitCreateLiveViewStmt(self, ctx:ClickHouseParser.CreateLiveViewStmtContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#CreateMaterializedViewStmt.
    def enterCreateMaterializedViewStmt(self, ctx:ClickHouseParser.CreateMaterializedViewStmtContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#CreateMaterializedViewStmt.
    def exitCreateMaterializedViewStmt(self, ctx:ClickHouseParser.CreateMaterializedViewStmtContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#CreateTableStmt.
    def enterCreateTableStmt(self, ctx:ClickHouseParser.CreateTableStmtContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#CreateTableStmt.
    def exitCreateTableStmt(self, ctx:ClickHouseParser.CreateTableStmtContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#CreateViewStmt.
    def enterCreateViewStmt(self, ctx:ClickHouseParser.CreateViewStmtContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#CreateViewStmt.
    def exitCreateViewStmt(self, ctx:ClickHouseParser.CreateViewStmtContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#dictionarySchemaClause.
    def enterDictionarySchemaClause(self, ctx:ClickHouseParser.DictionarySchemaClauseContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#dictionarySchemaClause.
    def exitDictionarySchemaClause(self, ctx:ClickHouseParser.DictionarySchemaClauseContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#dictionaryAttrDfnt.
    def enterDictionaryAttrDfnt(self, ctx:ClickHouseParser.DictionaryAttrDfntContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#dictionaryAttrDfnt.
    def exitDictionaryAttrDfnt(self, ctx:ClickHouseParser.DictionaryAttrDfntContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#dictionaryEngineClause.
    def enterDictionaryEngineClause(self, ctx:ClickHouseParser.DictionaryEngineClauseContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#dictionaryEngineClause.
    def exitDictionaryEngineClause(self, ctx:ClickHouseParser.DictionaryEngineClauseContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#dictionaryPrimaryKeyClause.
    def enterDictionaryPrimaryKeyClause(self, ctx:ClickHouseParser.DictionaryPrimaryKeyClauseContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#dictionaryPrimaryKeyClause.
    def exitDictionaryPrimaryKeyClause(self, ctx:ClickHouseParser.DictionaryPrimaryKeyClauseContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#dictionaryArgExpr.
    def enterDictionaryArgExpr(self, ctx:ClickHouseParser.DictionaryArgExprContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#dictionaryArgExpr.
    def exitDictionaryArgExpr(self, ctx:ClickHouseParser.DictionaryArgExprContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#sourceClause.
    def enterSourceClause(self, ctx:ClickHouseParser.SourceClauseContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#sourceClause.
    def exitSourceClause(self, ctx:ClickHouseParser.SourceClauseContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#lifetimeClause.
    def enterLifetimeClause(self, ctx:ClickHouseParser.LifetimeClauseContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#lifetimeClause.
    def exitLifetimeClause(self, ctx:ClickHouseParser.LifetimeClauseContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#layoutClause.
    def enterLayoutClause(self, ctx:ClickHouseParser.LayoutClauseContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#layoutClause.
    def exitLayoutClause(self, ctx:ClickHouseParser.LayoutClauseContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#rangeClause.
    def enterRangeClause(self, ctx:ClickHouseParser.RangeClauseContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#rangeClause.
    def exitRangeClause(self, ctx:ClickHouseParser.RangeClauseContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#dictionarySettingsClause.
    def enterDictionarySettingsClause(self, ctx:ClickHouseParser.DictionarySettingsClauseContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#dictionarySettingsClause.
    def exitDictionarySettingsClause(self, ctx:ClickHouseParser.DictionarySettingsClauseContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#clusterClause.
    def enterClusterClause(self, ctx:ClickHouseParser.ClusterClauseContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#clusterClause.
    def exitClusterClause(self, ctx:ClickHouseParser.ClusterClauseContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#uuidClause.
    def enterUuidClause(self, ctx:ClickHouseParser.UuidClauseContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#uuidClause.
    def exitUuidClause(self, ctx:ClickHouseParser.UuidClauseContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#destinationClause.
    def enterDestinationClause(self, ctx:ClickHouseParser.DestinationClauseContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#destinationClause.
    def exitDestinationClause(self, ctx:ClickHouseParser.DestinationClauseContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#subqueryClause.
    def enterSubqueryClause(self, ctx:ClickHouseParser.SubqueryClauseContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#subqueryClause.
    def exitSubqueryClause(self, ctx:ClickHouseParser.SubqueryClauseContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#SchemaDescriptionClause.
    def enterSchemaDescriptionClause(self, ctx:ClickHouseParser.SchemaDescriptionClauseContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#SchemaDescriptionClause.
    def exitSchemaDescriptionClause(self, ctx:ClickHouseParser.SchemaDescriptionClauseContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#SchemaAsTableClause.
    def enterSchemaAsTableClause(self, ctx:ClickHouseParser.SchemaAsTableClauseContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#SchemaAsTableClause.
    def exitSchemaAsTableClause(self, ctx:ClickHouseParser.SchemaAsTableClauseContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#SchemaAsFunctionClause.
    def enterSchemaAsFunctionClause(self, ctx:ClickHouseParser.SchemaAsFunctionClauseContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#SchemaAsFunctionClause.
    def exitSchemaAsFunctionClause(self, ctx:ClickHouseParser.SchemaAsFunctionClauseContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#engineClause.
    def enterEngineClause(self, ctx:ClickHouseParser.EngineClauseContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#engineClause.
    def exitEngineClause(self, ctx:ClickHouseParser.EngineClauseContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#partitionByClause.
    def enterPartitionByClause(self, ctx:ClickHouseParser.PartitionByClauseContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#partitionByClause.
    def exitPartitionByClause(self, ctx:ClickHouseParser.PartitionByClauseContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#primaryKeyClause.
    def enterPrimaryKeyClause(self, ctx:ClickHouseParser.PrimaryKeyClauseContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#primaryKeyClause.
    def exitPrimaryKeyClause(self, ctx:ClickHouseParser.PrimaryKeyClauseContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#sampleByClause.
    def enterSampleByClause(self, ctx:ClickHouseParser.SampleByClauseContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#sampleByClause.
    def exitSampleByClause(self, ctx:ClickHouseParser.SampleByClauseContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#ttlClause.
    def enterTtlClause(self, ctx:ClickHouseParser.TtlClauseContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#ttlClause.
    def exitTtlClause(self, ctx:ClickHouseParser.TtlClauseContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#engineExpr.
    def enterEngineExpr(self, ctx:ClickHouseParser.EngineExprContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#engineExpr.
    def exitEngineExpr(self, ctx:ClickHouseParser.EngineExprContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#TableElementExprColumn.
    def enterTableElementExprColumn(self, ctx:ClickHouseParser.TableElementExprColumnContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#TableElementExprColumn.
    def exitTableElementExprColumn(self, ctx:ClickHouseParser.TableElementExprColumnContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#TableElementExprConstraint.
    def enterTableElementExprConstraint(self, ctx:ClickHouseParser.TableElementExprConstraintContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#TableElementExprConstraint.
    def exitTableElementExprConstraint(self, ctx:ClickHouseParser.TableElementExprConstraintContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#TableElementExprIndex.
    def enterTableElementExprIndex(self, ctx:ClickHouseParser.TableElementExprIndexContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#TableElementExprIndex.
    def exitTableElementExprIndex(self, ctx:ClickHouseParser.TableElementExprIndexContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#TableElementExprProjection.
    def enterTableElementExprProjection(self, ctx:ClickHouseParser.TableElementExprProjectionContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#TableElementExprProjection.
    def exitTableElementExprProjection(self, ctx:ClickHouseParser.TableElementExprProjectionContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#tableColumnDfnt.
    def enterTableColumnDfnt(self, ctx:ClickHouseParser.TableColumnDfntContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#tableColumnDfnt.
    def exitTableColumnDfnt(self, ctx:ClickHouseParser.TableColumnDfntContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#tableColumnPropertyExpr.
    def enterTableColumnPropertyExpr(self, ctx:ClickHouseParser.TableColumnPropertyExprContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#tableColumnPropertyExpr.
    def exitTableColumnPropertyExpr(self, ctx:ClickHouseParser.TableColumnPropertyExprContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#tableIndexDfnt.
    def enterTableIndexDfnt(self, ctx:ClickHouseParser.TableIndexDfntContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#tableIndexDfnt.
    def exitTableIndexDfnt(self, ctx:ClickHouseParser.TableIndexDfntContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#tableProjectionDfnt.
    def enterTableProjectionDfnt(self, ctx:ClickHouseParser.TableProjectionDfntContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#tableProjectionDfnt.
    def exitTableProjectionDfnt(self, ctx:ClickHouseParser.TableProjectionDfntContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#codecExpr.
    def enterCodecExpr(self, ctx:ClickHouseParser.CodecExprContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#codecExpr.
    def exitCodecExpr(self, ctx:ClickHouseParser.CodecExprContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#codecArgExpr.
    def enterCodecArgExpr(self, ctx:ClickHouseParser.CodecArgExprContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#codecArgExpr.
    def exitCodecArgExpr(self, ctx:ClickHouseParser.CodecArgExprContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#ttlExpr.
    def enterTtlExpr(self, ctx:ClickHouseParser.TtlExprContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#ttlExpr.
    def exitTtlExpr(self, ctx:ClickHouseParser.TtlExprContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#describeStmt.
    def enterDescribeStmt(self, ctx:ClickHouseParser.DescribeStmtContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#describeStmt.
    def exitDescribeStmt(self, ctx:ClickHouseParser.DescribeStmtContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#DropDatabaseStmt.
    def enterDropDatabaseStmt(self, ctx:ClickHouseParser.DropDatabaseStmtContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#DropDatabaseStmt.
    def exitDropDatabaseStmt(self, ctx:ClickHouseParser.DropDatabaseStmtContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#DropTableStmt.
    def enterDropTableStmt(self, ctx:ClickHouseParser.DropTableStmtContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#DropTableStmt.
    def exitDropTableStmt(self, ctx:ClickHouseParser.DropTableStmtContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#ExistsDatabaseStmt.
    def enterExistsDatabaseStmt(self, ctx:ClickHouseParser.ExistsDatabaseStmtContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#ExistsDatabaseStmt.
    def exitExistsDatabaseStmt(self, ctx:ClickHouseParser.ExistsDatabaseStmtContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#ExistsTableStmt.
    def enterExistsTableStmt(self, ctx:ClickHouseParser.ExistsTableStmtContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#ExistsTableStmt.
    def exitExistsTableStmt(self, ctx:ClickHouseParser.ExistsTableStmtContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#ExplainASTStmt.
    def enterExplainASTStmt(self, ctx:ClickHouseParser.ExplainASTStmtContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#ExplainASTStmt.
    def exitExplainASTStmt(self, ctx:ClickHouseParser.ExplainASTStmtContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#ExplainSyntaxStmt.
    def enterExplainSyntaxStmt(self, ctx:ClickHouseParser.ExplainSyntaxStmtContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#ExplainSyntaxStmt.
    def exitExplainSyntaxStmt(self, ctx:ClickHouseParser.ExplainSyntaxStmtContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#insertStmt.
    def enterInsertStmt(self, ctx:ClickHouseParser.InsertStmtContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#insertStmt.
    def exitInsertStmt(self, ctx:ClickHouseParser.InsertStmtContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#columnsClause.
    def enterColumnsClause(self, ctx:ClickHouseParser.ColumnsClauseContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#columnsClause.
    def exitColumnsClause(self, ctx:ClickHouseParser.ColumnsClauseContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#DataClauseFormat.
    def enterDataClauseFormat(self, ctx:ClickHouseParser.DataClauseFormatContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#DataClauseFormat.
    def exitDataClauseFormat(self, ctx:ClickHouseParser.DataClauseFormatContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#DataClauseValues.
    def enterDataClauseValues(self, ctx:ClickHouseParser.DataClauseValuesContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#DataClauseValues.
    def exitDataClauseValues(self, ctx:ClickHouseParser.DataClauseValuesContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#DataClauseSelect.
    def enterDataClauseSelect(self, ctx:ClickHouseParser.DataClauseSelectContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#DataClauseSelect.
    def exitDataClauseSelect(self, ctx:ClickHouseParser.DataClauseSelectContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#assignmentValues.
    def enterAssignmentValues(self, ctx:ClickHouseParser.AssignmentValuesContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#assignmentValues.
    def exitAssignmentValues(self, ctx:ClickHouseParser.AssignmentValuesContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#assignmentValue.
    def enterAssignmentValue(self, ctx:ClickHouseParser.AssignmentValueContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#assignmentValue.
    def exitAssignmentValue(self, ctx:ClickHouseParser.AssignmentValueContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#KillMutationStmt.
    def enterKillMutationStmt(self, ctx:ClickHouseParser.KillMutationStmtContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#KillMutationStmt.
    def exitKillMutationStmt(self, ctx:ClickHouseParser.KillMutationStmtContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#optimizeStmt.
    def enterOptimizeStmt(self, ctx:ClickHouseParser.OptimizeStmtContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#optimizeStmt.
    def exitOptimizeStmt(self, ctx:ClickHouseParser.OptimizeStmtContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#renameStmt.
    def enterRenameStmt(self, ctx:ClickHouseParser.RenameStmtContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#renameStmt.
    def exitRenameStmt(self, ctx:ClickHouseParser.RenameStmtContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#projectionSelectStmt.
    def enterProjectionSelectStmt(self, ctx:ClickHouseParser.ProjectionSelectStmtContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#projectionSelectStmt.
    def exitProjectionSelectStmt(self, ctx:ClickHouseParser.ProjectionSelectStmtContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#selectUnionStmt.
    def enterSelectUnionStmt(self, ctx:ClickHouseParser.SelectUnionStmtContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#selectUnionStmt.
    def exitSelectUnionStmt(self, ctx:ClickHouseParser.SelectUnionStmtContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#selectStmtWithParens.
    def enterSelectStmtWithParens(self, ctx:ClickHouseParser.SelectStmtWithParensContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#selectStmtWithParens.
    def exitSelectStmtWithParens(self, ctx:ClickHouseParser.SelectStmtWithParensContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#selectStmt.
    def enterSelectStmt(self, ctx:ClickHouseParser.SelectStmtContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#selectStmt.
    def exitSelectStmt(self, ctx:ClickHouseParser.SelectStmtContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#withClause.
    def enterWithClause(self, ctx:ClickHouseParser.WithClauseContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#withClause.
    def exitWithClause(self, ctx:ClickHouseParser.WithClauseContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#topClause.
    def enterTopClause(self, ctx:ClickHouseParser.TopClauseContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#topClause.
    def exitTopClause(self, ctx:ClickHouseParser.TopClauseContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#fromClause.
    def enterFromClause(self, ctx:ClickHouseParser.FromClauseContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#fromClause.
    def exitFromClause(self, ctx:ClickHouseParser.FromClauseContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#arrayJoinClause.
    def enterArrayJoinClause(self, ctx:ClickHouseParser.ArrayJoinClauseContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#arrayJoinClause.
    def exitArrayJoinClause(self, ctx:ClickHouseParser.ArrayJoinClauseContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#windowClause.
    def enterWindowClause(self, ctx:ClickHouseParser.WindowClauseContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#windowClause.
    def exitWindowClause(self, ctx:ClickHouseParser.WindowClauseContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#prewhereClause.
    def enterPrewhereClause(self, ctx:ClickHouseParser.PrewhereClauseContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#prewhereClause.
    def exitPrewhereClause(self, ctx:ClickHouseParser.PrewhereClauseContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#whereClause.
    def enterWhereClause(self, ctx:ClickHouseParser.WhereClauseContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#whereClause.
    def exitWhereClause(self, ctx:ClickHouseParser.WhereClauseContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#groupByClause.
    def enterGroupByClause(self, ctx:ClickHouseParser.GroupByClauseContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#groupByClause.
    def exitGroupByClause(self, ctx:ClickHouseParser.GroupByClauseContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#havingClause.
    def enterHavingClause(self, ctx:ClickHouseParser.HavingClauseContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#havingClause.
    def exitHavingClause(self, ctx:ClickHouseParser.HavingClauseContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#orderByClause.
    def enterOrderByClause(self, ctx:ClickHouseParser.OrderByClauseContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#orderByClause.
    def exitOrderByClause(self, ctx:ClickHouseParser.OrderByClauseContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#projectionOrderByClause.
    def enterProjectionOrderByClause(self, ctx:ClickHouseParser.ProjectionOrderByClauseContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#projectionOrderByClause.
    def exitProjectionOrderByClause(self, ctx:ClickHouseParser.ProjectionOrderByClauseContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#limitByClause.
    def enterLimitByClause(self, ctx:ClickHouseParser.LimitByClauseContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#limitByClause.
    def exitLimitByClause(self, ctx:ClickHouseParser.LimitByClauseContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#limitClause.
    def enterLimitClause(self, ctx:ClickHouseParser.LimitClauseContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#limitClause.
    def exitLimitClause(self, ctx:ClickHouseParser.LimitClauseContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#settingsClause.
    def enterSettingsClause(self, ctx:ClickHouseParser.SettingsClauseContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#settingsClause.
    def exitSettingsClause(self, ctx:ClickHouseParser.SettingsClauseContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#JoinExprOp.
    def enterJoinExprOp(self, ctx:ClickHouseParser.JoinExprOpContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#JoinExprOp.
    def exitJoinExprOp(self, ctx:ClickHouseParser.JoinExprOpContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#JoinExprTable.
    def enterJoinExprTable(self, ctx:ClickHouseParser.JoinExprTableContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#JoinExprTable.
    def exitJoinExprTable(self, ctx:ClickHouseParser.JoinExprTableContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#JoinExprParens.
    def enterJoinExprParens(self, ctx:ClickHouseParser.JoinExprParensContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#JoinExprParens.
    def exitJoinExprParens(self, ctx:ClickHouseParser.JoinExprParensContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#JoinExprCrossOp.
    def enterJoinExprCrossOp(self, ctx:ClickHouseParser.JoinExprCrossOpContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#JoinExprCrossOp.
    def exitJoinExprCrossOp(self, ctx:ClickHouseParser.JoinExprCrossOpContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#JoinOpInner.
    def enterJoinOpInner(self, ctx:ClickHouseParser.JoinOpInnerContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#JoinOpInner.
    def exitJoinOpInner(self, ctx:ClickHouseParser.JoinOpInnerContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#JoinOpLeftRight.
    def enterJoinOpLeftRight(self, ctx:ClickHouseParser.JoinOpLeftRightContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#JoinOpLeftRight.
    def exitJoinOpLeftRight(self, ctx:ClickHouseParser.JoinOpLeftRightContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#JoinOpFull.
    def enterJoinOpFull(self, ctx:ClickHouseParser.JoinOpFullContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#JoinOpFull.
    def exitJoinOpFull(self, ctx:ClickHouseParser.JoinOpFullContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#joinOpCross.
    def enterJoinOpCross(self, ctx:ClickHouseParser.JoinOpCrossContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#joinOpCross.
    def exitJoinOpCross(self, ctx:ClickHouseParser.JoinOpCrossContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#joinConstraintClause.
    def enterJoinConstraintClause(self, ctx:ClickHouseParser.JoinConstraintClauseContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#joinConstraintClause.
    def exitJoinConstraintClause(self, ctx:ClickHouseParser.JoinConstraintClauseContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#sampleClause.
    def enterSampleClause(self, ctx:ClickHouseParser.SampleClauseContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#sampleClause.
    def exitSampleClause(self, ctx:ClickHouseParser.SampleClauseContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#limitExpr.
    def enterLimitExpr(self, ctx:ClickHouseParser.LimitExprContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#limitExpr.
    def exitLimitExpr(self, ctx:ClickHouseParser.LimitExprContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#orderExprList.
    def enterOrderExprList(self, ctx:ClickHouseParser.OrderExprListContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#orderExprList.
    def exitOrderExprList(self, ctx:ClickHouseParser.OrderExprListContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#orderExpr.
    def enterOrderExpr(self, ctx:ClickHouseParser.OrderExprContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#orderExpr.
    def exitOrderExpr(self, ctx:ClickHouseParser.OrderExprContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#ratioExpr.
    def enterRatioExpr(self, ctx:ClickHouseParser.RatioExprContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#ratioExpr.
    def exitRatioExpr(self, ctx:ClickHouseParser.RatioExprContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#settingExprList.
    def enterSettingExprList(self, ctx:ClickHouseParser.SettingExprListContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#settingExprList.
    def exitSettingExprList(self, ctx:ClickHouseParser.SettingExprListContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#settingExpr.
    def enterSettingExpr(self, ctx:ClickHouseParser.SettingExprContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#settingExpr.
    def exitSettingExpr(self, ctx:ClickHouseParser.SettingExprContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#windowExpr.
    def enterWindowExpr(self, ctx:ClickHouseParser.WindowExprContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#windowExpr.
    def exitWindowExpr(self, ctx:ClickHouseParser.WindowExprContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#winPartitionByClause.
    def enterWinPartitionByClause(self, ctx:ClickHouseParser.WinPartitionByClauseContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#winPartitionByClause.
    def exitWinPartitionByClause(self, ctx:ClickHouseParser.WinPartitionByClauseContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#winOrderByClause.
    def enterWinOrderByClause(self, ctx:ClickHouseParser.WinOrderByClauseContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#winOrderByClause.
    def exitWinOrderByClause(self, ctx:ClickHouseParser.WinOrderByClauseContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#winFrameClause.
    def enterWinFrameClause(self, ctx:ClickHouseParser.WinFrameClauseContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#winFrameClause.
    def exitWinFrameClause(self, ctx:ClickHouseParser.WinFrameClauseContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#frameStart.
    def enterFrameStart(self, ctx:ClickHouseParser.FrameStartContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#frameStart.
    def exitFrameStart(self, ctx:ClickHouseParser.FrameStartContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#frameBetween.
    def enterFrameBetween(self, ctx:ClickHouseParser.FrameBetweenContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#frameBetween.
    def exitFrameBetween(self, ctx:ClickHouseParser.FrameBetweenContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#winFrameBound.
    def enterWinFrameBound(self, ctx:ClickHouseParser.WinFrameBoundContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#winFrameBound.
    def exitWinFrameBound(self, ctx:ClickHouseParser.WinFrameBoundContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#setStmt.
    def enterSetStmt(self, ctx:ClickHouseParser.SetStmtContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#setStmt.
    def exitSetStmt(self, ctx:ClickHouseParser.SetStmtContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#showCreateDatabaseStmt.
    def enterShowCreateDatabaseStmt(self, ctx:ClickHouseParser.ShowCreateDatabaseStmtContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#showCreateDatabaseStmt.
    def exitShowCreateDatabaseStmt(self, ctx:ClickHouseParser.ShowCreateDatabaseStmtContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#showCreateDictionaryStmt.
    def enterShowCreateDictionaryStmt(self, ctx:ClickHouseParser.ShowCreateDictionaryStmtContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#showCreateDictionaryStmt.
    def exitShowCreateDictionaryStmt(self, ctx:ClickHouseParser.ShowCreateDictionaryStmtContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#showCreateTableStmt.
    def enterShowCreateTableStmt(self, ctx:ClickHouseParser.ShowCreateTableStmtContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#showCreateTableStmt.
    def exitShowCreateTableStmt(self, ctx:ClickHouseParser.ShowCreateTableStmtContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#showDatabasesStmt.
    def enterShowDatabasesStmt(self, ctx:ClickHouseParser.ShowDatabasesStmtContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#showDatabasesStmt.
    def exitShowDatabasesStmt(self, ctx:ClickHouseParser.ShowDatabasesStmtContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#showDictionariesStmt.
    def enterShowDictionariesStmt(self, ctx:ClickHouseParser.ShowDictionariesStmtContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#showDictionariesStmt.
    def exitShowDictionariesStmt(self, ctx:ClickHouseParser.ShowDictionariesStmtContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#showTablesStmt.
    def enterShowTablesStmt(self, ctx:ClickHouseParser.ShowTablesStmtContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#showTablesStmt.
    def exitShowTablesStmt(self, ctx:ClickHouseParser.ShowTablesStmtContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#systemStmt.
    def enterSystemStmt(self, ctx:ClickHouseParser.SystemStmtContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#systemStmt.
    def exitSystemStmt(self, ctx:ClickHouseParser.SystemStmtContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#truncateStmt.
    def enterTruncateStmt(self, ctx:ClickHouseParser.TruncateStmtContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#truncateStmt.
    def exitTruncateStmt(self, ctx:ClickHouseParser.TruncateStmtContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#useStmt.
    def enterUseStmt(self, ctx:ClickHouseParser.UseStmtContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#useStmt.
    def exitUseStmt(self, ctx:ClickHouseParser.UseStmtContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#watchStmt.
    def enterWatchStmt(self, ctx:ClickHouseParser.WatchStmtContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#watchStmt.
    def exitWatchStmt(self, ctx:ClickHouseParser.WatchStmtContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#ColumnTypeExprSimple.
    def enterColumnTypeExprSimple(self, ctx:ClickHouseParser.ColumnTypeExprSimpleContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#ColumnTypeExprSimple.
    def exitColumnTypeExprSimple(self, ctx:ClickHouseParser.ColumnTypeExprSimpleContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#ColumnTypeExprNested.
    def enterColumnTypeExprNested(self, ctx:ClickHouseParser.ColumnTypeExprNestedContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#ColumnTypeExprNested.
    def exitColumnTypeExprNested(self, ctx:ClickHouseParser.ColumnTypeExprNestedContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#ColumnTypeExprEnum.
    def enterColumnTypeExprEnum(self, ctx:ClickHouseParser.ColumnTypeExprEnumContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#ColumnTypeExprEnum.
    def exitColumnTypeExprEnum(self, ctx:ClickHouseParser.ColumnTypeExprEnumContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#ColumnTypeExprComplex.
    def enterColumnTypeExprComplex(self, ctx:ClickHouseParser.ColumnTypeExprComplexContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#ColumnTypeExprComplex.
    def exitColumnTypeExprComplex(self, ctx:ClickHouseParser.ColumnTypeExprComplexContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#ColumnTypeExprParam.
    def enterColumnTypeExprParam(self, ctx:ClickHouseParser.ColumnTypeExprParamContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#ColumnTypeExprParam.
    def exitColumnTypeExprParam(self, ctx:ClickHouseParser.ColumnTypeExprParamContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#columnExprList.
    def enterColumnExprList(self, ctx:ClickHouseParser.ColumnExprListContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#columnExprList.
    def exitColumnExprList(self, ctx:ClickHouseParser.ColumnExprListContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#ColumnsExprAsterisk.
    def enterColumnsExprAsterisk(self, ctx:ClickHouseParser.ColumnsExprAsteriskContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#ColumnsExprAsterisk.
    def exitColumnsExprAsterisk(self, ctx:ClickHouseParser.ColumnsExprAsteriskContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#ColumnsExprSubquery.
    def enterColumnsExprSubquery(self, ctx:ClickHouseParser.ColumnsExprSubqueryContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#ColumnsExprSubquery.
    def exitColumnsExprSubquery(self, ctx:ClickHouseParser.ColumnsExprSubqueryContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#ColumnsExprColumn.
    def enterColumnsExprColumn(self, ctx:ClickHouseParser.ColumnsExprColumnContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#ColumnsExprColumn.
    def exitColumnsExprColumn(self, ctx:ClickHouseParser.ColumnsExprColumnContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#ColumnExprTernaryOp.
    def enterColumnExprTernaryOp(self, ctx:ClickHouseParser.ColumnExprTernaryOpContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#ColumnExprTernaryOp.
    def exitColumnExprTernaryOp(self, ctx:ClickHouseParser.ColumnExprTernaryOpContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#ColumnExprAlias.
    def enterColumnExprAlias(self, ctx:ClickHouseParser.ColumnExprAliasContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#ColumnExprAlias.
    def exitColumnExprAlias(self, ctx:ClickHouseParser.ColumnExprAliasContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#ColumnExprExtract.
    def enterColumnExprExtract(self, ctx:ClickHouseParser.ColumnExprExtractContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#ColumnExprExtract.
    def exitColumnExprExtract(self, ctx:ClickHouseParser.ColumnExprExtractContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#ColumnExprNegate.
    def enterColumnExprNegate(self, ctx:ClickHouseParser.ColumnExprNegateContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#ColumnExprNegate.
    def exitColumnExprNegate(self, ctx:ClickHouseParser.ColumnExprNegateContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#ColumnExprSubquery.
    def enterColumnExprSubquery(self, ctx:ClickHouseParser.ColumnExprSubqueryContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#ColumnExprSubquery.
    def exitColumnExprSubquery(self, ctx:ClickHouseParser.ColumnExprSubqueryContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#ColumnExprLiteral.
    def enterColumnExprLiteral(self, ctx:ClickHouseParser.ColumnExprLiteralContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#ColumnExprLiteral.
    def exitColumnExprLiteral(self, ctx:ClickHouseParser.ColumnExprLiteralContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#ColumnExprArray.
    def enterColumnExprArray(self, ctx:ClickHouseParser.ColumnExprArrayContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#ColumnExprArray.
    def exitColumnExprArray(self, ctx:ClickHouseParser.ColumnExprArrayContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#ColumnExprSubstring.
    def enterColumnExprSubstring(self, ctx:ClickHouseParser.ColumnExprSubstringContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#ColumnExprSubstring.
    def exitColumnExprSubstring(self, ctx:ClickHouseParser.ColumnExprSubstringContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#ColumnExprCast.
    def enterColumnExprCast(self, ctx:ClickHouseParser.ColumnExprCastContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#ColumnExprCast.
    def exitColumnExprCast(self, ctx:ClickHouseParser.ColumnExprCastContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#ColumnExprOr.
    def enterColumnExprOr(self, ctx:ClickHouseParser.ColumnExprOrContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#ColumnExprOr.
    def exitColumnExprOr(self, ctx:ClickHouseParser.ColumnExprOrContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#ColumnExprPrecedence1.
    def enterColumnExprPrecedence1(self, ctx:ClickHouseParser.ColumnExprPrecedence1Context):
        pass

    # Exit a parse tree produced by ClickHouseParser#ColumnExprPrecedence1.
    def exitColumnExprPrecedence1(self, ctx:ClickHouseParser.ColumnExprPrecedence1Context):
        pass


    # Enter a parse tree produced by ClickHouseParser#ColumnExprPrecedence2.
    def enterColumnExprPrecedence2(self, ctx:ClickHouseParser.ColumnExprPrecedence2Context):
        pass

    # Exit a parse tree produced by ClickHouseParser#ColumnExprPrecedence2.
    def exitColumnExprPrecedence2(self, ctx:ClickHouseParser.ColumnExprPrecedence2Context):
        pass


    # Enter a parse tree produced by ClickHouseParser#ColumnExprPrecedence3.
    def enterColumnExprPrecedence3(self, ctx:ClickHouseParser.ColumnExprPrecedence3Context):
        pass

    # Exit a parse tree produced by ClickHouseParser#ColumnExprPrecedence3.
    def exitColumnExprPrecedence3(self, ctx:ClickHouseParser.ColumnExprPrecedence3Context):
        pass


    # Enter a parse tree produced by ClickHouseParser#ColumnExprInterval.
    def enterColumnExprInterval(self, ctx:ClickHouseParser.ColumnExprIntervalContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#ColumnExprInterval.
    def exitColumnExprInterval(self, ctx:ClickHouseParser.ColumnExprIntervalContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#ColumnExprIsNull.
    def enterColumnExprIsNull(self, ctx:ClickHouseParser.ColumnExprIsNullContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#ColumnExprIsNull.
    def exitColumnExprIsNull(self, ctx:ClickHouseParser.ColumnExprIsNullContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#ColumnExprWinFunctionTarget.
    def enterColumnExprWinFunctionTarget(self, ctx:ClickHouseParser.ColumnExprWinFunctionTargetContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#ColumnExprWinFunctionTarget.
    def exitColumnExprWinFunctionTarget(self, ctx:ClickHouseParser.ColumnExprWinFunctionTargetContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#ColumnExprTrim.
    def enterColumnExprTrim(self, ctx:ClickHouseParser.ColumnExprTrimContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#ColumnExprTrim.
    def exitColumnExprTrim(self, ctx:ClickHouseParser.ColumnExprTrimContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#ColumnExprTuple.
    def enterColumnExprTuple(self, ctx:ClickHouseParser.ColumnExprTupleContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#ColumnExprTuple.
    def exitColumnExprTuple(self, ctx:ClickHouseParser.ColumnExprTupleContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#ColumnExprArrayAccess.
    def enterColumnExprArrayAccess(self, ctx:ClickHouseParser.ColumnExprArrayAccessContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#ColumnExprArrayAccess.
    def exitColumnExprArrayAccess(self, ctx:ClickHouseParser.ColumnExprArrayAccessContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#ColumnExprBetween.
    def enterColumnExprBetween(self, ctx:ClickHouseParser.ColumnExprBetweenContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#ColumnExprBetween.
    def exitColumnExprBetween(self, ctx:ClickHouseParser.ColumnExprBetweenContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#ColumnExprParens.
    def enterColumnExprParens(self, ctx:ClickHouseParser.ColumnExprParensContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#ColumnExprParens.
    def exitColumnExprParens(self, ctx:ClickHouseParser.ColumnExprParensContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#ColumnExprTimestamp.
    def enterColumnExprTimestamp(self, ctx:ClickHouseParser.ColumnExprTimestampContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#ColumnExprTimestamp.
    def exitColumnExprTimestamp(self, ctx:ClickHouseParser.ColumnExprTimestampContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#ColumnExprAnd.
    def enterColumnExprAnd(self, ctx:ClickHouseParser.ColumnExprAndContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#ColumnExprAnd.
    def exitColumnExprAnd(self, ctx:ClickHouseParser.ColumnExprAndContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#ColumnExprTupleAccess.
    def enterColumnExprTupleAccess(self, ctx:ClickHouseParser.ColumnExprTupleAccessContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#ColumnExprTupleAccess.
    def exitColumnExprTupleAccess(self, ctx:ClickHouseParser.ColumnExprTupleAccessContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#ColumnExprCase.
    def enterColumnExprCase(self, ctx:ClickHouseParser.ColumnExprCaseContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#ColumnExprCase.
    def exitColumnExprCase(self, ctx:ClickHouseParser.ColumnExprCaseContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#ColumnExprDate.
    def enterColumnExprDate(self, ctx:ClickHouseParser.ColumnExprDateContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#ColumnExprDate.
    def exitColumnExprDate(self, ctx:ClickHouseParser.ColumnExprDateContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#ColumnExprNot.
    def enterColumnExprNot(self, ctx:ClickHouseParser.ColumnExprNotContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#ColumnExprNot.
    def exitColumnExprNot(self, ctx:ClickHouseParser.ColumnExprNotContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#ColumnExprWinFunction.
    def enterColumnExprWinFunction(self, ctx:ClickHouseParser.ColumnExprWinFunctionContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#ColumnExprWinFunction.
    def exitColumnExprWinFunction(self, ctx:ClickHouseParser.ColumnExprWinFunctionContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#ColumnExprIdentifier.
    def enterColumnExprIdentifier(self, ctx:ClickHouseParser.ColumnExprIdentifierContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#ColumnExprIdentifier.
    def exitColumnExprIdentifier(self, ctx:ClickHouseParser.ColumnExprIdentifierContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#ColumnExprFunction.
    def enterColumnExprFunction(self, ctx:ClickHouseParser.ColumnExprFunctionContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#ColumnExprFunction.
    def exitColumnExprFunction(self, ctx:ClickHouseParser.ColumnExprFunctionContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#ColumnExprAsterisk.
    def enterColumnExprAsterisk(self, ctx:ClickHouseParser.ColumnExprAsteriskContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#ColumnExprAsterisk.
    def exitColumnExprAsterisk(self, ctx:ClickHouseParser.ColumnExprAsteriskContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#columnArgList.
    def enterColumnArgList(self, ctx:ClickHouseParser.ColumnArgListContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#columnArgList.
    def exitColumnArgList(self, ctx:ClickHouseParser.ColumnArgListContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#columnArgExpr.
    def enterColumnArgExpr(self, ctx:ClickHouseParser.ColumnArgExprContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#columnArgExpr.
    def exitColumnArgExpr(self, ctx:ClickHouseParser.ColumnArgExprContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#columnLambdaExpr.
    def enterColumnLambdaExpr(self, ctx:ClickHouseParser.ColumnLambdaExprContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#columnLambdaExpr.
    def exitColumnLambdaExpr(self, ctx:ClickHouseParser.ColumnLambdaExprContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#columnIdentifier.
    def enterColumnIdentifier(self, ctx:ClickHouseParser.ColumnIdentifierContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#columnIdentifier.
    def exitColumnIdentifier(self, ctx:ClickHouseParser.ColumnIdentifierContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#nestedIdentifier.
    def enterNestedIdentifier(self, ctx:ClickHouseParser.NestedIdentifierContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#nestedIdentifier.
    def exitNestedIdentifier(self, ctx:ClickHouseParser.NestedIdentifierContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#TableExprIdentifier.
    def enterTableExprIdentifier(self, ctx:ClickHouseParser.TableExprIdentifierContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#TableExprIdentifier.
    def exitTableExprIdentifier(self, ctx:ClickHouseParser.TableExprIdentifierContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#TableExprSubquery.
    def enterTableExprSubquery(self, ctx:ClickHouseParser.TableExprSubqueryContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#TableExprSubquery.
    def exitTableExprSubquery(self, ctx:ClickHouseParser.TableExprSubqueryContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#TableExprAlias.
    def enterTableExprAlias(self, ctx:ClickHouseParser.TableExprAliasContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#TableExprAlias.
    def exitTableExprAlias(self, ctx:ClickHouseParser.TableExprAliasContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#TableExprFunction.
    def enterTableExprFunction(self, ctx:ClickHouseParser.TableExprFunctionContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#TableExprFunction.
    def exitTableExprFunction(self, ctx:ClickHouseParser.TableExprFunctionContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#tableFunctionExpr.
    def enterTableFunctionExpr(self, ctx:ClickHouseParser.TableFunctionExprContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#tableFunctionExpr.
    def exitTableFunctionExpr(self, ctx:ClickHouseParser.TableFunctionExprContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#tableIdentifier.
    def enterTableIdentifier(self, ctx:ClickHouseParser.TableIdentifierContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#tableIdentifier.
    def exitTableIdentifier(self, ctx:ClickHouseParser.TableIdentifierContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#tableArgList.
    def enterTableArgList(self, ctx:ClickHouseParser.TableArgListContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#tableArgList.
    def exitTableArgList(self, ctx:ClickHouseParser.TableArgListContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#tableArgExpr.
    def enterTableArgExpr(self, ctx:ClickHouseParser.TableArgExprContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#tableArgExpr.
    def exitTableArgExpr(self, ctx:ClickHouseParser.TableArgExprContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#databaseIdentifier.
    def enterDatabaseIdentifier(self, ctx:ClickHouseParser.DatabaseIdentifierContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#databaseIdentifier.
    def exitDatabaseIdentifier(self, ctx:ClickHouseParser.DatabaseIdentifierContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#floatingLiteral.
    def enterFloatingLiteral(self, ctx:ClickHouseParser.FloatingLiteralContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#floatingLiteral.
    def exitFloatingLiteral(self, ctx:ClickHouseParser.FloatingLiteralContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#numberLiteral.
    def enterNumberLiteral(self, ctx:ClickHouseParser.NumberLiteralContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#numberLiteral.
    def exitNumberLiteral(self, ctx:ClickHouseParser.NumberLiteralContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#literal.
    def enterLiteral(self, ctx:ClickHouseParser.LiteralContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#literal.
    def exitLiteral(self, ctx:ClickHouseParser.LiteralContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#interval.
    def enterInterval(self, ctx:ClickHouseParser.IntervalContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#interval.
    def exitInterval(self, ctx:ClickHouseParser.IntervalContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#keyword.
    def enterKeyword(self, ctx:ClickHouseParser.KeywordContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#keyword.
    def exitKeyword(self, ctx:ClickHouseParser.KeywordContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#keywordForAlias.
    def enterKeywordForAlias(self, ctx:ClickHouseParser.KeywordForAliasContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#keywordForAlias.
    def exitKeywordForAlias(self, ctx:ClickHouseParser.KeywordForAliasContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#alias.
    def enterAlias(self, ctx:ClickHouseParser.AliasContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#alias.
    def exitAlias(self, ctx:ClickHouseParser.AliasContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#identifier.
    def enterIdentifier(self, ctx:ClickHouseParser.IdentifierContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#identifier.
    def exitIdentifier(self, ctx:ClickHouseParser.IdentifierContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#identifierOrNull.
    def enterIdentifierOrNull(self, ctx:ClickHouseParser.IdentifierOrNullContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#identifierOrNull.
    def exitIdentifierOrNull(self, ctx:ClickHouseParser.IdentifierOrNullContext):
        pass


    # Enter a parse tree produced by ClickHouseParser#enumValue.
    def enterEnumValue(self, ctx:ClickHouseParser.EnumValueContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#enumValue.
    def exitEnumValue(self, ctx:ClickHouseParser.EnumValueContext):
        pass



del ClickHouseParser