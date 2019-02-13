<script type="text/javascript">
      var dataString = null;
      function csrfSafeMethod(method) {
            // these HTTP methods do not require CSRF protection
            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
      };  
      function make_ajax(dataString,url,method){
        var csrftoken = $.cookie('csrftoken');
        $.ajaxSetup({
              beforeSend: function(xhr, settings) {
              if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
                xhr.setRequestHeader("Content-Type", 'application/json')
                }
              }
            });
        $.ajax({
              type: method,
              url: url,
              data: dataString,
              success: function (data) {
                alert("Ajax call made successfully "+data);
                location.reload()
              },
              error: function (xhr, textStatus, errorThrown) {
              alert(errorThrown);
              }
           });
          $(document).ajaxStop(function(){
            window.location.reload();
          });
      }
      function Clear_inputs(){
        $('.ipt').val('');
        return 1;
      };

      function Validate_inputs(i){
        console.log(i)
        if (i==1){
          $('.ipt').each(function() {
          if(!$(this).val()){
              alert($(this).val())
              alert('Some fields are empty, Please Fill all the fields');
              return false;
          }
          });
          }
          else if (i==2){
            if(!$('#Name').val() && !$('#Btch').val()){
              alert('Name and Batch are empty, Please Fill the fields to update');
              return false;
            }
          }
          return true;
      };
      function Add_inputs(){
        if (Validate_inputs(1)){    
            dataString = JSON.stringify({
                'Name': $('#Name').val(),
                'Desc': $('#Dsc').val(),
                'Packaging': $('#Pck').val(),
                'HSN': $('#Hsnc').val(),
                'Batch': $('#Btch').val(),
                'Exp': $('#Exp').val(),
                'qty': $('#qty').val(),
                'gst': $('#gst').val(),
              }); 
            make_ajax(dataString,'ajax/add_inventory/','POST');
          }
        };
      function Delete_inputs(){
        if(Validate_inputs(2)){
          dataString = JSON.stringify({
            'Name': $('#Name').val(),
            'Batch': $('#Btch').val(),
          });
          make_ajax(dataString,'ajax/delete_inventory/','POST');
          }
        };
        function Search_inputs(){
          if (Validate_inputs(2)){
             dataString = JSON.stringify({
            'Name': $('#Name').val(),
            'Batch': $('#Btch').val(),
          });
          make_ajax(dataString,'ajax/search_inventory/','GET');
          }
        };
      </script>