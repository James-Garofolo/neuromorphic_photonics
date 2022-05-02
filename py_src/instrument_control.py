import visa

resources = visa.ResourceManager('@py')
resources.list_resources()