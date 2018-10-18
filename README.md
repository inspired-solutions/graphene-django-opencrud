# OpenCrud Graphene Django implementation

## Usage

```python
import graphene
from graphene_django.types import DjangoObjectType

from django.contrib.auth import models as auth_models
from graphene import Node

from opencrud.connection import WithOpenCrudConnection
from opencrud.list import OpenCrudDjangoFilterListField
from opencrud.filter import OpenCrudDjangoFilterConnectionField
from opencrud.field import OpenCrudDjangoField


class User(DjangoObjectType):
    @WithOpenCrudConnection(auth_models.User)
    class Meta:
        filter_fields = ('id', 'email', )
        interfaces = (Node, )


class Query(graphene.ObjectType):
    user = OpenCrudDjangoField(User)
    users = OpenCrudDjangoFilterListField(User)
    users_connection = OpenCrudDjangoFilterConnectionField(User)
```

## Contributing

After cloning this repo, ensure dependencies are installed by running:

```sh
pip install -e ".[test]"
```

After developing, the full test suite can be evaluated by running:

```sh
py.test opencrud --cov=opencrud # Use -v -s for verbose mode
```
