


$(function(){

	$(".image-upload > input").hide();
});
$("#photo").change(function(){
	var files = this.files;
	for( var i=0; i<files.length; i++ ){
		var imgtype = files[i].type;
		if( imgtype=="image/jpeg" || imgtype=="image/gif" || imgtype=="image/png" ) readFile(files[i]); 
	}

});

function readFile(file){
	if( ! file ) return;
	var reader = new FileReader();
	reader.onload = function(event){
		var src = event.target.result;
		var img = new Image();

		
		var html = "<img src='" + src + "' width='100%;' height='200px' style=' position:absolute;'>";

		$("#image-upload-img").html(html);

	}
	reader.readAsDataURL(file);
}

