import graphene
from graphql_auth import mutations
from graphql_auth.schema import UserQuery, MeQuery

class AuthMutation(graphene.ObjectType):
   register = mutations.Register.Field()
   verify_account = mutations.VerifyAccount.Field()

class Query(UserQuery, MeQuery, graphene.ObjectType):
    pass

class Mutation(AuthMutation, graphene.ObjectType):
   pass

schema = graphene.Schema(query=Query, mutation=Mutation)

