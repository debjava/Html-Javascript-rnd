<HTML>
<HEAD>
<TITLE>Unit Testing for Auriga Card Interface - Debadatta Mishra</TITLE>

<SCRIPT LANGUAGE="JavaScript">

var xmlhttp; 

function loadXMLDoc(url) 
{ 
    xmlhttp=null; 
	if (window.XMLHttpRequest) 
	 {// code for all new browsers 
		  xmlhttp=new XMLHttpRequest(); 
	 } 
	else if (window.ActiveXObject) 
	{// code for IE5 and IE6 
		  xmlhttp=new ActiveXObject("Microsoft.XMLHTTP"); 
	} 
	if (xmlhttp!=null) 
	{ 
		  xmlhttp.onreadystatechange=state_Change; 
		  xmlhttp.open("GET",url,true); 
		  xmlhttp.send(null); 
	} 
	else 
	{ 
		  alert("Your browser does not support XMLHTTP."); 
	} 
} 
 
function state_Change() 
{ 
    if (xmlhttp.readyState==4) 
    {// 4 = "loaded" 
          if (xmlhttp.status==200) 
          {
			//Do something
			//alert();
		  }
    } 
	else 
    { 
       
    } 
} 

function invokePosDevice()
{
	var refNoValue = document.getElementById('refNoTxtId').value;
	var amtValue = document.getElementById('amtTxtId').value;		
	var radioLength = document.atcTestForm.Payment.length;
	var paymentType;
	for( var i = 0 ; i < radioLength ; i++ )
	{
		if( document.atcTestForm.Payment[i].checked )
			paymentType = document.atcTestForm.Payment[i].value;
	}
	var url = "http://localhost:1080/devices/referenceno="+refNoValue+"&amount="+amtValue+"&paymentType="+paymentType;
	//alert(paymentType);	
	//alert("URL->"+url);
	loadXMLDoc(url) 
}
</SCRIPT>

</HEAD>

<BODY>

<form name="atcTestForm">

	<H2>This is a Simulated Application to test Auriga Card Interaction in ESA Workflow.</H2>
	<H3>Enter the following information and press submit.</H3>

	<table>
		<tr>
			<td>
				<fieldset style="width:260px">
				<legend>Transaction Type(Payment or Refund)</legend>
				<input type="radio" name="Payment" value="P" id="pmtId" CHECKED>Payment<br/>
				<input type="radio" name="Payment" value="R" id="rfndId">Refund<br/>
			</fieldset>
			</td>
		</tr>
	</table>

	<TABLE>
	<TR>
		<TD>Enter Reference Number : </TD>
		<TD><input type="Text" name="refNoText" value="REF1234" id="refNoTxtId"></TD>
		<TD>&nbsp;</TD>
	</TR>
	<TR>
		<TD>Enter Amount : </TD>
		<TD><input type="Text" name="amtText" value="5555" id="amtTxtId"></TD>
		<TD>&nbsp;</TD>
	</TR>
	<TR>
		<TD>&nbsp;</TD>
		<TD><input type="Button" value="Invoke POS" id="posBtnId" onClick="invokePosDevice();"></TD>
		<TD></TD>
	</TR>
	</TABLE>

</form>

</BODY>
</HTML>
