var model = {
            photos: ko.observableArray([]),
            
            onDeptClick: function(dept) {
                model.students.removeAll();
                model.selectedDept(dept);
                model.selectedCourse(undefined);
                model.selectedGroup(undefined);
                model.groups(model.selectedDept().groups());
                model.courses(model.selectedDept().courses());
            },
            
            saveClicked: function() {
                $.ajax({
                    url: '/update',
                    type: 'POST',
                    dataType: 'json',
                    data: {
                        ormdata: JSON.stringify(pony.getChanges())
                    },
                    success: function() {
                        location.reload();
                    }
                })
            },
            cancelClicked: function() {
                location.reload();
            }
        };
        var getData = function(url, func) {
            $.ajax({
                url: url,
                dataType: 'json',
                success: function(json) {
                    var data = pony.unmarshalData(json);
                    func(data);
                }
            })
        };
        $().ready(function() {
     getData('/photos', function(data) {
        console.log(data);
         model.photos(data);
     });
     $.getJSON('/photos', function (data) {
         console.log('json', data)
     })
     ko.applyBindings(model);
 });