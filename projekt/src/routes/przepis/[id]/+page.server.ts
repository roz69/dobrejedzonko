import { redirect, type Actions, fail } from '@sveltejs/kit';
import { auth } from '$lib/server/lucia';
import { prisma } from '$lib/server/prisma';


export const load = async ({ locals, params }) => {
	const przepis = await prisma.przepis.findUnique({
        where: {
            id: Number(params.id)
        }
    });
    console.log(przepis) 
	const { user } = await locals.auth.validateUser();
	return {
		user,
		przepis
	};
};



export const actions: Actions = {
	// signout
	default: async ({ locals, request }) => {
		const session = await locals.auth.validate();
		if (!session) return fail(401);
		const data = await request.formData();
        const nazwa = data.get('nazwa');
        const czas = data.get('czas');
		const opis = data.get('opis');
		 const zdj = data.get('zdj');
 		if (!nazwa) {
            return fail(400, { nazwa, missing: true });
		}
		if (!opis) {
			return fail(400, { opis, missing: true });
		}
		if (!czas) {
			return fail(400, { czas, missing: true });
		}
		const user = await prisma.przepis.create({
			data: {
			 user_id : session.userId,
			 name : String(nazwa), 
			 description: String(opis),
			 time : Number(czas),
		     image : String(zdj) || undefined,
			},
		  })
		  
	}
};



