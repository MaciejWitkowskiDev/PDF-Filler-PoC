
<script>
	let file;
	let year = 2021;
	let krs = "9898989898";
	let cel = "PxTest2021";
	let url = `https://px-website-test-01.pitax.pl/system-2020/pdfgenerator/generate.php`
	
</script>

<form>
    <select bind:value={file} name="file" id="fileselect">
    <option value="PIT-OP">PIT-OP</option>
    <option value="PIT-WZR-L">PIT-WZR-L</option>
    <option value="PIT-28">PIT-28</option>
    <option value="PIT-38-L">PIT-38-L</option>
    <option value="PIT-WZ-L">PIT-WZ-L</option>
    <option value="PIT-D-L">PIT-D-L</option>
    <option value="PIT-D">PIT-D</option>
    <option value="PIT-28B-L">PIT-28B-L</option>
    <option value="PIT-IP-L">PIT-IP-L</option>
    <option value="PIT-39-L">PIT-39-L</option>
    <option value="PIT-28-L">PIT-28-L</option>
    <option value="PIT-38">PIT-38</option>
    <option value="PIT-36L-L">PIT-36L-L</option>
    <option value="PIT-NZ">PIT-NZ</option>
    <option value="PIT-36-L">PIT-36-L</option>
    <option value="PIT-PM">PIT-PM</option>
    <option value="PIT-OP-L">PIT-OP-L</option>
    <option value="PIT-ZG-L">PIT-ZG-L</option>
    <option value="PIT-MIT">PIT-MIT</option>
    <option value="PIT-WZR">PIT-WZR</option>
    <option value="PIT-WZ">PIT-WZ</option>
    <option value="PIT-ZG">PIT-ZG</option>
    <option value="PIT-B">PIT-B</option>
    <option value="PIT-PM-L">PIT-PM-L</option>
    <option value="PIT-NZI">PIT-NZI</option>
    <option value="PIT-37-L">PIT-37-L</option>
    <option value="PIT-IP">PIT-IP</option>
    <option value="PIT-M">PIT-M</option>
    <option value="PIT-DS-L">PIT-DS-L</option>
    <option value="PIT-2K">PIT-2K</option>
    <option value="PIT-DS">PIT-DS</option>
    <option value="PIT-BR-L">PIT-BR-L</option>
    <option value="PIT-Z-L">PIT-Z-L</option>
    <option value="PIT-O-L">PIT-O-L</option>
    <option value="PIT-O">PIT-O</option>
    <option value="PIT-36L">PIT-36L</option>
    <option value="PIT-39">PIT-39</option>
    <option value="PIT-SE">PIT-SE</option>
    <option value="PIT-Z">PIT-Z</option>
    <option value="PIT-B-L">PIT-B-L</option>
    <option value="PIT-28B">PIT-28B</option>
    <option value="PIT-NZ-L">PIT-NZ-L</option>
    <option value="PIT-36">PIT-36</option>
    <option value="PIT-BR">PIT-BR</option>
    <option value="PIT-2K-L">PIT-2K-L</option>
    <option value="PIT-M-L">PIT-M-L</option>
    <option value="PIT-MIT-L">PIT-MIT-L</option>
    <option value="PIT-NZI-L">PIT-NZI-L</option>
    <option value="PIT-SE-L">PIT-SE-L</option>
    <option value="PIT-37">PIT-37</option>
</select><br>
<label for="text-1637145993777">rok</label>
<input bind:value={year} type="text" name="text-1637145993777" id="text-1637145993777"><br>
<label for="text-1637145994869" >krs</label>
<input bind:value={krs} type="text" name="text-1637145994869" id="text-1637145994869"><br>
<label for="text-1637145996030">cel</label>
<input bind:value={cel} type="text" name="text-1637145996030" id="text-1637145996030"><br>
</form><br><br>


{#if (file == "PIT-37" || file == "PIT-28" || file == "PIT-36" || file == "PIT-36L" || file == "PIT-38" || file == "PIT-39" || file == "PIT-OP") }
	<a href="{url}?file={file}&year={year}&krs={krs}&cel={cel}">{url}?file={file}&year={year}&krs={krs}&cel={encodeURIComponent(cel)}</a>
{:else}
	<a href="{url}?file={file}&year={year}">{url}?file={file}&year={year}</a>
{/if}