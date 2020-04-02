// JavaScript Document
var ws;
function login(){
	if(!ws){
		try{
			ws=new WebSocket("ws://127.0.0.1:24258");
			ws.onopen=function(event){
				var uer=document.getElementById("user_info").getElementsByTagName("li")[0].innerHTML;
				ws.send(uer);
				//console.log("true");
			}
			ws.onmessage=function(event){
				//console.log("get:"+event.data);
				var strs= new Array();
				strs=event.data.split(":&*");
				var time=strs[0]
				var id=strs[1]
				var talk_name=strs[2]
				var data_id=strs[3]
				var data_info=strs[4]
				var message_type=strs[5]
				//alert(message_type)
				if(message_type == "message"){
					var head="<dl class=\"talk  setton-2x\" time=\""+time+"\"id=\""+id+"\"><dt class=\"dropdown\"><div class=\"avatar avatar-setton-2x\"><span>server<\/span><\/div><div data-toggle=\"dropdown\" class=\"name\"><span class=\"select-text\">"+talk_name+"<\/span><\/div><ul class=\"dropdown-menu\" role=\"menu\" data-id=\""+data_id+"\" data-icon=\"setton-2x\" data-name=\""+talk_name+"\"><\/ul><\/dt><dd><div class=\"bubble\"><p class=\"body select-text\">"
					document.getElementById("talks").innerHTML = head+data_info+"<\/p><\/div><\/dd><\/dl>"+document.getElementById("talks").innerHTML;
				}
				if(message_type == "join"){
					var g_data="<div class=\"talk system\" time=\""+time+"\" id=\""+id+"\" >►► "+talk_name+" 加入房间 <\/div>"
					document.getElementById("talks").innerHTML = g_data+document.getElementById("talks").innerHTML;
				}
				if(message_type == "exit"){
					var g_data="<div class=\"talk system\" time=\""+time+"\" id=\""+id+"\" >►► "+talk_name+" 退出房间 <\/div>"
					document.getElementById("talks").innerHTML = g_data+document.getElementById("talks").innerHTML;
				}
			}
			ws.onclose=function(event){
				//console.log("close");
			}
			ws.onerror=function(event){
				//console.log("error");
			}
		}catch(ex){
			alert(ex.message);
		}
	}else{
		ws.close();
		ws=null;
	}
}
function SendData() {
	var data = document.getElementById("sendmessage").value;
    try {
		var uer=document.getElementById("user_info").getElementsByTagName("li")[0].innerHTML;
       	ws.send(uer+":"+data);
        } catch (ex) {
        alert(ex.message);
        }
};