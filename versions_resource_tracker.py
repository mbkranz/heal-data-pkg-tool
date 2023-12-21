# step 1: add new fields, delete deprecated fields, rename fields 

# for each schema property:

# if deprecated is true
#   delete any field with current or former field name(s)
# if deprecated is false
#   if field with current field name exists
#       leave field with current field name alone
#       delete any field with a former field name
#   if field with current field name does not exist
#       if former field name(s)
#           if field with former field name exists
#               copy field with former field name and rename to current field name
#           if field with former field name does not exist
#               create new field with current field name
#       if no former field name(s)
#           create new field with current field name
#
# after looping through all schema properties with above,
# for all schema properties where deprecated is False, collect all former field names,
# and delete any fields with a former field name

# step 2: update enums

# for each (non-deprecated) schema property:

# if mapEnums is not empty
#   if enum value is in keys of mapEnums
#       replace enum value with value specified by corresponding key of mapEnums
#   if enum value is not in keys of mapEnums
#       replace enum value with empty/null
# if mapEnums is empty
#   do nothing

# step 3: update subfield names

# for each (non-deprecated) schema property:

# if formerSubNames is not empty
#   if value is a list of dictionaries
#       replace keys in list of dictionaries according to the mapping in formerSubNames
#       (https://stackoverflow.com/questions/54637847/how-to-change-dictionary-keys-in-a-list-of-dictionaries)




fieldNameMap = {
    "latestVersion":"0.3.0",
    "properties":{
        "schemaVersionField":{
            "formerNames": [],
            "deprecated": False
        },
        "resourceId":{
            "formerNames": ["resource.id"],
            "deprecated": False
        },
        "path":{
            "formerNames":[],
            "deprecated": False
        },
        "description":{
            "formerNames":[],
            "deprecated": False
        },
        "category":{
            "formerNames":[],
            "deprecated": False,
            "mapEnum": {
                "publication":["multi-result"],
                "result":["single-result"]
            }
        },
        "expBelongsTo":{
            "formerNames": ["exp.belongs.to"],
            "deprecated": True
        },
        "experimentNameBelongsTo":{
            "formerNames": [],
            "deprecated": False
        },
        "name":{
            "formerNames": [],
            "deprecated": False
        },
        "title":{
            "formerNames": [],
            "deprecated": False
        },
        "descriptionFileNameConvention":{
            "formerNames": ["description.file.name.convention"],
            "deprecated": False
        },
        "descriptionFile":{
            "formerNames": ["description.file"],
            "deprecated": False
        },    
        "descriptionRow":{
            "formerNames": ["description.row"],
            "deprecated": False
        },
        "categorySubMetadata":{
            "formerNames": ["category.sub.metadata"],
            "deprecated": False,
            "deleteEnum": ["heal-formatted-experiment-tracker"]
        },
        "categorySubMetadataOther":{
            "formerNames": [],
            "deprecated": False
        },
        "categorySubData":{
            "formerNames": ["category.sub.data"],
            "deprecated": False
        },
        "categorySubResults":{
            "formerNames": ["category.sub.results"],
            "deprecated": True
        },
        "categorySubResult":{
            "formerNames": ["categorySubSingleResult","categorySubResults","category.sub.results"],
            "deprecated": False,
            "mapEnum": {
                "single-panel-figure":["figure"]
            },
            "deleteEnum":["draft-publication","publication","report","white-paper","presentation","poster"]
        },
        "categorySubPublication":{
            "formerNames": ["categorySubMultiResult","categorySubResults","category.sub.results"],
            "deprecated": False,
            "mapEnum": {
                "peer-review-manuscript":["publication","draft-publication"]
            },
            "deleteEnum":["figure","table","text","draft-publication","publication"]
        },
        "associatedFileDataDict":{
            "formerNames": ["assoc.file.dd"],
            "deprecated": False
        },
        "associatedFileProtocol":{
            "formerNames": ["assoc.file.protocol"],
            "deprecated": False
        },
        "associatedFileResultsTracker":{
            "formerNames": ["assoc.file.result.tracker"],
            "deprecated": False
        },
        "associatedFileDependsOn":{
            "formerNames": ["assoc.file.depends.on"],
            "deprecated": False
        },
        "associatedFileResultsDependOn":{
            "formerNames": ["assoc.file.result.depends.on"],
            "deprecated": False,
            "formerSubNames": {
                "resultId":["result.id"],
                "resultIdDependsOn":["result.id.depends.on"]
            }
        },
        "associatedFileMultiLikeFiles":{
            "formerNames": ["assoc.file.multi.like.file"],
            "deprecated": False
        },
        "access":{
            "formerNames": [],
            "deprecated": False
        },
        "accessDate":{
            "formerNames": ["access.date"],
            "deprecated": False
        },
        "format":{
            "formerNames": [],
            "deprecated": False
        },
        "softwareUsed":{
            "formerNames": ["format.software"],
            "deprecated": False
        },
        "profile":{
            "formerNames": [],
            "deprecated": False
        },
        "mediatype":{
            "formerNames": [],
            "deprecated": False
        },
        "encoding":{
            "formerNames": [],
            "deprecated": False
        },
        "schema":{
            "formerNames": [],
            "deprecated": False
        },
        "resourceCreateDateTime":{
            "formerNames": ["resource.create.date.time"],
            "deprecated": False
        },
        "resourceModDateTime":{
            "formerNames": ["resource.mod.date.time"],
            "deprecated": False
        },
        "annotationCreateDateTime":{
            "formerNames": ["restrk.create.date.time"],
            "deprecated": False
        },
        "annotationModDateTime":{
            "formerNames": ["restrk.mod.date.time"],
            "deprecated": False
        },
        "resourceIdNumber":{
            "formerNames": ["resource.id.num"],
            "deprecated": False
        },
        "resourceModTimeStamp":{
            "formerNames": ["resource.mod.time.stamp"],
            "deprecated": False
        },
        "annotationModTimeStamp":{
            "formerNames": ["restrk.mod.time.stamp"],
            "deprecated": False
        }
    }
}