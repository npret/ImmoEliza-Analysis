def expensive_locality(df):

    localities = df['Locality'].unique()
    df['Surface_total']=df['Living_Area']+df['Land_Surface']

    localities = df['Locality'].unique()
    results = []

    for locality in localities:
    
        locality_data = df[df['Locality'] == locality]

        average_price = locality_data['Price'].mean()
        median_price = locality_data['Price'].median()
        
        valid_surface_data = locality_data[locality_data['Surface_total'] > 0]  # to evite that the result is inf because surface is missing
        if not valid_surface_data.empty:
            price_per_square_meter = (valid_surface_data['Price'] / valid_surface_data['Surface_total']).mean()
        else:
             price_per_square_meter = None  # Nessun calcolo se non ci sono superfici valide

      
        results.append({
            'Locality': locality,
            'Average_Price': round(average_price, 2),
            'Median_Price': round(median_price, 2),
            'Avg_Price_per_SqM': round(price_per_square_meter, 2) if price_per_square_meter is not None else None
        })
    return results

# Convert in a DataFrame for a understoodable output
# municipality_stats = pd.DataFrame(results)
# municipality_stats = municipality_stats.sort_values(by='Average_Price', ascending=False)