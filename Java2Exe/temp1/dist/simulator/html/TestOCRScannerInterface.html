<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
    <head>
        <title>Giro slip display</title>
    </head>
    <script language="JavaScript">
    	
        function getXmlHttpRequest()
		{
			var xmlhttp;
            if (window.XMLHttpRequest) 
			{
				// code for IE7+, Firefox, Chrome, Opera, Safari
                xmlhttp = new XMLHttpRequest();
            }
            else 
			{
				// code for IE6, IE5
                xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
            }
            return xmlhttp;
        }
		
		function processAjaxRequest()
		{
			var timestamp = new Date();
			var ajaxReq = getXmlHttpRequest();
			//alert(dateNTime);
			ajaxReq.onreadystatechange=function()
			{
				if (ajaxReq.readyState==4 && ajaxReq.status==200)
    			{
					var textData = ajaxReq.responseText;
					var xmlTagName = ajaxReq.responseXML.documentElement.tagName;
					var giroNo = ajaxReq.responseXML.documentElement.getElementsByTagName("GiroNo")[0].text;
					var ocrNo = ajaxReq.responseXML.documentElement.getElementsByTagName("OcrNo")[0].text
					var amount = ajaxReq.responseXML.documentElement.getElementsByTagName("Belopp")[0].text
					var errMsg = ajaxReq.responseXML.documentElement.getElementsByTagName("ErrorMsg")[0].text
					if( errMsg == "" )
					{
						document.getElementById("giroId").value=giroNo;
						document.getElementById("ocrId").value=ocrNo;
						document.getElementById("amtId").value=amount;
					}
					else
					{
						alert(errMsg);
					}
					
    			}
			}
			ajaxReq.open("GET","http://localhost:1080/devices/ocr?timestamp="+ timestamp.getTime(),true);
			//ajaxReq.open("GET","testfiles/test1.xml",true);
			ajaxReq.send();

		}
		
		function ajaxTest()
		{
			var ajaxXml = getXmlHttpRequest();
			processAjaxRequest();
			
		}
    </script>
    <body>
	<table>
		<tr>
			<td>GIRO NO :</td>
			<td>
				<input type="text" value="" id="giroId" name="girotext">
			</td>
		</tr>
		<tr>
			<td>OCR NO :</td>
			<td>
				<input type="text" value="" id="ocrId" name="ocrtext">
			</td>
		</tr>
		<tr>
			<td>AMOUNT :</td>
			<td>
				<input type="text" value="" id="amtId" name="amttext">
			</td>
		</tr>
		
	</table>
		
    	<button type="button" onclick="ajaxTest()">Scan</button>

    </body>
</html>
