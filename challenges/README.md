# Adding new contracts
1. Put the contract in a .sol file in this directory (name must be ##_Name.ending)
2. Create a JSON file describing the contract, copy & modify one that already exists
3. Create a Python file which checks whether the contract has been hacked (copy & modify)

## Writing a validator
A minimal validator looks like this:
```python
import validator

class ValidatorImpl(validator.Validator):
    def perform_validation(self):
            self.set_hacked()
```
The class **must** be called `ValidatorImpl`, **must** extend `Validator` and **must** implement the `perform_validation` method.
`perform_validation` **must** call either `set_hacked` or `set_not_hacked`.

## Writing a JSON descriptor
A JSON descriptor looks like this:
```json
{
    "name" : "Test",
    "description" : "A test.",
    "level" : "3",
    "on_deploy": [{
        "method": "deposit",
        "value": "50000000000000000"
    }]
}
```

| Key           | Description                                         | Required |
| ------------- |-----------------------------------------------------|----------|
| name          | The name that will be displayed on the website      | [x]      |
| description   | The description to show on the website              | [x]      |
| level         | Difficulty on a scale of 1 to 10                    | [x]      |
| on_deploy     | An array of actions to be executed after deployment | [ ]      |
| method        | The action to take. Currently only deposit          | [ ]      |
| value         | Parameter for method                                | [ ]      |