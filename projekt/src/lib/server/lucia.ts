import lucia from 'lucia-auth';
import { sveltekit } from 'lucia-auth/middleware';
import prisma from '@lucia-auth/adapter-prisma';
import { dev } from '$app/environment';
import { PrismaClient } from '@prisma/client';

import { discord } from '@lucia-auth/oauth/providers';
import { DISCORD_CLIENT_ID, DISCORD_CLIENT_SECRET } from '$env/static/private';

export const auth = lucia({
	adapter: prisma(new PrismaClient()),
	env: dev ? 'DEV' : 'PROD',
	transformDatabaseUser: (userData) => {
		return {
			userId: userData.id,
			username: userData.username
		};
	},
	middleware: sveltekit()
});

export const discordAuth = discord(auth, {
	clientId: DISCORD_CLIENT_ID,
	clientSecret: DISCORD_CLIENT_SECRET,
	redirectUri: 'http://localhost:5173/api/oauth/discord/'
});

export type Auth = typeof auth;
