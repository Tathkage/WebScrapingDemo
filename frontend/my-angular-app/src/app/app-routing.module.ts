import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AnimeListComponent } from './anime-list/anime-list.component';

const routes: Routes = [
  { path: 'anime-list', component: AnimeListComponent },
  { path: '', redirectTo: '/anime-list', pathMatch: 'full' } // Redirect to anime list by default
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
