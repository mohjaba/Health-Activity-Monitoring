<?php

	exec("python ./python/lead.py",$out1);	
	echo json_encode($out1);

?> 
