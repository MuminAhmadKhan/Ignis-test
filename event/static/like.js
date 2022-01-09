document.addEventListener('DOMContentLoaded', function() {
    
    // Use buttons to toggle between views

    document.querySelectorAll("#heart").forEach(button=>button.onclick=like)
    
 } );
 function like(){
    

    if($(this).hasClass("liked")){
        $(this).html('<i class="fa fa-heart-o" aria-hidden="true"></i>');
        $(this).removeClass("liked");
        is_liked=false
        p_id=$(this).siblings('#id').text()
        
      }else{
        $(this).html('<i class="fa fa-heart" aria-hidden="true"></i>');
        $(this).addClass("liked");
        is_liked=true
        p_id=$(this).siblings('#id').text()
      }
      
      fetch(`/like`, {
        method: 'PUT',
        body: JSON.stringify({
            p_id:p_id,
            is_liked:is_liked,
             })
             
      
      })
      

    }



      