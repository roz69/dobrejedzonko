<script lang="ts">
	 import { enhance } from '$app/forms';
	 import type { PageData } from '../$types';
	 export let data: PageData;
	
	
</script>


<!-- {#if data.user}
	<pre>
		{JSON.stringify(data.user, null, 2)}
	</pre>
	<form use:enhance method="post">
		<input type="submit" class="button" value="Sign out" />
	</form>
{/if} -->
<body class="tlo" >
	<div class="header">
		<section class="wrapper">
			<a href="/">
				<div class="top">Dobre Jedzonko</div>
			</a>
		</section>
	</div>
	<input type="checkbox" class="openSidebarMenu" id="openSidebarMenu">
	<label for="openSidebarMenu" class="sidebarIconToggle">
		<div class="spinner diagonal part-1"></div>
		<div class="spinner horizontal"></div>
		<div class="spinner diagonal part-2"></div>
	</label>
	<div id="sidebarMenu">
		<ul class="sidebarMenuInner">
			<li><a href="/"> DOBRE JEDZONKO<span>Pyszne przepisy</span></a></li>
			<li> <a href="https://pl.wikipedia.org/wiki/Pornhub" target="_blank">Sponsor</a><span>PornHUB &copy;</span></li>
			{#if !data.user}
				<li><a href="/login">LOGOWANIE</a></li>
				<li><a href="/login">LOGOWANIE</a></li>
				<li><a href="/login">LOGOWANIE</a></li>
				<li><a href="/login">LOGOWANIE</a></li>
				<li><a href="/login">LOGOWANIE</a></li>
				<li><a href="/login">LOGOWANIE</a></li>
				<li><a href="/login">LOGOWANIE</a></li>
			{/if}
			{#if data.user}
				<li>ZALOGOWANO</li>
				<li>ZALOGOWANO</li>
				<li>ZALOGOWANO</li>
				<li>ZALOGOWANO</li>
				<li>ZALOGOWANO</li>
				<li>ZALOGOWANO</li>
				<li>ZALOGOWANO</li>
			{/if}
	
		</ul>
	</div>
	
	
	<div id="sidebarMenu2">
		<ul class="sidebarMenuInner2">
			<form class="przepis-form" method="post">
				<h1>Dodaj przepis</h1>
				<div class="form-input-material">
					<label for="nazwa">Nazwa</label> <br>
				<input type="text" name="nazwa" id="nazwa" placeholder=" " autocomplete="off" class="form-control-material" required/>
				</div>
				<div class="form-input-material">
					<label for="opis">Opis</label><br>
				<input type="text" name="opis" id="opis" placeholder=" " autocomplete="off" class="form-control-material" required />
				</div>
				<div class="form-input-material">
					<label for="czas">Czas przygotowania</label><br>
				<input type="number" name="czas" id="czas" placeholder=" " autocomplete="off" class="form-control-material" required/>
				</div>
				 <div class="form-input-material-zdj">
					<label for="zdj">Link do zdjęcia</label><br>
				<input id="zdj" type="text" name="zdj"  placeholder=" " autocomplete="off" class="form-control-material" />
				</div>
				<button type="submit" class="btn btn-primary btn-ghost">Dodaj przepis <br>
					{#if !data.user}
						(wymaga logowania)
					{/if}
				</button>
				{#if data.user}
					ZALOGOWANY <br>
					Użytkownik: {data.user.username}
				{/if}
			</form>
	
		</ul>
	</div>
	
	
	<div class="kwadracik">
		<div class="flexx">
			<div class="glowne22">
				<img src={data.przepis.image} alt="BRAK ZDJĘCIA PRZEPISU" class="glowne23">
			</div>          
					 <div class="prawo">
							<div class="prawocontainer">   
									<div id="nazwatytul">
										{data.przepis.name}
									</div>
									<div class="timer">
										<svg  xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-clock-filled" width="30" height="30" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round" >
											<path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
											<path d="M17 3.34a10 10 0 1 1 -14.995 8.984l-.005 -.324l.005 -.324a10 10 0 0 1 14.995 -8.336zm-5 2.66a1 1 0 0 0 -.993 .883l-.007 .117v5l.009 .131a1 1 0 0 0 .197 .477l.087 .1l3 3l.094 .082a1 1 0 0 0 1.226 0l.094 -.083l.083 -.094a1 1 0 0 0 0 -1.226l-.083 -.094l-2.707 -2.708v-4.585l-.007 -.117a1 1 0 0 0 -.993 -.883z" stroke-width="0" fill="currentColor"></path>
										  </svg>    {data.przepis.time}MIN.
									</div>
							</div>
							   <div class="opiss">
								   {data.przepis.description}
							   </div>
						</div>
		</div>
	</div>
	
	
	
</body> 





    

  





			
<footer>
&copy; Dobre Jedzonko.
</footer>
