import graphene
from crm.schema import Query as CRMQuery, Mutation as CRMMutation


class CRMQuery(graphene.ObjectType):
    hello = graphene.String(default_value="Hello, GraphQL!")


class Query(CRMQuery, graphene.ObjectType):
    pass


class Mutation(CRMMutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)