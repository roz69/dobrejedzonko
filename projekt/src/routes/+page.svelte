<script lang="ts">
	import { enhance } from '$app/forms';
	import type { PageData } from './$types';

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
		<li>DOBRE JEDZONKO <span>Pyszne przepisy</span></li>
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
			<input type="text" name="nazwa" id="nazwa" placeholder=" " autocomplete="off" class="form-control-material" required />
			</div>
			<div class="form-input-material">
				<label for="opis">Opis</label><br>
			 <input type="text" name="opis" id="opis" placeholder=" " autocomplete="off" class="form-control-material" required /> 
			</div>
			<div class="form-input-material">
				<label for="czas">Czas przygotowania</label><br>
			<input type="number" name="czas" id="czas" placeholder="min" autocomplete="off" class="form-control-material" required />
			</div>
			 <div class="form-input-material-zdj">
				<label for="zdj">Link do zdjęcia</label><br>
			<input id="zdj" type="text" name="zdj"  placeholder="https:// " autocomplete="off" class="form-control-material" />
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


		
			<ul class="grid">
				{#each data.przepisy as przepis}
					<li>
						{#if !data.user}
							<h1>ZALOGUJ SIĘ</h1>
						{/if}
						{#if data.user}
					<a href="/przepis/{przepis.id}">
						<figure class="grid__figure">
							<img src={przepis.image} alt="">
							<figcaption><h2>{przepis.name}</h2></figcaption>
						</figure>
					</a>
					{/if}	
					</li>
					{/each}
			</ul>
<footer>
&copy; Dobre Jedzonko.
</footer>
